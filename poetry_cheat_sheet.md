## Setting up environment
poetry init
poetry config virtualenvs.in-project true #make virtualenv in project dir instead of in poetry's virtualenv dir
poetry install --no-root

poetry shell #activate environment

poetry add scikit-learn
poetry remove scikit-learn

poetry env list

## Publishing package
poetry config repositories.test-pypi https://test.pypi.org/legacy
poetry config pypi-token.test-pypi pypi-<TOKEN>
poetry build
poetry publish --build -r test-pypi
