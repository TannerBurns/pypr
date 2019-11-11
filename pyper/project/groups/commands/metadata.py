import click

from ..utils import PyperMetadata

@click.group()
def project_metadata_group():
    '''Get and set attributes of Pyper project metadata'''
    pass

@project_metadata_group.command(name='description')
@click.option('--get', '-g', is_flag=True,
    help='Get description of current pyper project')
@click.option('--set_description', '-s', type=str,
    help='Set description of current pyper project')
def description(get, set_description):
    pyper_metadata = PyperMetadata()
    if get:
        print(f'\n{pyper_metadata.get_description()}\n')
    if set_description:
        pyper_metadata.set_description(set_description)
        print('\nNew description set!')
        print(f'{pyper_metadata.get_description()}\n')
        pyper_metadata.save()

@project_metadata_group.command(name='author')
@click.option('--get', '-g', is_flag=True,
    help='Get author of current pyper project')
@click.option('--set_author', '-s', type=str,
    help='Set author of current pyper project')
def author(get, set_author):
    pyper_metadata = PyperMetadata()
    if get:
        print(f'\n{pyper_metadata.get_author()}\n')
    if set_author:
        pyper_metadata.set_author(set_author)
        print('\nNew author set!')
        print(f'{pyper_metadata.get_author()}\n')
        pyper_metadata.save()

@project_metadata_group.command(name='author_email')
@click.option('--get', '-g', is_flag=True,
    help='Get author email of current pyper project')
@click.option('--set_author_email', '-s', type=str,
    help='Set author email of current pyper project')
def author_email(get, set_author_email):
    pyper_metadata = PyperMetadata()
    if get:
        print(f'\n{pyper_metadata.get_author_email()}\n')
    if set_author_email:
        pyper_metadata.set_author_email(set_author_email)
        print('\nNew author email set!')
        print(f'{pyper_metadata.get_author_email()}\n')
        pyper_metadata.save()

@project_metadata_group.command(name='url')
@click.option('--get', '-g', is_flag=True,
    help='Get url of current pyper project')
@click.option('--set_url', '-s', type=str,
    help='Set url of current pyper project')
def url(get, set_url):
    pyper_metadata = PyperMetadata()
    if get:
        print(f'\n{pyper_metadata.get_url()}\n')
    if set_url:
        pyper_metadata.set_url(set_url)
        print('\nNew url set!')
        print(f'{pyper_metadata.get_url()}\n')
        pyper_metadata.save()