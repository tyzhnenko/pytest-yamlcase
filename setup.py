from setuptools import setup

setup(
    name='pytest-yamlcase',
    description='Run tests for Fuel defined in yaml',
    author='Dmitry Tyzhnenko',
    author_email='t.dmitry@gmail.com',
    version='0.1',
    packages=['pytest_yamlcase'],
    entry_points={
        'pytest11': [
            'pytest_yamlcase = pytest_yamlcase.plugin',
        ]
    },
    install_requires=['pyyaml', 'pytest'],
)
