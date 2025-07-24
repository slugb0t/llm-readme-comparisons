# cwltool: The Reference Implementation of the Common Workflow Language (CWL) Standards

[![Linux Status](https://github.com/common-workflow-language/cwltool/actions/workflows/ci-tests.yml/badge.svg?branch=main)](https://github.com/common-workflow-language/cwltool/actions/workflows/ci-tests.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/common-workflow-language/cwltool.svg)](https://codecov.io/gh/common-workflow-language/cwltool)
[![Documentation Status](https://readthedocs.org/projects/cwltool/badge/?version=latest)](https://cwltool.readthedocs.io/en/latest/?badge=latest)
[![PyPI Version](https://badge.fury.io/py/cwltool.svg)](https://badge.fury.io/py/cwltool)
[![PyPI Downloads](https://pepy.tech/badge/cwltool/month)](https://pepy.tech/project/cwltool)
[![Conda Version](https://anaconda.org/conda-forge/cwltool/badges/version.svg)](https://anaconda.org/conda-forge/cwltool)
[![Debian Stable Package](https://badges.debian.net/badges/debian/stable/cwltool/version.svg)](https://packages.debian.org/stable/cwltool)
[![Quay.io Container](https://quay.io/repository/commonwl/cwltool/status)](https://quay.io/repository/commonwl/cwltool)

---

## Overview

**cwltool** is the official reference implementation of the [Common Workflow Language (CWL) open standards](https://www.commonwl.org/). It is designed to be feature complete and provides comprehensive validation of CWL files, along with tools for CWL workflow authoring and execution.

cwltool is written and tested for **Python 3.9, 3.10, 3.11, 3.12, and 3.13**.

The reference implementation consists of:

- **cwltool**: The main Python module and console executable.
- **cwlref-runner**: (Optional) Provides an additional entry point, `cwl-runner`, which is the implementation-agnostic name for the default CWL interpreter.

cwltool is maintained by the [CWL project](https://sfconservancy.org/news/2018/apr/11/cwl-new-member-project/) and [many contributors](https://github.com/common-workflow-language/cwltool/graphs/contributors).

---

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
  - [Linux / macOS / Conda](#linux--macos--conda)
  - [Windows](#windows)
  - [Development Version](#development-version)
  - [Recommended Software](#recommended-software)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Running with Containers](#running-with-containers)
  - [Remote and Local Tool Execution](#remote-and-local-tool-execution)
  - [Advanced Features](#advanced-features)
- [Development](#development)
- [Import as a Module](#import-as-a-module)
- [Extension Points](#extension-points)
- [Contributing](#contributing)
- [License](#license)
- [Links & Documentation](#links--documentation)

---

## Installation

### Linux / macOS / Conda

#### Using OS Packages

- **Debian/Ubuntu**:
    ```bash
    sudo apt-get update
    sudo apt-get install cwltool
    ```

- **Conda** (after [conda-forge setup](https://conda-forge.org/#about)):
    ```bash
    conda install -c conda-forge cwltool
    ```

#### Using `pip` with a Virtual Environment

If the packaged version is too old or you want the latest version:

```bash
python3 -m venv env
source env/bin/activate
pip install cwlref-runner   # or pip install cwltool
```

### Windows

1. [Install Windows Subsystem for Linux 2 and Docker Desktop](https://docs.docker.com/docker-for-windows/wsl/#prerequisites).
2. [Install Debian from the Microsoft Store](https://www.microsoft.com/en-us/p/debian/9msvkqc78pk6).
3. Set Debian as default: `wsl --set-default debian`
4. Enable WSL integration in Docker Desktop (`Settings` → `Resources` → `WSL Integration`).
5. Reboot if needed.
6. Launch Debian and follow Linux instructions above.

Network problems? See [these instructions](https://github.com/microsoft/WSL/issues/4731#issuecomment-702176954).

### Development Version

To install the latest development version:

```bash
git clone https://github.com/common-workflow-language/cwltool.git
cd cwltool
pip install .[deps]
cwltool --version
```

If co-installing multiple CWL implementations, manage `cwl-runner` using [Debian Alternatives](https://wiki.debian.org/DebianAlternatives) or similar.

### Recommended Software

- One of:
    - [Podman](https://podman.io/getting-started/installation)
    - [Docker](https://docs.docker.com/engine/install/)
    - Singularity/Apptainer: [See docs](https://github.com/hpcng/singularity/releases/)
    - uDocker: [See docs](https://github.com/indigo-dc/udocker)
- [Node.js](https://nodejs.org/en/download/) (for faster expression evaluation and required for `udocker`)

Without these, some [CWL tutorials](http://www.commonwl.org/user_guide/) may not work.

---

## Usage

### Basic Usage

```bash
cwl-runner my_workflow.cwl my_inputs.yaml
# or, to use cwltool directly
cwltool my_workflow.cwl my_inputs.yaml
```

Set default options via environment variable:

```bash
export CWLTOOL_OPTIONS="--debug"
```

### Running with Containers

- **With Docker on macOS (Apple Silicon):**
    ```bash
    export DOCKER_DEFAULT_PLATFORM=linux/amd64
    ```
    Add to your shell profile to set automatically.

- **With uDocker:**
    ```bash
    cwltool --udocker <workflow.cwl> <input.json>
    ```
    [uDocker installation guide](https://indigo-dc.github.io/udocker/installation_manual.html)

- **With Singularity:**
    ```bash
    cwltool --singularity <workflow.cwl> <input.json>
    ```

#### Special Notes for macOS with boot2docker
Set `--tmpdir-prefix` and `--tmp-outdir-prefix` under `/Users` due to Docker mount limitations.

### Remote and Local Tool Execution

- cwltool supports running workflows from local files or HTTP[S] URLs.
- Input jobs and workflow steps can reference CWL documents using relative or absolute paths.
- Use [`cwldep`](https://github.com/common-workflow-language/cwldep) to manage dependencies.

### Advanced Features

- **Overrides:** Add requirement overrides via the `--overrides` flag or in the job file.
- **Packing Workflows:** Combine multiple files into a single document:
    ```bash
    cwltool --pack my-wf.cwl > my-packed-wf.cwl
    ```
- **Partial Workflow Execution:** Use `--target` to run only part of a workflow.
- **Graph Visualization:** Generate a Graphviz dot file:
    ```bash
    cwltool --print-dot my-wf.cwl | dot -Tsvg > my-wf.svg
    ```
- **RDF Modeling:** Output workflows as RDF triples:
    ```bash
    cwltool --print-rdf --rdf-serializer=turtle mywf.cwl
    ```
- **Environment Variables:** Supports several methods, including `EnvVarRequirement`, command-line flags, and beta dependency management.
- **SoftwareRequirement Support (Beta):**
    - Use `pip install 'cwltool[deps]'` for optional dependency resolution features.
    - Supports integration with [Conda](https://conda.io/docs/#), Environment Modules, and Galaxy packages.
    - See [Dependency Resolvers in Galaxy](https://docs.galaxyproject.org/en/latest/admin/dependency_resolvers.html) for advanced configuration.

- **GA4GH Tool Registry API:** Launch tools from [Dockstore](https://dockstore.org/) or other GA4GH registries.
    ```bash
    cwltool quay.io/collaboratory/dockstore-tool-bamstats:develop test.json
    ```
    [GA4GH Tool Registry API docs](https://github.com/ga4gh/tool-registry-schemas)

- **MPI Support:** Use `--enable-ext` and see [MPIRequirement docs](https://www.commonwl.org/) for details.

- **Fast Parser (Experimental):** Use `--fast-parser` for faster initialization of large workflows. See [open issues](https://github.com/common-workflow-language/cwltool/pull/1720) for limitations.

---

## Development

### Running Tests

- **Basic Tests:**
    ```bash
    pip install -rtest-requirements.txt
    pytest
    ```
    (Requires node.js or Docker)

- **Testing on Multiple Python Versions (with tox):**
    ```bash
    pip install "tox<4"
    tox -p
    ```
    List environments: `tox --listenvs`
    Run a specific test: `tox -e py310-unit -- -v tests/test_examples.py::test_scandeps`

- **CWL Conformance Tests:**  
  See [CONFORMANCE_TESTS.md](https://github.com/common-workflow-language/common-workflow-language/blob/main/CONFORMANCE_TESTS.md) in the CWL Specification repository.

---

## Import as a Module

```python
import cwltool
import cwltool.factory

fac = cwltool.factory.Factory()
echo = fac.make("echo.cwl")
result = echo(inp="foo")
# result["out"] == "foo"
```

---

## Extension Points

cwltool provides many extension points for custom execution, loading, and environment management. See the [official documentation](https://cwltool.readthedocs.io/) for full details and examples.

[Add details here] if you wish to list specific extension points or provide code samples.

---

## Contributing

We welcome contributions! Please see the [contributing guidelines](https://github.com/common-workflow-language/cwltool/blob/main/CONTRIBUTING.md) for more information.

---

## License

[Apache License 2.0](https://github.com/common-workflow-language/cwltool/blob/main/LICENSE)

---

## Links & Documentation

- [Official website](https://www.commonwl.org/)
- [Full documentation](https://cwltool.readthedocs.io/)
- [User Guide](http://www.commonwl.org/user_guide/)
- [Issue Tracker](https://github.com/common-workflow-language/cwltool/issues)
- [Contributor Graph](https://github.com/common-workflow-language/cwltool/graphs/contributors)
- [Software Freedom Conservancy](https://sfconservancy.org/news/2018/apr/11/cwl-new-member-project/)

[Add additional links here as appropriate]