import jinja2

title = 'hello'
content = 'Hello, world!'
output_file = 'hello.html'

subs = jinja2.Environment(
    loader = jinja2.FileSystemLoader('./')
).get_template('template.html').render(title = title, content = content)

with open(output_file, 'w') as f: f.write(subs)
