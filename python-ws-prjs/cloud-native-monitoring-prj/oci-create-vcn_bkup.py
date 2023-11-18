import oci
import gettext


# Set the language for translation
language = 'en'

# Specify the path to the message catalog file
catalog_path = 'locales'

# Set the language for translation
# Replace 'en' with the appropriate language code
translation = gettext.translation('messages', localedir=catalog_path, languages=[language])
translation.install()

# Get the translated string
translated_hello = (_(gettext.gettext('hello').strip()))

# Use the translated string
print('(',translated_hello,')')  # Output: Hello, World!


# Access the variables
vcn_dns_label = (_(gettext.gettext('vcn_dns_label')))
vcn_display_name = (_(gettext.gettext('vcn_display_name')))
subnet_dns_label = (_(gettext.gettext('subnet_dns_label')))
subnet_display_name = (_(gettext.gettext('subnet_display_name')))
v_compartment_id = (_(gettext.gettext('v_compartment_id')))
# Load the configuration from a file
config = oci.config.from_file()


# Initialize the VirtualNetworkClient
virtual_network_client = oci.core.VirtualNetworkClient(config)

# Create a new VCN
create_vcn_details = oci.core.models.CreateVcnDetails(
    cidr_block='10.0.0.0/16',
    compartment_id=v_compartment_id,
    display_name=vcn_display_name,
    dns_label=vcn_dns_label
)
print('#########################################')
print('compartment_id:[',v_compartment_id)
print('vcn_display_name:',vcn_display_name)
print('vcn_dns_label:',vcn_dns_label)
print('#########################################')
create_vcn_response = virtual_network_client.create_vcn(create_vcn_details)
vcn = create_vcn_response.data

print('New VCN ID:', vcn.id)
print('New VCN CIDR Block:', vcn.cidr_block)
print('New VCN DNS Label:', vcn.dns_label)

'''

# Create a new subnet within the VCN
create_subnet_details = oci.core.models.CreateSubnetDetails(
    compartment_id = v_compartment_id,
    vcn_id=vcn.id,
    cidr_block='10.0.0.0/24',
    display_name=subnet_display_name,
    dns_label=subnet_dns_label
)

create_subnet_response = virtual_network_client.create_subnet(create_subnet_details)
subnet = create_subnet_response.data

print('New Subnet ID:', subnet.id)
print('New Subnet CIDR Block:', subnet.cidr_block)
print('New Subnet DNS Label:', subnet.dns_label)
print('#########################################')
print('VCN and Subnet Successfully Created')
print('#########################################')
'''