<div align="center">

  <h1>
    <a href="https://github.com/senaite/senaite.lims">
      <div>
        <img src="static/logo.png" alt="senaite.lims" />
      </div>
    </a>
  </h1>

  <p>SENAITE LIMS - Professional Open Source LIMS</p>

  <div>
    <a href="https://travis-ci.org/senaite/senaite.lims">
      <img src="https://img.shields.io/travis/senaite/senaite.lims.svg?style=flat-square" alt="travis-ci" />
    </a>
    <a href="docs/Contributing.rst">
      <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="travis-ci" />
    </a>
  </div>
</div>


## What does SENAITE mean?

[SENAITE](http://senaite.com) is a beautiful trigonal, oil-green to greenish
black [crystal](https://www.mindat.org/min-3617.html), with almost the hardness
of a diamond. Although the crystal is described with a complex formula, it still
has clear and straight shapes. Therefore, it reflects nicely the complexity of
the LIMS, while providing a modern, intuitive and friendly [UI](https://en.wikipedia.org/wiki/User_interface_design)/
[UX](https://en.wikipedia.org/wiki/User_experience).


## What is this Project about?

The primary goal of [SENAITE Project](https://github.com/senaite/senaite.lims) is to provide
a complete new and modern way to interact with [SENAITE CORE](https://github.com/senaite/bika.lims).

[SENAITE CORE](https://github.com/senaite/bika.lims) depends heavily on [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
and most of the logic is custom built with [jQuery](https://jquery.com).

While this is applicable for smaller projects, it becomes almost impossible to maintain it in larger projects.
Therefore, [SENAITE](http://senaite.com) introduces modern JavaScript frameworks like
[ReactJS](https://reactjs.org), [BackboneJS](http://backbonejs.org) or [AngularJS](https://angularjs.org)
to provide a robust user interface which follows industry standards.

[SENAITE](http://senaite.com) ships with a complete [RESTful JSON API](https://github.com/senaite/senaite.jsonapi)
built on [plone.jsonapi.routes](http://plonejsonapiroutes.readthedocs.io/en/latest), which serves as the main communication interface
between [SENAITE CORE](https://github.com/senaite/bika.lims) and any kind of modern web framework.

This makes great web applications like the [Spotlight Search](http://www.ridingbytes.com/de/portfolio/bika-spotlight-search/#content)
or the [Plone Commander](http://www.ridingbytes.com/de/portfolio/plone-commander/#content) possible
and allows frontend develpers to interface custom web application with [SENAITE CORE](https://github.com/senaite/bika.lims).

The User Interface of [SENAITE LIMS](https://github.com/senaite/senaite.lims) follows
a mobile first approach and is built with [Twitter Bootstrap](http://getbootstrap.com).
This makes it also possible to easily to operate in the web interface with tablets and smart devices


## Installation

Please follow these steps to install Plone:
https://docs.plone.org/4/en/manage/installing/index.html

To install SENAITE LIMS, you simply have to add `senaite.lims` into the `eggs` section
of your `buildout.cfg`:

    eggs =
      ...
      senaite.lims

Also see this section of the Plone documentation for further details:
https://docs.plone.org/4/en/manage/installing/installing_addons.html

---
**NOTE:** To install the latest version from the sources, follow the instructhion of the
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

```
git clone https://github.com/senaite/senaite.lims.git
cd senaite.lims
python bootstrap.py
bin/buildout
bin/instance fg
```


## License

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsenaite%2Fsenaite.lims.svg?type=large)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsenaite%2Fsenaite.lims?ref=badge_large)

<h2 align="center">Core Team</h2>

<table>
  <tbody>
    <tr>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/rockfruit.png?s=150">
        <br>
        <a href="https://github.com/rockfruit">Campbell McKellar Basset</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/xispa.png?s=150">
        <br>
        <a href="https://github.com/xispa">Jordi Puiggené</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/ramonski.png?s=150">
        <br>
        <a href="https://github.com/ramonski">Ramon Bartl</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/Espurna.png?s=150">
        <br>
        <a href="https://github.com/Espurna">Pau Soliva</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/juangallostra.png?s=150">
        <br>
        <a href="https://github.com/juangallostra">Juan Gallostra Acín</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/Nihadness.png?s=150">
        <br>
        <a href="https://github.com/Nihadness">Nihad M.</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/mikejmets.png?s=150">
        <br>
        <a href="https://github.com/mikejmets">Mike Metcalfe</a>
      </td>
      <td align="center" valign="top">
        <img width="150" src="https://github.com/Lunga001.png?s=150">
        <br>
        <a href="https://github.com/Lunga001">Lunga Baliwe</a>
      </td>
    </tr>
  </tbody>
</table>


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
