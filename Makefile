.PHONY = help create_project_env install_requirements run_tests

PROJECT_ENV = pydtm
PYTHON_VERSION = 3.9

help:
	@echo "----------------------------------------------------------------------"
	@echo "|                                HELP                                |"
	@echo "----------------------------------------------------------------------"
	@echo "To create the project's conda environment > make create_project_env"
	@echo "To install the project's requirements > make install_requirements"
	@echo "To run the tests > make run_tests"

create_project_env:
	@echo "Creating Project Environment with conda"
	@conda create -n ${PROJECT_ENV} python=${PYTHON_VERSION} -y

install_requirements:
	@echo "Installing the necessary requirements"
	@pip install -r env/requirements.txt

run_tests:
	@echo "Running tests..."
	@export PYTHONPATH=. && pytest tests --color yes --verbose