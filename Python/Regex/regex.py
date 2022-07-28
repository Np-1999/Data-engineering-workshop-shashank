# https://www.youtube.com/watch?v=AEE9ecgLgdQ
# in blog https://www.python-engineer.com/posts/regular-expressions/
# Use raw string for pattern matching raw string r"whatever_string"

from cgi import test
import re

test_string = '123abc123abc122ABC'

pattern = re.compile(r"abc")
# Must read: https://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile
# IMP stackoverflow comment: I just ran into a case where using re.compile gave a 10-50x improvement. 
# The moral is that if you have a lot of regexes (more than MAXCACHE = 100) and you use them a lot of times each 
# (and separated by more than MAXCACHE regexes in between, so that each one gets flushed from the cache: so using the same one a lot of times 
# and then moving on to the next one doesn't count), then it would definitely help to compile them. Otherwise, it doesn't make a difference.


matches = pattern.finditer(test_string) # Creates iterable object

for match in matches:
    print(match)
# OP:
# <re.Match object; span=(3, 6), match='abc'>
# <re.Match object; span=(9, 12), match='abc'>


# findall Prints string matching with regex instead of whole match object
matches = pattern.findall(test_string)
for match in matches:
    print(match)
# OP:
# abc
# abc

# match looks if the pattern matches with the begining of string. Returns match object
pattern_2 = re.compile(r"123")
match = pattern_2.match(test_string)
print(match)
# op:
# <re.Match object; span=(0, 3), match='123'>


# Search finds first occurence matching with regex and returns match object
match = pattern.search(test_string)
print(match)
# OP:
#<re.Match object; span=(3, 6), match='abc'>


# Summary: there are match(), search(), findall() and finditer methods to find match
# and every method can be used as match(pattern, input_string)

# Meta characters : . ^ $ * + ? { } [ ] \ | ( )

# . Any character (except newline character)
pattern_dot = re.compile(r".")
matches = pattern_dot.finditer(test_string)
for match in matches:
    print(match.group())

# If we want to match with actual dot we need to use backslash \

test_string = "123abc123abc122ABC."
pattern_exact_dot = re.compile(r"\.")
matches = pattern_exact_dot.finditer(test_string)
for match in matches:
    print(match.group())

# ^ Starts with. For example "^hello" i.e. starts with hello

pattern_start_with = re.compile(r"^123")
matches = pattern_start_with.findall(test_string)
if matches:
    print('String starts with 123')

# $ Ends with

pattern_ends_with = re.compile(r"ABC\.$")
matches = pattern_ends_with.findall(test_string)
if matches:
    print("Pattern ends with ABC.")

# * Zero or more occurences


# + One or more occureences
# { } Exactly specified number of occurences
# [] A set of characters
# \ Special sequence (or escape special characters)
# | either or
# ( ) Capture and group

# More special characters
# \d : Matches any decimal digit; [0-9]
# \D : Matches any non-digit character;
# \s : Matches any whitespace character; (space " " tab "\t" newline "\n")
# \S : Matches any non-whitespace character;
# \w : Matches any alphanumeric (word) character; [a-zA-Z0-9_].
# \W : Matches any non-alphanumeric character;
# \b : Matches where the specified characters are at the begining or at end of a word
# \B : Matches where the specified characters are present, but not at the begining or at end
test_string = "hello 123_ hey ho ho hey hohey"
pattern_digits = re.compile(r"\d")
matches = pattern_digits.finditer(test_string)
for match in matches:
    print(match.group())

pattern_non_digits = re.compile(r"\D")
matches = pattern_non_digits.finditer(test_string)
for match in matches:
    print(match.group())

pattern_find_whitespace = re.compile(r"\s")
matches = pattern_find_whitespace.finditer(test_string)
for match in matches:
    print(match)

pattern_word_starts_with = re.compile(r"\bhey")
matches = pattern_word_starts_with.finditer(test_string)
for match in matches:
    print(match)


