import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Brand Monitor", page_icon="")

st.title("AI Sentiment & Brand Monitor")
st.markdown("""
This app uses **Natural Language Processing (NLP)** to analyze the emotion behind text. 
Perfect for monitoring social media, product reviews, or customer support tickets.
""")

# --- NAVIGATION ---
menu = ["Live Analysis", "Batch Analysis (CSV)"]
choice = st.sidebar.selectbox("Select Feature", menu)

# --- FEATURE 1: LIVE ANALYSIS ---
if choice == "Live Analysis":
    st.subheader("Check a Single Review")
    raw_text = st.text_area("Enter text here...", "I love this product! It's amazing.")
    
    if st.button("Analyze"):
        analysis = TextBlob(raw_text)
        # Polarity: -1 (Negative) to 1 (Positive)
        # Subjectivity: 0 (Fact) to 1 (Opinion)
        
        col1, col2 = st.columns(2)
        with col1:
            if analysis.sentiment.polarity > 0:
                st.success(f"Positive Sentiment (Score: {analysis.sentiment.polarity:.2f})")
            elif analysis.sentiment.polarity < 0:
                st.error(f"Negative Sentiment (Score: {analysis.sentiment.polarity:.2f})")
            else:
                st.warning(f"Neutral Sentiment (Score: {analysis.sentiment.polarity:.2f})")
        
        with col2:
            st.info(f"Subjectivity: {analysis.sentiment.subjectivity:.2f} (1.0 = Highly Opinionated)")

# --- FEATURE 2: BATCH ANALYSIS ---
else:
    st.subheader("Bulk Review Analysis")
    uploaded_file = st.file_uploader("Upload a CSV file (Must have a 'Review' column)", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'Review' in df.columns:
            # Apply NLP to every row
            df['Polarity'] = df['Review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
            df['Sentiment'] = df['Polarity'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
            
            st.write(df.head())
            
            # Chart: Sentiment Distribution
            st.subheader("Brand Health Overview")
            fig, ax = plt.subplots()
            df['Sentiment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c', '#95a5a6'], ax=ax)
            st.pyplot(fig)
        else:
            st.error("Error: CSV must contain a column named 'Review'")