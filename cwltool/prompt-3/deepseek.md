# cwltool: The Common Workflow Language Reference Implementation

cwltool is the reference implementation of the Common Workflow Language (CWL) standards, providing comprehensive validation and execution capabilities for CWL workflows.

## Key Features

- **Complete CWL Support**: Fully implements CWL specifications for running tools and workflows
- **Multiple Execution Environments**: Supports Docker, Singularity, uDocker, and Conda
- **Portable**: Works across Linux, macOS, and Windows (via WSL2)
- **Extensible**: Offers multiple extension points for customization

## Installation Options

### Package Managers
```bash
# Debian/Ubuntu
sudo apt-get install cwltool

# Conda
conda install -c conda-forge cwltool
```

### Python Package
```bash
python3 -m venv env
source env/bin/activate
pip install cwlref-runner
```

## Basic Usage

```bash
cwl-runner workflow.cwl inputs.yaml
# or 
cwltool workflow.cwl inputs.yaml
```

## Advanced Features

- **Partial Workflow Execution**: Run only specific steps with `--target`
- **Workflow Packaging**: Combine multiple files into one with `--pack`
- **Visualization**: Generate workflow diagrams with `--print-dot`
- **Dependency Management**: Leverage Conda, Environment Modules, or custom resolvers
- **MPI Support**: Run parallel tools with MPI requirements

## Development

Run tests with:
```bash
pip install -rtest-requirements.txt
pytest
```

## Extensibility

cwltool provides multiple extension points including:
- Custom executor functions
- Version reporting
- Document fetching/resolving
- Resource selection
- Filesystem access

For complete documentation and advanced configuration options, visit the [official documentation](https://cwltool.readthedocs.io/).

cwltool is part of the CWL project, a member project of Software Freedom Conservancy.