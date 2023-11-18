import requests
import urllib3
from zeep import Client
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth

# Disable SSL warnings for self-signed certificates
urllib3.disable_warnings()

def trigger_ess_job():
    wsdl_url = "https://fa-esqj-test-saasfaprod1.fa.ocs.oraclecloud.com:443/fscmService/ErpIntegrationService?wsdl"
    username = "OIC_Integration"
    password = "Welcome@123"
    job_name = "ADMCItemMasterPriceCostJob"  # Replace with your ESS job name
    job_package = "/oracle/apps/ess/custom/shared/Custom/Supply Chain Management/Product Management/"
    # Create a SOAP client using the provided WSDL
    session = requests.Session()
    session.verify = False
    transport = Transport(session=session)
    client = Client(wsdl=wsdl_url, transport=transport)

    # Set the authentication credentials
    client.transport.session.auth = HTTPBasicAuth(username, password)

    # Build the SOAP request payload
    payload = [
         {
        "jobPackageName": job_package,
        "jobDefinitionName": job_name,
        'ParameterList': 'ADMC'
        }
      ]
     

    try:
        # Call the ESS service to trigger the job
        response = client.service.submitESSJobRequest(payload)
        job_id = response.outputParameters[0].value

        return f"ESS job triggered successfully with ID: {job_id}"
    except Exception as e:
        return f"Error triggering ESS job: {str(e)}"

# Trigger the ESS job
result = trigger_ess_job()
print(result)
