#!/usr/bin/env python3
"""tests for replaceit.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './replaceit.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Dies on bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -w {bad} it commit')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_not_a_sub():
    """Dies when substring does not appear in word"""

    rv, out = getstatusoutput(f'{prg} foo bar')
    assert rv != 0
    assert out == 'Substring "foo" does not appear in word "bar"'


# --------------------------------------------------
def run(word, expected):
    """ok"""

    rv, out = getstatusoutput(f'{prg} it {word}')
    assert rv == 0
    assert out.strip().split() == expected


# --------------------------------------------------
def test_01():
    """Test"""

    run('titular', ['tabular', 'tegular', 'tubular', 'tumular'])


# --------------------------------------------------
def test_02():
    """Test"""

    run('ignite', ['ignore', 'ignote'])


# --------------------------------------------------
def test_03():
    """Test"""

    run('commit', ['commie', 'commix', 'common', 'commot'])


# --------------------------------------------------
def test_04():
    """Test"""

    run('citrus', ['chorus', 'cirrus'])


# --------------------------------------------------
def test_05():
    """Test"""

    run('excite', ['excave', 'excide', 'excise', 'excuse'])


# --------------------------------------------------
def test_06():
    """Test"""

    run('citric', ['capric', 'choric', 'cleric', 'cupric', 'czaric'])


# --------------------------------------------------
def test_07():
    """Test"""

    run('invite', ['invade', 'invoke'])


# --------------------------------------------------
def test_08():
    """Test"""

    run('finite', ['finale'])


# --------------------------------------------------
def test_09():
    """Test"""

    run('marital', ['marshal', 'martial'])


# --------------------------------------------------
def test_10():
    """Test"""

    run('exploit', ['explode', 'explore'])


# --------------------------------------------------
def test_11():
    """Test"""

    run('smitten', ['smarten'])


# --------------------------------------------------
def test_12():
    """Test"""

    run('backbite', ['backbone'])


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
