from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
scaler = joblib.load("scaler.pkl")

class TextInput(BaseModel):
    text: str

app = FastAPI(title="Text Classification API")

@app.post("/predict")
async def predict(input_data: TextInput):
    
    text_vectorized = vectorizer.transform([input_data.text])
    text_scaled = scaler.transform(text_vectorized)   # scaler expects sparse matrix, no need .toarray()

    probs = model.predict_proba(text_scaled)[0]  # probabilities
    pred_class = model.predict(text_scaled)[0]   # label
    confidence = float(np.max(probs))            # max probability

    return {
      "label": str(pred_class),
      "confidence": round(confidence, 4)
    }

#To run this do uvicorn api:app --reload --port 8000
# then go to http://127.0.0.1:8000/docs 