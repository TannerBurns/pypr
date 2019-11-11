import click

from colored import fg

from ...utils import PyperVersion

@click.command(name='version')
@click.option('--get', '-g', is_flag=True,
    help='Get version of current pyper project directory')
@click.option('--increase_patch_version', '-ipv', type=int, default=0,
    help='Increase the patch version by a given amount')
def version(get, increase_patch_version):
    '''Get, set, and increment/decrement version for pyper project'''
    pyper_version = PyperVersion()
    if get:
        print(f'\n%s{pyper_version.print_version()}\n' % fg('green_3a'))
    if increase_patch_version > 0:
        pyper_version.increment_patch(increase_patch_version)
        print('\nNew version set!')
        print(f'%s{pyper_version.print_version()}\n' % fg('green_3a'))
        pyper_version.save()