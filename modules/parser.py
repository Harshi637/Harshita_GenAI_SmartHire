import hashlib
import json
import os

import time
from google.genai.errors import ServerError

from config import GEMINI_MODEL, RESUME_CACHE_DIR

from utils.gemini_client import client

CACHE_DIR = RESUME_CACHE_DIR
os.makedirs(CACHE_DIR, exist_ok=True)


def get_resume_hash(resume_text: str):
    return hashlib.sha256(
        resume_text.encode("utf-8")
    ).hexdigest()


def call_gemini(resume_text: str):

    prompt = f"""
You are an expert Resume Parser.

Extract information from the resume.

Return ONLY valid JSON.

Use this schema exactly.

{{
    "name": "",
    "email": "",
    "phone": "",

    "career_domain": "",

    "current_role": "",

    "target_role": "",

    "experience_years": 0,

    "experience_level": "",

    "education": [
    {
        "degree":"",
        "field":"",
        "institution":"",
        "year":""
    }],

    "skills": [],

    "certifications": [],

    "summary": ""
}}

Rules:

1. career_domain must be one of:

Software Engineering
Artificial Intelligence
Data Science
Cyber Security
Cloud Computing
Electronics
Electrical Engineering
Mechanical Engineering
Civil Engineering
Automobile
Sales
Marketing
Finance
Accounting
Human Resources
Healthcare
Education
Business
Consulting
Manufacturing
Government
Other

2. current_role

Extract the person's most recent role.

Examples:

Software Engineer

Regional Sales Manager

Embedded Engineer

Data Analyst

Mechanical Engineer

Professor

3. target_role

Infer the next logical career role.

Examples:

Software Engineer → Senior Software Engineer

Sales Executive → Sales Manager

Embedded Engineer → Senior Embedded Engineer

4. experience_years

Return only the number.

Example:

5

5. experience_level

One of

Fresher

Junior

Mid

Senior

Lead

Manager

Director

6. summary

Write a professional summary in under 80 words.

7. If a field is missing, return an empty string or empty list.
8. Determine the candidate's profession from the entire resume, not just the skills section.

9. Never classify an Electronics, Mechanical, Civil, Sales, Marketing, HR, Finance, or Healthcare resume as Software Engineering unless there is clear evidence.

10. If the career domain is uncertain, return "Other".

Resume:

{resume_text}
"""

    for _ in range(3):  # Try up to 3 times
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )
            break
        except ServerError as e:
            print(f"Server error occurred: {e}")
            time.sleep(2)  # Wait before retrying
    else:
        return {
    "error": "Gemini is temporarily unavailable."
}
    text = response.text.strip()

    if text.startswith("```"):
        text = (
            text.replace("```json", "")
                .replace("```", "")
                .strip()
        )

    return json.loads(text)


def parse_resume(resume_text):

    resume_hash = get_resume_hash(resume_text)

    cache_file = os.path.join(
        CACHE_DIR,
        f"{resume_hash}.json"
    )

    # Load from cache
    if os.path.exists(cache_file):

        with open(cache_file, "r") as f:
            return json.load(f)

    # Gemini API
    profile = call_gemini(resume_text)

    # Save cache
    with open(cache_file, "w") as f:
        json.dump(profile, f, indent=4)

    return profile