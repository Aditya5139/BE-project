"""
sentiment_core.py
Rule-based sentiment analyzer used for demo and interviews.
Returns: {"label": "Positive"/"Negative"/"Neutral", "score": float}
"""
def analyze(text: str):
    if not text or not text.strip():
        return {"label":"Neutral","score":0.0}
    txt = text.lower()
    # Simple keyword lists (can be extended)
    pos_keywords = ["good","great","happy","love","excellent","awesome","best","nice","like","positive","fantastic","satisfied","pleased"]
    neg_keywords = ["bad","sad","hate","terrible","worst","awful","angry","negative","boring","disappoint","unsatisfied","poor","issue","problem"]
    pos = sum(1 for k in pos_keywords if k in txt)
    neg = sum(1 for k in neg_keywords if k in txt)
    # score between -1 and 1
    if pos + neg == 0:
        score = 0.0
    else:
        score = (pos - neg) / (pos + neg)
    if pos > neg:
        label = "Positive"
    elif neg > pos:
        label = "Negative"
    else:
        label = "Neutral"
    return {"label": label, "score": round(score, 3)}
