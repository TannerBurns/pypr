# Pyper

<!--Badges-->
![MIT badge](https://img.shields.io/badge/license-MIT-black)
![Version badge](https://img.shields.io/github/manifest-json/v/tannerburns/pyper?color=red)
![RepoSize badge](https://img.shields.io/github/repo-size/tannerburns/pyper?color=green)
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
    $pyper --help
    Usage: pyper [OPTIONS] COMMAND [ARGS]...

      Pyper Setup CLI

    Options:
      --help  Show this message and exit.

    Commands:
      build    build a new project
      project  Inspect and modify Pyper project structures
```
```
    $pyper build --help
    Usage: pyper build [OPTIONS]

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
    $pyper project --help
    Usage: pyper project [OPTIONS] COMMAND [ARGS]...

      Inspect and modify Pyper project structures

    Options:
      --help  Show this message and exit.

    Commands:
      metadata  Get and set attributes of Pyper project metadata
      version   Get, set, and increment/decrement version for pyper project
```

Example building new project
=====
```
    $pyper build new --project pyper_cli --version 0.0.1 --author "Tanner Burns" --author_email tjburns102@gmail.com --requirements click --entry_point_header console_scripts --entry_point_command "pyper=pyper:cli" --package_data "templates/*" --package_data "templates/baseproject/*" --package_include pyper --package_include pyper/* --include_package_data 
```
