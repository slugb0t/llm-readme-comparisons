# Clustering of Haplotype Matrices

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
<!-- [![Build Status](https://github.com/<org>/<repo>/actions/workflows/ci.yml/badge.svg)](<link-to-actions>) -->

> **CMU Machine Learning and AI Approaches to Multimodal Problems in CompBio Hackathon 2025 - Group 1**

**Presentation:** [Google Slides](https://docs.google.com/presentation/d/1yswnVX3BMrS1aOnd0naY-LS3eOf_zn3z601ta6-wqNg/edit?usp=sharing)

## Table of Contents

- [Project Description](#project-description)
- [Team Members](#team-members)
- [Related / Previous Works](#related--previous-works)
- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
- [Results](#results)
- [Discussion](#discussion)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)
- [Packages/Tools Used](#packagestools-used)

---

## Project Description

This project presents a computational pipeline for the clustering and analysis of genetic haplotype matrices, focusing on data from the [1000 Genomes Project](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/). The pipeline integrates haplotype data processing, ancestral recombination graph (ARG) reconstruction, and machine learning techniques to explore genetic similarity among samples. Key steps include data conversion, preprocessing, ARG inference, and unsupervised clustering, with visualization and clinical annotation of results.

## Team Members

- Jon Moller  
- Ali Saadat V  
- Daniel Chang  
- William Lu  
- Emrah Kacar  
- Avish Jha  
- Francesco Andreace  

## Related / Previous Works

- [BCM HGSC / DNAnexus Hackathon 2024 - Haploblock Clusters](https://github.com/collaborativebioinformatics/Haploblock_Clusters)
- [Nucleate Pittsburgh 2024 - BioHack Haplotype](https://github.com/ShijieTang/BioHack_Haplotype)

## Installation

> **Note:** Please update this section with actual installation requirements and steps as appropriate for your codebase.

[Add details here: List required dependencies, environment setup instructions, and how to install them, e.g. via `conda`, `pip`, or Docker.]

Example:
```sh
git clone https://github.com/<org>/<repo>.git
cd <repo>
# Install dependencies
[Add installation commands here]
```

## Usage

> **Note:** Please update this section with actual usage instructions and example commands.

[Add details here: Provide step-by-step instructions for running the pipeline, including sample commands and input/output formats.]

Example:
```sh
# Preprocess VCF and generate HAP files
python scripts/preprocess.py --input data/chr6.vcf --output data/chr6.haps
# Run ARG-Needle
argneedle -i data/chr6.haps -o results/chr6.argn
# Perform clustering and visualization
python scripts/cluster_and_visualize.py --input results/chr6.argn
```

## Methods

This pipeline analyzes haplotype data from the 1000 Genomes Project and applies machine learning for clustering/similarity analysis. The workflow is as follows:

![Pipeline Flowchart](flowchart.png)

### 1. Data Acquisition

- Download phased Variant Call Format (VCF) files for chromosomes 6, 8, 21, and 22 from the [1000 Genomes Project](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/), pre-phased using SHAPEIT2.
- Chromosome selection: chr6 (comparison with prior groups), chr8 (beta defensin gene), chr21/22 (smaller size for test processing).

### 2. Data Conversion

- Convert VCFs to Oxford HAP (.haps) format using [PLINK2](https://www.cog-genomics.org/plink/2.0/).

### 3. Data Preprocessing

- Enforce space delimitation for ARG-Needle compatibility.
- Standardize sample IDs and variant identifiers.
- Limit allele length and generate new SNP IDs as needed.
- Prepare new sample files in the required format.

### 4. ARG Generation

- Modify map and hap files to ensure monotonically increasing variant positions and remove duplicates.
- Divide data into chunks for parallel ARG inference following [Zhang et al. 2023](https://www.nature.com/articles/s41588-023-01379-x).

### 5. Clustering Analysis & Visualization

- Use ARG-Needle-generated ARGN files for unsupervised clustering (e.g., hierarchical clustering).
- Visualize ARGs with [tskit](https://tskit.dev/tskit/docs/stable/introduction.html).
- Isolate and annotate biallelic SNPs using [OpenCravat](https://docs.opencravat.org/en/latest/) and ClinVar ACMG annotations.

## Results

### PCA Characterization of 1000 Genomes Data

![PCA](1000g_pca.webp)  
[Population Abbreviations](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/README_populations.md)

Whole-genome data was pruned for independent SNPs and PCA was run to reveal population overlap patterns.

### DEFB1

![DEFB1](DEFB1.png)

### HLA

![HLA](HLA.png)

- **X-axis:** Variants in each possible 1KG haplotype  
- **Y-axis:** 1KG individuals  
- Next step: annotate based on population/subpopulation on Y-axis (colors)

## Discussion

The pipeline successfully performs clustering and annotation analysis on example ARG-Needle data. However, generating ARGN files from chromosome-level 1000 Genomes data proved challenging, likely due to the genetic diversity of the 1000 Genomes population versus the more homogenous populations (e.g., UK Biobank) for which ARG-Needle was primarily developed.

Potential solutions include:
- Focusing ARG construction on more homogenous subpopulations.
- Exploring alternative tools such as [GenoTools](https://github.com/dvitale199/GenoTools).
- Brute-force similarity matrix calculation from haplotype data.

[Add further discussion or limitations here.]

## Contributing

Contributions are welcome!  
- Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  
- For questions and feature requests, open an [issue](https://github.com/<org>/<repo>/issues).  
- For major changes, please open a pull request.

## License

Distributed under the [MIT License](LICENSE).  
[Add details or alternative license here if necessary.]

## References

1. Sudmant, P. H., et al. (2015). An integrated map of structural variation in 2,504 human genomes. *Nature*, 526(7571), 75-81. https://doi.org/10.1038/nature15394
2. The 1000 Genomes Project Consortium. (2015). A global reference for human genetic variation. *Nature*, 526(7571), 68-74. https://doi.org/10.1038/nature15393
3. Vitale, D., et al. (2025). GenoTools: an open-source Python package for efficient genotype data quality control and analysis. *G3 Genes|Genomes|Genetics*, 15(1), jkae268. https://doi.org/10.1093/g3journal/jkae268
4. Zhang, B., et al. (2023). Biobank-scale inference of ancestral recombination enables genealogical analysis of complex traits. *Nature Genetics*, 55, 768–776. https://doi.org/10.1038/s41588-023-01379-x

## Packages/Tools Used

- [PLINK2](https://www.cog-genomics.org/plink/2.0/)
- [ARG-Needle](https://palamaralab.github.io/software/argneedle/) ([source publication](https://www.nature.com/articles/s41588-023-01379-x))
- [tskit](https://tskit.dev/tskit/docs/stable/introduction.html)
- [interpolate-genetic-position](https://github.com/lightning-auriga/interpolate-genetic-position)
- [OpenCravat](https://docs.opencravat.org/en/latest/)
- [DNANexus](https://platform.dnanexus.com/)
- [JupyterLab](https://jupyter.org/)

---

## Notes / TODOs

- Update [Installation](#installation) and [Usage](#usage) with concrete details and commands.
- Add links to GitHub Actions or other CI/CD badges if available.
- Expand [Discussion](#discussion) with further analysis and next steps.
- Add more examples and screenshots if possible.

---

### Summary of Changes

- Reorganized README with clear section headings and logical flow.
- Added a concise project description at the top.
- Added a Table of Contents for easy navigation.
- Added placeholder sections for Installation and Usage, with prompts to add real instructions.
- Included a Contributing section with links for future contributors.
- Added a License section for clarity.
- Provided badge examples (license; build status placeholder).
- Improved clarity and formatting throughout, with explicit links to referenced works and tools.
- Added a Notes/TODOs section to highlight remaining gaps.

These changes follow GitHub’s best practices for open source project documentation, ensuring the README is actionable, welcoming, and easy to update in the future.