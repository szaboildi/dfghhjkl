from transformers import AutoTokenizer, AutoModelForCausalLM
import re


def gen_prompt(tokenizer, sentence):
    converted_sample = [
        {"role": "user", "content": sentence},
    ]
    prompt = tokenizer.apply_chat_template(converted_sample,
                                           tokenize=False,
                                           add_generation_prompt=True)
    return prompt

def generate(model, tokenizer, query, max_new_tokens=128, skip_special_tokens=False):
    prompt = gen_prompt(tokenizer, query)

    tokenized_input = tokenizer(prompt, add_special_tokens=False, return_tensors="pt").to(model.device)

    model.eval()
    generation_output = model.generate(**tokenized_input,
                                       eos_token_id=tokenizer.eos_token_id,
                                       max_new_tokens=max_new_tokens)

    output = tokenizer.batch_decode(generation_output,
                                    skip_special_tokens=skip_special_tokens)
    reply = re.search('<\|assistant\|>(.*?)<\|end\|><\|endoftext\|>', output[0]).group(1)

    if reply is None:
        return output[0]
    return reply


def main():
    model_id = "szaboildi/phi3-mini-4k-instruct-texttosql-merged-noinstruction_gguf"
    filename = "phi3-mini-4k-instruct-texttosql-merged-noinstruction_gguf_q8.gguf"

    tokenizer = AutoTokenizer.from_pretrained(model_id, gguf_file=filename)
    model = AutoModelForCausalLM.from_pretrained(model_id, gguf_file=filename)

    while True:
        prompt = input()
        output = generate(model, tokenizer, prompt)
        print(output)
        cont = input("Would you like to continue? [Y/N] ")
        if cont.lower() != "y" and cont.lower() != "yes":
            break

if __name__ == "__main__" :
    main()
