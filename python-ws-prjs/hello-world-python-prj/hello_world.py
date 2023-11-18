import io
import json
import logging

from fdk import response

ctx = 'oracle.compartment-id ocid1.compartment.oc1..aaaaaaaael6rxzavybwasxz6ef5uppspivcshk3ohohk272rltt47xnipj2q'

def handler(ctx, data: io.BytesIO = None):
    name = "World"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name)}),
        headers={"Content-Type": "application/json"}
    )
