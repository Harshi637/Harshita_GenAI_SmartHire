import hashlib
import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AIzaSyBpi542uGiqaAbH7Aj1I_3pXf6PSu1_xqs")
)

CACHE_DIR = "cache/resumes"
os.makedirs(CACHE_DIR, exist_ok=True)


def get_resume_hash(resume_text: str):
    return hashlib.sha256(
        resume_text.encode("utf-8")
    ).hexdigest()


def call_gemini(resume_text: str):

    prompt = f"""
You are an expert resume parser.

Extract ONLY the following JSON.

Return valid JSON only.

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "education":[],
    "experience":[],
    "projects":[],
    "target_role":""
}}

Resume:

{resume_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

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