# AutoSec Monitor: Intelligent CVE and Patch Dashboard

## Overview
**AutoSec Monitor** is a full-stack security observability platform that automates the detection of known vulnerabilities (CVEs) and available patches across the core technologies used in a modern application stack. It provides real-time insights and alerting via a GraphQL-powered backend and a VueJS-based dashboard frontend, with infrastructure deployed to AWS and maintained using GitHub Actions CI/CD pipelines.

> This project simulates a Horizon3.ai-style internal security platform used to proactively identify risk, manage patching, and spin up sandbox environments for testing updates.

---

## 🧠 Key Features
- 🔎 **Live CVE Tracking** for project dependencies (e.g., FastAPI, PostgreSQL, VueJS, etc.) via the [NVD API](https://nvd.nist.gov/developers)
- 🧩 **Patch Intelligence**: checks PyPI, npm, and PostgreSQL for new releases
- ⚠️ **Alert Dashboard**: shows affected packages, versions, and available patches
- 🧪 **Sandbox Triggering**: deploy test environments using Docker for safe update validation
- 🔐 **Security-First**: designed with audit logs, RBAC, CVSS scoring, and best practices

---

## 🧱 Tech Stack
- **Backend**: Python + FastAPI + Strawberry (GraphQL)
- **Database**: PostgreSQL
- **Frontend**: VueJS 3 + Apollo Client
- **Cloud**: AWS (RDS, ECS/Fargate, S3/CloudFront)
- **CI/CD**: GitHub Actions (testing, deployment)

---

## 📦 Modules Breakdown
| Folder         | Description |
|----------------|-------------|
| `/backend`     | GraphQL API, CVE matching, patch checkers, sandbox logic |
| `/frontend`    | VueJS UI for real-time alerting dashboard |
| `/scripts`     | CLI scripts for scanning local package versions and triggering backend refresh |
| `/.github`     | GitHub Actions workflows for CI/CD |

---

## 🚀 Project Roadmap
### ✅ Phase 1: Core MVP
- [x] GraphQL API setup (alerts, mutations)
- [x] PostgreSQL backend and data models
- [x] Basic VueJS dashboard with static data

### 🔄 Phase 2: Intelligence Layer
- [x] CVE API polling + matching to local versions
- [ ] Patch checker (PyPI, npm, PostgreSQL release monitor)
- [ ] Real-time alert logic (CVSS scoring, audit trail)

### 🔬 Phase 3: Automation & Sandbox
- [ ] Sandbox spin-up via Docker Compose
- [ ] Auto-build patched containers for testing
- [ ] Alert + sandbox lifecycle workflows

### 🔒 Phase 4: Security Hardening
- [ ] Add token-based authentication
- [ ] RBAC for dashboard roles
- [ ] Query rate limiting and logging

---

## 📸 Demo Screenshots *(coming soon)*
- Alert dashboard
- CVE match explanation
- Sandbox deployment modal

---

## 💡 Inspiration
This project was inspired by Horizon3.ai’s emphasis on proactive security, autonomous detection, and empowering defenders with actionable intelligence. It’s designed as a career showcase project, portfolio demo, and potential platform prototype.

---

## 👨‍💻 Author
**Daniel Ryan**  
Cybersecurity Leader • Army Veteran • Technical Program Analyst  
🔗 [LinkedIn](https://linkedin.com/in/danielryan)  
📧 daniel.r.ryan6@hotmail.com

---

## 📜 License
MIT License
