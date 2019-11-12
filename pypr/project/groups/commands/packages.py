import click

from ..utils import PyprPackages

@click.group()
def packages_group():
    '''Get, add or remove included and excluded packages in pypr project'''
    pass

@packages_group.command(name='include')
@click.option('--get', '-g', is_flag=True,
    help='Get included packages of current pypr project')
@click.option('--add', '-a', type=str,
    help='Add a package to include in current pypr project')
@click.option('--remove', '-r', type=str,
    help='Remove an included package from current pypr project')
def include(get, add, remove):
    '''Get, add, or remove included packages from current pypr project'''
    pypr_packages = PyprPackages()
    if get:
        print('')
        for pypackage in pypr_packages.get_included_packages():
            print(pypackage)
        print('')
    if add:
        pypr_packages.add_included_packages(add)
    if remove:
        pypr_packages.remove_included_packages(remove)
    pypr_packages.save()

@packages_group.command(name='exclude')
@click.option('--get', '-g', is_flag=True,
    help='Get excluded packages of current pypr project')
@click.option('--add', '-a', type=str,
    help='Add an excluded package to current pypr project')
@click.option('--remove', '-r', type=str,
    help='Remove an excluded package from current pypr project')
def exclude(get, add, remove):
    '''Get, add, or remove excluded packages from current pypr project'''
    pypr_packages = PyprPackages()
    if get:
        print('')
        for pypackage in pypr_packages.get_excluded_packages():
            print(pypackage)
        print('')
    if add:
        pypr_packages.add_excluded_packages(add)
    if remove:
        pypr_packages.remove_excluded_packages(remove)
    pypr_packages.save()