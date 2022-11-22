from collections import defaultdict


with open('all_f.txt', 'r', encoding='utf8') as f:
    allnames = f.read().split('\n')
    
    
with open('JournalArticlesLinks2.txt', 'r', encoding='utf8') as f:
    all = f.read().split("\n\n")
    

    
all_ = defaultdict(list)

for i in range(len(all)):
    i_articles = all[i].split('\n')[3:]
    for article in i_articles:
        try:
            article_j, article = article.split('-')
            article_j = article_j[:-1]
            all_[str(i)+"_"+article_j] = article
        except:
            pass
        
all_ = {k: all_[k] for k in allnames if all_[k]!=[]}
        
from json import dumps

with open('data.json', 'w') as f:
  f.write(dumps(all_, indent=4))
        



