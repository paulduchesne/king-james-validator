# King James Validator

An interesting artistic constraint which occured to me a while ago, was to reuse only words which could be found in the King James translation of the Bible. This script validates a provided text, reporting on overlap percentage of both total and unique words.  


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