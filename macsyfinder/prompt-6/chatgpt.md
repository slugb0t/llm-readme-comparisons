Here is the improved version of the MacSyFinder README, rewritten using modern open-source documentation standards and best practices. The goal was to enhance structure, clarity, and accessibility while retaining all verifiable content.

---

````markdown
![MacSyFinder banner](./.github/logo_macsyfinder.png "MacSyFinder")

# MacSyFinder

[![Build Status](https://github.com/gem-pasteur/macsyfinder/actions/workflows/testing.yml/badge.svg?branch=master)](https://github.com/gem-pasteur/macsyfinder/actions/workflows/testing.yml)
[![codecov](https://codecov.io/gh/gem-pasteur/macsyfinder/branch/master/graph/badge.svg?token=q31HWcV3SM)](https://codecov.io/gh/gem-pasteur/macsyfinder)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/macsyfinder)](https://pypi.org/project/macsyfinder/)
[![PyPI](https://img.shields.io/pypi/v/macsyfinder)](https://pypi.org/project/macsyfinder/)
[![Docker Image Version](https://img.shields.io/docker/v/gempasteur/macsyfinder?label=docker&sort=semver)](https://hub.docker.com/r/gempasteur/macsyfinder)
[![Conda](https://img.shields.io/conda/vn/bioconda/macsyfinder?style=plastic)](https://github.com/bioconda/bioconda-recipes/tree/master/recipes/macsyfinder)
[![Docs](https://readthedocs.org/projects/macsyfinder/badge/?version=latest)](https://macsyfinder.readthedocs.io/en/latest)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6010/badge)](https://bestpractices.coreinfrastructure.org/projects/6010)
[![FAIR software badge](https://fairsoftwarechecklist.net/badge.svg)](https://fairsoftwarechecklist.net/v0.2?f=31&a=32113&i=32321&r=133)

**MacSyFinder** is a computational tool to **detect macromolecular systems in protein datasets** using a combination of **systems modeling** and **similarity search**. It enables the identification of complex molecular machineries (e.g., secretion systems, pili, or CRISPR-Cas) across genomes, using user-defined models.

---

## 🚀 Features

- Detection of complex molecular systems in genome-scale protein datasets
- Flexible, user-defined system modeling
- Support for curated and custom models
- Integration with HMMER, Docker, Conda, and Apptainer

---

## 📦 Installation

> **Important:** `MacSyFinder` requires **HMMER ≥ 3.1**. Please install it manually unless using `conda/mamba`. If you are a model developer, `git` is also required.

### Recommended: Install in a virtual environment

```bash
python3 -m venv macsy-env
source macsy-env/bin/activate
````

### Option 1: Install via PyPI

```bash
pip install macsyfinder==<version>
```

### Option 2: Install via Conda/Mamba

```bash
mamba install -c bioconda macsyfinder=<version>
```

### Option 3: Install from source

```bash
git clone https://github.com/gem-pasteur/macsyfinder.git
cd macsyfinder
pip install .
```

---

## 🧪 Running Tests

You can run unit tests with:

```bash
python3 setup.py test
# or
python3 tests/run_tests.py -vv
# or a specific test
python3 tests/run_tests.py -vv tests/test_example.py
```

---

## 🧬 Installing Models

MacSyFinder uses external *models* to define system architectures. These are **not bundled** with the software. Use the `macsydata` tool to install and manage models from [macsy-models](https://github.com/macsy-models):

### Basic usage:

```bash
macsydata available        # List available models
macsydata search <query>   # Search models
macsydata install <package>  # Install specific model(s)
```

📘 [Detailed guide](https://macsyfinder.readthedocs.io/en/latest/user_guide/installation.html#models-installation-with-macsydata)

> ⚠️ Models not hosted on `macsy-models` must be downloaded manually and installed using `macsydata`.

---

## 🐳 Docker & Apptainer

### Using Docker

```bash
mkdir shared_dir && cd shared_dir
docker run -v ${PWD}:/home/msf -u $(id -u):$(id -g) gempasteur/macsyfinder:<tag> macsydata install --target /home/msf/my_models <MODELS>

docker run -v ${PWD}:/home/msf -u $(id -u):$(id -g) gempasteur/macsyfinder:<tag> \
  macsyfinder --db-type gembase --models-dir=/home/msf/my_models \
  --models TFF-SF ComM T4P --sequence-db my_genome.fasta -w 12
```

### Using Apptainer (formerly Singularity)

```bash
apptainer run -H $HOME docker://gempasteur/macsyfinder:<tag> \
  macsydata install --target my_models <MODELS>

apptainer run -H $HOME docker://gempasteur/macsyfinder:<tag> \
  macsyfinder --db-type gembase --models-dir=my_models \
  --models TFF-SF ComM T4P --sequence-db my_genome.fasta -w 12
```

---

## 📂 Example Datasets

* [Basic dataset with example command line and outputs](https://doi.org/10.6084/m9.figshare.21581280.v1)
* [Extended dataset](https://doi.org/10.6084/m9.figshare.21716426.v1)
* [Quickstart tutorial](https://macsyfinder.readthedocs.io/en/latest/user_guide/quickstart.html#an-example-data-set)

---

## 📖 Documentation

Full user, developer, and modeler documentation is available on [ReadTheDocs](https://macsyfinder.readthedocs.io/en/latest/).

* [User Guide](https://macsyfinder.readthedocs.io/en/latest/user_guide/)
* [Modeler Guide](https://macsyfinder.readthedocs.io/en/latest/modeler_guide/)
* [Developer Guide](https://macsyfinder.readthedocs.io/en/latest/developer_guide/)

---

## 🆕 What's New in v2.x

Check the [release notes and upgrade guide](https://macsyfinder.readthedocs.io/en/latest/user_guide/new_v2.html) to learn about major changes in v2.x.

---

## 📚 Citation

If you use MacSyFinder in your research, please cite:

**MacSyFinder v2:**
Néron *et al.* (2023). *MacSyFinder v2: Improved modelling and search engine to identify molecular systems in genomes.*
Peer Community Journal, 3\:e28. [DOI:10.24072/pcjournal.250](https://doi.org/10.24072/pcjournal.250)

**MacSyFinder v1:**
Abby *et al.* (2014). *MacSyFinder: A Program to Mine Genomes for Molecular Systems with an Application to CRISPR-Cas Systems.*
PLoS ONE 9(10)\:e110726. [DOI:10.1371/journal.pone.0110726](https://doi.org/10.1371/journal.pone.0110726)

---

## 👥 Contributing

We welcome bug reports, feature requests, and contributions.

Please read our [Contributing Guide](CONTRIBUTING.md) before submitting a pull request.

👤 [List of Contributors](CONTRIBUTORS.md)

---

## 🔐 License

MacSyFinder is licensed under the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0).

---

## 📝 Notes for macOSX Testing

The `setsid` binary in the `utils/` directory is used **only** for macOS functional testing. It is built using the [setsid-macosx project](https://github.com/tzvetkoff/setsid-macosx).

```

---

### ✅ Summary of Changes

| Section | Changes Made |
|--------|--------------|
| Top | Reordered badges for readability; rewrote description for clarity |
| Structure | Added logical sectioning: Features, Installation, Models, Docker, Examples, Docs, etc. |
| Installation | Standardized virtualenv + pip/conda/git sections |
| Docker | Made the section concise, corrected casing, added clearer command block syntax |
| Apptainer | Improved instructions and made behavior differences from Docker clearer |
| Documentation & Examples | Prominently linked relevant sections |
| Language | Rephrased for clarity, corrected typos and grammar |
| Footer | Consolidated License, Contributing, and Testing Notes |
| Format | Used consistent code blocks, headers, bullets, and emphasis styles |

Let me know if you'd like a version split into separate files like `INSTALL.md`, `CONTRIBUTING.md`, etc.
```
