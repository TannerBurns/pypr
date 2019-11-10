from typing import NamedTuple, List

class PyperSetup(NamedTuple):
    """NamedTuple for building struct around setuptools setup call
    """
    name: str
    version: str
    description: str
    url: str
    author: str
    author_email: str
    requirements: List[str]
    classifiers: List[str]
    package_data: dict
    package_exclude: List[str]
    include_package_data: bool
    entry_points: dict
    scripts: List[str]
    keywords: List[str]