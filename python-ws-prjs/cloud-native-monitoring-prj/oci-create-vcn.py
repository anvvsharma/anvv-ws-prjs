import oci
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the resource bundle file
config.read('config.ini')

# Access the variables

v_compartment_id = config.get('Variables', 'v_compartment_id')

vcn_cidr_block = config.get('Variables', 'vcn_cidr_block')
vcn_display_name = config.get('Variables', 'vcn_display_name')
vcn_dns_label = config.get('Variables', 'vcn_dns_label')

subnet_cidr_block = config.get('Variables', 'subnet_cidr_block')
subnet_display_name = config.get('Variables', 'subnet_display_name')
subnet_dns_label = config.get('Variables', 'subnet_dns_label')

print('#########################################')

# Load the configuration from a file

config = oci.config.from_file()

# Initialize the VirtualNetworkClient
virtual_network_client = oci.core.VirtualNetworkClient(config)

# List the VCNs in the compartment
list_vcns_response = virtual_network_client.list_vcns(compartment_id=v_compartment_id)

# Iterate over the list of VCNs and check if the desired VCN already exists
for vcn in list_vcns_response.data:
    if vcn.display_name == vcn_display_name:
        print("VCN display_name='",vcn_display_name,"' already exists, Skipping VCN Creation !! ")
        break
    elif vcn.dns_label == vcn_dns_label:
        print("VCN dns_label='",vcn_dns_label,"' already exists, Skipping VCN Creation !! ")
        break
else:
        print("No VCN Found with", vcn_display_name ," Creating VCN")
        # Create a new VCN
        create_vcn_details = oci.core.models.CreateVcnDetails(
            cidr_block=vcn_cidr_block,
            compartment_id=v_compartment_id,
            display_name=vcn_display_name,
            dns_label=vcn_dns_label
        )

        create_vcn_response = virtual_network_client.create_vcn(create_vcn_details)
        vcn = create_vcn_response.data

        print('New VCN ID:', vcn.id)
        print('New VCN CIDR Block:', vcn.cidr_block)
        print('New VCN DNS Label:', vcn.dns_label)
        print('#########################################')
        print('VCN Successfully Created')
        print('#########################################')

        # Create a new subnet within the VCN
        create_subnet_details = oci.core.models.CreateSubnetDetails(
            compartment_id = v_compartment_id,
            vcn_id=vcn.id,
            cidr_block=subnet_cidr_block,
            display_name=subnet_display_name,
            dns_label=subnet_dns_label
        )

        create_subnet_response = virtual_network_client.create_subnet(create_subnet_details)
        subnet = create_subnet_response.data

        print('New Subnet ID:', subnet.id)
        print('New Subnet CIDR Block:', subnet.cidr_block)
        print('New Subnet DNS Label:', subnet.dns_label)
        print('#########################################')
        print('Subnet Successfully Created')
        print('#########################################')
