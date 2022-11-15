import tika, os
from tika import parser, language
import re

from tqdm import tqdm



for i, name in enumerate(tqdm(os.listdir('data'))):
    parsed = parser.from_file('data/'+name)
    content = parsed['content']
    metadata = parsed['metadata']
    title = metadata['title']
    content = re.sub("\n|\r", "", content)

    print(title)

    if len(content) > 200:
        with open('extracted/'+str(i)+'.txt', 'w', encoding="utf8") as f:
            f.write(content)
            f.close()



