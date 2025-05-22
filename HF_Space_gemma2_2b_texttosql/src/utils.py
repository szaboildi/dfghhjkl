import torch
torch.classes.__path__ = []

from llama_cpp import Llama
import re
import os


# LLM setup
def llm_setup():
    filename = "gemma-2_2B-texttosql-with_instrction-merged_gguf_q8.gguf"
    llm = Llama(model_path=os.path.join("models", filename))

    return llm


def format_prompt_llama(sentence):
    prompt = f"<start_of_turn>user\nYou are a helpful and competent SQL Query writer, please turn the following English-language request, marked by <REQUEST> tags, and turn it into a semantically equivalent, syntactically correct SQL query.\n<REQUEST>{sentence}</REQUEST><end_of_turn>\n<start_of_turn>model"
    return prompt


def chat(model_llama, query):
    prompt = format_prompt_llama(query)

    output = model_llama(
        prompt, max_tokens=128, echo=True)
    print("###########################################################")
    reply = re.search(
        r'<start_of_turn>model\n(.*?;)',
        output["choices"][0]["text"])

    if reply is not None:
        return reply.group(1)

    return output["choices"][0]["text"]
