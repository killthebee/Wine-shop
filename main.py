from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import text_file_parser
import argparse


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

parser = argparse.ArgumentParser(
    description='Insert path to text file here'
 )
parser.add_argument('-f', '--file', help='Insert path to text file here')
args = parser.parse_args()
file_name = args.file
drinks = text_file_parser.fetch_drinks(file_name)


rendered_page = template.render(
    years=years,
    drinks=drinks,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)
