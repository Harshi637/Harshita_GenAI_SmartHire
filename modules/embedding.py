import pandas as pd
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, DATASET_PATH

model = SentenceTransformer(EMBEDDING_MODEL)

def load_jobs(csv_path=DATASET_PATH):
    """
    Load and standardize different job datasets.
    """

    df = pd.read_csv(csv_path)

    # -------- New Dataset --------
    if "Job_Title" in df.columns:

        df = df.rename(columns={
            "Job_Title": "job_title",
            "Company": "company",
            "City": "job_location",
            "Job_Type": "job_type",
            "Skills_Required": "job_skills",
            "Industry": "industry",
            "Experience_Level": "experience_level",
            "Education_Required": "education_required",
            "Work_Mode": "work_mode",
            "Salary_LPA": "salary"
        })

        # Build a richer summary for embeddings
        df["job_summary"] = (
            "Industry: " + df["industry"].fillna("") +
            "\nExperience: " + df["experience_level"].fillna("") +
            "\nEducation: " + df["education_required"].fillna("") +
            "\nWork Mode: " + df["work_mode"].fillna("") +
            "\nSalary (LPA): " + df["salary"].astype(str)
        )

    # -------- Old Dataset --------
    else:

        columns = [
            "job_title",
            "company",
            "job_location",
            "job_type",
            "job_summary",
            "job_skills",
        ]

        df = df[columns]

    # Keep only the columns used by the app
    required_columns = [
        "job_title",
        "company",
        "job_location",
        "job_type",
        "job_summary",
        "job_skills",
    ]

    df = df[required_columns]

    df.fillna("", inplace=True)

    return df


def prepare_job_text(df):
    """
    Combine useful job fields into one text block.
    """

    jobs = []

    for _, row in df.iterrows():

        text = f"""
Job Title: {row['job_title']}

Company: {row['company']}

Location: {row['job_location']}

Type: {row['job_type']}

Skills:
{row['job_skills']}

Summary:
{row['job_summary']}
"""

        jobs.append(text.strip())

    return jobs


def embed_text(texts):
    """
    Generate embeddings.
    """

    embeddings = model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings