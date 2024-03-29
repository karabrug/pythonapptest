from setuptools import setup

setup(name='cpxrhyotherm',
      version='0.1',
      description='Low-Aluminum Clinopyroxene-Liquid Geothermometer for High-Silica Magmatic Systems',
      url='http://github.com/karabrug/cpxrhyotherm',
      author='Karalee K. Brugman',
      author_email='kara.brugman@gmail.com',
      license='GPL-3.0',
      packages=['cpxrhyotherm'],
      install_requires=[
          'pandas',
      ],
      zip_safe=False)
