Project Explainer — Customer Feedback Sentiment Analyzer (one page)

What it does:
- Analyzes customer feedback text and returns Positive / Negative / Neutral and a small score.

How it works (simple):
1. Text is converted to lowercase.
2. Presence of words is checked against positive and negative lists.
3. Score = (pos - neg) / (pos + neg) if any keywords present; otherwise 0.
4. Label is chosen based on which count is higher.

Why this design:
- Transparent and fast for demo and interview purposes.
- Useful for support teams for quick triage of tickets.

How to demo (2 minutes):
1. Run the app and open the browser.
2. Paste a customer message and click Analyze.
3. Explain the core logic (refer to Code_Explanation_Guide.pdf).

Future improvement:
- Replace `sentiment_core.analyze` with a trained ML model (e.g., Logistic Regression or BERT) for better context understanding.
