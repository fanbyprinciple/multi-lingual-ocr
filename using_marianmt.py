from transformers import MarianTokenizer, MarianMTModel

src='bn'
dst='en'

model_name = f'Helsinki-NLP/opus-mt-{src}-{dst}'
model = MarianMTModel.from_pretrained(model_name)

print(f"Model loaded {model_name}")
tokenizer = MarianTokenizer.from_pretrained(model_name)

sample_text = "আমি বাংলায় গান গাই।"
batch = tokenizer([sample_text], return_tensors="pt")
gen = model.generate(**batch)
result = tokenizer.batch_decode(gen,skip_special_tokens=True)

print(result)
