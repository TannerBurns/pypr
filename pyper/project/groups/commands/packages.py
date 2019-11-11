import click

from ..utils import PyperPackages

@click.group()
def packages_group():
    '''Get, add or remove included and excluded packages in pyper project'''
    pass

@packages_group.command(name='include')
@click.option('--get', '-g', is_flag=True,
    help='Get included packages of current pyper project')
@click.option('--add', '-a', type=str,
    help='Add a package to include in current pyper project')
@click.option('--remove', '-r', type=str,
    help='Remove an included package from current pyper project')
def include(get, add, remove):
    '''Get, add, or remove included packages from current pyper project'''
    pyper_packages = PyperPackages()
    if get:
        print('')
        for pypackage in pyper_packages.get_included_packages():
            print(pypackage)
        print('')
    if add:
        pyper_packages.add_included_packages(add)
    if remove:
        pyper_packages.remove_included_packages(remove)
    pyper_packages.save()

@packages_group.command(name='exclude')
@click.option('--get', '-g', is_flag=True,
    help='Get excluded packages of current pyper project')
@click.option('--add', '-a', type=str,
    help='Add an excluded package to current pyper project')
@click.option('--remove', '-r', type=str,
    help='Remove an excluded package from current pyper project')
def exclude(get, add, remove):
    '''Get, add, or remove excluded packages from current pyper project'''
    pyper_packages = PyperPackages()
    if get:
        print('')
        for pypackage in pyper_packages.get_excluded_packages():
            print(pypackage)
        print('')
    if add:
        pyper_packages.add_excluded_packages(add)
    if remove:
        pyper_packages.remove_excluded_packages(remove)
    pyper_packages.save()