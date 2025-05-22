# Finetuned phi3-mini-4k model
Phi3-mini-4k model fine-tuned for a text-to-SQL task, using a subset of the [gretelai/synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql/viewer/default/train?p=999&views%5B%5D=train&row=99901) dataset.

- Base model: [microsoft/Phi-3-mini-4k-instruct.](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
- LoRA adapter: [szaboildi/phi3-mini-texttosql-adapter-no_instrction](https://huggingface.co/szaboildi/phi3-mini-texttosql-adapter-no_instrction)
- Merged model: [szaboildi/phi3-mini-4k-instruct-texttosql-merged-noinstruction](https://huggingface.co/szaboildi/phi3-mini-4k-instruct-texttosql-merged-noinstruction)
- GGUF (Q8_0): [szaboildi/phi3-mini-4k-instruct-texttosql-merged-noinstruction_gguf](https://huggingface.co/szaboildi/phi3-mini-4k-instruct-texttosql-merged-noinstruction_gguf)

The model was trained with the `LLM_finetuning_TextoSQL_phi3_SZABO.ipynb` notebook (using TRL) on google collab and is deployed in a streamlit app on [Hugging Face Spaces](https://huggingface.co/spaces/szaboildi/phi3-mini-4k-texttosql), the code for which is also duplicated in the `HF_Space_phi3-mini-4k-texttosql/` folder in this repo.

If you would like to run the final model on your local machine, you can do so from using the following commands from your terminal:
```
make setup
source .venv/bin/activate
make tryout
```
Note, that the requirements for this trial are only a subset of the requirements for the fine-tuning.

# Finetuned gemma2-2b model
Gemma2-2b model fine-tuned for a text-to-SQL task, using a subset of the [gretelai/synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql/viewer/default/train?p=999&views%5B%5D=train&row=99901) dataset.

- Base model: [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)
- Merged model: [szaboildi/gemma-2_2B-texttosql-with_instrction-merged](https://huggingface.co/szaboildi/gemma-2_2B-texttosql-with_instrction-merged)
- GGUF (Q8_0): [szaboildi/gemma-2_2B-texttosql-with_instrction-merged_gguf](https://huggingface.co/szaboildi/gemma-2_2B-texttosql-with_instrction-merged_gguf)

The model was trained with the `LLM_finetuning_TextoSQL_gemma2_2b_SZABO.ipynb` notebook (using TRL) on google collab and is deployed in a streamlit app on [Hugging Face Spaces](https://huggingface.co/spaces/szaboildi/gemma_2_2B_texttosql_finetuned), the code for which is also duplicated in the `HF_Space_gemma2_2b-texttosql/` folder in this repo.

If you would like to run the final model on your local machine, you can do so from using the following commands from your terminal (this will download a 2.6GB model file into the folder you cloned this repo to):
```
make setup_gemma
source .venv_g/bin/activate
make tryout_gemma
```
Note, that the requirements for this trial are only a subset of the requirements for the fine-tuning.
