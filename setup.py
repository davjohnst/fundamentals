from setuptools import setup

setup(name='Sorting Fun',
      version='0.0.1',
      description='Playing with sorting algorithms',
      url='https://github.com/davjohnst/sorting',
      author='David Johnston',
      author_email='davjohnst at gmail dot com',
      license='Apache 2',
      packages=['sorting', 'sorting.mergesort', 'sorting.quicksort', 'sorting.tests'],
      zip_safe=False,
      test_suite='nose.collector',  # $ python setup.py test
      tests_require=['nose'],
)
