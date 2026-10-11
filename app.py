import streamlit as st
import pandas as pd
from analyzer import analyze_sales_call

# 1. הגדרות דף בסיסיות ל-Streamlit
st.set_page_config(page_title="Sales Call Analyzer", page_icon="📈", layout="wide")

# 2. כותרת ותיאור הממשק
st.title("📞 Call Center AI Evaluator")
st.markdown("""
Welcome to the AI-powered Sales Call Analyzer. 
Upload a transcript or type one manually to evaluate salesperson performance using **Chain-of-Thought** prompting.
""")

st.divider()

# 3. חלוקה ללשוניות (Tabs) - מראה על חשיבה חוויית משתמש (UX)
tab1, tab2 = st.tabs(["Analyze Single Call", "Batch Processing Results"])

with tab1:
    st.subheader("Manual Analysis")
    # אזור הזנת טקסט למשתמש
    user_transcript = st.text_area(
        "Enter Call Transcript:",
        height=150,
        placeholder="Customer: I am not interested. Salesperson: OK, bye."
    )

    # כפתור הפעלה
    if st.button("Analyze Call", type="primary"):
        if user_transcript.strip() == "":
            st.warning("Please enter a transcript first.")
        else:
            # ספינר טעינה שנותן פידבק ויזואלי בזמן שה-API רץ
            with st.spinner("AI is analyzing the call..."):
                analysis_result = analyze_sales_call(user_transcript)

            st.success("Analysis Complete!")
            # הצגת התוצאה בתוך תיבה יפה
            st.info(analysis_result)

with tab2:
    st.subheader("Batch Processed Data")
    st.markdown("Here are the results of our backend batch processing script (`analyzed_calls.csv`):")

    # טעינת והצגת קובץ התוצאות מהשלב הקודם (אם קיים)
    try:
        df = pd.read_csv("analyzed_calls.csv")
        st.dataframe(df, use_container_width=True)
    except FileNotFoundError:
        st.error("The file 'analyzed_calls.csv' was not found. Please run the batch processor script first.")