FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y && apt-get install -y wget \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 user

# Getting necessary files and folders
RUN git clone https://github.com/ggerganov/llama.cpp.git
RUN mkdir -p /app/models && wget -O "/app/models/gemma-2_2B-texttosql-with_instrction-merged_gguf_q8.gguf" "https://huggingface.co/szaboildi/gemma-2_2B-texttosql-with_instrction-merged_gguf/resolve/main/gemma-2_2B-texttosql-with_instrction-merged_gguf_q8.gguf"

COPY requirements.txt ./
COPY src/ ./src/
# Installing dependencies
RUN pip3 install -r llama.cpp/requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
