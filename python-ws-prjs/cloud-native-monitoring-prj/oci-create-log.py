# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
config = oci.config.from_file("~/.oci/config", "DEFAULT")
#config = oci.config.from_file()


# Initialize service client with default config file
logging_client = oci.logging.LoggingManagementClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
create_log_response = logging_client.create_log(
    log_group_id="ocid1.loggroup.oc1.ap-hyderabad-1.amaaaaaahalaqoaady3ck7pjvp4jiaae33ov4hv647d7vv3qqhqd2gzfawya",
    create_log_details=oci.logging.models.CreateLogDetails(
        display_name="EXAMPLE-displayName-Value",
        log_type="SERVICE",
        is_enabled=True,
        defined_tags={
            'EXAMPLE_KEY_GDKMh': {
                'EXAMPLE_KEY_Kqtbd': 'EXAMPLE--Value'}},
        freeform_tags={
            'EXAMPLE_KEY_xGBx7': 'EXAMPLE_VALUE_zUWs4wlv2RcW1bWRXy7A'},
        configuration=oci.logging.models.Configuration(
            source=oci.logging.models.OciService(
                source_type="OCISERVICE",
                service="EXAMPLE-service-Value",
                resource="EXAMPLE-resource-Value",
                category="EXAMPLE-category-Value",
                parameters={
                    'EXAMPLE_KEY_ymk2R': 'EXAMPLE_VALUE_Thp58UpezvZlqr3RxuY6'}),
            compartment_id="ocid1.compartment.oc1..aaaaaaaael6rxzavybwasxz6ef5uppspivcshk3ohohk272rltt47xnipj2q",
            archiving=oci.logging.models.Archiving(
                is_enabled=False)),
        retention_duration=47),
    opc_retry_token="EXAMPLE-opcRetryToken-Value",
    opc_request_id="9NGSNQL5PWBVQTOYGIP7101")

# Get the data from response
print(create_log_response.headers)
