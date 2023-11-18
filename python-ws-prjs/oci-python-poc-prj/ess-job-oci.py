import oci

# Set up the configuration using instance principal
config = oci.config.from_file(profile_name="DEFAULT")

# Replace these values with your specific information
ess_job_name = "ADMCItemMasterPriceCostJob"
essb_job_pkg_name = "/oracle/apps/ess/custom/shared/Custom/Supply Chain Management/Product Management/"
ess_service_endpoint = "https://fa-esqj-test-saasfaprod1.fa.ocs.oraclecloud.com:443/fscmService/ErpIntegrationService?wsdl"  # Replace with the actual ESS service endpoint URL

# Create the ESS client
ess_client = oci.ess.EssJobClient(config=config, service_endpoint=ess_service_endpoint)

# Prepare the ESS job request
job_request = oci.ess.models.SubmitJobRequestDetails(
    job_definition_name=ess_job_name,
    job_definition_key=essb_job_pkg_name,
    job_schedule_type="ONETIME",
    parameters={},
    metadata={"opc-request-id": "unique-id"}  # Provide a unique request ID
)

# Submit the ESS job
job_response = ess_client.submit_job(job_request)

print("ESS job submitted with ID:", job_response.data.job_id)
