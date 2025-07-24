# Clustering of Haplotype Matrices

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
> CMU Machine Learning and AI Approaches to Multimodal Problems in CompBio Hackathon 2025 — Group 1

A computational pipeline for exploring genetic similarity and clustering among samples using haplotype data from the 1000 Genomes Project. This project integrates haplotype data processing, ancestral recombination graph (ARG) reconstruction, and machine learning techniques to analyze population-level genetic variation.

**Presentation:** [Google Slides](https://docs.google.com/presentation/d/1yswnVX3BMrS1aOnd0naY-LS3eOf_zn3z601ta6-wqNg/edit?usp=sharing)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Quick Start](#quick-start)
- [Pipeline and Methods](#pipeline-and-methods)
- [Results](#results)
- [Discussion](#discussion)
- [Related Works](#related-works)
- [References](#references)
- [Packages and Tools](#packages-and-tools)
- [Contributing](#contributing)
- [Team](#team)
- [License](#license)

---

## Project Overview

Haplotype analysis is essential for understanding genetic variation and evolutionary relationships. This project presents a robust pipeline for:
- Processing phased variant call format (VCF) files from the 1000 Genomes Project
- Converting data to haplotype (HAP) format with PLINK2
- Preprocessing for ARG-Needle compatibility
- Performing clustering and similarity analysis on gene-specific haplotypes
- Visualizing results with PCA and hierarchical clustering

The pipeline focuses on chromosomes 6, 8, 21, and 22, with gene-specific filtering for TNF, HLA-A, and beta defensin—genes of varying variability and clinical importance.

---

## Features

- End-to-end pipeline for haplotype data processing and clustering
- ARG reconstruction using [ARG-Needle](https://palamaralab.github.io/software/argneedle/)
- SNP annotation with [OpenCravat](https://docs.opencravat.org/en/latest/)
- Gene-specific filtering and visualization
- Reproducible analysis leveraging open-source tools

---

## Getting Started

### Installation

> **Note:** This project relies on several external tools. Please refer to each tool's official documentation for installation.  
> [Add details here for setting up the repository, dependencies, and configuring the environment.]

#### Prerequisites

- [PLINK2](https://www.cog-genomics.org/plink/2.0/)
- [ARG-Needle](https://palamaralab.github.io/software/argneedle/)
- [tskit](https://tskit.dev/tskit/docs/stable/introduction.html)
- [OpenCravat](https://docs.opencravat.org/en/latest/)
- [DNANexus](https://platform.dnanexus.com/)
- [JupyterLab](https://jupyter.org/)
- [interpolate-genetic-position](https://github.com/lightning-auriga/interpolate-genetic-position)

### Quick Start

1. **Clone the repository**

   ```bash
   git clone [Add repository URL here]
   cd [repository-directory]
   ```

2. **Prepare input data**

   - Download phased VCF files for chromosomes 6, 8, 21, and 22 from the [1000 Genomes Project](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/).

3. **Convert VCF to HAP format**

   - Use PLINK2 to convert VCF files:
     ```bash
     plink2 --vcf input.vcf --make-just-hap --out output
     ```

4. **Preprocess data for ARG-Needle**

   - Ensure correct formatting as described in [Pipeline and Methods](#pipeline-and-methods).

5. **Run ARG-Needle and downstream analysis**

   - See [Pipeline and Methods](#pipeline-and-methods) for step-by-step instructions.

> [Add details here for running specific scripts, setting parameters, or using example data.]

---

## Pipeline and Methods

The pipeline consists of the following key steps:

### 1. Data Acquisition

- Obtain phased VCFs for chromosomes 6, 8, 21, and 22 (prephased with SHAPEIT2).
- Focused on chr 6 (TNF, HLA-A), chr 8 (beta defensin), and smaller chromosomes for test runs.

### 2. Data Conversion

- Convert VCF files to Oxford phased haplotype format (`.haps`) using PLINK2.

### 3. Data Preprocessing

- Enforce space delimitation for ARG-Needle compatibility.
- Synchronize IDs in `.sample` files.
- Assign unique IDs to variants missing identifiers.
- Set maximum allele length to 280.
- Generate new SNP names/IDs by combining columns 2-4.
- Create a new sample file with the modified format.

### 4. ARG Generation

- Modify map and hap files to ensure monotonically increasing variant positions.
- Remove duplicated variants.
- Split phased data into non-overlapping chunks as in [Zhang et al. 2023](https://www.nature.com/articles/s41588-023-01379-x).
- Perform ARG inference in parallel.

### 5. Clustering Analysis and Visualization

- Use ARG-Needle output for initial clustering pipelines.
- Visualize ARGs and haplotype clusters with tskit and custom scripts.
- Annotate haplotypes with clinical significance using OpenCravat and ClinVar ACMG.

---

## Results

### PCA Characterization of 1000 Genomes Data

![1000 Genomes PCA](1000g_pca.webp)

- [Population Abbreviations](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/README_populations.md)
- PCA performed on pruned, independent SNPs reveals patterns of population overlap.

### DEFB1

![DEFB1 Results](DEFB1.png)

### HLA

![HLA Results](HLA.png)

- X-axis: Variants in each possible 1KG haplotype  
- Y-axis: 1KG individuals  
- [Add further annotation and interpretation here.]

---

## Discussion

Despite achieving clustering and annotation on example ARG-Needle data, producing ARGN files from the full chromosome-level 1000 Genomes haplotype data proved challenging. ARG-Needle, primarily tested on homogeneous populations (UK Biobank), faced difficulties with the diverse 1000 Genomes data. A potential solution is to select more homogeneous subpopulations for ARG construction.

Alternative approaches:
- Use tools like [GenoTools](https://github.com/dvitale199/GenoTools)
- Directly generate similarity matrices from haplotype data

> [Add further insights, limitations, and future directions here.]

---

## Related Works

- [BCM HGSC / DNAnexus Hackathon 2024 - Haploblock Clusters](https://github.com/collaborativebioinformatics/Haploblock_Clusters)
- [Nucleate Pittsburgh 2024 - BioHack Haplotype](https://github.com/ShijieTang/BioHack_Haplotype)

---

## References

1. Sudmant, P. H., et al. (2015). An integrated map of structural variation in 2,504 human genomes. *Nature*, 526(7571), 75-81. https://doi.org/10.1038/nature15394
2. The 1000 Genomes Project Consortium. (2015). A global reference for human genetic variation. *Nature*, 526(7571), 68-74. https://doi.org/10.1038/nature15393
3. Vitale, D., et al. (2025). GenoTools: an open-source Python package for efficient genotype data quality control and analysis. *G3 Genes|Genomes|Genetics*, 15(1), jkae268. https://doi.org/10.1093/g3journal/jkae268
4. Zhang, B., et al. (2023). Biobank-scale inference of ancestral recombination enables genealogical analysis of complex traits. *Nature Genetics*, 55, 768–776. https://doi.org/10.1038/s41588-023-01379-x.

---

## Packages and Tools

- [PLINK2](https://www.cog-genomics.org/plink/2.0/)
- [ARG-Needle](https://palamaralab.github.io/software/argneedle/) ([publication](https://www.nature.com/articles/s41588-023-01379-x))
- [tskit](https://tskit.dev/tskit/docs/stable/introduction.html)
- [interpolate-genetic-position](https://github.com/lightning-auriga/interpolate-genetic-position)
- [OpenCravat](https://docs.opencravat.org/en/latest/)
- [DNANexus](https://platform.dnanexus.com/)
- [JupyterLab](https://jupyter.org/)

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  
[Add link or details if a contributing guide exists.]

---

## Team

- Jon Moller
- Ali Saadat V
- Daniel Chang
- William Lu
- Emrah Kacar
- Avish Jha
- Francesco Andreace

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

### Summary of Changes

- **Reorganized sections** for logical flow and clear navigation, adding a Table of Contents.
- **Added an actionable project summary** and a concise features list.
- **Inserted badges** for license (other badges can be added as available).
- **Clarified installation and quick-start steps**, with placeholders for missing repo-specific details.
- **Refined and structured the methods section** for stepwise reproducibility.
- **Linked all referenced tools and resources** to their official documentation or repositories.
- **Added placeholders** where project-specific instructions, links, or details are missing to avoid fabrication.
- **Enhanced readability** with consistent formatting, clear headings, and markdown best practices.
- **Included sections for contributing and license** to meet open source standards.

This restructuring follows GitHub's recommended README structure and community best practices, making the document clearer and more actionable for both users and potential contributors.