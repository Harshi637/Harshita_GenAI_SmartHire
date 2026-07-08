import pandas as pd
from sentence_transformers import SentenceTransformer

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_jobs(csv_path="data/postings_small.csv"):
    """
    Load jobs dataset and clean missing values.
    """
    df = pd.read_csv(csv_path)

    # Keep only the required columns
    columns = [
        "job_title",
        "company",
        "job_location",
        "job_type",
        "job_summary",
        "job_skills",
    ]

    df = df[columns]

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