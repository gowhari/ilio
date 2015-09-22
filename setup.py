from setuptools import setup


setup(name='ilio',
      version='0.3.0',
      description='inline io: just one function call instead of file open(), read(), close()',
      long_description=open('README.rst').read(),
      url='https://github.com/gowhari/ilio',
      author='Iman Gowhari',
      author_email='gowhari@gmail.com',
      license='MIT',
      packages = ['ilio'],
      zip_safe=False)
