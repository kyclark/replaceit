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

To test:

```
$ pytest -xv test.py
============================= test session starts ==============================
...

test.py::test_exists PASSED                                              [  6%]
test.py::test_usage PASSED                                               [ 12%]
test.py::test_bad_file PASSED                                            [ 18%]
test.py::test_not_a_sub PASSED                                           [ 25%]
test.py::test_01 PASSED                                                  [ 31%]
test.py::test_02 PASSED                                                  [ 37%]
test.py::test_03 PASSED                                                  [ 43%]
test.py::test_04 PASSED                                                  [ 50%]
test.py::test_05 PASSED                                                  [ 56%]
test.py::test_06 PASSED                                                  [ 62%]
test.py::test_07 PASSED                                                  [ 68%]
test.py::test_08 PASSED                                                  [ 75%]
test.py::test_09 PASSED                                                  [ 81%]
test.py::test_10 PASSED                                                  [ 87%]
test.py::test_11 PASSED                                                  [ 93%]
test.py::test_12 PASSED                                                  [100%]

============================== 16 passed in 2.00s ==============================
```
