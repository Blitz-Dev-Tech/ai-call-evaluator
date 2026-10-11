# 📞 Enterprise Sales & Customer Service AI Analyzer

An intelligent API project designed to evaluate and score sales representatives based on call transcripts, utilizing advanced Large Language Models (LLMs). This tool demonstrates how AI can be applied to call center environments to extract valuable insights from customer interactions.

## 🚀 Features
* **Advanced Prompt Engineering:** Implements Few-Shot Prompting and Chain-of-Thought (CoT) techniques to ensure the AI evaluates calls logically (Objection -> Handling -> Score) and reduces hallucinations.
* **Batch Processing:** A robust data pipeline using pandas to process multiple call transcripts from a CSV file automatically.
* **Resilience:** Built-in error handling and rate-limiting to prevent API blocks and ensure smooth execution during bulk analysis.
* **Interactive UI:** A user-friendly web interface built with Streamlit for rapid manual testing and viewing batch results.

## 🛠️ Tech Stack
* Python 3.12
* OpenAI API (gpt-4o-mini)
* Pandas (Data manipulation)
* Streamlit (Frontend/UI)

python-dotenv (Environment variables management)

## ⚙️ Installation & Setup
Clone the repository:
git clone https://github.com/Blitz-Dev-Tech/ai-call-evaluator.git

Create a virtual environment and install dependencies:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create a .env file in the root directory and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

## 💻 Usage
To run the batch processing script:
python batch_processor.py

To launch the Streamlit Web Interface:
python -m streamlit run app.py
