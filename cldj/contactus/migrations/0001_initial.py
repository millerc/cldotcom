# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=32),), ('email', models.EmailField(max_length=75),), ('title', models.CharField(max_length=64),), ('extension', models.CharField(max_length=5),), ('active', models.BooleanField(),)],
            bases = (models.Model,),
            options = {},
            name = 'ContactListing',
        ),
    ]
