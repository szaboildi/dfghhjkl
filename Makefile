
# Create the virtual environment
venv:
	python3 -m venv .venv

# Activate the virtual environment and install required packages
setup: venv
	. .venv/bin/activate && pip install --upgrade pip && pip install transformers torch gguf

# Try out the model
tryout:
	source .venv/bin/activate
	python main_gguf.py
