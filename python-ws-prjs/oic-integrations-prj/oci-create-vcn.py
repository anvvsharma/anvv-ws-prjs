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
