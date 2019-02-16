'''
Created on 25 Jul 2017

@author: jdrumgoole
'''

from pymongo_import.version import __VERSION__

from setuptools import setup, find_packages
import os
import glob

pyfiles = [ f for f in os.listdir( "." ) if f.endswith( ".py" ) ]

    
setup(
    name = "pymongo_import",
    version =__VERSION__,
    
    author = "Joe Drumgoole",
    author_email = "joe@joedrumgoole.com",
    description = "pymongo_import - a program for reading CSV files into mongodb",
    long_description =
    '''
Pymongo_import is a program that can parse a csv file from its header and first line to
create an automated type conversion file (a .ff file) to control how types in the CSV
file are converted. This file can be edited once created (it is a ConfigParser format file).
For types that fail conversion the type conversion will fail back on string conversion.
Blank columns in the CSV file are marked as [blank-0], [blank-1] ... [blank-n] and are ignored
by the parser.
''',

    license = "AGPL",
    keywords = "MongoDB import csv",
    url = "https://github.com/jdrumgoole/pymongo_import",
    
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',


        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6' ],
   
    install_requires = [  "pymongo",
                          "nose",
                          "dnspython",
                          "dateutils"],
       
    packages=find_packages(),

    data_files = [ ( "test", glob.glob( "data/*.ff" ) +
                             glob.glob( "data/*.csv" ) +
                             glob.glob( "data/*.txt" ))],
    python_requires='>3.6',
    scripts=[],
    entry_points={
        'console_scripts': [
            'pymongo_import=pymongo_import.pymongo_import_main:mongo_import_main',
            'splitfile=pymongo_import.splitfile:splitfile',
            'pymongo_multiimport=pymongo_import.pymongo_multiimport_main:multi_import',
            'pwc=pymongo_import.pwc:pwc',
        ]
    },

    test_suite='nose.collector',
    tests_require=['nose'],
)
