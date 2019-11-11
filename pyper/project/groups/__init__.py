import click

from .commands.metadata import project_metadata_group
from .commands.version import version

@click.group()
def project_group():
    '''Inspect and modify Pyper project structures'''
    pass


project_group.add_command(project_metadata_group, name='metadata')
project_group.add_command(version, name='version')
    
