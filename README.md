# SvaraAI – Reply Classification Project

This project implements a reply classification pipeline for outbound sales replies using ML/NLP, along with a FastAPI deployment.

## 📦 Project Structure

- `notebook.ipynb` – **Part A**: ML/NLP pipeline (data preprocessing, baseline model, transformer fine-tuning, evaluation, and model selection)  
- `api.py` – **Part B**: FastAPI application exposing `/predict` endpoint  
- `answers.md` – **Part C**: Short reasoning answers  
- `requirements.txt` – Python dependencies  

## ⚙️ Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server
Navigate to the directory containing `api.py` and run:
```bash
uvicorn api:app --reload --port 8000
```

### 3. Access the API
Open your browser at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 4. Sample Texts for Testing
- "Plz provide contract terms"
- "Lets arrange demo next week"
- "Dont have budget for this"

## 🔬 Part A – ML Pipeline

Run `notebook.ipynb` to execute the complete ML pipeline, which includes:

- **Data loading and preprocessing**
- **Baseline model training** (Logistic Regression / LightGBM)
- **Transformer fine-tuning** (distilbert-base-uncased)
- **Model evaluation** (Accuracy + F1 score)
- **Final model selection and reasoning** at the end of the notebook

## 🚀 Part B – FastAPI Deployment

The `api.py` file provides a FastAPI application with:
- `/predict` endpoint for reply classification
- Interactive API documentation at `/docs`
- Real-time model inference

## 💭 Part C – Reasoning

See `answers.md` for short reasoning answers covering:
- Improving the model with only 200 labeled replies
- Ensuring the model avoids biased or unsafe outputs
- Prompt design strategies for personalized cold email openers

## 📋 Requirements

- **Python version**: >= 3.10 recommended
- **Dependencies**: Listed in `requirements.txt`
- **File organization**: Keep all project files in the same directory
