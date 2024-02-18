from fastapi import FastAPI, HTTPException, status, Security
from fastapi.security import APIKeyHeader, APIKeyQuery

import btc_app

api_keys = [
    "my_api_key"
] # These need to be retrieved from a secure location, database, etc.

api_keys.append(btc_app.api_key) # Let's add the API key from the config file

# Define the API key header
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in api_keys:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "OK!"}

@app.get("/public")
def public():
    """A public endpoint that does not require any authentication."""
    return {"message": "Public Endpoint. No API Key required."}

@app.get("/protected")
def private(api_key: str = Security(get_api_key)):
    """A private endpoint that requires a valid API key to be provided."""
    if api_key in api_keys:
        return {"message": "API Key is valid. You can access the private endpoint."}
    
    return {"message": "Private Endpoint. API Key required."}
