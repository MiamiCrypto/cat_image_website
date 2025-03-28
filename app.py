import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from io import BytesIO

# Set up Azure Blob Storage connection (use the connection string from Azure portal)
connection_string = "<your_connection_string>"  # Replace with your actual connection string
container_name = "uploads"  # Replace with your container name

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get the uploaded file from the request
        file = req.files.get('file')
        if not file:
            return func.HttpResponse("No file uploaded", status_code=400)
        
        # Create a BlobServiceClient and a BlobClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
        
        # Upload the file to Azure Blob Storage
        blob_client.upload_blob(file.stream, overwrite=True)
        
        return func.HttpResponse(f"File {file.filename} uploaded successfully.", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
