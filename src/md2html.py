import os
import pypandoc
import re

volume = '1'
dir = f'../doc/{volume}/'

tag = lambda x,y,z: f'<{x}{y}>{z}</{x}>'
line = lambda z: re.sub('\n|\r|\t', '', z)

# Articles
articles = []
for i, f in enumerate(os.listdir(dir)):
	article = pypandoc.convert_file(dir+f, to='html5', format='markdown_strict+hard_line_breaks')
	article = re.sub(' id="([a-z]|-)*"', '', article)
	article = tag('article', f" id='#{volume}-{i+2}'", article)
	article = line(article)
	articles.append(article)

# Contents
contents = re.findall('<h1>(.*?)</h1>', ''.join(articles))
contents = '<h1>Contents</h1><h4>'+'</h4><h4>'.join(contents)+'</h4>'
contents = tag('article', f" id='#{volume}-1'", contents)
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
	button = f'''<button onclick='display(this,"#{volume}-{i}")'></button>'''
	buttons.append(button)
buttons = tag('div', '', line(''.join(buttons)))
buttons = line(buttons)

html = '\n'.join([front,contents,*articles,buttons])
print(html, file=open(f'../doc/{volume}.html',mode='w',encoding='utf-8'))
