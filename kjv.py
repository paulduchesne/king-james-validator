import json
import pathlib
import pydash
import re
import requests
import sys

def text_normalise(t):

    # convert linebreaks to spaces.

    t = t.replace('\r', ' ')
    t = t.replace('\n', ' ')

    # split to array.

    t = t.split(' ')

    # cast lowercase and remove any non-alpha characters.

    t = [x.lower() for x in t]
    t = [re.sub(r'[^a-zA-Z]', '', x)  for x in t]

    # sort and remove empty strings.

    t = sorted([x for x in t if x])

    return t

kjv = pathlib.Path.cwd() / 'words.json'
if not kjv.exists():

    # pull from gutenberg.

    r = requests.get('https://www.gutenberg.org/cache/epub/10/pg10.txt')
    if r.status_code != 200:
        raise Exception('API call failed.')

    # remove header and footer.

    t = r.text
    t = t.split('*** START OF THE PROJECT GUTENBERG EBOOK THE KING JAMES VERSION OF THE BIBLE ***')[1]
    t = t.split('*** END OF THE PROJECT GUTENBERG EBOOK THE KING JAMES VERSION OF THE BIBLE ***')[0]

    # normalise.

    t = text_normalise(t)

    # unique words only, and sort.

    t = pydash.uniq(t)
    t = sorted([x for x in t if x])

    # export word list.

    with open(kjv, 'w') as words_out:
        json.dump({'words':t}, words_out, indent=4)

# load kjv word array.

with open(kjv) as kjv_words:
    kjv_words = json.load(kjv_words)['words']

# load comparison text.

input_file = pathlib.Path.cwd() / sys.argv[1]
if not input_file.exists():
    raise Exception('Input file not found.')

with open(input_file) as input_text:
    input_text = input_text.read()

word_array = text_normalise(input_text)

# determine score for all words.

a = [(x in kjv_words) for x in word_array]
total_score = round((sum(a)/len(a)), 2)

# determine score for unique words.

b = pydash.uniq(word_array)
b = [(x in kjv_words) for x in b]
unique_score = round((sum(b)/len(b)), 2)

# print results.

print({
    'text': input_file.name,
    'total_score': total_score,
    'unique_score': unique_score
    })

