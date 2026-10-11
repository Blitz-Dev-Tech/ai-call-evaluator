import pandas as pd

def create_sample_csv():
    """
    יוצרת קובץ CSV עם תמלילי שיחות מכירה פיקטיביים עבור הפרויקט.
    """
    data = [
        {
            "call_id": "C-100",
            "transcript": "Customer: It's too expensive. Salesperson: We can offer a 10% discount if you sign today. Customer: Still not sure..."
        },
        {
            "call_id": "C-101",
            "transcript": "Customer: I don't have time right now. Salesperson: Okay, I will call you next year. Bye."
        },
        {
            "call_id": "C-102",
            "transcript": "Customer: We use competitor X. Salesperson: That's a great product! What do you feel is missing from their offering?"
        },
        {
            "call_id": "C-103",
            "transcript": "Customer: I need to talk to my manager. Salesperson: Makes sense. Would it help if I joined that meeting to answer technical questions?"
        }
    ]

    # שימוש ב-Pandas כדי להמיר את הרשימה לטבלה (DataFrame) ולשמור כקובץ
    df = pd.DataFrame(data)
    df.to_csv("calls.csv", index=False)

    print(f"Success! Created 'calls.csv' with {len(df)} rows.")

if __name__ == "__main__":
    create_sample_csv()