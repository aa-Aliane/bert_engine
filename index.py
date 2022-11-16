import os, faiss
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L12-v1')





alldocs = []

for name in os.listdir('paragraphs'):
    with open('paragraphs/'+name, 'r', encoding="utf8") as f:
        alldocs += [f.read()]
        
encoded_data = model.encode(alldocs)
encoded_data = np.asarray(encoded_data.astype('float32'))
index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
index.add_with_ids(encoded_data, np.array(range(0, len(alldocs))))
faiss.write_index(index, 'asjp.index')
