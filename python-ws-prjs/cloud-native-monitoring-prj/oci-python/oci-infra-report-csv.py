import csv
import oci

# Initialize the OCI SDK and service clients
# ...

# Create a CSV file
csv_file = open('infra_report.csv', 'w', newline='')
NoValueString = "n/a"           # what value should be used when no data is available
FieldSeperator = ","            # what value should be used as field seperator
ReportFile = "C:\\oci\\report.csv"
EndLine = "\n"
csv_writer = csv.writer(csv_file)

# Write the headers
csv_writer.writerow(['Compartment', 'VCN', 'Subnet', 'Compute Instance', 'Block Volume'])

# Initialize the OCI SDK
config = oci.config.from_file()
identity_client = oci.identity.IdentityClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)
compute_client = oci.core.ComputeClient(config)
blockstorage_client = oci.core.BlockstorageClient(config)

# Fetch list of compartments
compartments = identity_client.list_compartments(config['tenancy']).data

# Fetch and write the infrastructure information
for compartment in compartments:
    compartment_id = compartment.id
    #csv_writer.writerow([compartment.name])

    # Fetch list of VCNs in the compartment
    vcns = virtual_network_client.list_vcns(compartment_id=compartment_id).data
    #csv_writer.writerow([vcn.display_name])

    # Fetch list of subnets in the compartment
    subnets = virtual_network_client.list_subnets(compartment_id=compartment_id).data

    # Fetch list of compute instances in the compartment
    instances = compute_client.list_instances(compartment_id=compartment_id).data

    # Fetch list of block volumes in the compartment
    block_volumes = blockstorage_client.list_volumes(compartment_id=compartment_id).data

    # Write the information to the CSV file
    for vcn in vcns:
        for subnet in subnets:
            for instance in instances:
                for volume in block_volumes:
                    csv_writer.writerow([compartment.name, vcn.display_name, subnet.display_name, instance.display_name, volume.display_name])

# Close the CSV file
csv_file.close()
