import click
import os
import json

from colored import fg

from ..utils import PyperVersion

@click.group()
def project_group():
    '''Inspect and modify Pyper project structures'''
    pass

@project_group.command(name='version')
@click.option('--get', '-g', is_flag=True,
    help='Get version of current pyper project directory')
@click.option('--increase_patch_version', '-ipv', type=int, default=0,
    help='Increase the patch version by a given amount')
def version(get, increase_patch_version):
    manifest_path = './manifest.json'
    if not os.path.exists(manifest_path):
        raise Exception('Failed to find manifest.json in cwd')
    manifest = json.load(open(manifest_path, 'r'))
    name, version = (manifest.get('name'), manifest.get('version'))
    if not name and not version:
        raise Exception('Failed to load name and version from manifest.json')
    pyper_version = PyperVersion(name, version)
    if get:
        print(f'\n%s{pyper_version.print_version()}\n' % fg('green_3a'))
    if increase_patch_version > 0:
        pyper_version.increment_patch(increase_patch_version)
        manifest['version'] = pyper_version.get_version()
        print('New version')
        print(f'%s{pyper_version.print_version()}\n' % fg('green_3a'))
        open(manifest_path, 'w').write(json.dumps(manifest, indent=4))

