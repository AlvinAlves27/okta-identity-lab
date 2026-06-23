# Okta Identity Lab

**Cloud-Native IAM Implementation with Okta Workforce Identity**

A comprehensive hands-on lab demonstrating enterprise-grade identity management using Okta — covering Universal Directory, SAML and OIDC federation, phishing-resistant MFA, SCIM-based lifecycle automation, no-code workflow orchestration, and programmatic API operations.

---

## Project Overview

This lab walks through the full Okta operational stack as it would be deployed in a modern enterprise. Starting with directory services and custom profile attributes, the lab progresses through application federation, adaptive authentication policies, automated provisioning, and Python-based API automation — demonstrating both the click-ops admin workflow and the programmatic side of identity engineering.

| Component | Description |
|-----------|-------------|
| **Platform** | Okta Workforce Identity Cloud (Developer Edition) |
| **Directory** | Okta Universal Directory with custom profile schema |
| **Federation** | SAML 2.0 · OpenID Connect · OAuth 2.0 |
| **Authentication** | Phishing-resistant MFA · FIDO2 · Okta Verify FastPass |
| **Provisioning** | SCIM 2.0 · Group-based access control |
| **Automation** | Okta Workflows · Python SDK · REST API |

---

## Lab Series

| Part | Topic | Focus Area |
|------|-------|------------|
| [**Part 1**](docs/part-1-universal-directory.md) | Universal Directory | Custom attributes, users, groups, and automated membership rules |
| [**Part 2**](docs/part-2-application-integration-sso.md) | Application Integration & SSO | SAML federation with Salesforce, OIDC for custom apps |
| [**Part 3**](docs/part-3-multi-factor-authentication.md) | Multi-Factor Authentication | Phishing-resistant MFA, adaptive policies for privileged access |
| [**Part 4**](docs/part-4-lifecycle-management.md) | Lifecycle Management | SCIM provisioning, joiner-mover-leaver automation |
| [**Part 5**](docs/part-5-okta-workflows.md) | Okta Workflows | No-code automation with 70+ connectors |
| [**Part 6**](docs/part-6-api-automation.md) | API & Code Automation | Python scripts for programmatic identity operations |

Full step-by-step documentation lives in [`docs/`](docs/). Automation scripts are in [`scripts/`](scripts/).

---

## Technologies

![Okta](https://img.shields.io/badge/Okta-007DC1?style=flat-square&logo=okta&logoColor=white)
![SAML 2.0](https://img.shields.io/badge/SAML_2.0-FF6C37?style=flat-square)
![OIDC](https://img.shields.io/badge/OpenID_Connect-F78C40?style=flat-square)
![OAuth 2.0](https://img.shields.io/badge/OAuth_2.0-EB5424?style=flat-square&logo=oauth&logoColor=white)
![SCIM](https://img.shields.io/badge/SCIM_2.0-4A154B?style=flat-square)
![Salesforce](https://img.shields.io/badge/Salesforce-00A1E0?style=flat-square&logo=salesforce&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![REST API](https://img.shields.io/badge/REST_API-009688?style=flat-square)

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    OKTA WORKFORCE IDENTITY                       │
│  ─────────────────────────────────────────────────────────       │
│                                                                  │
│   ┌─────────────────────┐         ┌──────────────────────┐       │
│   │ Universal Directory │────────▶│  Authentication      │       │
│   │ ├─ Custom Attrs     │         │  ├─ MFA Policies     │       │
│   │ ├─ Group Rules      │         │  ├─ FIDO2 / FastPass │       │
│   │ └─ User Profiles    │         │  └─ Adaptive Access  │       │
│   └──────────┬──────────┘         └──────────┬───────────┘       │
│              │                               │                   │
│              ▼                               ▼                   │
│   ┌─────────────────────┐         ┌──────────────────────┐       │
│   │  Federation (IdP)   │         │  Lifecycle (SCIM)    │       │
│   │  ├─ SAML 2.0        │         │  ├─ Joiner           │       │
│   │  └─ OIDC / OAuth    │         │  ├─ Mover            │       │
│   └──────────┬──────────┘         │  └─ Leaver           │       │
│              │                    └──────────┬───────────┘       │
│              │                               │                   │
└──────────────┼───────────────────────────────┼───────────────────┘
               │                               │
               ▼                               ▼
       ┌───────────────┐               ┌───────────────┐
       │  Salesforce   │               │  Provisioned  │
       │  (SP)         │               │  Apps         │
       └───────────────┘               └───────────────┘

       ┌──────────────────────────────────────────────┐
       │  AUTOMATION LAYER                            │
       │  ├─ Okta Workflows (no-code)                 │
       │  └─ Python + REST API (programmatic)         │
       └──────────────────────────────────────────────┘
```

---

## Skills Demonstrated

- **Directory Services** — Universal Directory configuration, custom profile schemas, group rules engine
- **Federation** — SAML 2.0 and OIDC integration, metadata exchange, protocol selection
- **Authentication** — MFA policy design, phishing-resistant factors (FIDO2, FastPass), adaptive access
- **Provisioning** — SCIM-based lifecycle automation, attribute mapping, joiner-mover-leaver workflows
- **Automation** — No-code workflows with Okta Workflows, Python SDK for API operations
- **Security** — Zero Trust principles, privileged access controls, conditional authentication

---

## Repository Structure

```
okta-identity-lab/
├── README.md
├── docs/                                       # Step-by-step documentation
│   ├── part-1-universal-directory.md
│   ├── part-2-application-integration-sso.md
│   ├── part-3-multi-factor-authentication.md
│   ├── part-4-lifecycle-management.md
│   ├── part-5-okta-workflows.md
│   └── part-6-api-automation.md
├── scripts/                                    # Python automation
│   ├── list_users.py
│   └── list_groups.py
└── images/                                     # Screenshots organized by part
    ├── part-1/   (18 images)
    ├── part-2/   (7 images)
    ├── part-3/   (5 images)
    ├── part-4/   (1 image)
    ├── part-5/   (5 images)
    └── part-6/   (10 images)
```

---

## Key Takeaways

**Enterprise Relevance:**
- Mirrors the workforce identity model used by enterprises standardizing on Okta as their IdP
- Demonstrates secure federation patterns across both SaaS and custom applications
- Establishes the automated lifecycle workflows required to manage identity at scale
- Lays the foundation for Zero Trust architecture through phishing-resistant authentication

**What This Lab Proves:**
- Ability to design and operate the Okta Universal Directory at the schema level
- Hands-on experience with SAML and OIDC federation as an identity provider
- Practical implementation of adaptive, risk-based MFA for privileged users
- Programmatic identity operations through the Okta Management API

---

## Related Labs

- [**Enterprise Identity Lab**](https://github.com/AlvinAlves27/enterprise-identity-lab) — Hybrid identity with Active Directory, Entra Connect, SAML SSO, and Conditional Access

---

## Author

**Alvin Alves** — Identity & Access Management Engineer

[![Portfolio](https://img.shields.io/badge/Portfolio-alvinalves.com-1a1a2e?style=flat-square)](https://alvinalves.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alvin-alves/)

---

📍 United States · 🌐 [alvinalves.com](https://alvinalves.com) · 💼 [LinkedIn](https://www.linkedin.com/in/alvin-alves/)
