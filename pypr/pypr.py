import os
import click

from .build import build
from .project.groups import project_group

@click.group()
def cli():
    '''Pypr Setup CLI'''
    pass

cli.add_command(build, name='build')
cli.add_command(project_group, name='project')

if __name__ == '__main__':
    cli()