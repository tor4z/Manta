PACKAGE      = "manta"
NAME         = PACKAGE
DESCRIPTION  = "multithread framwork"
AUTHOR       = "tor4z"
AUTHOR_EMAIL = "vwenjie@hotmail.com"
URL          = "https://github.com/tor4z/Manta"
LICENSE      = "MIT License"
VERSION      = __import__(PACKAGE).__version__

from setuptools import setup, find_packages

setup(name         = NAME,
      version      = VERSION,
      description  = DESCRIPTION,
      author       = AUTHOR,
      author_email = AUTHOR_EMAIL,
      license      = LICENSE,
      url          = URL,
      packages = find_packages(exclude=["test"])
      )