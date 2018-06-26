# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "1.2.1"

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
    description="SENAITE LIMS User Interface",
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
    author="SENAITE Foundation",
    author_email="hello@senaite.com",
    url="https://github.com/senaite/senaite.lims",
    license="GPLv2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    namespace_packages=["senaite"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "senaite.core",
        "senaite.api",
        "senaite.jsonapi",
        "setuptools",
    ],
    extras_require={
        "test": [
            "Products.PloneTestCase",
            "Products.SecureMailHost",
            "plone.app.robotframework",
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
