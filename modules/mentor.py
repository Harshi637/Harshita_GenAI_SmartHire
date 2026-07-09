from config import GEMINI_MODEL
from utils.gemini_client import client


def ask_mentor(profile, job, question):

    prompt = f"""
You are an experienced AI Career Mentor.

Candidate Profile:
{profile}

Recommended Job

Title:
{job['job_title']}

Skills:
{job['job_skills']}

Summary:
{job['job_summary']}

Student Question:
{question}

Instructions:
- Give practical advice.
- Keep the response under 300 words.
- Use bullet points where appropriate.
- If a roadmap is requested, provide a step-by-step plan.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text