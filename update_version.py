import re

# Read the version from the VERSION file
with open('VERSION') as version_file:
    version = version_file.read().strip()

# Update pyproject.toml
with open('pyproject.toml', 'r+') as pyproject_file:
    content = pyproject_file.read()
    content = re.sub(r'version = ".*"', f'version = "{version}"', content)
    pyproject_file.seek(0)
    pyproject_file.write(content)
    pyproject_file.truncate()

# Update conf.py
with open('docs/source/conf.py', 'r+') as conf_file:
    content = conf_file.read()
    content = re.sub(r'release = ".*"', f'release = "{version}"', content)
    conf_file.seek(0)
    conf_file.write(content)
    conf_file.truncate()

print(f'Updated version to {version} in pyproject.toml and docs/conf.py')
