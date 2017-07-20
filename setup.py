import os
import re
import codecs
from distutils.core import setup


def open_local(paths, mode='r', encoding='utf8'):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        *paths
    )

    return codecs.open(path, mode, encoding)


with open_local(['validator', '__init__.py'], encoding='latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

with open_local(['README.rst']) as rm:
    long_description = rm.read()

setup(
    name='simple-validator',
    version=version,
    packages=['validator'],
    platforms='any',
    url='https://github.com/seanpar203/validator',
    license='MIT',
    author='Sean Parsons',
    author_email='seanpatrick2013@gmail.com',
    long_description=long_description,
    description='A simple way to validate dictionary values by using functions.',
    download_url='https://github.com/seanpar203/validator/archive/{}.tar.gz'.format(version),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
