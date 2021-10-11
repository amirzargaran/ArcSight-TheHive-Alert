#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact, CustomFieldHelper


THEHIVE_URL = 'http://<thehive-url>:9000'
THEHIVE_API_KEY = '***API-KEY***'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

# Prepare observables
inmemory_file = open('sample.txt', 'rb')
artifacts = [
    AlertArtifact(dataType='ip', data='x.x.x.x'),
    AlertArtifact(dataType='domain', data='google.com'),
    AlertArtifact(dataType='file', data='pic.png'),
    AlertArtifact(dataType='file', data=(inmemory_file, 'sample.txt'), sighted=True, ioc=True)
]

# Prepare the custom field 
customFields = CustomFieldHelper()\
	.add_date('endtime', int(time.time())*1000)\
	.add_string('name', sys.argv[0])\
	.add_string('sourceaddress', sys.argv[1])\
	.add_string('destinationaddress', sys.argv[2])\
	.add_string('categorybehavior', sys.argv[3])\
	.add_string('categorydevicegroup', sys.argv[4])\
	.add_string('categoryobject', sys.argv[5])\
	.add_string('categoryoutcome', sys.argv[6])\
	.add_string('categorysignificance', sys.argv[7])\
	.add_string('categorytechnique', sys.argv[8])\
	.add_string('destinationusername', sys.argv[9])\
	.add_number('priority', sys.argv[10])\
    .build()

# Prepare the sample Alert
sourceRef = str(uuid.uuid4())[0:6]
alert = Alert(title='Brute Force Alert',
    tlp=3,
    tags=['arcsight', 'esm', 'alert', 'action'],
    description='Sample Alert',
    type='external',
    source='instance1',
    sourceRef=sourceRef,
    artifacts=artifacts,
    customFields=customFields
)

# Create the alert
try:
  response = api.create_alert(alert)

  # Print the JSON response 
  print(json.dumps(response.json(), indent=4, sort_keys=True))

except AlertException as e:
  print("Alert create error: {}".format(e))

inmemory_file.close()

# Exit the program
sys.exit(0)
