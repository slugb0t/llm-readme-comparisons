# cwltool

[![Linux Build Status](https://github.com/common-workflow-language/cwltool/actions/workflows/ci-tests.yml/badge.svg?branch=main)](https://github.com/common-workflow-language/cwltool/actions/workflows/ci-tests.yml)
[![Coverage Status](https://img.shields.io/codecov/c/github/common-workflow-language/cwltool.svg)](https://codecov.io/gh/common-workflow-language/cwltool)
[![Documentation Status](https://readthedocs.org/projects/cwltool/badge/?version=latest)](https://cwltool.readthedocs.io/en/latest/?badge=latest)
[![PyPI Version](https://badge.fury.io/py/cwltool.svg)](https://pypi.org/project/cwltool/)
[![Conda Version](https://anaconda.org/conda-forge/cwltool/badges/version.svg)](https://anaconda.org/conda-forge/cwltool)
[![Debian Stable](https://badges.debian.net/badges/debian/stable/cwltool/version.svg)](https://packages.debian.org/stable/cwltool)
[![Docker Image](https://quay.io/repository/commonwl/cwltool/status)](https://quay.io/repository/commonwl/cwltool)

> The official reference implementation of the [Common Workflow Language (CWL)](https://www.commonwl.org/) standards.

`cwltool` provides a feature-complete, standards-compliant engine for executing CWL workflows. It validates CWL files, supports containerized execution, and integrates with a wide array of computing environments.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Running on Different Platforms](#running-on-different-platforms)
- [Advanced Features](#advanced-features)
- [Development](#development)
- [License](#license)
- [Community and Contributing](#community-and-contributing)

---

## Features

- Validates and runs CWL workflows and tools
- Supports Docker, Podman, Singularity, uDocker
- Execution of remote workflows and job inputs
- CWL visualization and RDF export
- Override requirements dynamically
- Partial workflow execution
- Experimental support for MPI and software requirement resolution

---

## Installation

### Using a Package Manager

#### Debian/Ubuntu

```bash
sudo apt-get update
sudo apt-get install cwltool
````

#### Conda (macOS, Linux)

```bash
conda install -c conda-forge cwltool
```

### Using pip and Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
pip install cwlref-runner  # also installs cwltool
```

To install just `cwltool` (e.g. alongside other CWL runners):

```bash
pip install cwltool
```

### Development Version

```bash
git clone https://github.com/common-workflow-language/cwltool.git
cd cwltool
pip install .[deps]
```

### Windows (WSL2)

1. Install WSL2 and Docker Desktop
2. Install Debian from the Microsoft Store
3. Set Debian as default:

   ```bash
   wsl --set-default debian
   ```
4. Enable WSL integration for Debian in Docker Desktop
5. Follow Linux install instructions inside Debian terminal

---

## Usage

### Basic Example

```bash
cwltool my_workflow.cwl my_inputs.yml
```

Or using the implementation-agnostic `cwl-runner` (requires `cwlref-runner`):

```bash
cwl-runner my_workflow.cwl my_inputs.yml
```

### Environment Configuration

```bash
export CWLTOOL_OPTIONS="--debug"
```

### Run from URL

```bash
cwltool https://example.com/workflow.cwl https://example.com/inputs.yml
```

---

## Running on Different Platforms

### macOS + Docker (Apple Silicon)

```bash
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

Add this line to `~/.zshrc` or `~/.bash_profile` to persist.

### Using uDocker

```bash
cwltool --udocker my_workflow.cwl my_inputs.json
```

[Installation instructions](https://indigo-dc.github.io/udocker/installation_manual.html)

### Using Singularity

```bash
cwltool --singularity my_workflow.cwl my_inputs.json
```

### Visualizing Workflows

Generate an SVG graph using Graphviz:

```bash
cwltool --print-dot my_workflow.cwl | dot -Tsvg > workflow.svg
```

### Run Partial Workflows

```bash
cwltool --target step3 my_workflow.cwl
```

Print available targets:

```bash
cwltool --print-targets my_workflow.cwl
```

---

## Advanced Features

### Requirement Overrides

Override requirements via `--overrides` or within input YAML.

```yaml
cwltool:overrides:
  echo.cwl:
    requirements:
      EnvVarRequirement:
        envDef:
          MESSAGE: override_value
```

### Packed Workflows

```bash
cwltool --pack my-workflow.cwl > packed-workflow.cwl
```

### SoftwareRequirement Support

Enable dependency resolution:

```bash
pip install 'cwltool[deps]'
cwltool --beta-conda-dependencies my_tool.cwl job.json
```

Supports Conda, Environment Modules, Galaxy packages.

### MPI Execution (Experimental)

Run MPI-based tools:

```bash
cwltool --enable-ext --mpi-config-file mpi-config.yml my_mpi_tool.cwl job.yml
```

See [`MPIRequirement` documentation](https://www.commonwl.org/v1.1/CommandLineTool.html#Extensions) for details.

---

## Development

### Run Tests

```bash
pip install -r test-requirements.txt
pytest
```

Or using `tox` for multiple Python versions:

```bash
pip install "tox<4"
tox -p
```

Run a specific test:

```bash
tox -e py310-unit -- -v tests/test_examples.py::test_scandeps
```

### CWL Conformance Tests

See [CONFORMANCE\_TESTS.md](https://github.com/common-workflow-language/common-workflow-language/blob/main/CONFORMANCE_TESTS.md)

### Use as a Python Module

```python
import cwltool.factory
fac = cwltool.factory.Factory()
result = fac.make("echo.cwl")(inp="hello")
print(result["out"])
```

---

## License

`cwltool` is licensed under the Apache License 2.0. See [LICENSE](https://github.com/common-workflow-language/cwltool/blob/main/LICENSE) for details.

---

## Community and Contributing

`cwltool` is a project of the [Software Freedom Conservancy](https://sfconservancy.org/news/2018/apr/11/cwl-new-member-project/) and maintained by [many contributors](https://github.com/common-workflow-language/cwltool/graphs/contributors).

* 📚 [Documentation](https://cwltool.readthedocs.io/en/latest/)
* 🐛 [Issue Tracker](https://github.com/common-workflow-language/cwltool/issues)
* 🤝 [Contributing Guide](https://github.com/common-workflow-language/cwltool/blob/main/CONTRIBUTING.md)


---

### Summary of Changes

- **Added Clear Project Description:** A brief, top-level summary was added to communicate what the project is and why it matters.
- **Reorganized Structure:** Introduced logical, scannable headings (Features, Installation, Usage, etc.) for better navigation.
- **Added Missing Sections:** Included Contributing, License, and Development to match standard open source README structure.
- **Standardized Badge Layout:** All badges are placed under the project title for immediate visibility.
- **Linked to Documentation and Resources:** Added or updated links to official documentation, contribution guidelines, and issue tracker.
- **Formatted Code Blocks Clearly:** All commands are now shown in fenced code blocks with syntax highlighting when applicable.
- **Removed Redundancy:** Condensed repeated information, grouped similar topics, and cleaned up long paragraphs to improve readability.

Let me know if you'd like a shorter version or one tailored for PyPI or ReadTheDocs.
```
