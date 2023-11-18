import requests
import urllib3
import faulthandler
from zeep import Client
from zeep.wsse.utils import WSU
from zeep.wsse import username
from datetime import datetime, timedelta

from zeep.transports import Transport
from requests.auth import HTTPBasicAuth

import logging.config
import zeep.wsse.utils as utils

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings()

def submit_ess_job():
    # The ErpIntegration WSDL
    username = "OIC_Integration"
    password = "Welcome@123"
    job_name = "ADMCItemMasterPriceCostJob"  # Replace with your ESS job name
    job_package = "/oracle/apps/ess/custom/shared/Custom/Supply Chain Management/Product Management/"    
    wsdl_url = "https://fa-esqj-test-saasfaprod1.fa.ocs.oraclecloud.com:443/fscmService/ErpIntegrationService?wsdl"
    
    # Create a SOAP client using the provided WSDL
    session = requests.Session()
    session.verify = False
    transport = Transport(session=session)
    client = Client(wsdl=wsdl_url, transport=transport)

    # Set the authentication credentials
    client.transport.session.auth = HTTPBasicAuth(username, password)
        
    payload = { 
        "jobPackageName": job_package,
        "jobDefinitionCode": job_name,
         "paramList": "ADMC"
    }
    print(('hi---1'))
    try:
        # loadAndImportData is the SOAP endpoint
        print(('hi---2'))
        response = client.service.submitESSJobRequest(payload)
        print((response))
        
        if response.status_code == 200:
            print(
                'Successfully submitted ESS job, with ESS job ID: {}'.format(response))
        else:
            print('FAILED submitting ESS job')

    except Exception as e:
        print(e)
        return f"Error triggering ESS job: {str(e)}"

if __name__ == '__main__':
    submit_ess_job()
