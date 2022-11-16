import fasttokenizer, os
from rich.progress import track


segmenter = fasttokenizer.Segmenter()







for name in track(os.listdir('extracted'), description="Processing..."):
    with open('extracted/'+name, 'r', encoding="utf8") as f:
        text = f.read()
        output: str = segmenter.normalize_and_segment(text)
        tokens = output.split()

        paragraphs = ' '.join(tokens).split('.')

        
        for i, p in enumerate(paragraphs):
            if p:
                with open('paragraphs/'+name+'_'+str(i), 'w', encoding="utf8") as f:
                    f.write(p)
    