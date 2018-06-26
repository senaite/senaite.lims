<div align="center">

  <h1>
    <a href="https://github.com/senaite/senaite.lims">
      <div>
        <img src="static/senaite-logo.png" alt="senaite.lims" height="64" />
      </div>
    </a>
  </h1>
  <p>Responsive User Interface for SENAITE Core</p>

  <div>
    <a href="https://pypi.python.org/pypi/senaite.lims">
      <img src="https://img.shields.io/pypi/v/senaite.lims.svg?style=flat-square" alt="pypi-version" />
    </a>
    <a href="https://github.com/senaite/senaite.lims/pulls">
      <img src="https://img.shields.io/github/issues-pr/senaite/senaite.lims.svg?style=flat-square" alt="open PRs" />
    </a>
    <a href="https://github.com/senaite/senaite.lims/issues">
      <img src="https://img.shields.io/github/issues/senaite/senaite.lims.svg?style=flat-square" alt="open Issues" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="pr" />
    </a>
  </div>
</div>


## What does SENAITE mean?

[SENAITE](https://www.senaite.com) is a beautiful trigonal, oil-green to greenish
black [crystal](https://www.mindat.org/min-3617.html), with almost the hardness
of a diamond. Although the crystal is described with a complex formula, it still
has clear and straight shapes. Therefore, it reflects nicely the complexity of
the LIMS, while providing a modern, intuitive and friendly [UI](https://en.wikipedia.org/wiki/User_interface_design)/
[UX](https://en.wikipedia.org/wiki/User_experience).


## What is this Project about?

The primary goal of [SENAITE Project](https://github.com/senaite/senaite.lims) is to provide
a complete new and modern way to interact with [SENAITE CORE](https://github.com/senaite/senaite.core).

[SENAITE CORE](https://github.com/senaite/senaite.core) depends heavily on [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
and most of the logic is custom built with [jQuery](https://jquery.com).

While this is applicable for smaller projects, it becomes almost impossible to
maintain it in larger projects. Therefore, [SENAITE](https://www.senaite.com)
introduces modern JavaScript frameworks to provide a robust user interface which
follows industry standards.

[SENAITE](https://www.senaite.com) ships with a complete [RESTful JSON API](https://github.com/senaite/senaite.jsonapi)
built on [plone.jsonapi.routes](http://plonejsonapiroutes.readthedocs.io/en/latest), which serves as the main communication interface
between [SENAITE CORE](https://github.com/senaite/senaite.core) and any kind of modern web framework.

This makes great web applications like the [Spotlight Search](http://www.ridingbytes.com/de/portfolio/bika-spotlight-search/#content)
or the [Plone Commander](http://www.ridingbytes.com/de/portfolio/plone-commander/#content) possible
and allows frontend develpers to interface custom web application with [SENAITE CORE](https://github.com/senaite/senaite.core).

The User Interface of [SENAITE LIMS](https://github.com/senaite/senaite.lims) follows
a mobile first approach and is built with [Twitter Bootstrap](http://getbootstrap.com).
This makes it also possible to easily to operate in the web interface with tablets and smart devices


## Installation

Please follow the installations instructions for
[Plone 4](https://docs.plone.org/4/en/manage/installing/index.html)


Before installing SENAITE LIMS or Plone, there are some system dependencies that
must be installed. They are listed below.

Debian/Ubuntu:

    sudo apt-get install build-essential gcc python-dev git-core libffi-dev
    sudo apt-get install libpcre3 libpcre3-dev autoconf libtool pkg-config
    sudo apt-get install zlib1g-dev libssl-dev libexpat1-dev libxslt1.1
    sudo apt-get install gnuplot libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0

Fedora:

    sudo dnf install make automake-1.15-1.fc22.noarch gcc gcc-c++-5.3.1-2.fc22.x86_64
    sudo dnf install kernel-devel-4.3.4-200.fc22.x86_64 gdk-pixbuf2-devel-2.31.6-1.fc22.x86_64
    sudo dnf install python-devel-2.7.10-8.fc22.x86_64 git-2.4.3-7.fc22.x86_64
    sudo dnf install libffi-devel-3.1-7.fc22.x86_64 pcre-devel-8.38-1.fc22.x86_64
    sudo dnf install autoconf-2.69-20.fc22.noarch libtool-2.4.2-35.fc22.x86_64
    sudo dnf install pkgconfig-1\:0.28-8.fc22.x86_64 zlib-devel-1.2.8-7.fc22.x86_64
    sudo dnf install openssl-devel-1\:1.0.1k-13.fc22.x86_64 expat-devel-2.1.0-10.fc22.x86_64
    sudo dnf install libxslt-devel-1.1.28-8.fc22.x86_64 gnuplot-5.0.0-8.fc22.x86_64
    sudo dnf install cairo-devel-1.14.2-1.fc22.x86_64 pango-devel-1.36.8-6.fc22.x86_64


To install SENAITE LIMS, you have to add `senaite.lims` into the `eggs`
list inside the `[buildout]` section of your `buildout.cfg`:

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

The above example works for the buildout created by the unified installer. If
you however have a custom buildout you might need to add the egg to the `eggs`
list in the `[instance]` section rather than adding it in the `[buildout]`
section.

Also see this section of the Plone documentation for further details:
https://docs.plone.org/4/en/manage/installing/installing_addons.html


**Important**

For the changes to take effect you need to re-run buildout from your console:

    bin/buildout


### Installation Requirements

The following versions are required for SENAITE LIMS:

- Plone >= 4.3.17
- senaite.core >= 1.2.6
- senaite.api >= 1.2.3
- senaite.jsonapi

Please follow these steps to install Plone:
https://docs.plone.org/4/en/manage/installing/index.html

---
**IMPORTANT:** SENAITE is **not** yet compatible with Plone 5.x.x versions

---

---
**NOTE:** To install the latest version from the sources, follow the instructions in the
[Development](#development) section to install `senaite.lims` on your computer.

---

## Development

You can create a development environment using [Buildout](https://pypi.python.org/pypi/zc.buildout)
directly from the root folder of the project.
Please have a look into the [buildout.cfg](https://github.com/senaite/senaite.lims/blob/master/buildout.cfg)
configuration for further details.

It is recommended that you use
a [Virtualenv](https://virtualenv.pypa.io/en/stable) before preparing the
environment with the following commands:

    git clone https://github.com/senaite/senaite.lims.git
    cd senaite.lims
    python bootstrap.py
    bin/buildout
    bin/instance fg


## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsenaite%2Fsenaite.lims.svg?type=large)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsenaite%2Fsenaite.lims?ref=badge_large)


**We want contributing to SENAITE LIMS to be fun, enjoyable, and educational for
anyone, and everyone.**

Contributions go far beyond pull requests and commits. Although we love giving
you the opportunity to put your stamp on SENAITE LIMS, we also are thrilled to
receive a variety of other contributions including:

* [Documentation](https://github.com/senaite/senaite.lims.com) updates, enhancements, designs, or bugfixes
* Spelling or grammar fixes
* README.md corrections or redesigns
* Adding unit, or functional tests
* Triaging GitHub issues -- especially determining whether an issue still persists or is reproducible.
* [Searching #senaite on twitter](https://twitter.com/search?q=senaitelims) and helping someone else who needs help
* Teaching others how to contribute to one of the many SENAITE repo's!
* [Blogging, speaking about, or creating tutorials](https://github.com/senaite-contrib/awesome-senaite) about one of senaite's many features.
* Helping others in our SENAITE [gitter channel](https://gitter.im/senaite/Lobby).
