from setuptools import setup, find_packages
from HTTP.version import (__version__)


setup(
    name='CD_HTTP',
    version=__version__,
    description='An HTTP wrapper around the wonderful requests library to make it easier for new users and old.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nicholas Capasso',
    author_email='codedocta@gmail.com',
    url='https://github.com/codedocta/cdhttp',
    packages=find_packages(),
    install_requires=[
        'setuptools~=65.5.1',
        'requests~=2.31.0',
    ],
    classifiers=[
        -
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
