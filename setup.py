from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

setup(
    name='8D-Action-Planner',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Diogismar Barai, Jean Sandro, João Vitor & Júlio Cézar',
    author_email='joaovpro17@gmail.com',
    url='https://github.com/jvitorcosta/8d-action-planner',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')) + ['src'],
    install_requires=[line.strip() for line in open('requirements.txt')],
    entry_points={
        'console_scripts': [
            'planner8=src.run_app:main'
        ]
    }
)
