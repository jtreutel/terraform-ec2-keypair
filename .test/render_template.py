import re, os, glob, yaml
from jinja2 import Environment, FileSystemLoader

# Load vars that will be used to render Terraform Jinja templates
templatevars_yml = open("templatevars.yml")
templatevars = yaml.load(templatevars_yml, Loader=yaml.FullLoader)

#Set directory in which jinja2 will look for templates
env = Environment(loader=FileSystemLoader('')) #default dir is ./templates

# Create list of all jinja files in templates dir
template_file_list = glob.glob('./templates/*.j2')

if not os.path.exists('rendered'):
    os.makedirs('rendered')

for file_fullpath in template_file_list:
    template = env.get_template(file_fullpath)

    parsed_template = template.render(templatevars)

    #Write rendered template to ./rendered/foo.tf
    filename = re.search(r"(?<=\.\/templates\/).*?(?=\.j2)", file_fullpath).group(0)
    with open(''.join(["./rendered/", filename.removesuffix('.j2')]), "w") as fh:
        fh.write(parsed_template)