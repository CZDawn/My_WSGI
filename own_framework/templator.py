from os.path import join
from jinja2 import Template

def render(template_name, folder='templates', **kwargs):
    """Renders the templates

    :param template_name - name of tamplate wich will be rendered
    :param folder - the folder in wich we are looking for the template
    :param kwargs - arguments passed to the template
    :return:
    """

    file_path = join(folder, template_name)
    # open the tamplate by name
    with open(file_path, encoding='UTF-8') as file:
        #read template
        template = Template(file.read())
    #render tamplate with arguments
    return template.render(**kwargs)

