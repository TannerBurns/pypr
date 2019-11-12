import click

from ..utils import PyprRequirements

@click.command(name='requirements')
@click.option('--get', '-g', is_flag=True,
    help='Get requirements of current pypr project')
@click.option('--add', '-a', type=str,
    help='Add a requirement to current pypr project')
@click.option('--remove', '-r', type=str,
    help='Remove a requirement from current pypr project')
def requirements(get, add, remove):
    '''Get, add, or remove pip requirements from current pypr project'''
    pypr_requirements = PyprRequirements()
    if get:
        print('')
        for pyreq in pypr_requirements.get_requirements():
            print(pyreq)
        print('')
    if add:
        pypr_requirements.add_requirement(add)
    if remove:
        pypr_requirements.remove_requirement(remove)
    pypr_requirements.save()