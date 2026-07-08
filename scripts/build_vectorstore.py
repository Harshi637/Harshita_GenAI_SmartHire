import faiss
import pickle

from modules.embedding import embed_text
from modules.embedding import load_jobs
from modules.embedding import prepare_job_text

print("Loading jobs...")

df = load_jobs()

jobs = prepare_job_text(df)

print(f"{len(jobs)} jobs loaded.")

print("Generating embeddings...")

embeddings = embed_text(jobs)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "vectorstore/jobs.index"
)

with open("vectorstore/jobs.pkl", "wb") as f:
    pickle.dump(df, f)

print("Vectorstore created successfully!")