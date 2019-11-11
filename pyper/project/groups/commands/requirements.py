import click

from ..utils import PyperRequirements

@click.command(name='requirements')
@click.option('--get', '-g', is_flag=True,
    help='Get requirements of current pyper project')
@click.option('--add', '-a', type=str,
    help='Add a requirement to current pyper project')
@click.option('--remove', '-r', type=str,
    help='Remove a requirement from current pyper project')
def requirements(get, add, remove):
    '''Get, add, or remove pip requirements from current pyper project'''
    pyper_requirements = PyperRequirements()
    if get:
        print('')
        for pyreq in pyper_requirements.get_requirements():
            print(pyreq)
        print('')
    if add:
        pyper_requirements.add_requirement(add)
    if remove:
        pyper_requirements.remove_requirement(remove)
    pyper_requirements.save()