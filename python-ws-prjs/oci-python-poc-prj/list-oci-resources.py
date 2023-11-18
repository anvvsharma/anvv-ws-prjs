import csv
import oci

# Initialize the OCI SDK and service clients
# ...

# Create a CSV file
csv_file = open('infra_report.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Write the headers
csv_writer.writerow(['Compartment', 'VCN', 'Subnet', 'Compute Instance', 'Block Volume'])

# Initialize the OCI SDK
config = oci.config.from_file('~/.oci/oic-config-main/AA-veerabhadra.sharma/config', 'DEFAULT')
#config = oci.config.from_file('~/.oci/anvvsharmageneral-.oci-config/config', 'DEFAULT')
# Initialize service client with default config file
#core_client = oci.core.ComputeClient(config)
#config = oci.config.from_file()
identity_client = oci.identity.IdentityClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)
compute_client = oci.core.ComputeClient(config)
blockstorage_client = oci.core.BlockstorageClient(config)

# Fetch list of compartments
compartments = identity_client.list_compartments(config['tenancy']).data

# Fetch and write the infrastructure information
for compartment in compartments:
    compartment_id = compartment.id
    print(compartment.name, " = ", compartment_id)
    # Fetch list of VCNs in the compartment
    vcns = virtual_network_client.list_vcns(compartment_id=compartment_id).data
    print("vcns = ", vcns)
    # Fetch list of subnets in the compartment
    subnets = virtual_network_client.list_subnets(compartment_id=compartment_id).data
    print("subnets = ", subnets)
    # Fetch list of compute instances in the compartment
    instances = compute_client.list_instances(compartment_id=compartment_id).data
    print("instances = ", instances)
    # Fetch list of block volumes in the compartment
    block_volumes = blockstorage_client.list_volumes(compartment_id=compartment_id).data
    print("block_volumes = ", block_volumes)
    # Write the information to the CSV file
    for vcn in vcns:
        for subnet in subnets:
            #for instance in instances:
                #for volume in block_volumes:
            #csv_writer.writerow([compartment.name, vcn.display_name, subnet.display_name, instance.display_name, volume.display_name])
            csv_writer.writerow([compartment.name, vcn.display_name, subnet.display_name])

# Close the CSV file
csv_file.close()
