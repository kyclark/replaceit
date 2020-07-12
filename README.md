# replaceit

Python program to replace letters to create new word, inspired by https://www.npr.org/2020/07/12/890052466/puzzle-remove-it-replace-it.

```
$ ./replaceit.py -h
usage: replaceit.py [-h] [-w FILE] str str

Replace letters to create new word

positional arguments:
  str                   Substring to replace
  str                   Word

optional arguments:
  -h, --help            show this help message and exit
  -w FILE, --wordlist FILE
                        File of words (default: /usr/share/dict/words)
```

For example:

```
$ ./replaceit.py it ignite
ignore
ignote
```
