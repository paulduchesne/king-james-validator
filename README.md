# King James Validator

An interesting artistic constraint occured to me a short time ago, to use only words found in the King James translation of the Bible. 

This validator produces a short report containing a percentage score of total words which overlap and a percentage of unique words which overlap, against a source text.

**Example**

```sh
python3 kjv.py jane_austen.txt
```

returns the following report

```sh
{
    'text': 'jane_austen.txt', 
    'total_score': 0.86, 
    'unique_score': 0.24
}
```

**License**

Creative Commons Zero