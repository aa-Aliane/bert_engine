import tika, os
from tika import parser, language
import re

from tqdm import tqdm

import json
with open('data.json', 'r') as f:
    all_f = json.loads(f.read())


for j in tqdm(os.listdir('asjp')):
    for i, name in enumerate(os.listdir('asjp/'+j)):       
        try:
            if os.path.getsize('asjp/'+j+'/'+name) < 1000000:
                parsed = parser.from_file('asjp/'+j+'/'+name)
                filename = name[7:-4]
                content = parsed['content']
                
                # metadata = parsed['metadata']
                # title = metadata['title']
                content = re.sub("\n|\r", "", content)
                # print(filename)
                # print(len(content))
                if len(content) > 1000:
                    with open('extracted/'+filename+'.txt', 'w', encoding="utf8") as f:
                        f.write(content)
                        f.close()
        except:
            pass




for i, name in enumerate(tqdm(os.listdir('asjp/581/'))):       
    try:
        if os.path.getsize('asjp/581/'+name) < 1000000:
            parsed = parser.from_file('asjp/581/'+name)
            filename = name[7:-4]
            content = parsed['content']
            
          
            
            metadata = parsed['metadata']
            # print(metadata)
            # title = metadata['title']
            content = re.sub("\n|\r", "", content)
            # print(filename)
            # print(len(content))
            print(content)
            if len(content) > 1000:
                with open('extracted/'+filename+'.txt', 'w', encoding="utf8") as f:
                    f.write(content)
                    f.close()
    except:
        pass
