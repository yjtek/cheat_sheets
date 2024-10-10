`uv init`
- Initialises a project in the directory

`uv venv ./my/dir/name --python 3.11`
- Create new virtualenv

`uv python install` / `uv python uninstall` / `uv python list` / `uv python find`
- Manage python versions

`uv python pin` 
- Pin current project to python version

`uv add numpy==1.0.0`
- Add package to virtual env

`uv remove numpy==1.0.0`
- Remove package to virtual env

`uv lock`
- Create lockfile for project's dependencies

`uv lock --upgrade-package numpy`
- Upgrade package

`uv tool install ruff` / `uv tool uninstall ruff` / `uv tool run ruff` / `uv tool list`
- Install/Uninstall/Run a tool

`uv run -- flask run -p 3000`
- Use UV to run any arbitrary script or package

`uv build`
- Build source distribution and binary distribution for project