import os

from dotenv import load_dotenv
from google import genai

from config import GEMINI_MODEL

load_dotenv()

from utils.gemini_client import client
from google.genai.errors import ClientError

def generate_suggestions(profile, job):

    prompt = f"""
You are an ATS Resume Expert.

Candidate Profile

{profile}

Target Job

Title:
{job["job_title"]}

Skills:
{job["job_skills"]}

Summary:
{job["job_summary"]}

Return markdown in exactly this format.

# ATS Score

Score: xx/100

# Missing Skills

- ...

# Resume Improvements

- ...

# Professional Summary

...

# Top Action Items

- ...
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text

    except ClientError:

        return None