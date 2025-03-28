import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os

# Initialize BlobServiceClient to interact with Blob Storage
blob_connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')  # Get connection string from environment variable
blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
container_name = "your-container-name"  # Use the container you created in Azure Blob Storage

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get the image from the request
        uploaded_file = req.files['file']
        file_name = uploaded_file.filename
        
        # Upload the image to Azure Blob Storage
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        blob_client.upload_blob(uploaded_file.stream, overwrite=True)

        return func.HttpResponse(f"Image uploaded successfully: {file_name}", status_code=200)
    
    except Exception as e:
        logging.error(f"Error during file upload: {str(e)}")
        return func.HttpResponse(f"Error uploading image: {str(e)}", status_code=500)
