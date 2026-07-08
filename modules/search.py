import faiss
import pickle

from modules.embedding import embed_text

from config import VECTOR_INDEX_PATH, VECTOR_METADATA_PATH, TOP_K

class JobSearcher:

    def __init__(self):

        self.index = faiss.read_index(
            VECTOR_INDEX_PATH
        )

        with open(
            VECTOR_METADATA_PATH,
            "rb"
        ) as f:

            self.jobs = pickle.load(f)

    def search(self, query, top_k=TOP_K):

        query_embedding = embed_text([query])

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx, distance in zip(
            indices[0],
            distances[0]
        ):

            job = self.jobs.iloc[idx].to_dict()

            job["score"] = float(distance)

            results.append(job)

        return results