import oci

# Load the configuration from a file
#config = oci.config.from_file("/home/anvvsharma/.oci/AA-veerabhadra.sharma/config", "DEFAULT")
#config = oci.config.from_file("/home/anvvsharma/.oci/anvvsharmageneral/config", "DEFAULT")
config = oci.config.from_file()

# Initialize the ComputeClient
compute_client = oci.core.ComputeClient(config)

# List all instances in a compartment
compartment_id = 'ocid1.tenancy.oc1..aaaaaaaa3ao2whbmnblvhfdkbdfne6b3o4vrnthbxqlombqoihqz2jrozjnq'
#compartment_id='ocid1.tenancy.oc1..aaaaaaaa5hcjk5lxsvtlze26gbhttcqv52rgjjvwthhhe5km6akqdh77aozq'
instances = compute_client.list_instances(compartment_id).data

# Print the instance details
for instance in instances:
    print('Instance ID:', instance.id)
    print('Display Name:', instance.display_name)
    print('Availability Domain:', instance.availability_domain)
    print('State:', instance.lifecycle_state)
    print('')
'''
# Create a new instance
create_instance_details = oci.core.models.LaunchInstanceDetails(
    display_name='NewInstance',
    compartment_id=compartment_id,
    shape='VM.Standard2.1',
    image_id='<image OCID>',
    subnet_id='<subnet OCID>'
)

create_response = compute_client.launch_instance(create_instance_details)
print('New Instance ID:', create_response.data.id)
'''
