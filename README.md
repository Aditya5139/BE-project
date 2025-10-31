# Customer Feedback Sentiment Analyzer

This is a **Rule-Based Sentiment Analysis Web App** built with **Python** and **Flask**.
It is designed as a lightweight tool to analyze customer feedback or support messages and return a sentiment label: **Positive**, **Negative**, or **Neutral**.

## Files
- `sentiment_core.py` — core rule-based analyzer
- `flask_app/app.py` — Flask web application
- `flask_app/templates/index.html` — web UI (Microsoft-style)
- `flask_app/static/style.css` — styling
- `PROJECT_EXPLAINER.md` — 1-page interview cheat sheet
- `resume_summary.txt` — copy-paste for resume/LinkedIn
- `Code_Explanation_Guide.pdf` — PDF guide to explain the code in interviews

## Quick start
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
```
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
python flask_app/app.py
```
4. Open your browser at `http://localhost:5000` and type customer feedback into the box, then click Analyze.

## Notes for interviews
- This is intentionally rule-based (easy to explain). You can upgrade the core to a machine-learning model later without changing the web UI.
- The API endpoint `/api/predict` accepts JSON like {"text": "..."} and returns a JSON prediction.
