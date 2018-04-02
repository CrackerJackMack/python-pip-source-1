from setuptools import setup, find_packages

setup(
    name='testpip_1',
    version='0.0.1',
    packages=find_packages(),
    package_data={},
    author='Kevin Landreth',
    author_email='crackerjackmack@gmail.com',
    description='bug testing',
    include_package_data=False,
    install_requires=[
        'libtestpip',
    ],
    dependency_links=[
        'git+ssh://git@github.com/crackerjackmack/python-pip-source-2@dont-use-parse#egg=libtestpip-0',
    ],
    entry_points='''
    '''
)


