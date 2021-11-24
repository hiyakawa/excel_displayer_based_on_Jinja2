import jinja2

title = 'Hello, world!'
output_file = 'hello.html'

subs = jinja2.Environment(
    loader = jinja2.FileSystemLoader('./')
).get_template('template.html').render(title = title)

with open(output_file, 'w') as f: f.write(subs)