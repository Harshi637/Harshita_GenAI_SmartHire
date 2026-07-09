import time
from google.genai.errors import ServerError, ClientError
from config import GEMINI_MODEL
from utils.gemini_client import client


def ask_mentor(profile, job, question):

    profile_text = f"""
Career Domain:
{profile.get("career_domain", "")}

Current Role:
{profile.get("current_role", "")}

Target Role:
{profile.get("target_role", "")}

Experience:
{profile.get("experience_years", "")} years

Experience Level:
{profile.get("experience_level", "")}

Skills:
{", ".join(profile.get("skills", []))}

Education:
{profile.get("education", [])}

Summary:
{profile.get("summary", "")}
"""

    if job:

        job_text = f"""
Matched Job

Title:
{job.get("job_title", "")}

Industry:
{job.get("industry", "")}

Skills:
{job.get("job_skills", "")}

Summary:
{job.get("job_summary", "")}
"""

    else:

        job_text = """
No suitable job match was found.
Use only the candidate profile.
"""

    prompt = f"""
You are an experienced Career Mentor.

Candidate Profile

{profile_text}

{job_text}

Candidate Question

{question}

Rules:

1. The candidate's career domain is the highest priority.

2. Never recommend another profession unless the candidate explicitly asks for a career switch.

3. Use the matched job only as supporting information.

4. If the matched job conflicts with the candidate's profession,
ignore it.

5. Tailor your advice according to experience level:

• Fresher → learning roadmap, projects, internships

• Junior → technical growth and certifications

• Mid → specialization and career progression

• Senior → leadership, mentoring, architecture, management

• Manager/Director → strategy, business impact, leadership

6. Recommend only domain-relevant skills and certifications.

7. Keep the answer practical.

8. Use headings.

9. Use bullet points.

10. If the user asks for a roadmap,
provide a month-wise roadmap.

Suggested response format:

## Current Situation

...

## Recommendations

...

## Skills to Learn

...

## Certifications

...

## Next Steps

...
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
            return "⚠️ Career Mentor is temporarily unavailable due to an API issue. Please try again later."

    return "⚠️ Gemini servers are currently busy. Please try again in a few minutes."