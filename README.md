# Pypr

<!--Badges-->
![MIT badge](https://img.shields.io/badge/license-MIT-black)
![Version badge](https://img.shields.io/github/manifest-json/v/tannerburns/pypr?color=red)
![RepoSize badge](https://img.shields.io/github/repo-size/tannerburns/pypr?color=green)
![Python badge](https://img.shields.io/badge/python-setuptools-blue?logo=python&logoColor=yellow)
![Platform badge](https://img.shields.io/badge/platform-linux%20%7C%20osx%20%7C%20win32-yellow)

  An easy cli tool to create new python projects with a README.md, setup.py and manifest.json


Quick start
=====

  *virtualenv is recommended*

  pip3 install .

Examples
=====
```
    $pypr --help
    Usage: pypr [OPTIONS] COMMAND [ARGS]...

      Pypr Setup CLI

    Options:
      --help  Show this message and exit.

    Commands:
      build    build a new project
      project  Inspect and modify Pypr project structures
```
```
    $pypr build --help
    Usage: pypr build [OPTIONS]

      build a new project

    Options:
      -p, --project TEXT              Name of directory to be created for project
                                      [required]
      -n, --name TEXT                 Name to use for setuptools, if blank project
                                      name is used
      -v, --version TEXT              Version to set for project  [default: 0.0.1]
      -d, --description TEXT          Description for project
      -a, --author TEXT               Author of project
      -ae, --author_email TEXT        Author's email for project
      -u, --url TEXT                  URL for the project
      -r, --requirements TEXT         Requirements for pip related to project
      -c, --classifiers TEXT          Classifier strings for project
      -pd, --package_data TEXT        Package data to include in project directory
      -pi, --package_include TEXT     Packages to include during install
      -pe, --package_exclude TEXT     Packages to exclude during install
      -ipd, --include_package_data BOOLEAN
                                      Flag for including package data
      -eph, --entry_point_header TEXT
                                      entry_point header
      -epc, --entry_point_command TEXT
                                      entry_point command
      -s, --scripts TEXT              Scripts to include for project
      -k, --keywords TEXT             Keywords to describe project
      --help                          Show this message and exit.
```
```
    $pypr project --help
    Usage: pypr project [OPTIONS] COMMAND [ARGS]...

      Inspect and modify Pypr project structures

    Options:
      --help  Show this message and exit.

    Commands:
      metadata      Get and set attributes of Pypr project metadata
      packages      Get, add or remove included and excluded packages in pypr...
      requirements  Get, add, or remove pip requirements from current pypr...
      version       Get, set, and increment/decrement version for pypr project
```

Example building new project
=====
```
    $pypr build new --project pypr_cli --version 0.0.1 --author "Tanner Burns" --author_email tjburns102@gmail.com --requirements click --entry_point_header console_scripts --entry_point_command "pypr=pypr:cli" --package_data "templates/*" --package_data "templates/baseproject/*" --package_include pypr --package_include pypr/* --include_package_data 
```
