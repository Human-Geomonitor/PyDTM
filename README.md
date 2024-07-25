# PyDTM

![PyPI](https://img.shields.io/pypi/v/pydtm)
![Documentation Status](https://readthedocs.org/projects/pydtm/badge/?version=latest)
![License](https://img.shields.io/github/license/Human-Geomonitor/PyDTM)

![](https://github.com/Human-Geomonitor/PyDTM/blob/dev/samples_per_countries.png)

`pydtm` is a Python toolkit designed to interact with [IOM's Displacement Tracking Matrix (DTM) API](https://dtm.iom.int/data-and-analysis/dtm-api) using the `requests` package. The DTM API enables the humanitarian community, academia, media, government, and non-governmental organizations to access data collected by DTM. This data includes non-sensitive figures of internally displaced persons (IDPs), aggregated at various administrative levels.


## Installation

`pydtm` is available on [PyPi](https://pypi.org/project/pydtm/). You can install it using pip:

```sh
pip install pydtm
```
## Usage

Here's a basic example to get you started:

```python
import pydtm

# Query country level data for Yemen from January 2000 to December 2023
from pydtm.api import countryLevelData
response_country = countryLevelData(admin0Pcode="YEM", monthFrom_month= "1", monthFrom_year=2000, monthTo_month= "12", monthTo_year=2023, to_pandas=True)
print(response_country)

# Query admin1 level data for Yemen from January 2000 to December 2023
from pydtm.api import admin1LevelData
response_admin1 = admin1LevelData(admin0Pcode="YEM", monthFrom_month= "1", monthFrom_year=2000, monthTo_month= "12", monthTo_year=2023, to_pandas=True)
print(response_admin1)

# Query admin2 level data for Yemen from January 2000 to December 2023
from pydtm.api import admin2LevelData
response_admin2 = admin2LevelData(admin0Pcode="YEM", monthFrom_month= "1", monthFrom_year=2000, monthTo_month= "12", monthTo_year=2023, to_pandas=True)
print(response_admin2)
```


## Documentation
``pydtm``'s documentation is available on [readthedocs.org](https://pydtm.readthedocs.io/en/latest/index.html).

## Contribution Guidelines

We welcome contributions! Please follow these guidelines to contribute:

1. **Fork the Repository**: Click the "Fork" button at the top right of this page to create a copy of this repository on your GitHub account.
2. **Clone the Forked Repository**: Clone your forked repository to your local machine.
    ```sh
    git clone https://github.com/yourusername/pydtm.git
    cd pydtm
    ```
3. **Create a New Branch**: Create a new branch for your feature or bug fix.
    ```sh
    git checkout -b feature-name
    ```
4. **Make Your Changes**: Implement your feature or bug fix.
5. **Add Docstrings**: Ensure all functions and classes have docstrings following the [Sphinx-RTD format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).
6. **Update Documentation**: Add new functions and classes to the documentation by editing `docs/source/pydtm.rst` using [Sphinx autodoc directives](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directives).
7. **Write Tests**: Ensure your new code is tested with `unittest`. 
    - If you add a function to an existing file, add corresponding tests to the related file in the `tests/` folder.
    - If you create a new file, create a corresponding test file in the `tests/` folder, with a class inheriting from `unittest.TestCase`.
8. **Commit and Push Your Changes**: Commit your changes and push to your forked repository.
    ```sh
    git add .
    git commit -m "Description of your changes"
    git push origin feature-name
    ```
9. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request from your forked repository. Please ensure your pull request is against the `dev` branch.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
