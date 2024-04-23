# requirements_dev.txt we use for testing.
It makes it easier to install and manage dependencies development and testing, separate from the dependencies required for production.

# Difference between requirements_dev.txt and requirements.txt

requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

# Tox.ini
We use it for the testing in the python package testing against different version of the python.

## How tox works, tox environment creation
1. Install dependencies and packages
2. Run Commands
3. It is a combination of the {virtualenwrapper and makefile)
4. It creates a .tox file.

# pyproject.toml
It is being used for configuration the python project. It is an alternative of the setup.cfg file. It contains configuration related to the build system such as the build tool used, package name, version, author, license and dependencies.

# setup.cfg
In summary, setup.cfg is used by setup tools to configure the packaging and installation of Python project.

# Testing python application
*types of testing*
1. Automated testing
2. Manual testing

# Modes of testing
1. Unit testing
2. Integrated testing