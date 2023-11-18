import requests
import urllib3
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings()

def trigger_ess_job():
    wsdl_url = "https://fa-esqj-test-saasfaprod1.fa.ocs.oraclecloud.com:443/fscmService/ErpIntegrationService?wsdl"
    username = "OIC_Integration"
    password = "Welcome@123"
    job_name = "ADMCItemMasterPriceCostJob"
    job_package = "/oracle/apps/ess/custom/shared/Custom/Supply Chain Management/Product Management/"
    
    # Create a SOAP client using the provided WSDL
    session = requests.Session()
    #session.verify = False
    session.auth = HTTPBasicAuth(username, password)
    transport = Transport(session=session)
    client = Client(wsdl_url, transport=transport)
    
    # Build the SOAP request payload
    payload = """<submitESSJobRequest><jobDefinitionName>ADMCItemMasterPriceCostJob</jobDefinitionName>
        <jobPackageName>/oracle/apps/ess/custom/shared/Custom/Supply Chain Management/Product Management/</jobPackageName>
        <paramList>ALL</paramList>
      </submitESSJobRequest>"""

    try:
        # Call the ESS service to trigger the job
        response = client.service.submitESSJobRequest(payload)
        
        # Check if the request was successful
        if response.status_code == 200:
            return "ESS job triggered successfully"
        else:
            return f"Error triggering ESS job. Response code: {response}"

    except Exception as e:
        return f"Error triggering ESS job: {str(e)}"

# Trigger the ESS job
result = trigger_ess_job()
print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n")
print("ESS Job Response - " + result + "\n")
