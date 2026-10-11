import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. טעינת משתני הסביבה (מפתח ה-API מהקובץ .env)
load_dotenv()

# 2. אתחול הלקוח של OpenAI
# הוא אוטומטית מחפש את OPENAI_API_KEY במשתני הסביבה
client = OpenAI()

def analyze_sales_call(transcript: str) -> str:
    """
    מקבלת תמליל שיחה ומחזירה ניתוח מבוסס AI של ביצועי איש המכירות.
    """

    # 3. הפרומפט המורכב (System Prompt)
    system_prompt = """
    You are an expert Sales Manager evaluating sales calls.
    Your goal is to analyze the salesperson's performance based on the transcript provided.

    # INSTRUCTIONS (Chain-of-Thought)
    Please think step-by-step and structure your response exactly like this:
    1. Objection: Identify the customer's main objection.
    2. Handling: Evaluate how the salesperson handled it (Good/Bad and why).
    3. Score: Provide a final score from 1 to 10.

    # EXAMPLES (Few-Shot Prompting)

    Example 1:
    Transcript: "Customer: It's too expensive for us right now. Salesperson: But it has many features! Customer: Still too much."
    Analysis:
    1. Objection: Price and budget constraints.
    2. Handling: Poor. The salesperson became defensive and pushed features instead of exploring the underlying budget concern.
    3. Score: 3/10.

    Example 2:
    Transcript: "Customer: We are already using a competitor. Salesperson: I appreciate your transparency. What do you like most about them?"
    Analysis:
    1. Objection: Loyalty to a competitor.
    2. Handling: Excellent. The salesperson validated the customer and asked open-ended questions to uncover potential pain points.
    3. Score: 9/10.
    """

    # 4. עמידות (Resilience) - עטיפה ב-Try/Except
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # מודל מהיר וזול לטסטים, מספיק חכם למשימה הזו
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Analyze this transcript:\n{transcript}"}],temperature=0.3)
        return response.choices[0].message.content

    except Exception as e:
        # טיפול בשגיאות רשת, מגבלות Rate Limit או בעיות במפתח
        return f"Error: API call failed. Details: {str(e)}"

if __name__ == "__main__":
    test_transcript = "Customer: I don't have time to talk right now. Salesperson: I completely understand, your time is valuable. When would be a better time to call you back for a 5-minute chat?"

    print("Sending test transcript to API...")
    result = analyze_sales_call(test_transcript)
    print("\n--- ANALYSIS RESULT ---")
    print(result)