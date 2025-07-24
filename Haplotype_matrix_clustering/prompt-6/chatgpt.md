Here is your improved README in Markdown format, following best practices for open source documentation:

---

# 🧬 Clustering of Haplotype Matrices

> CMU Machine Learning and AI Approaches to Multimodal Problems in CompBio Hackathon 2025 — Group 1

A computational pipeline for analyzing haplotype data using ARG (Ancestral Recombination Graph) reconstruction and unsupervised machine learning. This project leverages phased genomic data from the 1000 Genomes Project to explore genetic similarity, cluster individuals, and annotate haplotypes by clinical significance.

[![Hackathon Presentation](https://img.shields.io/badge/slides-presentation-blue)](https://docs.google.com/presentation/d/1yswnVX3BMrS1aOnd0naY-LS3eOf_zn3z601ta6-wqNg/edit?usp=sharing)

---

## 🚀 Quick Start

> **Requirements:** [PLINK2](https://www.cog-genomics.org/plink/2.0/), [ARG-Needle](https://palamaralab.github.io/software/argneedle/), [tskit](https://tskit.dev/), [OpenCravat](https://docs.opencravat.org/en/latest/), Python 3.8+

1. **Download phased VCFs** from [1000 Genomes Project](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/).
2. **Convert VCF to HAP format** with PLINK2:

   ```bash
   plink2 --vcf input.vcf --export haps --out output
   ```
3. **Preprocess files** to match ARG-Needle input requirements (details below).
4. **Run ARG-Needle** on chunked haplotype data.
5. **Perform clustering** and visualize results using `tskit` and custom scripts.

> \[Add installation/setup instructions or link if available.]

---

## 📂 Table of Contents

* [Introduction](#introduction)
* [Pipeline Overview](#pipeline-overview)
* [Methods](#methods)
* [Results](#results)
* [Discussion](#discussion)
* [Related Work](#related-work)
* [References](#references)
* [Tools Used](#tools-used)
* [Contributors](#contributors)

---

## 🧪 Introduction

Haplotype analysis is essential for exploring genetic variation and ancestry. This project constructs a full pipeline on DNAnexus for processing haplotype data, generating ARGs, and applying clustering to investigate genetic relationships. We focused on regions with known clinical relevance (e.g., **TNF**, **HLA-A**, **beta defensin**) due to their contrasting variability.

We used SHAPEIT2-phased VCFs from chromosomes 6, 8, 21, and 22 from the 1000 Genomes Project and filtered for gene-specific regions. Hierarchical clustering and similarity matrices were produced from haplotype data.

---

## 🧭 Pipeline Overview

![Pipeline Overview](flowchart.png)

---

## ⚙️ Methods

### Step 1: Data Acquisition

* Downloaded phased VCFs for chromosomes 6, 8, 21, and 22.
* Selected chromosomes based on size, gene variability, and relevance to immune function.

### Step 2: Data Conversion

* Used PLINK2 to convert `.vcf` files into `.haps/.sample` format:

  ```bash
  plink2 --vcf input.vcf --export haps --out output
  ```

### Step 3: Preprocessing

* Ensured space-delimited formatting for `.haps` files.
* Matched sample IDs in `.sample` file (ID\_1 = ID\_2).
* Assigned variant IDs where missing.
* Standardized max allele length (280).
* Created unique SNP IDs by concatenating columns 2–4.

### Step 4: ARG Inference

* Removed duplicate variants and ensured monotonic position ordering.
* Chunked data for parallel inference, following [Zhang et al., 2023](https://www.nature.com/articles/s41588-023-01379-x).
* Used ARG-Needle for generating `.argn` files from each data chunk.

### Step 5: Clustering and Annotation

* Conducted hierarchical clustering using custom scripts on ARG-Needle outputs.
* Used [OpenCravat](https://docs.opencravat.org/en/latest/) to annotate SNPs with clinical significance via ClinVar ACMG annotations.
* Visualization done with `tskit`.

---

## 📊 Results

### Principal Component Analysis (PCA)

![PCA](1000g_pca.webp)
Dimensionality reduction of low-LD SNPs reveals population clustering patterns.
👉 [Population Abbreviations](https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/README_populations.md)

### Gene-Specific Cluster Visualizations

#### DEFB1 (Beta Defensin)

![DEFB1](DEFB1.png)

#### HLA-A

![HLA](HLA.png)

* X-axis: SNP variants
* Y-axis: 1KG individuals
* Next Step: Add population annotations by color

---

## 💬 Discussion

We successfully developed methods for ARG generation and clustering on sample data. However, full-scale ARG construction from the diverse 1000 Genomes dataset proved challenging.

**Potential issues:**

* ARG-Needle was originally benchmarked on UK Biobank (a homogeneous dataset).
* High population diversity in 1000G likely disrupted threading algorithms.

**Proposed solutions:**

* Filter for subpopulations within 1000G to reduce genetic variability.
* Explore tools like [GenoTools](https://github.com/dvitale199/GenoTools) or direct computation of similarity matrices.

---

## 🔗 Related Work

* [Haploblock Clusters (DNAnexus Hackathon 2024)](https://github.com/collaborativebioinformatics/Haploblock_Clusters)
* [BioHack Haplotype (Nucleate Pittsburgh 2024)](https://github.com/ShijieTang/BioHack_Haplotype)

---

## 📚 References

1. Sudmant et al., *Nature* (2015): [10.1038/nature15394](https://doi.org/10.1038/nature15394)
2. The 1000 Genomes Project Consortium, *Nature* (2015): [10.1038/nature15393](https://doi.org/10.1038/nature15393)
3. Vitale et al., *G3* (2025): [10.1093/g3journal/jkae268](https://doi.org/10.1093/g3journal/jkae268)
4. Zhang et al., *Nature Genetics* (2023): [10.1038/s41588-023-01379-x](https://doi.org/10.1038/s41588-023-01379-x)

---

## 🧰 Tools Used

| Tool                                                                                             | Purpose                   |
| ------------------------------------------------------------------------------------------------ | ------------------------- |
| [PLINK2](https://www.cog-genomics.org/plink/2.0/)                                                | Haplotype file conversion |
| [ARG-Needle](https://palamaralab.github.io/software/argneedle/)                                  | ARG construction          |
| [tskit](https://tskit.dev/)                                                                      | ARG/tree visualization    |
| [OpenCravat](https://docs.opencravat.org/en/latest/)                                             | Clinical annotation       |
| [DNANexus](https://platform.dnanexus.com/)                                                       | Pipeline hosting          |
| [JupyterLab](https://jupyter.org/)                                                               | Development environment   |
| [interpolate-genetic-position](https://github.com/lightning-auriga/interpolate-genetic-position) | Genetic map interpolation |

---

## 👥 Contributors

* Jon Moller
* Ali Saadat V
* Daniel Chang
* William Lu
* Emrah Kacar
* Avish Jha
* Francesco Andreace

---

## 📌 To Do

* [ ] Add ARG visualization for chromosome-specific datasets
* [ ] Annotate cluster plots by population group
* [ ] Package pipeline steps into reproducible scripts or notebook
* [ ] Add license and installation instructions

---

## 📝 Summary of Changes

* **Added** a clear project description and badges for readability.
* **Reorganized** sections with consistent Markdown formatting.
* **Added** a Quick Start section to improve usability.
* **Improved clarity** in Methods and Results with bullet points and inline code.
* **Linked tools and references** to their official sources.
* **Created placeholders** (e.g., for setup instructions or ARG figures) without assuming missing content.
* **Standardized terminology** and added visual hierarchy for easier scanning.

Let me know if you'd like a version with live links, LaTeX support for equations, or conversion to reStructuredText (`.rst`).
