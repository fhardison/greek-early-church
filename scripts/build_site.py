from pathlib import Path
from collections import defaultdict

lines = (Path(__file__).resolve().parents[1] / Path('analysis/lem_homily.txt')).read_text().strip().split('\n')

data = defaultdict(dict)

for line in lines:
    if not line.strip():
        continue
    tag, rest = line.split(' ', maxsplit=1)
    id, linetype = tag.rsplit('.', maxsplit=1)
    data[id][linetype] = rest.split(' ')

for id, items in data.items():
    if 'title' in id:
        print('<h1>' + ' '.join(items['text']) + "</h1>")
    else:
        print('<div class="line">')
        print('<span class="line-num">' + id.split('.')[-1] + '</span>')
        for i, w in enumerate(items['text']):
            print('<ul>')
            print('<li class="text">' + w + '</li>')
            print('<li class="lemma notvisible">' + items['lemma'][i] + '</li>')
            print('</ul>')
        print('</div>')