pattern_contains_word_but_dont_start_withs = re.compile(r"\Bhey")
matches = pattern_contains_word_but_dont_start_withs.finditer(test_string)
for match in matches:
    print(match)

# Good read on \b and \B https://stackoverflow.com/a/58261061/8597871


# Sets: Defined in a square bracket


test_string = 'helloHELLO 123-_'
pattern_find_lo = re.compile(r'[lo]')
matches = pattern_find_lo.finditer(test_string)
for i in matches:
    print(i)

# Use '-' to specify a range

pattern_find_alphabets = re.compile(r"[a-zA-Z]")
matches = pattern_find_alphabets.finditer(test_string)
for i in matches:
    print(i)

pattern_find_all = re.compile(r"[a-zA-Z\s0-9-_]")
matches = pattern_find_all.finditer(test_string)
for i in matches:
    print(i)


# Quantifiers
#    # * : 0 or more
#    # + : 1 or more
#    # ? :0 or 1 i.e. optional character
#    # {4}: Exact number
#    # {4,6} : range numbers (min, max)

# * : 0 or more
test_string = 'hello_123'
pattern_quantifier_star = re.compile(r'\d*') # This means all occurences of with zero or more digits
matches = pattern_quantifier_star.finditer(test_string)
for match in matches:
    print(match)
# OP
# re.Match object; span=(0, 0), match=''>
# <re.Match object; span=(1, 1), match=''>
# <re.Match object; span=(2, 2), match=''>
# <re.Match object; span=(3, 3), match=''>
# <re.Match object; span=(4, 4), match=''>
# <re.Match object; span=(5, 5), match=''>
# <re.Match object; span=(6, 9), match='123'>
# <re.Match object; span=(9, 9), match=''>

# + : 1 or more matches
pattern_quantifier_plus = re.compile(r'\d+') # This means all occurences of with zero or more digits
matches = pattern_quantifier_plus.finditer(test_string)
for match in matches:
    print(match)

# OP
# <re.Match object; span=(6, 9), match='123'>

#? : Optional character
test_string_2 = 'hello123'
pattern_extract_digit_with_or_without_underscore = re.compile(r'_?\d+')
matches = pattern_extract_digit_with_or_without_underscore.finditer(test_string)
for match in matches:
    print(match)
# OP
# <re.Match object; span=(5, 9), match='_123'>

matches = pattern_extract_digit_with_or_without_underscore.finditer(test_string_2)
for match in matches:
    print(match)
# OP
# <re.Match object; span=(5, 8), match='123'>


# {} exact number of times pattern occurs
pattern_repeat_check = re.compile(r'\d{3}')
matches = pattern_repeat_check.finditer(test_string_2)
for match in matches:
    print(match)
# OP
# <re.Match object; span=(5, 8), match='123'>

dates = '''
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
'''
# Pattern to extract dates with Pattern yyyy-mm-dd

pattern_date_yyyy__mm_dd_withdash = re.compile(r'\d\d\d\d-\d\d-\d\d')
matches = pattern_date_yyyy__mm_dd_withdash.finditer(dates)
for match in matches:
    print(match)
# OP
# <re.Match object; span=(13, 23), match='2020-04-01'>
# <re.Match object; span=(24, 34), match='2020-05-23'>
# <re.Match object; span=(35, 45), match='2020-06-11'>
# <re.Match object; span=(46, 56), match='2020-07-11'>
# <re.Match object; span=(57, 67), match='2020-08-11'>

pattern_date_yyyy__mm_dd_withdash_neat = re.compile(r'\d{4}-\d{2}-\d{2}')
matches = pattern_date_yyyy__mm_dd_withdash_neat.findall(dates)
matches_2 = pattern_date_yyyy__mm_dd_withdash.findall(dates)
if matches == matches_2:
    print("Both patterns are same")


