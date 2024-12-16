import json
import pathlib
import pydash
import re
import requests

kjv_words = pathlib.Path.cwd() / 'words.json'
if not kjv_words.exists():

    # pull text from gutenberg.

    r = requests.get('https://www.gutenberg.org/cache/epub/10/pg10.txt')
    if r.status_code != 200:
        raise Exception('API call failed.')

    # remove header and footer.

    t = r.text
    t = t.split('*** START OF THE PROJECT GUTENBERG EBOOK THE KING JAMES VERSION OF THE BIBLE ***')[1]
    t = t.split('*** END OF THE PROJECT GUTENBERG EBOOK THE KING JAMES VERSION OF THE BIBLE ***')[0]

    # convert linebreaks to spaces.

    t = t.replace('\r', ' ')
    t = t.replace('\n', ' ')

    # split to array.

    t = t.split(' ')

    # cast lowercase and remove any non-alpha characters.

    t = [x.lower() for x in t]
    t = [re.sub(r'[^a-zA-Z]', '',x)  for x in t]

    # unique words only, and sort.

    t = pydash.uniq(t)
    t = sorted([x for x in t if x])

    # render word list.

    with open(kjv_words, 'w') as words_out:
        json.dump({'words':t}, words_out, indent=4)