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

  (virtualenv is recommended)
  pip3 install .

Examples
=====

```bash
$pyper --help
Usage: pyper [OPTIONS] COMMAND [ARGS]...

  Pyper Setup CLI

Options:
  --help  Show this message and exit.

Commands:
  build
```

```bash
$pyper build --help
Usage: pyper build [OPTIONS]

Options:
  -p, --project TEXT              Name of directory to be created for project
                                  [required]
  -n, --name TEXT                 Name to use for setuptools, if blank project
                                  name is used
  -v, --version TEXT              [default: 0.0.1]
  -d, --description TEXT
  -a, --author TEXT
  -ae, --author_email TEXT
  -u, --url TEXT
  -r, --requirements TEXT
  -c, --classifiers TEXT
  -pd, --package_data TEXT
  -pe, --package_exclude TEXT
  -ipd, --include_package_data BOOLEAN
  -eph, --entry_point_header TEXT
                                  entry_point header
  -epc, --entry_point_command TEXT
                                  entry_point command
  -s, --scripts TEXT
  -k, --keywords TEXT
  --help                          Show this message and exit.

```

```bash
$pyper build --project pyper --version 0.0.1 --author "Tanner Burns" --author_email tjburns102@gmail.com --requirements click --entry_point_header console_scripts --entry_point_command "pyper=pyper:cli" --package_data "templates/*" --package_data "templates/baseproject/*" 
```
