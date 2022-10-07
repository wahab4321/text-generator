from transformers import pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
res = generator("EleutherAI has", do_sample=True, min_length=20)
print(res[0]['generated_text'])
