# auth.py

import msal
import os
from dotenv import load_dotenv
from fastapi import Request, HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
AUTHORITY = os.getenv("AUTHORITY")
REDIRECT_PATH = "/token"
SCOPE = ["User.Read"]

msal_app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
)

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://login.microsoftonline.com/your_tenant_id/oauth2/v2.0/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=http://localhost:8000{REDIRECT_PATH}&scope=openid profile email User.Read",
    tokenUrl=f"https://login.microsoftonline.com/your_tenant_id/oauth2/v2.0/token"
)

def get_token_from_code(auth_code: str) -> dict:
    result = msal_app.acquire_token_by_authorization_code(
        auth_code,
        scopes=SCOPE,
        redirect_uri="http://localhost:8000" + REDIRECT_PATH,
    )
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error_description"])
    return result

def get_token(request: Request) -> dict:
    token = request.session.get("token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return token

def get_user_email(token: dict) -> str:
    return token.get("id_token_claims", {}).get("preferred_username", "Unknown")

def ensure_authenticated(request: Request):
    try:
        get_token(request)
    except HTTPException as e:
        if e.status_code == 401:
            raise HTTPException(status_code=401, detail="Not authenticated. Please log in.")
        else:
            raise
