import click

from .commands.metadata import project_metadata_group
from .commands.version import version
from .commands.requirements import requirements
from .commands.packages import packages_group

@click.group()
def project_group():
    '''Inspect and modify Pyper project structures'''
    pass


project_group.add_command(project_metadata_group, name='metadata')
project_group.add_command(version, name='version')
project_group.add_command(requirements, name='requirements')
project_group.add_command(packages_group, name='packages')
    
