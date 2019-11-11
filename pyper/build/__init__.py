import os
import click
import json

from shutil import copy, copytree
from typing import List

from .utils import PyperSetup

@click.group()
def build_group():
    pass

@build_group.command(name='new')
@click.option('--project', '-p', type=str, required=True, 
    help='Name of directory to be created for project')
@click.option('--name', '-n', type=str, 
    help='Name to use for setuptools, if blank project name is used')
@click.option('--version', '-v', type=str, default='0.0.1', show_default=True,
    help='Version to set for project')
@click.option('--description', '-d', type=str,
    help='Description for project')
@click.option('--author', '-a', type=str,
    help='Author of project')
@click.option('--author_email', '-ae', type=str,
    help="Author's email for project")
@click.option('--url', '-u', type=str,
    help='URL for the project')
@click.option('--requirements', '-r', type=str, multiple=True,
    help='Requirements for pip related to project')
@click.option('--classifiers', '-c', type=str, multiple=True,
    help='Classifier strings for project')
@click.option('--package_data', '-pd', type=str, multiple=True,
    help='Package data to include in project directory')
@click.option('--package_include', '-pi', type=str, multiple=True,
    help='Packages to include during install')
@click.option('--package_exclude', '-pe', type=str, multiple=True,
    help='Packages to exclude during install')
@click.option('--include_package_data', '-ipd', type=bool, is_flag=True,
    help='Flag for including package data')
@click.option('--entry_point_header', '-eph', type=str, 
    help='entry_point header')
@click.option('--entry_point_command', '-epc', type=str, 
    help='entry_point command')
@click.option('--scripts', '-s', type=str, multiple=True,
    help='Scripts to include for project')
@click.option('--keywords', '-k', type=str, multiple=True,
    help='Keywords to describe project')
def build(
    project, name, version, description, author, author_email, url, requirements, 
    classifiers, package_data, package_include, package_exclude, include_package_data, 
    entry_point_header, entry_point_command, scripts, keywords):
    '''build a new project'''
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
        [package.replace('/', '.') for package in package_include],
        [package.replace('/', '.') for package in package_exclude],
        include_package_data,
        {entry_point_header: [entry_point_command]},
        list(scripts),
        list(keywords)
    )
    with open(os.path.join(project_dir, 'manifest.json'), 'w') as fout:
        fout.write(json.dumps(pyper_setup._asdict(), indent= 4))