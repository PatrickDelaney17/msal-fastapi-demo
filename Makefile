# Makefile

# Variables
VENV_DIR=venv
PYTHON=$(VENV_DIR)/bin/python
PIP=$(VENV_DIR)/bin/pip
UVICORN=$(VENV_DIR)/bin/uvicorn
APP=main:app
HOST=127.0.0.1
PORT=8000

# Default target
.PHONY: all
all: run

# Create virtual environment
.PHONY: venv
venv:
	python -m venv $(VENV_DIR)

# Install dependencies
.PHONY: install
install: venv
	$(PIP) install -r requirements.txt

# Start the FastAPI server
.PHONY: run
run: install
	$(UVICORN) $(APP) --reload --host $(HOST) --port $(PORT)

# Stop the FastAPI server
.PHONY: stop
stop:
	@echo "Stopping server is handled by interrupting the process (Ctrl+C)."

# Clean up the virtual environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

# Generate SECRET_KEY
.PHONY: generate-secret-key
generate-secret-key:
	$(PYTHON) -c "import secrets; print(secrets.token_urlsafe(32))"
