import pandas as pd
import time
from analyzer import analyze_sales_call # ייבוא פונקציית הליבה שיצרנו בשלב 2

def process_csv(input_csv: str, output_csv: str):
    """
    קוראת קובץ CSV של שיחות, שולחת כל שיחה לניתוח ב-API, ושומרת את התוצאות לקובץ חדש.
    """
    print(f"Loading data from {input_csv}...")

    # 1. קריאת הנתונים בעזרת Pandas
    try:
        df = pd.read_csv(input_csv)
    except FileNotFoundError:
        print(f"Error: Could not find {input_csv}. Did you run generate_data.py?")
        return

    print(f"Found {len(df)} calls to process. Starting batch analysis...\n")

    # רשימה ריקה לשמירת תוצאות הניתוח
    analysis_results = []

    # 2. לולאת עיבוד (Iterating over rows)
    for index, row in df.iterrows():
        call_id = row['call_id']
        transcript = row['transcript']

        print(f"Analyzing call {call_id} ({index + 1}/{len(df)})...")

        # 3. קריאה לפונקציית ה-API שלנו
        result = analyze_sales_call(transcript)
        analysis_results.append(result)

        # 4. מנגנון הגנה: Rate Limiting
        # המתנה של שניה אחת בין קריאה לקריאה כדי לא להציף את ה-API ולהיחסם
        time.sleep(1)

    # 5. הוספת עמודת התוצאות לטבלה הקיימת ושמירה לקובץ חדש
    df['ai_analysis'] = analysis_results
    df.to_csv(output_csv, index=False)

    print(f"\nSuccess! Processing complete. Results saved to {output_csv}")

if __name__ == "__main__":
    process_csv(input_csv="calls.csv", output_csv="analyzed_calls.csv")