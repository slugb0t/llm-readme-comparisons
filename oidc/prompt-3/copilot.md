# Abblix OIDC Server

[![Abblix OIDC Server](https://resources.abblix.com/imgs/jpg/abblix-oidc-server-github-banner.jpg)](https://www.abblix.com/abblix-oidc-server)

[![.NET](https://img.shields.io/badge/.NET-6.0%2C%207.0%2C%208.0%2C%209.0-512BD4)](https://docs.abblix.com/docs/technical-requirements)
[![language](https://img.shields.io/badge/language-C%23-239120)](https://learn.microsoft.com/ru-ru/dotnet/csharp/tour-of-csharp/overview)
[![OS](https://img.shields.io/badge/OS-linux%2C%20windows%2C%20macOS-0078D4)](https://docs.abblix.com/docs/technical-requirements)
[![CPU](https://img.shields.io/badge/CPU-x86%2C%20x64%2C%20ARM%2C%20ARM64-FF8C00)](https://docs.abblix.com/docs/technical-requirements)
[![security rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=security_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![reliability rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=reliability_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![maintainability rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=sqale_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![CodeQL analysis](https://github.com/Abblix/Oidc.Server/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Abblix/Oidc.Server/security/code-scanning?query=is%3Aopen)
[![GitHub release](https://img.shields.io/github/v/release/Abblix/Oidc.Server)](https://github.com/Abblix/Oidc.Server/releases)
[![GitHub release date](https://img.shields.io/github/release-date/Abblix/Oidc.Server)](https://github.com/Abblix/Oidc.Server/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/Abblix/Oidc.Server)](https://github.com/Abblix/Oidc.Server/commits)
[![ChatGPT Helper](https://img.shields.io/badge/ChatGPT-available-brightgreen.svg)](https://chatgpt.com/g/g-1icXaNyOR-abblix-oidc-server-helper)
[![Getting Started](https://img.shields.io/badge/getting_started-guide-1D76DB)](https://docs.abblix.com/docs/getting-started-guide)
[![Free](https://img.shields.io/badge/free_for_non_commercial_use-brightgreen)](#license)

> **Abblix OIDC Server** is a robust .NET library for implementing OAuth2 and OpenID Connect protocols on the server side. Built with modular and hexagonal architectures, it enables secure, flexible, and maintainable authentication solutions for modern applications.

⭐ Star us on GitHub — let's reach 100 stars together! 😊

[![Share on X](https://img.shields.io/badge/share-000000?logo=x&logoColor=white)](https://x.com/intent/tweet?text=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Abblix/Oidc.Server%20%23OpenIDConnect%20%23Security%20%23Authentication)
[![Share on Facebook](https://img.shields.io/badge/share-1877F2?logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/Abblix/Oidc.Server)
[![Share on LinkedIn](https://img.shields.io/badge/share-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/Abblix/Oidc.Server)
[![Share on Reddit](https://img.shields.io/badge/share-FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/submit?title=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Abblix/Oidc.Server)
[![Share on Telegram](https://img.shields.io/badge/share-0088CC?logo=telegram&logoColor=white)](https://t.me/share/url?url=https://github.com/Abblix/Oidc.Server&text=Check%20out%20this%20project%20on%20GitHub)

🔥 **Why choose OIDC Server?** — Discover the benefits in our [presentation](https://resources.abblix.com/pdf/abblix-oidc-server-presentation-eng.pdf).

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Certification](#certification)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Helper Tool](#helper-tool)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Community & Social](#community--social)

---

## Overview

**Abblix OIDC Server** provides a complete server-side solution for OAuth2 and OpenID Connect, built on .NET. It is designed for seamless integration with ASP.NET WebApi, supporting standard controller classes, binding, and routing. Key advantages include:

- **Modularity:** Each component operates independently for easier maintenance.
- **Testability:** Clear separation of concerns for robust testing.
- **Maintainability:** Well-organized codebase for scalable projects.
- **Dependency Injection:** Full support via the .NET DI container.

---

## Features

- Certified for all standard OpenID Connect and OAuth2 profiles
- Works with .NET 6.0, 7.0, 8.0, and 9.0
- Cross-platform: Linux, Windows, macOS
- Supports x86, x64, ARM, ARM64 architectures
- Designed for integration with ASP.NET WebApi
- Modular, maintainable, and extensible architecture
- [Add details here if more features are available]

---

## Certification

[![OpenID Certification](https://resources.abblix.com/imgs/svg/abblix-oidc-server-openid-foundation-certification-mark.svg)](https://openid.net/certification/#OPENID-OP-P)

Abblix OIDC Server is certified for all OpenID profiles. **630 tests passed** with zero skipped tests and no warnings.

- [Certified OpenID Providers & Profiles](https://openid.net/certification/#OPENID-OP-P)
- [Certified OpenID Providers for Logout Profiles](https://openid.net/certification/#OPENID-OP-LP)

### Regular Profiles

| OIDC Profile     | Response Types                                             | Tests |
| :--------------- | :-------------------------------------------------------- | :---- |
| Basic OP         | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=FQHG2VEct7wwy) | 37    |
| Implicit OP      | [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=cQxDzZ2AF6kCd) | 58    |
| Hybrid OP        | [code id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=3axSifHKQAsx7) | 102   |
| Config OP        | [config](https://www.certification.openid.net/plan-detail.html?public=true&plan=MJLv3jEc7mjPa) | 1     |
| Dynamic OP       | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=spiRykedA0Mwt) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=MYpjkY7SCvGGm) ... | 121   |
| Form Post OP     | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=mmLewPQ5CRI5Y) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=m201EDuUSSGC4) ... | 197   |
| 3rd Party-Init OP| [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=AZDaS1Bgcz05b) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=Ra3nyzTuFrk3x) ... | 12    |
| **Total**        |                                                           | **528** |

### Logout Profiles

| OIDC Profile        | Response Types                                             | Tests |
| :------------------ | :-------------------------------------------------------- | :---- |
| RP-Initiated OP     | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=t3gEmJDtpGeBv) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=Oe06IYAYLq0Sg) ... | 66    |
| Session OP          | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=14cK3zXIwOHZ1) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=MP0JEAuuLFWAr) ... | 12    |
| Front-Channel OP    | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=3D5QcW9lq6H0Z) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=OYv7ccnbWElth) ... | 12    |
| Back-Channel OP     | [code](https://www.certification.openid.net/plan-detail.html?public=true&plan=muYvBNgY6O90P) &#124; [id_token](https://www.certification.openid.net/plan-detail.html?public=true&plan=W7SL9FbkaqM5w) ... | 12    |
| **Total**           |                                                           | **102** |

---

## Installation

To install and build Abblix OIDC Server:

```shell
# Clone the repository
git clone https://github.com/Abblix/Oidc.Server.git

# Go to the project directory
cd Oidc.Server

# Verify .NET SDK is installed
dotnet --version

# Restore dependencies
dotnet restore

# Build the project
dotnet build
```

For supported .NET versions and system requirements, see the [Technical Requirements](https://docs.abblix.com/docs/technical-requirements).

---

## Usage

See the [Getting Started Guide](https://docs.abblix.com/docs/getting-started-guide) for a step-by-step tutorial on building an OpenID Connect Provider using ASP.NET MVC and Abblix OIDC Server.

For advanced configuration and integration details, refer to the [full documentation](https://docs.abblix.com/docs).

[Add details here if there are usage examples, code snippets, or additional instructions.]

---

## Documentation

- [Product Documentation](https://docs.abblix.com/docs)
- [Getting Started Guide](https://docs.abblix.com/docs/getting-started-guide)
- [Presentation (PDF)](https://resources.abblix.com/pdf/abblix-oidc-server-presentation-eng.pdf)
- [Technical Requirements](https://docs.abblix.com/docs/technical-requirements)
- [Add details here for API or developer documentation if available]

---

## Helper Tool

The [**Abblix OIDC Server Helper**](https://chat.openai.com/g/g-1icXaNyOR-abblix-oidc-server-helper) is a ChatGPT-based assistant equipped with extensive documentation and support for:

- Integration guidance for .NET projects
- Configuration best practices
- Troubleshooting and technical support
- Licensing and pricing information
- Feature overviews
- Security and compliance advice
- Extending and customizing the server

Ideal for both beginners and experienced developers.

---

## Contributing

We welcome feedback, feature requests, and contributions!

- [Submit an Issue](https://github.com/Abblix/Oidc.Server/issues)
- [Join Discussions](https://github.com/orgs/Abblix/discussions)
- [Add details here for contribution guidelines if available]

Your input helps us make Abblix OIDC Server more robust and user-friendly.

---

## License

This product is distributed under a proprietary license. Please review the full agreement here: [Standard License Agreement for Abblix OIDC Server (PDF)](https://resources.abblix.com/docs/eng/standard-license-agreement-abblix-oidc-server.pdf).

- **Free for non-commercial use.**
- [Add details here for commercial licensing if needed.]

---

## Contact

For support or more information:

- **Email:** [support@abblix.com](mailto:support@abblix.com)
- **Website:** [Abblix OIDC Server](https://www.abblix.com/abblix-oidc-server)

---

## Community & Social

Connect with us:

[![LinkedIn](https://img.shields.io/badge/subscribe-white.svg?logo=linkedin)](https://www.linkedin.com/company/103540510/)
[![X](https://img.shields.io/badge/subscribe-white.svg?logo=x)](https://twitter.com/OIDCServer)

---

[Back to top](#top)

---

**Summary of Changes:**

- Added a concise project description at the top.
- Organized content under clear, logical headings (Overview, Features, Certification, Installation, Usage, etc.).
- Added a Features section for clarity.
- Standardized Installation and Usage instructions under their own headings.
- Consolidated documentation links, added prompts for missing documentation details.
- Clearly linked to the ChatGPT Helper tool and described its use.
- Moved feedback, issues, and discussions under a unified "Contributing" section.
- Improved badge linking (release, last commit) and made badge order logical.
- Ensured clear links to license and contact information.
- Added a Community & Social section for easy access to social channels.
- Used [Add details here] placeholders where information could not be verified.
- Cleaned up formatting, collapsed duplicate/overlapping sections, and ensured compliance with best practices for README files.