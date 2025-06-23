
[![Release][badge-release]][release]
![Version][badge-pypi-version]
![Release Date][badge-release-date]
![Python Version][badge-python-version]
![License][badge-license]
![Monthly Downloads][badge-monthly-downloads]
# hexd - Hex Dumper

> TUI file viewer.

<!-- project description -->

## Features

<!-- project features --> 

## Installation

### pip

```console
python3 -m pip install hexd
```

### uvx
```console
uvx --from hexd hexd
```

### uv

```console
uvx pip install hexd
```

## Usage

```console
hexd --help
```


## Development

This project and it's virtual environment is managed using [uv][uv] and
is configured to support automatic activation of virtual environments
using [direnv][direnv]. Development activites such as linting and testing
are automated via [Poe The Poet][poethepoet], run `poe` after cloning
this repo.

### Clone
```console
git clone https://github.com/JnyJny/hexd
cd hexd
```
### Allow Direnv _optional_ but recommended
```console
direnv allow
```

### Create a Virtual Environment
```console
uv venv
```
### Install Dependencies
```console
uv sync
```
### Run `poe`
```console
poe --help
```

<hr>

[![gh:JnyJny/python-package-cookiecutter][python-package-cookiecutter-badge]][python-package-cookiecutter]

<!-- End Links -->

[python-package-cookiecutter-badge]: https://img.shields.io/badge/Made_With_Cookiecutter-python--package--cookiecutter-green?style=for-the-badge
[python-package-cookiecutter]: https://github.com/JnyJny/python-package-cookiecutter
[badge-release]: https://github.com/JnyJny/hexd/actions/workflows/release.yaml/badge.svg
[release]: https://github.com/JnyJny/hexd/actions/workflows/release.yaml
[badge-pypi-version]: https://img.shields.io/pypi/v/hexd
[badge-release-date]: https://img.shields.io/github/release-date/JnyJny/hexd
[badge-python-version]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FJnyJny%2Fhexd%2Fmain%2Fpyproject.toml
[badge-license]: https://img.shields.io/github/license/JnyJny/hexd
[badge-monthly-downloads]: https://img.shields.io/pypi/dm/hexd
[poe]: https://poethepoet.natn.io
[uv]: https://docs.astral.sh/uv/
[direnv]: https://direnv.net
