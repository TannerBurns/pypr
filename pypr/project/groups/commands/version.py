import click

from colored import fg

from ..utils import PyprVersion

@click.command(name='version')
@click.option('--get', '-g', is_flag=True,
    help='Get version of current pypr project directory')
@click.option('--increase_patch_version', '-ipv', type=int, default=0,
    help='Increase the patch version by a given amount')
def version(get, increase_patch_version):
    '''Get, set, and increment/decrement version for pypr project'''
    pypr_version = PyprVersion()
    if get:
        print(f'\n%s{pypr_version.print_version()}\n' % fg('green_3a'))
    if increase_patch_version > 0:
        pypr_version.increment_patch(increase_patch_version)
        print('\nNew version set!')
        print(f'%s{pypr_version.print_version()}\n' % fg('green_3a'))
        pypr_version.save()