<div align="center">

  <h1>
    <a href="https://github.com/senaite/senaite.lims">
      <div>
        <img src="static/senaite-logo.png" alt="senaite.lims" height="64" />
      </div>
    </a>
  </h1>

  <p>SENAITE LIMS Meta Installation Package</p>

  <div>
    <a href="https://pypi.python.org/pypi/senaite.lims">
      <img src="https://img.shields.io/pypi/v/senaite.lims.svg?style=flat-square" alt="pypi-version" />
    </a>
    <a href="https://github.com/senaite/senaite.lims">
      <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="pr" />
    </a>
    <a href="https://www.senaite.com">
      <img src="https://img.shields.io/badge/Made%20for%20SENAITE-%E2%AC%A1-lightgrey.svg" alt="Made for SENAITE" />
    </a>
  </div>
</div>

## What does SENAITE mean?

[SENAITE](https://www.senaite.com) is a beautiful trigonal, oil-green to
greenish black [crystal](https://www.mindat.org/min-3617.html), with almost the
hardness of a diamond. Although the crystal is described with a complex formula,
it still has clear and straight shapes. Therefore, it reflects nicely the
complexity of the LIMS, while providing a modern, intuitive and friendly
[UI](https://en.wikipedia.org/wiki/User_interface_design)/
[UX](https://en.wikipedia.org/wiki/User_experience).

## Installation (Modern - UV)

The recommended way to install SENAITE LIMS is using
[UV](https://docs.astral.sh/uv/), the extremely fast Python package manager.

### Prerequisites

- Python 3.10 or higher
- [UV](https://docs.astral.sh/uv/) package manager

### Quick Start

```bash
# Install UV (if not already installed)
# Windows (PowerShell)
irm https://astral.sh/uv/install.ps1 | iex

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/senaite/senaite.lims.git
cd senaite.lims

# Sync dependencies (creates .venv automatically)
uv sync

# Activate the virtual environment
# Windows
.\.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

# Run SENAITE instance
uv run instance fg
```

### Alternative: Buildout Installation

For traditional buildout-based installation, see the
[Installation Guide](docs/About.rst).

## License

**SENAITE.LIMS** Copyright (C) [RIDING BYTES](http://ridingbytes.com) &
[NARALABS](https://naralabs.com)

This program is free software; you can redistribute it and/or modify it under
the terms of the
[GNU General Public License version 2](https://github.com/senaite/senaite.lims/blob/master/LICENSE)
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsenaite%2Fsenaite.lims.svg?type=large)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsenaite%2Fsenaite.lims?ref=badge_large)
