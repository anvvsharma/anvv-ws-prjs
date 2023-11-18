import io
import logging

from fdk import response

def handler(ctx, data: io.BytesIO = None):
    logging.getLogger().info("Got incoming request")
    return response.Response(ctx, response_data="hello world")
