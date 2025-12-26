git add .🧠 AI-Powered Sentiment & Brand Monitor
[Live Demo Link (Paste your Streamlit URL here)]
📖 Project Overview
This project is an NLP (Natural Language Processing) application that analyzes the emotional tone of text. It is designed for businesses to monitor brand health by automatically categorizing customer reviews, social media mentions, or support tickets into Positive, Negative, or Neutral sentiments.

🚀 Key Features
Live Emotion Analysis: Users can type or paste any text (tweets, reviews) to get an instant sentiment score and subjectivity rating.

Enterprise Batch Processing: Supports CSV file uploads, allowing for the analysis of thousands of reviews simultaneously.

Automated Data Visualization: Generates real-time Pie Charts using Matplotlib to show the percentage breakdown of customer satisfaction.

Subjectivity Detection: Distinguishes between factual information and personal opinions to help filter biased data.

🛠️ Tech Stack
Language: Python 3.13

NLP Engine: TextBlob (based on NLTK)

Web Framework: Streamlit

Data Analysis: Pandas

Visualization: Matplotlib

📊 Methodology
The system uses the TextBlob library to calculate two specific metrics for every input:

Polarity: A score from -1 (Extremely Negative) to +1 (Extremely Positive).

Subjectivity: A score from 0 (Objective/Fact) to 1 (Subjective/Opinion).
