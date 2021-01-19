import glob, yaml
from jinja2 import Environment, FileSystemLoader

# Load vars that will be used to render Terraform Jinja templates
templatevars_yml = open("templatevars.yml")
templatevars = yaml.load(templatevars_yml, Loader=yaml.FullLoader)

#Set directory in which jinja2 will look for templates
env = Environment(loader=FileSystemLoader('templates'))

# Create list of all jinja files in templates dir
template_file_list = glob.glob('./templates/*.j2')
#print(template_file_list) #debug

for filename in template_file_list:
    template = env.get_template(filename)

    parsed_template = template.render(templatevars)
    #print(parsed_template) #debug

    with open(''.join("./rendered/", filename.removesuffix('.j2')), "w") as fh:
        fh.write(parsed_template)