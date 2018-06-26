.. image:: https://raw.githubusercontent.com/senaite/senaite.lims/master/static/senaite-logo.png
   :alt: senaite.lims
   :height: 64 px
   :align: center

- **SENAITE.LIMS**: Responsive User Interface for SENAITE Core**

.. image:: https://img.shields.io/pypi/v/senaite.lims.svg?style=flat-square
   :target: https://pypi.python.org/pypi/senaite.lims

.. image:: https://img.shields.io/github/issues-pr/senaite/senaite.lims.svg?style=flat-square
   :target: https://github.com/senaite/senaite.lims/pulls

.. image:: https://img.shields.io/github/issues/senaite/senaite.lims.svg?style=flat-square
   :target: https://github.com/senaite/senaite.lims/issues

.. image:: https://img.shields.io/badge/README-GitHub-blue.svg?style=flat-square
   :target: https://github.com/senaite/senaite.lims#readme


About
=====

The primary goal of SENAITE LIMS is to provide a complete new and modern way to
interact with SENAITE CORE.


Installation
============

Please follow the installations instructions for `Plone 4`_ and
`senaite.lims`_.

To install SENAITE.LIMS, you have to add `senaite.lims` into the
`eggs` list inside the `[buildout]` section of your
`buildout.cfg`::

   [buildout]
   parts =
       instance
   extends =
       http://dist.plone.org/release/4.3.17/versions.cfg
   find-links =
       http://dist.plone.org/release/4.3.17
       http://dist.plone.org/thirdparty
   eggs =
       Plone
       Pillow
       senaite.lims
   zcml =
   eggs-directory = ${buildout:directory}/eggs

   [instance]
   recipe = plone.recipe.zope2instance
   user = admin:admin
   http-address = 0.0.0.0:8080
   eggs =
       ${buildout:eggs}
   zcml =
       ${buildout:zcml}

   [versions]
   setuptools =
   zc.buildout =


**Note**

The above example works for the buildout created by the unified
installer. If you however have a custom buildout you might need to add
the egg to the `eggs` list in the `[instance]` section rather than
adding it in the `[buildout]` section.

Also see this section of the Plone documentation for further details:
https://docs.plone.org/4/en/manage/installing/installing_addons.html

**Important**

For the changes to take effect you need to re-run buildout from your
console::

   bin/buildout


Installation Requirements
-------------------------

The following versions are required for SENAITE.LIMS:

-  Plone 4.3.17
-  senaite.core >= 1.2.7
-  senaite.api >= 1.2.0


.. _Plone 4: https://docs.plone.org/4/en/manage/installing/index.html
.. _senaite.lims: https://github.com/senaite/senaite.lims#installation
