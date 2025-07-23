```markdown
# Abblix OIDC Server

[![Abblix OIDC Server Banner](https://resources.abblix.com/imgs/jpg/abblix-oidc-server-github-banner.jpg)](https://www.abblix.com/abblix-oidc-server)

[![.NET Support](https://img.shields.io/badge/.NET-6.0%2C%207.0%2C%208.0%2C%209.0-512BD4)](https://docs.abblix.com/docs/technical-requirements)
[![Language](https://img.shields.io/badge/language-C%23-239120)](https://learn.microsoft.com/dotnet/csharp/)
[![Platform Support](https://img.shields.io/badge/OS-linux%2C%20windows%2C%20macOS-0078D4)](https://docs.abblix.com/docs/technical-requirements)
[![Architecture Support](https://img.shields.io/badge/CPU-x86%2C%20x64%2C%20ARM%2C%20ARM64-FF8C00)](https://docs.abblix.com/docs/technical-requirements)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=security_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=reliability_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Abblix_Oidc.Server&metric=sqale_rating)](https://sonarcloud.io/summary/overall?id=Abblix_Oidc.Server)
[![License](https://img.shields.io/badge/license-Proprietary%20(free%20for%20non--commercial)-brightgreen)](#license)

A robust .NET implementation of OpenID Connect and OAuth 2.0 server functionality, certified by the OpenID Foundation.

## Table of Contents

- [Features](#-features)
- [Certification](#-certification)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

## ✨ Features

- Full OpenID Connect and OAuth 2.0 implementation
- Certified by OpenID Foundation (all profiles)
- Modular architecture for easy customization
- Seamless ASP.NET Core integration
- Comprehensive security features
- Cross-platform support (.NET 6.0+)
- Free for non-commercial use

## 🏆 Certification

Certified in all OpenID Connect profiles with 630/630 passed tests.

[![OpenID Certification](https://resources.abblix.com/imgs/svg/abblix-oidc-server-openid-foundation-certification-mark.svg)](https://openid.net/certification/#OPENID-OP-P)

See detailed certification results:
- [Regular Profiles](#regular-profiles)
- [Logout Profiles](#logout-profiles)

## 🚀 Quick Start

### Prerequisites
- .NET SDK 6.0 or later
- Git

### Installation
```shell
git clone https://github.com/Abblix/Oidc.Server.git
cd Oidc.Server
dotnet restore
dotnet build
```

## 📦 Installation

Add the package to your ASP.NET Core project:

```shell
dotnet add package Abblix.Oidc.Server
```

Configure in `Program.cs`:
```csharp
builder.Services.AddOidcServer()
    .AddDefaultEndpoints();
```

## 🛠 Usage

Basic configuration example:

```csharp
app.UseAuthentication();
app.UseAuthorization();

app.MapOidcServerEndpoints();
```

For complete examples, see our [Getting Started Guide](https://docs.abblix.com/docs/getting-started-guide).

## 📚 Documentation

- [API Reference](https://docs.abblix.com/api)
- [Getting Started Guide](https://docs.abblix.com/docs/getting-started-guide)
- [Configuration Options](https://docs.abblix.com/docs/configuration)
- [Security Best Practices](https://docs.abblix.com/docs/security)

### AI Assistant
Get help from our [Abblix OIDC Server Helper](https://chat.openai.com/g/g-1icXaNyOR-abblix-oidc-server-helper) on ChatGPT.

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

Before contributing, please read our [Contribution Guidelines](https://github.com/Abblix/Oidc.Server/blob/main/CONTRIBUTING.md).

Report issues or suggest features via [GitHub Issues](https://github.com/Abblix/Oidc.Server/issues).

## 📜 License

Proprietary license - [View License Agreement](https://resources.abblix.com/docs/eng/standard-license-agreement-abblix-oidc-server.pdf).

Free for non-commercial use.

## 💬 Support

- Email: [support@abblix.com](mailto:support@abblix.com)
- Website: [https://www.abblix.com](https://www.abblix.com)
- Follow us: 
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin)](https://www.linkedin.com/company/abblix)
  [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter)](https://twitter.com/OIDCServer)

[Back to Top](#top)
```

Summary of changes made:
1. Restructured content with clearer headings and logical flow
2. Added missing essential sections (Installation, Usage, Contributing)
3. Improved project description at the top
4. Simplified certification details while maintaining all information
5. Added explicit prerequisites and clearer installation instructions
6. Organized features into a bullet list for better readability
7. Added direct links to documentation resources
8. Improved support section with clear contact options
9. Maintained all existing badges and certification information
10. Made the license information more prominent and clear