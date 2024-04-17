from flask import Flask
from flask import request
# from model import mask_generation

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

app = Flask(__name__)

base_model_id = "mistralai/Mistral-7B-v0.1"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_id,  # Mistral, same as before
    quantization_config=bnb_config,  # Same quantization config as before
    device_map="auto",
    trust_remote_code=True,
)

eval_tokenizer = AutoTokenizer.from_pretrained(base_model_id, add_bos_token=True, trust_remote_code=True)

ft_model = PeftModel.from_pretrained(base_model, "checkpoint-75")
print("Model generated")

def mask_generation(eval_prompt):
    model_input = eval_tokenizer(eval_prompt, return_tensors="pt").to("cuda")

    ft_model.eval()
    with torch.no_grad():
        return (eval_tokenizer.decode(ft_model.generate(**model_input, max_new_tokens=100, repetition_penalty=1.15)[0], skip_special_tokens=True))

def formatting_func(text):
    question=text
    prompt=f"### The given text input delimited by three backticks has some personal informations, generate PII masks for those informations.\n ```{question}```"
    return prompt

@app.route('/', methods=['GET', 'POST'])
def ganerate():
    query= request.args.get("data")
    return mask_generation(formatting_func(query))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=106)