#t5 implementation of PII masking
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("./checkpoint-35500", return_dict = False)

def mask_prediction(text):
    text = "mask PII: " + text
    tokenized = tokenizer([text], truncation = True, padding="longest", return_tensors = 'pt')
    #tokenized = {k: v.to('cuda') for k, v in tokenized.items()}
    tokenized_result = model.generate(**tokenized, max_length = 128)
    tokenized_result = tokenized_result.to('cpu')
    predicted_summary = tokenizer.decode(tokenized_result[0])
    return predicted_summary
