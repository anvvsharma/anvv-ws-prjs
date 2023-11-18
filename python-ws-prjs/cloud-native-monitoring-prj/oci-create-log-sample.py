import oci

# Load the configuration
config = oci.config.from_file()
compartment_id = config["tenancy"]

# Create a LoggingAnalyticsClient
client = oci.logging.LoggingAnalyticsClient(config)

# Create a query to retrieve logs
query = 'search source "Audit" | fields message'

# Make the query request
response = client.query_logs(
    oci.logging.models.QueryDetails(
        compartment_id=compartment_id,
        query=query,
        is_monitor_query=True
    )
)

# Retrieve the results
results = response.data.results
for result in results:
    print(result['message'])
