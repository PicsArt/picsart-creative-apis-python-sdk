# PICSART CREATIVE APIS

## Description

This is a Python SDK of Picsart Programmable Image APIs and Picsart GenAI APIs. 
You can do many actions with your images just by adding a few lines of code to your Python projects.

## Usage

Create the client:
1. Default session. It is shorter if the `PICSART_API_KEY` environment variable is set.

```python
import picsart_sdk
upload_client = picsart_sdk.client("upload")
```
otherwise you can create the session manually and passing the api key. 

```python
import picsart_sdk
session = picsart_sdk.Session(api_key="API_KEY")
upload_client = session.client("upload")
```

afterwords, you can use the specific client. 

Example for uploading a file:
```python
import picsart_sdk
upload_client = picsart_sdk.client("upload")

upload_client.upload_from_path(file_path="/path/to/image.jpg")
upload_client.upload_from_url(url="http://domain.com/file.jpg")
```

