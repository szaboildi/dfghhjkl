# Create the virtual environment
venv:
	python3 -m venv .venv

# Activate the virtual environment and install required packages
setup: venv
	. .venv/bin/activate && pip install --upgrade pip && pip install transformers torch gguf accelerate

# Try out the model
tryout:
	python main_gguf.py



# Create the virtual environment
venv_g:
	python3 -m venv .venv_g

# Activate the virtual environment and install required packages
setup_gemma: venv_g
	. .venv_g/bin/activate && pip install --upgrade pip && pip install torch gguf llama-cpp-python huggingface_hub && mkdir -p models && wget -O "models/gemma-2_2B-texttosql-with_instrction-merged_gguf_q8.gguf" "https://huggingface.co/szaboildi/gemma-2_2B-texttosql-with_instrction-merged_gguf/resolve/main/gemma-2_2B-texttosql-with_instrction-merged_gguf_q8.gguf"


# Try out the model
tryout_gemma:
	python main_gguf_gemma2_2b.py
