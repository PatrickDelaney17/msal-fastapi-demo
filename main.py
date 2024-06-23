# main.py

import os
from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.sessions import SessionMiddleware
from auth import get_token_from_code, get_token, get_user_email, CLIENT_ID, REDIRECT_PATH, ensure_authenticated

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

@app.get("/login")
def login():
    return RedirectResponse(url=oauth2_scheme.authorizationUrl)

@app.get(REDIRECT_PATH)
def auth_callback(request: Request, code: str):
    token = get_token_from_code(code)
    request.session["token"] = token
    return RedirectResponse(url="/docs")

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request, token: dict = Depends(ensure_authenticated)):
    user_email = get_user_email(token)
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Docs", swagger_favicon_url=None, swagger_ui_init_oauth=None, oauth2_redirect_url=None, swagger_ui_parameters={"persistAuthorization": True}, swagger_custom_js=f"document.addEventListener('DOMContentLoaded', function() {{ document.body.insertAdjacentHTML('afterbegin', '<h3>Welcome {user_email}</h3>'); }});")

@app.get("/show_user_token")
def show_user_token(token: dict = Depends(ensure_authenticated)):
    return token
