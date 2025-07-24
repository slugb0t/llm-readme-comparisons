# Codefair

<div align="center">
  <img src="https://raw.githubusercontent.com/fairdataihub/codefair-app/main/ui/public/assets/images/codefair_logo.png" alt="Codefair Logo" width="200" />
  <br /><br />
  <strong>Your coding assistant to make research software reusable without breaking a sweat!</strong>
  <br /><br />
  <a href="https://github.com/marketplace/codefair-app"><strong>Get the app »</strong></a>
  &nbsp;|&nbsp;
  <a href="https://codefair.io/"><strong>Learn more »</strong></a>
  <br /><br />
  <a href="https://github.com/fairdataihub/codefair-app/graphs/contributors"><img src="https://img.shields.io/github/contributors/fairdataihub/codefair-app.svg?style=flat-square" alt="Contributors" /></a>
  <a href="https://github.com/fairdataihub/codefair-app/stargazers"><img src="https://img.shields.io/github/stars/fairdataihub/codefair-app.svg?style=flat-square" alt="Stars" /></a>
  <a href="https://github.com/fairdataihub/codefair-app/issues/"><img src="https://img.shields.io/github/issues/fairdataihub/codefair-app.svg?style=flat-square" alt="Open Issues" /></a>
  <a href="https://github.com/fairdataihub/codefair-app/blob/main/LICENSE"><img src="https://img.shields.io/github/license/fairdataihub/codefair-app.svg?style=flat-square" alt="License" /></a>
  <a href="https://doi.org/10.5281/zenodo.13376616"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.13376616.svg" alt="Zenodo DOI" /></a>
  <a href="https://archive.softwareheritage.org/browse/origin/https://github.com/fairdataihub/codefair-app/"><img src="https://archive.softwareheritage.org/badge/origin/https://github.com/fairdataihub/codefair-app/" alt="Software Heritage archive" /></a>
</div>

---

## Overview

**Codefair** is a GitHub app that helps make your research software reusable and ensures compliance with the [FAIR Principles for Research Software](https://doi.org/10.1038/s41597-022-01710-x). Whether you’re developing AI/ML models in Python, data visualization tools in Jupyter, or data analysis code in R, Codefair guides you to best practices, metadata standards, proper licensing, archiving, and more—all through GitHub issues and pull requests.

> By using Codefair, you’re not just developing software; you’re advocating for better, more reusable research software.

![Screenshot of a License issue being resolved with a PR](https://imgur.com/fcOuzTC.png)

---

## Live Status

Monitor Codefair’s uptime and service health at [status.codefair.io](https://status.codefair.io/). This page provides real-time updates on app availability, incidents, and outages.

---

## Table of Contents

- [Overview](#overview)
- [Live Status](#live-status)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Development](#development)
- [Contributing](#contributing)
- [Issues and Feedback](#issues-and-feedback)
- [License](#license)
- [Citation](#citation)

---

## Features

- Assists with making research software [FAIR](https://doi.org/10.1038/s41597-022-01710-x)
- Communicates via GitHub issues and pull requests
- Supports multiple programming languages and research workflows
- Automates metadata, licensing, and archiving tasks
- Integrates seamlessly with GitHub

---

## Installation

1. **Install Codefair** from the [GitHub Marketplace](https://github.com/marketplace/codefair-app) on your desired GitHub organizations or repositories.
2. **Alternatively**, install directly from the [app page](https://github.com/apps/codefair-io) to avoid Marketplace credit card requirements.
3. **Start coding** as usual—Codefair will monitor and assist via GitHub issues.

> **Note**: While Codefair is free, the GitHub Marketplace may require a credit card for installation on some accounts.

---

## Usage

- Track FAIR compliance issues in your repository’s issue dashboard.
- Address suggestions and improvements through Codefair’s issue comments and automated pull requests.
- Use the [Codefair website](https://codefair.io/) for further management and to view your compliance dashboard.

---

## Documentation

- Full documentation, including permissions, features, and setup instructions, is available at [docs.codefair.io](https://docs.codefair.io/docs/installation.html).
- For details on running the app locally, see [Running Locally](https://docs.codefair.io/dev/running-locally.html).

---

## Development

- Codefair is built with [Probot](https://probot.github.io/docs/) and deployed as a serverless function.
- It is written in [Node.js](https://nodejs.org/en) and utilizes the [Octokit library](https://github.com/octokit) for GitHub API interactions.
- The app responds to webhooks for pushes, issues, pull requests, and discussion comments.
- Serverless deployment enables Codefair to automatically scale with GitHub workloads.

[Add details here] if you need more information about contributing to development or running advanced setups.

---

## Contributing

[![Contributors](https://contrib.rocks/image?repo=fairdataihub/codefair-app)](https://github.com/fairdataihub/codefair-app/graphs/contributors)

We welcome contributions of all kinds! Please read [CONTRIBUTING.md](CONTRIBUTING.md) to get started, including details on reporting bugs, submitting pull requests, and our code of conduct.

---

## Issues and Feedback

- Report bugs, request features, or suggest improvements by [opening an issue](https://github.com/fairdataihub/codefair-app/issues).
- You can also reach us via our [contact form](https://tally.so/r/3E0dao).
- Please provide relevant details (operating system, steps to reproduce, etc.) to help us assist you effectively.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/mit). See the [LICENSE](https://github.com/fairdataihub/codefair-app/blob/main/LICENSE) file for details.

---

## Citation

If you use Codefair or its source code, please cite the corresponding Zenodo record:

- [Zenodo DOI](https://doi.org/10.5281/zenodo.13376616)

Citation instructions are also available in the GitHub Citation panel, the `CITATION.cff` file, and on the Zenodo page (including for prior versions).

---

<div align="center">
  <a href="https://codefair.io">
    <img src="https://raw.githubusercontent.com/fairdataihub/codefair-app/main/ui/public/assets/images/codefair_logo_name.png" alt="Codefair Logo" width="200" />
  </a>
</div>

---

### Summary of Changes

- **Added/clarified section headings** for logical flow: Features, Installation, Usage, Documentation, Development, Contributing, Issues and Feedback, License, Citation.
- **Moved project description and badges to the top** for immediate visibility.
- **Expanded Installation and Usage sections** with stepwise clarity.
- **Added Table of Contents** for better navigation.
- **Ensured all links point to correct, existing resources.**
- **Standardized language and formatting** for clarity and consistency.
- **Moved screenshots and badges under appropriate headings.**
- **Included a Features section** for quick scanning of app capabilities.
- **Resolved minor factual discrepancies (e.g., correct LICENSE link).**
- **Used [Add details here]** where information was referenced but not provided in the original README.
- **Provided a summary of changes** as required.