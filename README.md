# 🧠 Personal Note Assistant (CLI)

A simple **LangChain-powered CLI assistant** that can **summarize** your notes and **answer questions** about them.

---

## 🚀 Features
- Summarizes your notes into concise bullet points.
- Answers questions based on your notes using vector search.
- Simple CLI interface—no extra setup beyond cloning and installing.

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/note_assistant.git
cd note_assistant

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

export OPENAI_API_KEY=your_key_here      # macOS/Linux
setx OPENAI_API_KEY "your_key_here"      # Windows PowerShell

python app.py

$ python app.py
📄 Enter the path to your notes file (default: data/sample_notes.txt): 
