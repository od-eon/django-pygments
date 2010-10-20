import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README'))
readme = f.read()
f.close()

setup(
        name='django-pygments',
        version='0.1',
        description='A django app that provides a template tag and 2 filters for \
                doing syntax highlighting with Pygments',
        long_description=readme,
        author='Stefan Talpalaru',
        author_email='developers@od-eon.com',
        url='http://github.com/odeoncg/django-pygments/tree/master',
        packages=find_packages(),
        include_package_data=True,
        install_requires=['pygments', 'lxml'],
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
            ],
        )
