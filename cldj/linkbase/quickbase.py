import urllib2
from lxml import etree

quser = 'chris.miller@communitylink.com'
qpass = 'curd998-opus'
qdbid = 'bgr8fxea4'

url_base = 'https://communitylink.quickbase.com/db/' 
headers = {'Content-Type': 'application/xml'}

def ticketor(quser=quser, qpass=qpass, hours='1'):
    'Authenticates and returns ticket'
    url = '%smain' % url_base
    headers['QUICKBASE-ACTION'] = 'API_Authenticate'
    qdbapi = etree.Element('qdbapi')
    username = etree.SubElement(qdbapi, "username").text=quser
    password = etree.SubElement(qdbapi, "password").text=qpass
    hours = etree.SubElement(qdbapi, "hours").text=hours
    request = urllib2.Request(url=url, data=etree.tostring(qdbapi), headers=headers)
    response = etree.fromstring(urllib2.urlopen(request).read())
    return response.find('ticket').text

def dblist():
    'Lists databases available to logged in user'
    ticket = ticketor()
    url = '%smain' % url_base
    headers['QUICKBASE-ACTION'] = 'API_GrantedDBs'
    qdbapi = etree.Element('qdbapi')
    ticket = etree.SubElement(qdbapi, "ticket").text=ticket
    request = urllib2.Request(url=url, data=etree.tostring(qdbapi), headers=headers)
    response = etree.fromstring(urllib2.urlopen(request).read())
    return [ { 'id': id.text, 'name': name.text } for (name,id) in zip(response.iterdescendants('dbname'),response.iterdescendants('dbid')) ]
    #return [ item.text, item.tag for item in response.iterdescendants('dbname') ]
    #return response.find('databases').findall('dbinfo')