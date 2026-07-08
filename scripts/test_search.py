from modules.search import JobSearcher

searcher = JobSearcher()

query = """
Python
Machine Learning
Streamlit
FAISS
LLMs
"""

results = searcher.search(query)

print()

for i, job in enumerate(results, start=1):

    print("=" * 60)

    print(i)

    print(job["job_title"])

    print(job["company"])

    print(job["job_location"])

    print(job["score"])