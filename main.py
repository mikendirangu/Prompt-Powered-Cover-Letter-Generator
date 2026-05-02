import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Missing API key. Add it to .env file.")
    exit()

# Initialize client
client = genai.Client(api_key=API_KEY)

def generate_cover_letter(name, role, skills, company):
    prompt = f"""
Write a professional and concise cover letter.

Candidate Name: {name}
Job Role: {role}
Company: {company}
Skills: {skills}

Requirements:
- Personalized to the company
- Confident tone
- 150-200 words
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text if hasattr(response, "text") else str(response)

    except Exception as e:
        print(f"\n⚠️ API failed: {e}")
        print("🔁 Using fallback generator...\n")

        # Fallback (no API needed)
        return f"""
Dear Hiring Manager at {company},

My name is {name}, and I am excited to apply for the {role} position at your company.

With skills in {skills}, I have developed strong technical abilities that align well with your team's needs. I am passionate about building efficient and user-focused solutions, and I am eager to contribute to your organization.

I admire {company}'s commitment to innovation and excellence, and I would welcome the opportunity to bring my skills and enthusiasm to your team.

Thank you for considering my application. I look forward to the possibility of contributing to your success.

Sincerely,  
{name}
"""

def main():
    print("\n⚡ AI Cover Letter Generator (Gemini)\n")

    name = input("Enter your name: ")
    role = input("Enter job role: ")
    company = input("Enter company name: ")
    skills = input("Enter your skills (comma separated): ")

    print("\n⏳ Generating cover letter...\n")

    letter = generate_cover_letter(name, role, skills, company)

    print("📄 Your Cover Letter:\n")
    print(letter)

    with open("cover_letter.txt", "w") as f:
        f.write(letter)

    print("\n✅ Saved as cover_letter.txt")

if __name__ == "__main__":
    main()