from transformers import pipeline

# Load model once
classifier = pipeline(
    "sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict_sentiment(text: str):
    result = classifier(text)[0]
    return result["label"]
