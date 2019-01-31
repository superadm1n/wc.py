"""
MIT License

Copyright (c) 2018 Kyle Kowalczyk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This is designed to be a Python implementation of the GNU wc program
"""
from argparse import ArgumentParser
import sys


app = ArgumentParser()
app.add_argument('-m', '--chars', help='print the character counts', action='store_true')
app.add_argument('-l', '--lines', help='print the newline counts', action='store_true')
app.add_argument('-w', '--words', help='print the word counts', action='store_true')
app.add_argument('-c', '--bytes', help='print the byte counts', action='store_true')
app.add_argument('-L', '--max-line-length', help='print the maximum display width', action='store_true')
if sys.stdin.isatty():
    app.add_argument('file', help='File to read from')
args = app.parse_args()

if sys.stdin.isatty():
    with open(args.file, 'r') as f:
        file = f.readlines()
else:
    file = [x.strip('\n') for x in sys.stdin.readlines()]

# Handles all of the arguments
if args.lines:
    print(len(file))

if args.words:
    count = 0
    for x in file:
        for y in x.split():
            count += 1
    print(count)

if args.chars:
    count = 0
    for x in file:
        for y in x:
            if y != ' ':
                count += 1
    print(count)

if args.bytes:
    count = 0
    with open(args.file, 'rb') as f:
        tmp = f.readlines()
    for x in tmp:
        count += len(x)
    print(count)

if args.max_line_length:
    count = 0
    for x in file:
        if len(x) > count:
            count = len(x)
    print(count)
