from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import textoparser

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


date_now = datetime.datetime.now()
date_of_foundation = datetime.datetime(
    year=1921,
    month=1,
    day=1,
    hour=0,
)
delta = date_now - date_of_foundation
years = round(delta.days/365.2425)


drinks = textoparser.fetch_drinks()


rendered_page = template.render(
    years=years,
    drinks=drinks,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)
