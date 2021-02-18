# we need to install pytorch first

from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-ar-en'
sample_text = 'إذا أمكن ، تعرّف على المؤامرة مسبقًا.'


tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

translated = model.generate(**tokenizer.preprare_seq2seq_batch(sample_text, return_tensors="pt"))
tgt_text = [tokenizer.decode(t) for t in translated]

print(tgt_text)