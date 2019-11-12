import click

from ..utils import PyprMetadata

@click.group()
def project_metadata_group():
    '''Get and set attributes of Pypr project metadata'''
    pass

@project_metadata_group.command(name='description')
@click.option('--get', '-g', is_flag=True,
    help='Get description of current pypr project')
@click.option('--set_description', '-s', type=str,
    help='Set description of current pypr project')
def description(get, set_description):
    pypr_metadata = PyprMetadata()
    if get:
        print(f'\n{pypr_metadata.get_description()}\n')
    if set_description:
        pypr_metadata.set_description(set_description)
        print('\nNew description set!')
        print(f'{pypr_metadata.get_description()}\n')
        pypr_metadata.save()

@project_metadata_group.command(name='author')
@click.option('--get', '-g', is_flag=True,
    help='Get author of current pypr project')
@click.option('--set_author', '-s', type=str,
    help='Set author of current pypr project')
def author(get, set_author):
    pypr_metadata = PyprMetadata()
    if get:
        print(f'\n{pypr_metadata.get_author()}\n')
    if set_author:
        pypr_metadata.set_author(set_author)
        print('\nNew author set!')
        print(f'{pypr_metadata.get_author()}\n')
        pypr_metadata.save()

@project_metadata_group.command(name='author_email')
@click.option('--get', '-g', is_flag=True,
    help='Get author email of current pypr project')
@click.option('--set_author_email', '-s', type=str,
    help='Set author email of current pypr project')
def author_email(get, set_author_email):
    pypr_metadata = PyprMetadata()
    if get:
        print(f'\n{pypr_metadata.get_author_email()}\n')
    if set_author_email:
        pypr_metadata.set_author_email(set_author_email)
        print('\nNew author email set!')
        print(f'{pypr_metadata.get_author_email()}\n')
        pypr_metadata.save()

@project_metadata_group.command(name='url')
@click.option('--get', '-g', is_flag=True,
    help='Get url of current pypr project')
@click.option('--set_url', '-s', type=str,
    help='Set url of current pypr project')
def url(get, set_url):
    pypr_metadata = PyprMetadata()
    if get:
        print(f'\n{pypr_metadata.get_url()}\n')
    if set_url:
        pypr_metadata.set_url(set_url)
        print('\nNew url set!')
        print(f'{pypr_metadata.get_url()}\n')
        pypr_metadata.save()