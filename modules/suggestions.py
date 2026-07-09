from config import GEMINI_MODEL

from utils.gemini_client import client
from google.genai.errors import ClientError,ServerError

import time

def generate_suggestions(profile, job):

    prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

Your goal is to improve the candidate's resume for THEIR OWN career domain.

Candidate Profile

{profile}

Matched Job

Title:
{job["job_title"] if job else "No suitable job match"}

Industry:
{job.get("industry", "Unknown") if job else "Unknown"}

Required Skills:
{job.get("job_skills", "Not Available") if job else "Not Available"}

Summary:
{job.get("job_summary", "Not Available") if job else "Not Available"}

Rules:

1. First determine the candidate's career domain from the profile.

2. Respect the candidate's profession.

3. Never recommend Software Engineering, AI, Data Science,
Programming, Cloud, DevOps or Cyber Security skills unless:

- the candidate already belongs to that domain, OR
- the candidate explicitly wants to change careers.

4. If the matched job does not belong to the candidate's domain,
ignore the matched job and generate suggestions only from the resume.

5. Recommend:

• missing domain-specific skills

• relevant certifications

• resume improvements

• stronger professional summary

• realistic next career steps

6. If the candidate has more than 8 years of experience,
focus on:

- leadership
- management
- strategy
- communication
- certifications
- industry trends

instead of beginner technical skills.

Return the response in Markdown exactly in this format.

# ATS Score

Score: xx/100

# Missing Skills

- ...

# Resume Improvements

- ...

# Recommended Certifications

- ...

# Professional Summary

...

# Top Action Items

- ...
"""

    for _ in range(3):

        try:

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )

            return response.text

        except ServerError:
            time.sleep(3)

        except ClientError:
            return None

    return None
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text