# cwltool: Reference Implementation of the Common Workflow Language (CWL)

[![Linux Status](https://github.com/common-workflow-language/cwltool/actions/workflows/ci-tests.yml/badge.svg?branch=main)](https://github.com/common-workflow-language/cwltool/actions/workflows/ci-tests.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/common-workflow-language/cwltool.svg)](https://codecov.io/gh/common-workflow-language/cwltool)
[![Documentation Status](https://readthedocs.org/projects/cwltool/badge/?version=latest)](https://cwltool.readthedocs.io/en/latest/?badge=latest)

**Package Status**

| Platform                                                | Version                                                                                                                                                         | Downloads                                                                                                                                                                                                                            |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [PyPI](https://pypi.org/project/cwltool/)               | ![PyPI](https://badge.fury.io/py/cwltool.svg)                                                                                                                   | ![Monthly](https://pepy.tech/badge/cwltool/month) / ![Total](https://static.pepy.tech/personalized-badge/cwltool?period=total\&units=international_system\&left_color=black\&right_color=orange\&left_text=Total%20PyPI%20Downloads) |
| [conda-forge](https://anaconda.org/conda-forge/cwltool) | ![Conda](https://anaconda.org/conda-forge/cwltool/badges/version.svg)                                                                                           | ![Installs](https://anaconda.org/conda-forge/cwltool/badges/downloads.svg)                                                                                                                                                           |
| [Debian](https://packages.debian.org/stable/cwltool)    | ![Stable](https://badges.debian.net/badges/debian/stable/cwltool/version.svg) / ![Testing](https://badges.debian.net/badges/debian/testing/cwltool/version.svg) |                                                                                                                                                                                                                                      |
| [Quay.io](https://quay.io/repository/commonwl/cwltool)  | ![Quay.io Container](https://quay.io/repository/commonwl/cwltool/status)                                                                                        |                                                                                                                                                                                                                                      |

---

## What is `cwltool`?

`cwltool` is the official reference implementation of the [Common Workflow Language (CWL)](https://www.commonwl.org/) standards. It provides:

* Complete validation and execution of CWL workflows and tools
* Support for multiple container backends
* Extensibility via CWL and CWL-specific hints

Developed in Python (3.9–3.13), `cwltool` is maintained by the [CWL Project](https://www.commonwl.org/) and supported by the [Software Freedom Conservancy](https://sfconservancy.org/).

---

## Installation

### Using System Package Managers

**Debian/Ubuntu**:

```bash
sudo apt-get update
sudo apt-get install cwltool
```

**macOS/UNIX with conda**:

```bash
conda install -c conda-forge cwltool
```

### Using pip (Recommended for Latest Version)

```bash
python3 -m venv env
source env/bin/activate
pip install cwlref-runner  # Installs both cwltool and cwl-runner
```

To avoid conflicts with other CWL runners:

```bash
pip install cwltool
```

### Windows (WSL2 Required)

Follow [WSL2 and Docker setup instructions](https://docs.docker.com/docker-for-windows/wsl/#prerequisites), then install Debian via the [Microsoft Store](https://www.microsoft.com/en-us/p/debian/9msvkqc78pk6) and follow the Linux installation steps.

### Development Version

```bash
git clone https://github.com/common-workflow-language/cwltool.git
cd cwltool
pip install .[deps]
cwltool --version
```

---

## Quick Start

Run a workflow:

```bash
cwltool my_workflow.cwl my_inputs.yaml
```

Or using the implementation-agnostic runner alias:

```bash
cwl-runner my_workflow.cwl my_inputs.yaml
```

Set global options:

```bash
export CWLTOOL_OPTIONS="--debug"
```

---

## Features

* **Container Support**: Docker, Podman, Singularity/Apptainer, uDocker
* **Partial Workflow Execution**: `--target`, `--print-targets`, `--print-subgraph`
* **Dependency Management**: Built-in support for Conda, Environment Modules, Galaxy packages
* **Remote Workflows**: Load CWL documents from HTTP\[S] URLs
* **Overrides**: Customize workflow/tool behavior at runtime with `--overrides`
* **Visualization**: Export to Graphviz (`--print-dot`) or RDF (`--print-rdf`)
* **Tool Registry Support**: Launch tools directly from GA4GH TRS (e.g., Dockstore)
* **MPI Execution**: Use `--enable-ext` to run MPI-based workflows
* **Fast Parser**: Speed up initialization for large workflows (experimental)

---

## Recommended Software

Install one of the following container engines:

* [Podman](https://podman.io/getting-started/installation)
* [Docker](https://docs.docker.com/engine/install/)
* [Singularity/Apptainer](https://apptainer.org/)
* [uDocker](https://indigo-dc.github.io/udocker/)

Optional (but recommended):

* [Node.js](https://nodejs.org/en/download/) for CWL Expressions

---

## Developer Guide

### Run Tests

```bash
pip install -r test-requirements.txt
pytest
```

Using `tox` for all supported Python versions:

```bash
pip install "tox<4"
tox -p
```

### Import as Python Module

```python
import cwltool.factory
fac = cwltool.factory.Factory()
echo = fac.make("echo.cwl")
result = echo(inp="foo")
print(result["out"])
```

### Conformance Testing

See: [CWL Conformance Test Guide](https://github.com/common-workflow-language/common-workflow-language/blob/main/CONFORMANCE_TESTS.md)

---

## Contributing

We welcome contributions! See the [contributing guide](https://github.com/common-workflow-language/cwltool/blob/main/CONTRIBUTING.md) and [issues](https://github.com/common-workflow-language/cwltool/issues) to get started.

---

## License

This project is [MIT licensed](https://github.com/common-workflow-language/cwltool/blob/main/LICENSE). It is a [Software Freedom Conservancy](https://sfconservancy.org/) member project.

---

## Resources

* [CWL User Guide](http://www.commonwl.org/user_guide/)
* [CWL Specification](https://www.commonwl.org/specification/)
* [Documentation](https://cwltool.readthedocs.io/)
* [CWLTool GitHub](https://github.com/common-workflow-language/cwltool/)

---

## Acknowledgments

Thanks to [our contributors](https://github.com/common-workflow-language/cwltool/graphs/contributors) and the open-source community.

---

## Summary of Improvements

* **Clear project description**: Frontloaded the "What is cwltool?" section.
* **Logical structure**: Organized into sections (Installation, Quick Start, Features, etc.) using modern open-source README conventions.
* **Badges consolidated**: Displayed under a consistent header.
* **Reduced redundancy**: Removed over-explained sections (e.g., repeated examples, inline command flags).
* **Added contribution & license info**: Essential for community participation.
* **Linked to resources**: User guide, docs, issues, contributing guide.
* **Maintained all original technical content**: Streamlined, not removed.

Let me know if you want this in `.rst` instead of Markdown.
