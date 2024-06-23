# FastAPI with MSAL Authentication

This project demonstrates a basic FastAPI application with MSAL authentication, protecting the Swagger documentation page, and displaying user information.

## Auth 

### App Registration
> https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate#register-an-application

## Setup

1. **Clone the repository**

```sh
git clone https://github.com/your_username/your_repo.git
cd your_repo
```


## Execution


```sh
# start api

uvicorn main:app --reload


```

1. login: http://localhost:8000/login
2. swagger: http://localhost:8000/docs


# Optional
## creating a secret key
SECRET_KEY: This is a secret key used by your FastAPI application to sign session cookies and other cryptographic operations. It's used to ensure the integrity and confidentiality of the session data. It should also be kept confidential and not exposed publicly.


```sh
# generate secret key in terminal
python generate_secret_key.py

#Add the generated SECRET_KEY to your .env file

```