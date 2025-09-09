from jinja2 import Environment, FileSystemLoader
from utils import get_path_to

env = Environment(loader=FileSystemLoader(get_path_to("templates")))
VACANCY_TEMPLATE = env.get_template('template.jinja')
