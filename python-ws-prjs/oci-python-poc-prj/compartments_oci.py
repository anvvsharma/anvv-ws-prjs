import io
import json

from fdk import response
import oci.identity

def handler(ctx, data: io.BytesIO = None):
    signer = oci.auth.signers.get_resource_principals_signer()
    print("1.", signer)
    resp = list_compartments(signer)  # function defined below
    return response.Response(
        ctx,
        response_data=json.dumps(resp),
        headers={"Content-Type": "application/json"}
    )

# List compartments ------------------------------------------------------------

def list_compartments(signer):
    config = oci.config.from_file('~/.oci/oic-config-main/AA-veerabhadra.sharma/config', 'DEFAULT')
    client = oci.identity.IdentityClient(config={}, signer=signer)
    print("3.", client)
    # OCI API for managing users, groups, compartments, and policies
    try:
        # Returns a list of all compartments and subcompartments in the tenancy (root compartment)
        compartments = client.list_compartments(
            signer.tenancy_id,
            compartment_id_in_subtree=True,
            access_level='ANY'
        )
        # Create a list that holds a list of the compartments id and name next to each other
        compartments = [[c.id, c.name] for c in compartments.data]
    except Exception as ex:
        print("ERROR: Cannot access compartments", ex, flush=True)
        raise
    resp = {"compartments": compartments}
    return resp
