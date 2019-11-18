from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = []

setup(name='libraryname',
      version='0.0',  # TODO make this set programmatically
      description='libraryname, a python library which solves problems related to x',
      url='https://github.com/ofloveandhate/pythonlibrarystarter.com',
      author='Silviana Amethyst',
      author_email='silvianaamethyst@gmail.com',
      packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
      install_requires=['matplotlib',
                        'numpy'],
      package_dir={'libraryname': 'libraryname'},
      zip_safe=False)
