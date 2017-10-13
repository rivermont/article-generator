"""
Copyright (c) Will Bennett/rivermont 2017.
"""

import markovify
import time as t

date = t.time()

lines = 200  # Number of lines to be generated.
tries = 50  # Number of tries to get a valid sentence.

# Load most recent markov model
# Generate article and insert into empty HTML page.

with open('data.txt', 'r') as file:
    model = markovify.Text(file, retain_original=False)

article = ''''''
for i in range(lines):
    article += (model.make_sentence(tries=tries))

page = '''<!DOCTYPE html>
<html lang="en_US">
<head>
    <title>
</head>
<body>
    <div id="article">{0}</div>
</body>
</html>
'''.format(article)

with open('{0}.html'.format(date), 'w+') as file:
    file.write(page)

print('Done.')
