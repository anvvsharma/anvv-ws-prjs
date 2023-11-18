import oci
print('#########################################')

# Initialize the OCI SDK
config = oci.config.from_file("/home/anvvsharma/.oci/AA-veerabhadra.sharma/config", "DEFAULT")
#config = oci.config.from_file("~/.oci/anvvsharmageneral/config", "DEFAULT")
#config = oci.config.from_file()
identity_client = oci.identity.IdentityClient(config)
virtual_network_client = oci.core.VirtualNetworkClient(config)
compute_client = oci.core.ComputeClient(config)
blockstorage_client = oci.core.BlockstorageClient(config)

# Fetch list of compartments
compartments = identity_client.list_compartments(config['tenancy']).data

# Iterate over compartments
for compartment in compartments:
    compartment_id = compartment.id

    # Fetch list of VCNs in the compartment
    vcns = virtual_network_client.list_vcns(compartment_id=compartment_id).data

    # Fetch list of subnets in the compartment
    subnets = virtual_network_client.list_subnets(compartment_id=compartment_id).data

    # Fetch list of compute instances in the compartment
    instances = compute_client.list_instances(compartment_id=compartment_id).data

    # Fetch list of block volumes in the compartment
    block_volumes = blockstorage_client.list_volumes(compartment_id=compartment_id).data

    # Process and print the fetched information
    print(f"Compartment: {compartment.name}")
    print("VCNs:")
    for vcn in vcns:
        print(f" - {vcn.display_name}")
    print("Subnets:")
    for subnet in subnets:
        print(f" - {subnet.display_name}")
    print("Compute Instances:")
    for instance in instances:
        print(f" - {instance.display_name}")
    print("Block Volumes:")
    for volume in block_volumes:
        print(f" - {volume.display_name}")

    print("\n")  # Add a newline for readability