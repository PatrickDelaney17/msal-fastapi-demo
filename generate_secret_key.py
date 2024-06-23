import secrets

# Generate a random URL-safe text string, which is suitable for a SECRET_KEY
secret_key = secrets.token_urlsafe(32)
print(secret_key)
