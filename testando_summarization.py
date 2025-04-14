from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ In ancient Rome, there was the habit of celebrating the birthday of a person. 
There weren’t parties like we know today, but cakes were prepared and offers were made. 
Then, the habits of wishing happy birthday, giving gifts and lighting candles became popular as a way to protect the birthday person from devils and ensure good things to the next year in the person’s life.
 The celebrations only became popular like we know today after fourteen centuries, in a collective festival performed in Germany
"""
resultado = summarizer(ARTICLE, max_length=80, min_length=30)
print(resultado[0]['summary_text'])