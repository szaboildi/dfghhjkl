import torch
torch.classes.__path__ = []

from llama_cpp import Llama
import os
from HF_Space_gemma2_2b_texttosql.src.utils import chat


def main():
    filename = "gemma-2_2B-texttosql-with_instrction-merged_gguf_q8.gguf"
    llm = Llama(model_path=os.path.join("models", filename))

    while True:
        prompt = input("What request would you like to transform into an SQL query?")
        output = chat(llm, prompt)
        print(output)
        cont = input("Would you like to continue? [Y/N] ")
        if cont.lower() != "y" and cont.lower() != "yes":
            break

if __name__ == "__main__" :
    main()
