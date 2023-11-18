import requests
import urllib3
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session
import xml.etree.ElementTree as ET
import logging.config
import zeep.wsse.utils as utils

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings()

def trigger_ess_job():
    '''
    wsdl_url = "https://fa-esdr-dev13-saasfademo1.ds-fa.oraclepdemos.com:443/fscmService/ErpIntegrationService?wsdl"
    username = "SCM_TRN_USR"
    password = "SCMUSER@1234"
    job_name = "SamplePOReportESSJob"
    job_package = "/oracle/apps/ess/custom/users/scm_trn_usr/ESS/"
    param_sch1 = "52166"
    '''
    
    wsdl_url = "https://fa-esqj-test-saasfaprod1.fa.ocs.oraclecloud.com:443/fscmService/ErpIntegrationService?wsdl"
    username = "OIC_Integration"
    password = "Welcome@123"
    job_name = "ADMCItemMasterPriceCostJob"
    job_package = "/oracle/apps/ess/custom/shared/Custom/Supply Chain Management/Product Management/"
    param_sch1 = "52166"
    
    # Build the SOAP request payload
    payload = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:typ="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/types/">
                <soapenv:Body>
                    <typ:submitESSJobRequest>
                        <typ:jobPackageName>'''+job_package+'''</typ:jobPackageName>
                        <typ:jobDefinitionName>'''+job_name+'''</typ:jobDefinitionName>
                        <typ:paramList>'''+param_sch1+'''</typ:paramList>
                    </typ:submitESSJobRequest>
                </soapenv:Body>
            </soapenv:Envelope>'''

    try:
        # headers
        headers = {
            'Content-Type': 'text/xml; charset=utf-8'
        }

        # Create a SOAP client using the provided WSDL
        session = requests.Session()
        session.verify = False
        session.auth = HTTPBasicAuth(username, password)
        transport = Transport(session=session)
        client = Client(wsdl_url, transport=transport)
        
        # POST request with the authenticated session
        response = session.post(wsdl_url, headers=headers, data=payload)
        #print(response.status_code)
        if response.status_code == 200:
            print('Successfully submitted ESS job, with ESS job ID: {}'.format(response))
            return response.status_code

        else:
            print('FAILED submitting ESS job')
            
    except Exception as e:
        return f"Error triggering ESS job: {str(e)}"
      
# Trigger the ESS job
result = trigger_ess_job()
#print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
#print(result)
