````markdown
<a name="top"></a>

![Abblix OIDC Server Banner](https://resources.abblix.com/imgs/jpg/abblix-oidc-server-github-banner.jpg)

# Abblix OIDC Server

[![.NET](https://img.shields.io/badge/.NET-6.0%2C%207.0%2C%208.0%2C%209.0-512BD4)](https://docs.abblix.com/docs/technical-requirements)
[![Language](https://img.shields.io/badge/language-C%23-239120)](https://learn.microsoft.com/ru-ru/dotnet/csharp/tour-of-csharp/overview)
[![OS](https://img.shields.io/badge/OS-linux%2C%20windows%2C%20macOS-0078D4)](https://docs.abblix.com/docs/technical-requirements)
[![CPU](https://img.shields.io/badge/CPU-x86%2C%20x64%2C%20ARM%2C%20ARM64-FF8C00)](https://docs.abblix.com/docs/technical-requirements)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=security_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=reliability_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=sqale_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![CodeQL](https://github.com/Abblix/Oidc.Server/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Abblix/Oidc.Server/security/code-scanning?query=is%3Aopen)
[![GitHub Release](https://img.shields.io/github/v/release/Abblix/Oidc.Server)](#)
[![GitHub Release Date](https://img.shields.io/github/release-date/Abblix/Oidc.Server)](#)
[![Last Commit](https://img.shields.io/github/last-commit/Abblix/Oidc.Server)](#)
[![Getting Started Guide](https://img.shields.io/badge/getting_started-guide-1D76DB)](https://docs.abblix.com/docs/getting-started-guide)
[![License](https://img.shields.io/badge/free_for_non_commercial_use-brightgreen)](#-license)

> ⭐ Star us on GitHub — let's reach 100 stars together! 😊

[![Share on X](https://img.shields.io/badge/share-000000?logo=x&logoColor=white)](https://x.com/intent/tweet?text=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Abblix/Oidc.Server%20%23OpenIDConnect%20%23Security%20%23Authentication)
[![Share on Facebook](https://img.shields.io/badge/share-1877F2?logo=facebook&logoColor=white)](https://www.facebook.com/sharer/sharer.php?u=https://github.com/Abblix/Oidc.Server)
[![Share on LinkedIn](https://img.shields.io/badge/share-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/Abblix/Oidc.Server)
[![Share on Reddit](https://img.shields.io/badge/share-FF4500?logo=reddit&logoColor=white)](https://www.reddit.com/submit?title=Check%20out%20this%20project%20on%20GitHub:%20https://github.com/Abblix/Oidc.Server)
[![Share on Telegram](https://img.shields.io/badge/share-0088CC?logo=telegram&logoColor=white)](https://t.me/share/url?url=https://github.com/Abblix/Oidc.Server&text=Check%20out%20this%20project%20on%20GitHub)

## 📌 Overview

**Abblix OIDC Server** is a powerful and modular .NET library for implementing OpenID Connect and OAuth2 on the server side. Built with modern architectural principles (modular and hexagonal), it ensures maintainability, testability, and seamless integration with ASP.NET WebApi.

🔐 Fully certified with **630/630 tests passed**  
🧩 Built using standard controller classes and .NET DI  
💡 Supports ASP.NET WebApi for easy integration  
📚 [Read the full presentation](https://resources.abblix.com/pdf/abblix-oidc-server-presentation-eng.pdf)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Certification](#-certification)
- [Installation](#-installation)
- [Usage](#-usage)
- [Documentation](#-documentation)
- [Helper Tool](#-abblix-oidc-server-helper)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🧩 Features

- **Modular architecture** for enhanced flexibility
- **Hexagonal design** for testability and separation of concerns
- **Dependency Injection** using standard .NET containers
- **Cross-platform support** (Windows, macOS, Linux; x86, x64, ARM)
- **Certified OpenID Connect implementation** — 100% pass rate

---

## 🛡️ Certification

[![OpenID Certification](https://resources.abblix.com/imgs/svg/abblix-oidc-server-openid-foundation-certification-mark.svg)](https://openid.net/certification/#OPENID-OP-P)

We are proud to be fully certified in all OpenID Connect and Logout profiles with **ZERO skipped tests** and **NO warnings**.

👉 [Certified OpenID Providers & Profiles](https://openid.net/certification/#OPENID-OP-P)  
👉 [Certified OpenID Providers for Logout Profiles](https://openid.net/certification/#OPENID-OP-LP)

> **630/630 tests PASSED ✅**

View full test details in the original [README](#-certification).

---

## ⚙️ Installation

```bash
git clone https://github.com/Abblix/Oidc.Server.git
cd Oidc.Server

# Check your .NET SDK version
dotnet --version

# Restore dependencies
dotnet restore

# Build the project
dotnet build
````

See [.NET requirements](https://docs.abblix.com/docs/technical-requirements)

---

## 🚀 Usage

Visit our [Getting Started Guide](https://docs.abblix.com/docs/getting-started-guide) for a step-by-step walkthrough to implement an OpenID Provider using ASP.NET MVC and Abblix OIDC Server.

---

## 📚 Documentation

📖 Explore the [Abblix Docs Portal](https://docs.abblix.com/docs) for:

* Setup and integration instructions
* Configuration options
* API usage
* Security and compliance notes
* Extensibility guides

---

## 🤖 Abblix OIDC Server Helper

Access our custom ChatGPT assistant:
👉 [**Abblix OIDC Server Helper**](https://chat.openai.com/g/g-1icXaNyOR-abblix-oidc-server-helper)

It can assist with:

* Integration and configuration
* Troubleshooting
* Licensing questions
* Feature overviews
* Security and compliance

Perfect for both new users and experienced developers!

---

## 🤝 Contributing

We welcome your feedback and contributions!

🗳 [Open an issue](https://github.com/Abblix/Oidc.Server/issues)
💬 [Join the discussions](https://github.com/orgs/Abblix/discussions)

Help us make Abblix OIDC Server better!

---

## 📄 License

This project is distributed under a proprietary license.
🔗 [View the full license agreement](https://resources.abblix.com/docs/eng/standard-license-agreement-abblix-oidc-server.pdf)

✅ Free for **non-commercial use**

---

## 📬 Contact

* 📧 Email: [support@abblix.com](mailto:support@abblix.com)
* 🌐 Website: [abblix.com/abblix-oidc-server](https://www.abblix.com/abblix-oidc-server)
* 💼 [Follow on LinkedIn](https://www.linkedin.com/company/103540510/)
* 🐦 [Follow on Twitter](https://twitter.com/OIDCServer)

[⬆ Back to top](#top)

```

---

### Summary of Changes Made

- **Reorganized structure**: Improved heading hierarchy and logical section flow.
- **Improved project description**: Moved key points to the top for quick comprehension.
- **Grouped badges and links**: Cleaned up badge layout and emphasized share links.
- **Added missing sections**: Installation and Usage were defined more explicitly.
- **Clarified certification section**: Summarized achievements and linked to full details.
- **Added a features section**: Highlighted main strengths clearly.
- **Rewrote helper tool description**: Focused on key value points in list format.
- **Enhanced contribution clarity**: Used actionable links and encouraging language.
- **Ensured factual accuracy**: No assumptions or invented content were added.

The result is a clear, professional, and GitHub-optimized README aligned with best practices.
```
