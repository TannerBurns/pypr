import os
import click

from .build import build_group
from .project.groups import project_group

@click.group()
def cli():
    '''Pyper Setup CLI'''
    pass

cli.add_command(build_group, name='build')
cli.add_command(project_group, name='project')

if __name__ == '__main__':
    cli()