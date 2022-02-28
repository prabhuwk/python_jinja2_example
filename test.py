import os
from dotenv import dotenv_values
from jinja2 import Environment, FileSystemLoader

config = { 
  **dotenv_values('test.env')
}

j2_env = Environment(loader=FileSystemLoader(os.getcwd()), trim_blocks=True)
template = j2_env.get_template('test.j2')
output = template.render(config)
print(output)
