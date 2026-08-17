# Create ARM 32-bit asm project skeleton

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_arm32asm/dev/docs/gen_arm32asm_logo.png" width="25%">

**gen_arm32asm** is tool for creating ARM 32-bit asm project skeleton.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the tool and provide instructions on
how to install the tool, any machine dependencies it may have and any
other information that should be provided before the tool is installed.

[![gen_arm32asm python checker](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python_checker.yml) [![gen_arm32asm package checker](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_arm32asm.svg)](https://github.com/vroncevic/gen_arm32asm/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_arm32asm.svg)](https://github.com/vroncevic/gen_arm32asm/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_arm32asm/dev/docs/debtux.png)

[![gen_arm32asm python3 build](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_arm32asm/actions/workflows/gen_arm32asm_python3_build.yml)

Currently there are four ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_arm32asm** is located at **[pypi.org](https://pypi.org/project/gen_arm32asm/)**.

You can install by using pip

```bash
# python3
pip3 install gen_arm32asm
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_arm32asm/releases/)** download and extract release archive.

To install **gen_arm32asm** type the following

```bash
tar xvzf gen_arm32asm-x.y.z.tar.gz
cd gen_arm32asm-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
# python3
python3 get-pip.py
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_arm32asm-*-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_arm32asm/releases)** download and extract release archive.

To install **gen_arm32asm** locate and run setup.py with arguments

```bash
tar xvzf gen_arm32asm-x.y.z.tar.gz
cd gen_arm32asm-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies

**gen_arm32asm** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_arm32asm** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_arm32asm/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_pro_command_definition.py
         │   │   ├── gen_pro_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_arm32asm.cfg
         │   │   ├── gen_arm32asm.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 45 files
```
</details>

#### ✨ Features

* Automatically scaffolds ARM 32-bit assembly projects with build/make files.
* Provides a modular and extensible architecture based on OOP and SOLID principles.
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Comes with configurable templates and JSON schema definitions.
* High code quality with full type checking and 100% unit test coverage.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_arm32asm/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/core/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/core/model/project_setup.py` | 14 | 0 | 100%|
| `gen_arm32asm/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/core/service/engine.py` | 27 | 0 | 100%|
| `gen_arm32asm/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_arm32asm/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_arm32asm/engine.py` | 57 | 0 | 100%|
| `gen_arm32asm/infrastructure/__init__.py` | 8 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/engine.py` | 39 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/icli.py` | 14 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/bundle.py` | 22 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/factory.py` | 35 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/opt_validator.py` | 36 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/options.py` | 15 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/registry.py` | 24 | 0 | 100%|
| `gen_arm32asm/infrastructure/cli/setup/validator.py` | 43 | 0 | 100%|
| `gen_arm32asm/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_arm32asm/infrastructure/command/gen_pro_command_definition.py` | 24 | 0 | 100%|
| `gen_arm32asm/infrastructure/command/gen_pro_command_executor.py` | 21 | 0 | 100%|
| `gen_arm32asm/infrastructure/command/icommand_definition.py` | 14 | 0 | 100%|
| `gen_arm32asm/infrastructure/command/icommand_executor.py` | 13 | 0 | 100%|
| `gen_arm32asm/infrastructure/subprocessor.py` | 55 | 0 | 100%|
| `gen_arm32asm/setup/__init__.py` | 9 | 0 | 100%|
| `gen_arm32asm/setup/bundle.py` | 23 | 0 | 100%|
| `gen_arm32asm/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_arm32asm/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_arm32asm/setup/factory.py` | 48 | 0 | 100%|
| `gen_arm32asm/setup/keys.py` | 27 | 0 | 100%|
| `gen_arm32asm/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_arm32asm/setup/options.py` | 12 | 0 | 100%|
| `gen_arm32asm/setup/registry.py` | 32 | 0 | 100%|
| `gen_arm32asm/setup/validator.py` | 48 | 0 | 100%|
| **Total** | 935 | 0 | 100% |

</details>

### 🛠 Usage

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

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen-arm32asm/badge/?version=latest)](https://gen-arm32asm.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_arm32asm.readthedocs.io](https://gen-arm32asm.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_arm32asm](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2025 - 2026 by [vroncevic.github.io/gen_arm32asm](https://vroncevic.github.io/gen_arm32asm/)

**gen_arm32asm** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_arm32asm/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)
