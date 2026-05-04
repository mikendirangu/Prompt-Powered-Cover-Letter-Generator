# ⚡ Prompt-Powered Cover Letter Generator

An AI-powered CLI tool that generates professional cover letters using Google Gemini API and prompt engineering.

Built as part of the **Moringa AI Capstone Project**.

---

## 🚀 Overview

This project uses generative AI to automatically create personalized cover letters based on user input such as:

- Name  
- Job role  
- Skills  
- Target company  

It demonstrates how prompt engineering and AI APIs can be used to automate real-world writing tasks.

---

## 🧠 Powered By

- :contentReference[oaicite:0]{index=0}  
- Python 3.8+  
- google-genai SDK  

---

## ✨ Features

- 🧾 AI-generated cover letters  
- 🎯 Personalized output based on user input  
- 💾 Saves output to `.txt` file  
- ⚡ CLI-based lightweight tool  
- 🔁 Fallback system for API failure handling  

---

## 📦 Project Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/cover-letter-generator.git
cd cover-letter-generator
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install google-genai python-dotenv
4. Add Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
▶️ Run the Project
python main.py
🧪 Example Usage
Enter your name: Mike  
Enter job role: Frontend Developer  
Enter company: Andela  
Enter skills: React, Tailwind, APIs  
Output:

## A professional AI-generated cover letter is displayed and saved as:

cover_letter.txt
🧠 How It Works
User inputs personal and job details
A structured prompt is created
Prompt is sent to Gemini API
AI generates a professional cover letter
Output is displayed and saved locally
⚠️ Error Handling
Common Issues:
❌ Module not found
pip install google-genai
❌ Invalid model error

#Use:

model="gemini-2.0-flash"
❌ API quota exceeded
Enable billing OR
Wait for quota reset OR
App uses a fallback generator automatically
# 🔁 Fallback System

If the AI API fails, the system generates a pre-built professional cover letter template to ensure the app still works.

# 📁 Project Structure
cover-letter-generator/
│── main.py
│── .env
│── requirements.txt
│── README.md
📚 Learning Outcomes
API integration with Python
Prompt engineering for AI models
Error handling in real-world APIs
Building CLI-based applications
Working with generative AI systems
🧠 AI Prompt Strategy

Better prompts = better results.

Example improvement:

❌ Basic prompt:

Write a cover letter

✔ Improved prompt:

Write a professional cover letter for a frontend developer at Andela with React and Tailwind skills, 150–200 words, confident tone.

👨‍💻 Author

Name: Mike
Project: Moringa AI Capstone
Focus: Prompt Engineering + AI Integration

📌 License

This project is for educational purposes only.


---

