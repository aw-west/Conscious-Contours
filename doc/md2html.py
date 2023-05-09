
volume = '1'

# Functions
import os
import pypandoc
import re
tag = lambda x,y,z: f'<{x}{y}>{z}</{x}>'
line = lambda z: re.sub('\n|\r|\t', '', z)

# Articles
articles = []
for i, f in enumerate(os.listdir(volume), -1):
	article = pypandoc.convert_file(volume+'/'+f, to='html5', format='markdown_strict+hard_line_breaks')
	article = re.sub(' id="([a-z]|-)*"', '', article)
	article = tag('article', f" id='#{volume}-{i+2}'", article)
	article = line(article)
	articles.append(article)

# Contents
contents = re.findall('<h1>(.*?)</h1>', ''.join(articles))
iS = [i+2 for i in range(len(contents))]
iS[0] -= 1
contents = [f'''<h4><a href="javascript:display('\u0023{volume}-{i}')">''' + content + '</a></h4>' for i, content in zip(iS, contents)]

contents = '<h1>Contents</h1>' + ''.join(contents)
contents = tag('article', f" id='#{volume}-2'", contents)
contents = line(contents)

# Front Cover
front_style = f'''
	background: url(img/{volume}.png);
	background-size: cover;
'''
front_content = f'''
'''
front = tag('article', f" id='#{volume}-0' style='{front_style}'", front_content)
front = line(front)

# Button
buttons = []
for i in range(2+len(articles)):
	button = f'''<button id='#{volume}-{i}button' onclick="display('#{volume}-{i}')"></button>'''
	buttons.append(button)
buttons = tag('div', '', line(''.join(buttons)))
buttons = line(buttons)
html = '\n'.join([front, articles[0], contents, *articles[1:], buttons])

# Images
html = html.replace('<img ', '<img loading="lazy" ')

print(html, file=open(f'{volume}.html',mode='w',encoding='utf-8'))
