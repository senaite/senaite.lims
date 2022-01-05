# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "2.1.0"

with open("docs/About.rst", "r") as fh:
    long_description = fh.read()

with open("docs/Changelog.rst", "r") as fh:
    long_description += "\n\n"
    long_description += "Changelog\n"
    long_description += "=========\n\n"
    long_description += fh.read()


setup(
    name="senaite.lims",
    version=version,
    description="SENAITE LIMS - Meta Package",
    long_description=long_description,
    # long_description_content_type="text/markdown",
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="",
    author="RIDING BYTES & NARALABS",
    author_email="senaite@senaite.com",
    url="https://github.com/senaite/senaite.lims",
    license="GPLv2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    namespace_packages=["senaite"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Plone==5.2.6",
        "senaite.core==2.1.0",
        "senaite.app.listing==2.1.0",
        "senaite.app.spotlight==2.1.0",
        "senaite.app.supermodel==2.1.0",
        "senaite.impress==2.1.0",
        "senaite.jsonapi==2.1.0",
        "setuptools",
    ],
    extras_require={
        "test": [
            "Products.PloneTestCase",
            "Products.SecureMailHost",
            "plone.app.testing",
            "unittest2",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
