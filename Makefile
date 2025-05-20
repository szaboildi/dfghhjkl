
# Create the virtual environment
venv:
	python3 -m venv .venv

# Activate the virtual environment and install required packages
setup: venv
	. .venv/bin/activate && pip install --upgrade pip && pip install transformers torch gguf accelerate

# Try out the model
tryout:
	python main_gguf.py
