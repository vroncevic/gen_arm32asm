# Create ARM 32-bit asm project skeleton

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_arm32asm/dev/docs/gen_arm32asm_logo.png" width="25%">

**gen_arm32asm** is tool for creating ARM 32-bit asm project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_arm32asm python checker](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python_checker.yml) [![gen_arm32asm package checker](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_arm32asm.svg)](https://github.com/vroncevic/gen_arm32asm/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_arm32asm.svg)](https://github.com/vroncevic/gen_arm32asm/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Code coverage](#code-coverage)
- [Usage](#usage)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_arm32asm/dev/docs/debtux.png)

[![gen_arm32asm python3 build](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python3_build.yml)

Currently there are four ways to install framework
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python is located at **[pypi.org](https://pypi.org/project/gen_arm32asm/)**.

You can install by using pip

```bash
#python3
pip3 install gen_arm32asm
```

##### Install using build

Navigate to **[release page](https://github.com/vroncevic/gen_arm32asm/releases)** download and extract release archive.

To install **gen-arm32asm** run

```bash
tar xvzf gen-arm32asm-x.y.z.tar.gz
cd gen-arm32asm-x.y.z
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build -s --no-isolation --wheel
pip3 install dist/gen-arm32asm-x.y.z-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/gen_arm32asm/releases/)** download and extract release archive.

To install **gen_arm32asm** type the following

```bash
tar xvzf gen_arm32asm-x.y.z.tar.gz
cd gen_arm32asm-x.y.z/
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_arm32asm** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_arm32asm)

### Tool structure

**gen_arm32asm** is based on OOP

Generator structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_arm32asm/
         ├── application/
         │   ├── __init__.py
         │   └── service.py
         ├── domain/
         │   ├── __init__.py
         │   ├── models.py
         │   └── ports/
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── gen_arm32asm_bundle.py
         ├── infrastructure/
         │   ├── cli.py
         │   ├── cli_bundle.py
         │   ├── config/
         │   │   ├── gen_arm32asm.cfg
         │   │   ├── gen_arm32asm.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── gen_pro_command.py
         │   ├── icli.py
         │   ├── icli_command.py
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         └── py.typed

     6 directories, 22 files
```
</details>

### Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_arm32asm/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/application/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/application/service.py` | 22 | 0 | 100%|
| `gen_arm32asm/domain/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/domain/models.py` | 18 | 0 | 100%|
| `gen_arm32asm/domain/ports/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/domain/ports/iservice.py` | 11 | 0 | 100%|
| `gen_arm32asm/domain/ports/isubprocessor.py` | 11 | 0 | 100%|
| `gen_arm32asm/engine.py` | 66 | 0 | 100%|
| `gen_arm32asm/gen_arm32asm_bundle.py` | 39 | 0 | 100%|
| `gen_arm32asm/infrastructure/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli.py` | 36 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli_bundle.py` | 33 | 0 | 100%|
| `gen_arm32asm/infrastructure/gen_pro_command.py` | 32 | 0 | 100%|
| `gen_arm32asm/infrastructure/icli.py` | 11 | 0 | 100%|
| `gen_arm32asm/infrastructure/icli_command.py` | 14 | 0 | 100%|
| `gen_arm32asm/infrastructure/subprocessor.py` | 53 | 0 | 100%|
| **Total** | 386 | 0 | 100% |

</details>

### Usage

Install package

```bash
pip3 install gen_arm32asm
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_arm32asm/main/main.py) or create your own.


```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_arm32asm/main/main.py
```

Running tool for creating new ARM Pico M project

```bash
python3 main.py create --name mytool --output ./demo/
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_arm32asm/badge/?version=latest)](https://gen-arm32asm.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_arm32asm.readthedocs.io](https://gen-arm32asm.readthedocs.io)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_arm32asm](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2025 - 2026 by [vroncevic.github.io/gen_arm32asm](https://vroncevic.github.io/gen_arm32asm/)

**gen_arm32asm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_arm32asm/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
