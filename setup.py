from setuptools import setup

setup(
  name = 'mydumper',
  description = 'Simple MySQL dumper',
  author = 'Roman Dolgushin',
  author_email = 'rd@roman-dolgushin.ru',
  url = 'https://github.com/rdolgushin/mydumper',
  license = 'MIT',
  version = '0.1',
  packages = ['mydumper'],
  install_requires = ['argparse'],
  entry_points = {
    'console_scripts': ['mydumper = mydumper.mydumper:main']
  },
  classifiers = [
    'Topic :: Utilities',
    'Topic :: Database',
    'Topic :: System :: Systems Administration',
    'Environment :: Console',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX'
  ],
)
