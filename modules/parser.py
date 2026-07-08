import json
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("AIzaSyBpi542uGiqaAbH7Aj1I_3pXf6PSu1_xqs")
)

def parse_resume(resume_text: str):

    prompt = f"""
You are an expert Resume Parser.

Extract the following information from the resume.

Return ONLY valid JSON.

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
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "").strip()

    return json.loads(text)