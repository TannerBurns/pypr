import os
import click
import json

from shutil import copy, copytree
from typing import List

from .utils import PyperSetup

@click.group()
def cli():
    """Pyper Setup CLI"""
    pass

@cli.command()
@click.option('--project', '-p', type=str, required=True, help='Name of directory to be created for project')
@click.option('--name', '-n', type=str, help='Name to use for setuptools, if blank project name is used')
@click.option('--version', '-v', type=str, default='0.0.1', show_default=True)
@click.option('--description', '-d', type=str)
@click.option('--author', '-a', type=str)
@click.option('--author_email', '-ae', type=str)
@click.option('--url', '-u', type=str)
@click.option('--requirements', '-r', type=str, multiple=True)
@click.option('--classifiers', '-c', type=str, multiple=True)
@click.option('--package_data', '-pd', type=str, multiple=True)
@click.option('--package_exclude', '-pe', type=str, multiple=True)
@click.option('--include_package_data', '-ipd', type=bool)
@click.option('--entry_point_header', '-eph', type=str, help='entry_point header')
@click.option('--entry_point_command', '-epc', type=str, help='entry_point command')
@click.option('--scripts', '-s', type=str, multiple=True)
@click.option('--keywords', '-k', type=str, multiple=True)
def build(project, name, version, description, author, author_email, url, requirements, classifiers, package_data, package_exclude, include_package_data, entry_point_header, entry_point_command, scripts, keywords):
    basepath = os.path.realpath(os.getcwd())
    project_dir = os.path.join(basepath, project)
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
    name = name or project.lower()
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    copy(f'{templates_dir}/setup.py', f'{project_dir}/setup.py')
    copy(f'{templates_dir}/README.md', f'{project_dir}/README.md')
    copytree(f'{templates_dir}/baseproject', f'{project_dir}/{name}')
    pyper_setup = PyperSetup(
        name,
        version,
        description,
        author,
        author_email,
        url,
        list(requirements),
        list(classifiers),
        {'': list(package_data)} if package_data else {},
        list(package_exclude),
        include_package_data,
        {entry_point_header: [entry_point_command]},
        list(scripts),
        list(keywords)
    )
    with open(os.path.join(project_dir, 'manifest.json'), 'w') as fout:
        fout.write(json.dumps(pyper_setup._asdict(), indent= 4))


if __name__ == '__main__':
    cli()