import faiss
from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer('msmarco-distilbert-base-dot-prod-v3')

index = faiss.read_index('asjp.index')

query = "جامعة العربي بن مهيدي أم البواقي حسب ة و الحركية لدى التالميذ"


def search(query, top_k, index, model):
    t=time.time()
    query_vector = model.encode([query])
    top_k = index.search(query_vector, top_k)
    print('>>>> Results in Total Time: {}'.format(time.time()-t))
    top_k_ids = top_k[1].tolist()[0]
    top_k_ids = list(np.unique(top_k_ids))
    results =  [idx for idx in top_k_ids]
    return results


print(search(query, 5, index, model))