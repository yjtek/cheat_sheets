`export UV_PROJECT_ROOT=.` | `uv init`
- Initialises a project in the directory

`uv venv ./my/dir/name --python 3.11`
- Create new virtualenv

`uv python install` / `uv python uninstall` / `uv python list` / `uv python find`
- Manage python versions

`uv python pin` 
- Pin current project to python version

`uv add numpy==1.0.0` / `uv add --dev flake8` / `uv add --group lint ruff`
- Add package to virtual env. You can specify dev dependencies, or some custom grouping as well

`uv add "jax; sys_platform == 'linux'"`
- It is also possible to add packages CONDITIONALLY, only if a platform marker meets the requirements
  
`uv remove numpy==1.0.0`
- Remove package to virtual env

`uv sync` | `uv sync --group dev` | `uv sync --extra dev`
- Sync env with requirements. Useful if you've updated your pyproject.toml manually

`uv lock`
- Create lockfile for project's dependencies

`uv lock --upgrade-package numpy`
- Upgrade package

`uv tool install ruff` / `uv tool uninstall ruff` / `uv tool run ruff` / `uv tool list`
- Install/Uninstall/Run a tool

`uv run -- flask run -p 3000`
- Use UV to run any arbitrary script or package

`uv build`
- Build source distribution and binary distribution for project, generates wheel and tar.gz file

`uv publish`
- Publish to pypi or whatever directory you specify

`uv pip freeze > requirements.txt`
- Output requirements.txt

`uv pip compile pyproject.toml > requirements.txt` | `uv pip compile --extra dev pyproject.toml > requirements.txt`
- Output requirements.txt with more detail. Use `--extra` flag for optional groups