pattern_date_yyyy__mm_dd_withdash_or_withslash = re.compile(r"\d{4}[-/]\d{2}[-/]\d{2}")
matches = pattern_date_yyyy__mm_dd_withdash_or_withslash.finditer(dates)
for match in matches:
    print(match)

# OP
# <re.Match object; span=(13, 23), match='2020-04-01'>
# <re.Match object; span=(24, 34), match='2020-05-23'>
# <re.Match object; span=(35, 45), match='2020-06-11'>
# <re.Match object; span=(46, 56), match='2020-07-11'>
# <re.Match object; span=(57, 67), match='2020-08-11'>
# <re.Match object; span=(69, 79), match='2020/04/02'>


# Dates only from 5 month to 7 th month both inclusive

pattern_dates_with_month_5_7  = re.compile(r"\d{4}[-/]0[5-7][-/]\d{2}")
matches = pattern_dates_with_month_5_7.finditer(dates)
for match in matches:
    print(match)

# OP
# re.Match object; span=(24, 34), match='2020-05-23'>
# <re.Match object; span=(35, 45), match='2020-06-11'>
# <re.Match object; span=(46, 56), match='2020-07-11'>

# Conditions

my_string = """
hello
1223
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

pattern_extract_names = re.compile(r'(Ms|Mr|Mrs)\.?\s\w+') # we have used brackets for grouping and | to specify it's either or
matches = pattern_extract_names.finditer(my_string)
for match in matches:
    print(match)

# OP
# <re.Match object; span=(12, 22), match='Mr Simpson'>
# <re.Match object; span=(23, 34), match='Mrs Simpson'>
# <re.Match object; span=(35, 44), match='Mr. Brown'>
# <re.Match object; span=(45, 53), match='Ms Smith'>
# <re.Match object; span=(54, 59), match='Mr. T'>

# Grouping
# If you use grouping in your regex you can extract value according to groups as shown below

pattern_email_with_groups = re.compile(r'([a-zA-Z0-9-]+@([a-zA-Z-]+)\.([a-zA-Z]+))')
matches = pattern_email_with_groups.finditer(my_string)
for match in matches:
    print(f' Username: {match.group(1)} \t Domain: {match.group(2)} \t tld: {match.group(3)}') # Group 0 means whole string and after that it address to groups according to regex

# OP
# Username: pythonengineer@gmail.com      Domain: gmail   tld: com
#  Username: Python-engineer@gmx.de        Domain: gmx     tld: de
#  Username: python-engineer123@my-domain.org      Domain: my-domain       tld: org

# Modfications
# Split and sub


# Split: Returns list of strings splitted on pattern
# good read on split using capturing group: https://stackoverflow.com/a/9049626 and https://pynative.com/python-regex-split/
test_string ='123abc456789abc123ABC'
pattern_split_example = re.compile(r'abc|ABC')
splitted = pattern_split_example.split(test_string)
print(splitted)
# op
# ['123', '456789', '123', ''] # Notice the last element from the list it because seperating character is last character

# Sub: Substitute in place of pattern

subbed_string = pattern_split_example.sub("def",test_string)
print(subbed_string)
#op
# 123def456789def123def

# Another example of sub

url = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern_url_with_groups = re.compile(r'https?://(www\.)?([a-zA-Z-]+)\.([a-zA-Z]+)')
subbed_string = pattern_url_with_groups.sub(r"\2.\3",url) # This \2 and \3 refers to group(2) and group(3)
print(subbed_string)

# Compilation flags
# ASCII, A : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
# DOTALL, S : Make . match any character, including newlines.
# IGNORECASE, I : Do case-insensitive matches.
# LOCALE, L : Do a locale-aware match.
# MULTILINE, M : Multi-line matching, affecting ^ and $.
# VERBOSE, X (for ‘extended’) : Enable verbose REs, which can be organized more cleanly and understandably.


# Methods on Match objects
# group, start, end ,spans
test_string = '123abc123abc122ABC'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string) # Creates iterable object
for match in matches:
    print(match.span(), match.start(), match.end())
    print(match.group())