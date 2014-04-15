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
    return [ { 'id': id.text, 'name': name.text } for (name,id) in zip(
        response.iterdescendants('dbname'),response.iterdescendants('dbid')
        ) ]

def getfields(qdbid=qdbid):
    'Returns field id list of given dbid'
    ticket = ticketor()
    url = '%s%s' % (url_base, qdbid)
    headers['QUICKBASE-ACTION'] = 'API_GetSchema'
    qdbapi = etree.Element('qdbapi')
    ticket = etree.SubElement(qdbapi, "ticket").text=ticket
    request = urllib2.Request(url=url, data=etree.tostring(qdbapi), headers=headers)
    response = etree.fromstring(urllib2.urlopen(request).read())
    return response
    
def getrecords(qdbid=qdbid):
    'Get all records from given table id'
    ticket = ticketor()
    url = '%s%s' % (url_base, qdbid)
    headers['QUICKBASE-ACTION'] = 'API_DoQuery'
    qdbapi = etree.Element('qdbapi')
    ticket = etree.SubElement(qdbapi, "ticket").text=ticket
    includeRids = etree.SubElement(qdbapi, "includeRids").text='1'
    request = urllib2.Request(url=url, data=etree.tostring(qdbapi), headers=headers)
    response = etree.fromstring(urllib2.urlopen(request).read())
    return response

def get_voucher_data(project_code):
    'Gets project info and sponsor list for project_code. Returns dict for use in linkbase.views.email_vouchers'
    ticket = ticketor()
    
    # Part 1: Get project info
    url = '%sbgziijbpx' % url_base
    headers['QUICKBASE-ACTION'] = 'API_DoQuery'
    qdbapi = etree.Element('qdbapi')
    ticket = etree.SubElement(qdbapi, "ticket").text=ticket
    # fid11/project_code contains project_code
    query = etree.SubElement(qdbapi, "query").text="{'11'.CT." + project_code + "}"
    # client,code,title,product,address1,address2,city,state,zip
    clist = etree.SubElement(qdbapi, "clist").text='245.11.22.244.260.261.262.263.264.273'
    request = urllib2.Request(url=url, data=etree.tostring(qdbapi), headers=headers)
    response = etree.fromstring(urllib2.urlopen(request).read())
    project = { f.tag: f.text for f in response.find('record') }

    # Part 2: Generate sponsor list
    url = '%sbgzankk6e' % url_base
    headers['QUICKBASE-ACTION'] = 'API_DoQuery'
    qdbapi = etree.Element('qdbapi')
    ticket = etree.SubElement(qdbapi, "ticket").text=ticket
    # Sales Status is not Cancelled; Balance Due = 0; Paid Copies and/or Free Products > 0 
    query = etree.SubElement(qdbapi, "query")
    query.text = ("{'395'.CT." + project_code + "}AND{'528'.XCT.'Cancelled'}"
                  "AND{'60'.EX.'0'}AND({'176'.XEX.''}OR{'197'.XEX.''})")
    # customer,billing_contact,billing_contact_email,paid_copies_quantity,free_products
    clist = etree.SubElement(qdbapi, "clist").text='41.294.336.197.176'
    includeRids = etree.SubElement(qdbapi, "includeRids").text='1'
    request = urllib2.Request(url=url, data=etree.tostring(qdbapi), headers=headers)
    response = etree.fromstring(urllib2.urlopen(request).read())
    sponsors = [ { f.tag: f.text for f in sponsor } 
                 for sponsor in response.findall('record') ]
        
    return { 'project': project, 'sponsors': sponsors }
    