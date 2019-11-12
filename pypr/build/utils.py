from typing import NamedTuple, List

class PyprSetup(NamedTuple):
    """NamedTuple for building struct around setuptools setup call
    """
    name: str
    version: str
    description: str
    author: str
    author_email: str
    url: str
    requirements: List[str]
    classifiers: List[str]
    package_data: dict
    package_include: List[str]
    package_exclude: List[str]
    include_package_data: bool
    entry_points: dict
    scripts: List[str]
    keywords: List[str]
    
