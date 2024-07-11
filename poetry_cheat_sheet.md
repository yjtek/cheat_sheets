## Setting up environment
- poetry init
- poetry config virtualenvs.in-project true #make virtualenv in project dir instead of in poetry's virtualenv dir
- poetry config virtualenvs.in-project true --local #if .venv exists in directory, poetry uses this path to manage installation 
- poetry install --no-root

- poetry shell #activate environment

- poetry add scikit-learn==">1.0.0"
- poetry remove scikit-learn

- poetry env list

- poetry env info --path # Find poetry env path

- deactivate


## Publishing package
- poetry config repositories.test-pypi https://test.pypi.org/legacy
- poetry config pypi-token.test-pypi pypi-<TOKEN>
- poetry build
- poetry publish --build -r test-pypi

## Export requirements.txt from poetry
- poetry export --without-hashes --format=requirements.txt > requirements.txt
