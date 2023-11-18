import oci
import json
import shapes
import logging

# Script configuation ###################################################################################

# Initialize the OCI SDK
config = oci.config.from_file("/home/anvvsharma/.oci/AA-veerabhadra.sharma/config", "DEFAULT")

#validating configuration file, making sure the connection is established
oci.config.validate_config(config)

#setting and initializing OCI parameters
identity = oci.identity.IdentityClient(config)
user = identity.get_user(config["user"]).data

#prints information about the OCID user
print(user)