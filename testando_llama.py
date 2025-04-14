from transformers import pipeline

pipe = pipeline("text-generation", model="ahxt/LiteLlama-460M-1T")

prompt = """prompt = "Responda em português: O que é a linguagem Python?"""

resultado = pipe(
    prompt,
    max_length=80,
    min_length=30,
    temperature=0.7,           # equilíbrio entre criatividade e coerência
    top_p=0.9,                 # só considera palavras mais prováveis
    repetition_penalty=1.2    # evita repetições
    
)

print(resultado[0]['generated_text'])