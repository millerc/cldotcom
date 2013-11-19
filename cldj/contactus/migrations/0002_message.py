# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [('contactus', '0001_initial')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=64),), ('email', models.EmailField(max_length=75),), ('message', models.TextField(),), ('created', models.DateTimeField(auto_now=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Message',
        ),
    ]
