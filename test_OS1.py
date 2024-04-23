from opensearchpy import OpenSearch

# Assuming OpenSearch is running on localhost:9200
host = 'localhost'
port = 9200
auth = ('admin', 'YourStrongPassword123!')  # Only needed if security features are enabled

# Create an instance of the OpenSearch client
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_auth=auth
)

# Test the connection
print(client.info())
