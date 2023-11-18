import oci
import os

config = oci.config.from_file('~/.oci/oic-config-main/AA-veerabhadra.sharma/config', 'DEFAULT')
# Initialize service client with default config file
core_client = oci.core.ComputeClient(config)

compartment_id_selected="ocid1.tenancy.oc1..aaaaaaaakya26vteec7ickcuoppdvzehuvuiqm3gvs5et57ocyot3qsltvtq"
# list_instances_response = core_client.list_instances(compartment_id=compartment_id_selected)
list_instances_response = core_client.list_instances(compartment_id=compartment_id_selected)

# Get the data from response
print(list_instances_response)
