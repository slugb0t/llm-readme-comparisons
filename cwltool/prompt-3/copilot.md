# cwltool: The Reference Implementation of the Common Workflow Language Standards

**cwltool** is the official reference implementation of the [Common Workflow Language (CWL)](https://www.commonwl.org/) standards. It aims to be feature-complete and provide comprehensive validation for CWL files, along with utilities for working with CWL workflows and tools.

## Key Features

- **Robust CWL Support:** Validates and runs CWL v1.x workflows and tools.
- **Comprehensive Validation:** Ensures adherence to the CWL specification for portability and reproducibility.
- **Multiple Installation Options:** Available via pip, conda, Debian/Ubuntu packages, and as a Docker container.
- **Container Support:** Runs tools using Docker, Podman, Singularity/Apptainer, or udocker.
- **Flexible Execution:** Execute workflows from local files or remote URLs. Supports GA4GH Tool Registry API.
- **Development and Extension:** Can be used as a Python module, supports custom extension points for workflow execution, resource selection, and more.
- **Advanced Features:** Includes support for dependency resolution via Conda, Environment Modules, or custom mappings; workflow packing; partial workflow execution; visualization; and MPI-based parallelism.

## Installation

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get update
  sudo apt-get install cwltool
  ```
- **Conda (macOS/Linux):**
  ```bash
  conda install -c conda-forge cwltool
  ```
- **Pip (with virtual environment):**
  ```bash
  python3 -m venv env
  source env/bin/activate
  pip install cwlref-runner  # Installs cwltool as a dependency
  ```
- **Development Version:**
  ```bash
  git clone https://github.com/common-workflow-language/cwltool.git
  cd cwltool
  pip install .[deps]
  ```

> *MS Windows users should use WSL2 with a Linux distribution and follow Linux installation steps.*

## Basic Usage

Run a workflow using the implementation-agnostic entry point:
```bash
cwl-runner my_workflow.cwl my_inputs.yaml
```

Or, specifically with cwltool:
```bash
cwltool my_workflow.cwl my_inputs.yml
```

Set global options via the environment:
```bash
export CWLTOOL_OPTIONS="--debug"
```

## Advanced Capabilities

- **Partial workflow execution:** Use `--target` to run only specific workflow steps.
- **Workflow visualization:** Use `--print-dot` to output Graphviz DOT files.
- **Dependency management:** Use flags like `--beta-conda-dependencies` for automatic Conda-based resolution, or configure custom dependency resolvers.
- **Remote execution:** Run CWL workflows and tools directly from HTTP(S) URLs or GA4GH Tool Registry endpoints.
- **MPI Support:** Run parallel workflows with MPI (e.g., `mpirun`) using the `MPIRequirement` extension and `--enable-ext`.
- **Pack workflows:** Combine multiple CWL files into a single packed document with `--pack`.

## Development & Testing

- **Run tests:**
  ```bash
  pip install -rtest-requirements.txt
  pytest
  ```
- **Comprehensive testing with tox:**
  ```bash
  pip install "tox<4"
  tox -p
  ```

## As a Python Module

Import and use cwltool in your Python scripts:
```python
import cwltool.factory
fac = cwltool.factory.Factory()
echo = fac.make("echo.cwl")
result = echo(inp="foo")
assert result["out"] == "foo"
```

## Documentation & Resources

- [Full documentation](https://cwltool.readthedocs.io/en/latest/)
- [CWL specification](https://www.commonwl.org/)
- [CWL User Guide](http://www.commonwl.org/user_guide/)
- [Dependency resolver configuration](https://docs.galaxyproject.org/en/latest/admin/dependency_resolvers.html)

---

cwltool is developed by the [Common Workflow Language project](https://www.commonwl.org/) and is a member project of the [Software Freedom Conservancy](https://sfconservancy.org/).  
For contributors, see the [GitHub contributor graph](https://github.com/common-workflow-language/cwltool/graphs/contributors).