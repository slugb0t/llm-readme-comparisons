# Blended Sequence Imputation Pipeline

[![Nextflow](https://img.shields.io/badge/nextflow-%E2%89%A520.04.0-brightgreen.svg)](https://www.nextflow.io/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-10.1101%2F2024.04.03.587209-blue)](https://doi.org/10.1101/2024.04.03.587209)

A scalable Nextflow pipeline for constructing imputation reference panels from blended genome-exome sequencing data.

> Developed during the *Machine Learning and AI Approaches to Multimodal Problems in Computational Biology Hackathon*  
> (CMU Libraries and DNAnexus), March 03-05, 2025

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Results](#results)
- [Contributors](#contributors)
- [References](#references)

## Introduction

Blended Genome Exome (BGE) sequencing is an innovative approach that integrates:
- Low-pass whole genome sequencing (WGS) at ~3x coverage
- 30x coverage whole exome sequencing (WES)

This pipeline creates imputation reference panels using:
- Harmonized data from 1000 Genomes Project (1kGP) and Human Genome Diversity Project (HGDP)
- 4,091 subjects from diverse ancestries
- Cloud-optimized workflow (DNAnexus, GCP compatible)

Key advantages over traditional genotyping arrays:
- Not limited by predefined probe sets
- More inclusive for diverse populations
- Cost-effective alternative to deep whole genomes

## Features

- **Scalable processing**: Handles all autosomes (1-22) in parallel
- **Cloud-native**: Tested on DNAnexus, GCP, and local HPC systems
- **Efficient**: <1 hour runtime for full reference panel generation
- **Reproducible**: Containerized with Docker
- **Cost-effective**: ~$1.50 compute cost on DNAnexus

## Installation

### Prerequisites
- [Nextflow](https://www.nextflow.io/) (≥20.04.0)
- [Docker](https://www.docker.com/) (for containerized execution)
- [bcftools](https://samtools.github.io/bcftools/) (v1.10+ recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/[organization]/blended_seq_imputation.git
   cd blended_seq_imputation
   ```

2. Download reference data:
   - Available on [Google Cloud](gs://gcp-public-data--gnomad/resources/hgdp_1kg/phased_haplotypes_v2)
   - Or [AWS S3](s3://gnomad-public-us-east-1/resources/hgdp_1kg/phased_haplotypes_v2)

## Quick Start

Run the pipeline locally:
```bash
nextflow run main.nf \
  --input samples.txt \
  --map_dir path/to/map_files \
  --outdir results \
  -profile docker
```

## Usage

### Input Requirements
- Phased, imputed genotype data in VCF/BCF format (indexed)
- Sample sheet (see `example_inputs/samples_dnanexus.txt`)
- GLIMPSE2 map files

### Pipeline Steps
1. **Multiallelic conversion**: Convert to biallelic sites (SNPs + indels)
2. **Site extraction**: Extract cohort-wide site information
3. **Chunking**: Divide reference data using GLIMPSE2_chunk
4. **Splitting**: Create binary chromosome chunks

![Pipeline Workflow](figures/nextflow.drawio_whitebackground.png)

### DNAnexus Execution
1. Import repository following [nf-core instructions](https://academy.dnanexus.com/buildingworkflows/nf/importingandrunningnfcore)
2. Upload:
   - Sample sheet
   - Map files from GLIMPSE2 repository
3. Run with `-queue-size 22` for full autosome parallelization

## Results

- Binary reference panel files for imputation
- [Presentation slides](https://docs.google.com/presentation/d/1FQdrbxCqVt1jzBpF6MPERIgx8S5RtXtNTYlFa6TiLg4/edit?usp=sharing)

## Contributors

- Phil Greer
- Tien Ly
- Yuning Zheng
- Gobikrishnan Subramaniam

## References

1. DeFelice M, et al. Blended Genome Exome (BGE) as a Cost Efficient Alternative... bioRxiv (2024). [DOI:10.1101/2024.04.03.587209](https://doi.org/10.1101/2024.04.03.587209)
2. Koenig Z, et al. A harmonized public resource of deeply sequenced diverse human genomes. bioRxiv (2024). [DOI:10.1101/2023.01.23.525248](https://doi.org/10.1101/2023.01.23.525248)
3. Rubinacci S, et al. Efficient phasing and imputation... Nat Genet 53, 120–126 (2021). [DOI:10.1038/s41588-020-00756-0](https://doi.org/10.1038/s41588-020-00756-0)
4. Di Tommaso P, et al. Nextflow enables reproducible computational workflows. Nat Biotechnol 35, 316–319 (2017) [DOI:10.1038/nbt.3820](https://doi.org/10.1038/nbt.3820)

### Summary of Changes Made:

1. **Structure & Organization**:
   - Added a clear table of contents
   - Created logical sections with consistent heading hierarchy
   - Added badges for Nextflow version, license, and DOI
   - Moved contributors to a dedicated section

2. **Content Improvements**:
   - Wrote a concise project description at the top
   - Added a "Features" section highlighting key benefits
   - Separated installation from quick start instructions
   - Clarified input requirements and execution options
   - Standardized reference formatting with DOI links

3. **Readability Enhancements**:
   - Used bullet points for lists
   - Added code blocks for commands
   - Included visual hierarchy with section headers
   - Made links to resources more prominent

4. **Best Practice Additions**:
   - Added prerequisites section
   - Included quick start example
   - Maintained all original technical details
   - Kept all existing references with improved formatting

The improved README now provides better guidance for users while maintaining all the original technical information and academic references.