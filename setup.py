from setuptools import setup, find_packages
import version

PACKAGE = 'xbmc-client'

setup(name = PACKAGE, version = version.VERSION,
    license = "WTFPL",
    description = "XBMC command line client",
    author = "Jean-Christophe Saad-Dupuy",
    author_email = "saad.dupuy@gmail.com",
    url = "https://github.com/jcsaaddupuy/xbmc-client",
    packages = find_packages('src'),
    package_dir = {'':'src'},   # tell distutils packages are under src
    include_package_data = True,
    package_data = {
      '':['config/*.conf']
      },
    entry_points = {
      'console_scripts': [
        'xbmc-client = xbmc_client:main',
        ]
      },
    install_requires = ["xbmc-json >= 0.2.0", ]
    )
