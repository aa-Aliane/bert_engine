import tika, os
from tika import parser, language
import re

from tqdm import tqdm



for i, name in enumerate(tqdm(os.listdir('data'))):
    parsed = parser.from_file('0/'+name)
    content = parsed['content']
    metadata = parsed['metadata']
    content = re.sub("\n|\r", "", content)

    print(metadata['dc:title'])

    if len(content) > 200:
        with open('extracted/'+str(i)+'.txt', 'w', encoding="utf8") as f:
            f.write(content)
            f.close()



