# PICSART CREATIVE APIS

## Description

This is a Python SDK of Picsart Programmable Image APIs and Picsart GenAI APIs. 
You can do many actions with your images just by adding a few lines of code to your Python projects.

## Usage

```python
import picsart_sdk
upload_client = picsart_sdk.client("upload")
```
or 

```python
import picsart_sdk
session = picsart_sdk.Session(api_key="API_KEY")
upload_client = session.client("upload")
```

and then use it:

```python
upload_client.upload_image("razvan.jpg")
upload_client.upload_image("http://domain.com/file.jpg")
```
