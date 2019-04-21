from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(
        name = 'pgbackup',
        version = '0.1.0',
        author = 'Andres Mella Romero',
        author_email = 'andres.mella.romero@gmail.com',
        decription = 'A utility for backing uo PostgreSQL databases',
        long_decription = long_description,
        long_description_content_type = 'text/markdown',
        url = 'https://github.com/am3lla/projects.git',
        packages = find_packages('src')
)
