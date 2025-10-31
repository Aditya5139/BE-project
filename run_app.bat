@echo off
echo ----------------------------------------
echo Starting Customer Feedback Sentiment Analyzer...
echo ----------------------------------------

cd C:\Users\adity\Downloads\Product sentiment analysis in ecommerce
call venv\Scripts\activate.bat
python flask_app\app.py

pause
