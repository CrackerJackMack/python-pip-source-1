import uuid
from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs if ir.req]

setup(
    name='testpip_1',
    version='0.0.1',
    packages=find_packages(),
    package_data={},
    author='Kevin Landreth',
    author_email='crackerjackmack@gmail.com',
    description='bug testing',
    include_package_data=False,
    install_requires=reqs,
    entry_points='''
    '''
)
