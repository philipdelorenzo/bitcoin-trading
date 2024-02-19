from fastapi import FastAPI, HTTPException, status, Security, Depends 
from fastapi.security import APIKeyHeader, APIKeyQuery
from fastapi.security import OAuth2PasswordBearer

import btc_app

api_keys = [] # These need to be retrieved from a secure location, database, etc.
api_keys.append(btc_app.api_key) # Let's add the API key from the config file

# Define the API key header
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication

def api_key_auth(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in api_keys:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )

def api_key_oauth(api_key: str = Depends(oauth2_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )
