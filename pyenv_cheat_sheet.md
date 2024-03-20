## Pyenv Cheat Sheet

### Installing pyenv
curl https://pyenv.run | bash

### Using pyenv
- Get all python version 3.6/3.7/3.8
  - `pyenv install --list | grep " 3\.[678]"`

- Install python using pyenv, verbosely
  - `pyenv install -v 3.7.2`

- By default, pyenv installs into this path
  - `ls ~/.pyenv/versions/`

- Uninstall version
  - `pyenv uninstall 2.7.15`

- Check all installed versions
  - `pyenv versions`
  - `pyenv version`

- Check current version
  - `python -V`
  - `which python`
  - `pyenv which python`
  
- Set default python version to be used globally/locally/shell
  - `pyenv global 3.6.8`
  - `pyenv local 3.6.8`
  - `pyenv shell 3.6.8`

### Creating a virtual environment
- Pyenv can be used with virtualenv to create and manage virtual environments
  - `pyenv virtualenv 3.6.8 virtual_environment_name`
- 
