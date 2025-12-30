# Adaptive API Automation Framework (Python + Pytest)

The **Adaptive API Automation Framework** is a modular, extensible API test automation framework built using **Python and Pytest**, designed to evolve incrementally into a production-grade solution.

The framework emphasizes:
- Clean architecture
- Separation of concerns
- Maintainability over shortcuts
- Real-world API testing patterns

This repository is developed in **private mode** and follows a **phased roadmap**.  
All phases are planned upfront to avoid repeated documentation changes during development.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-green.svg)
![API Automation](https://img.shields.io/badge/API-Automation-orange.svg)
![Phase](https://img.shields.io/badge/Phase-P1--S1%20Completed-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-blue.svg)

---
## 🎯 Core Objectives

- Provide a **reusable API automation foundation**
- Abstract HTTP communication and authentication
- Support multiple environments
- Enable reliable, readable, and scalable test suites
- Prepare the framework for CI/CD and large-scale execution

---

## 🧱 Architecture Principles

- Tests never call HTTP libraries directly
- All configuration is environment-driven
- Authentication is isolated from test logic
- Fixtures manage lifecycle and dependencies
- Failures must represent **real API behavior**, not framework issues

---

## 🏗️ Project Structure

adaptive-api-framework/ </br>
│</br>
├── core/ </br>
│ ├── api_client.py # Centralized HTTP client </br>
│ ├── auth_handler.py # Authentication & headers handling </br>
│ ├── config.py # Application configuration </br>
│ └── path_resolver.py # Reliable path resolution </br>
│ </br>
├── tests/ </br>
│ ├── conftest.py # Pytest fixtures & setup </br>
│ └── test_*.py # API test cases </br>
│ </br>
├── utils/ </br>
│ └── logger.py # Logging utility </br>
│ </br>
├── .config/ </br>
│ └── .env # Environment variables (not committed) </br>
│ </br>
├── requirements.txt </br>
└── README.md </br>


---

## 🔌 API Client Layer

The framework uses a **single API client abstraction** responsible for:

- HTTP request execution
- Base URL handling
- Headers and authentication injection
- Timeout configuration

This ensures:
- No duplicated request logic
- Easy future extension (retries, hooks, tracing)

---

## 🔐 Authentication Strategy

- Token-based authentication (e.g., GitHub Personal Access Token)
- Credentials sourced only from environment variables
- Authentication logic isolated from tests

The framework is designed to later support:
- OAuth-based flows
- Multiple auth strategies per environment

---

## ⚙️ Configuration Management

- Environment variables loaded via `python-dotenv`
- Central configuration access through `AppConfig`
- Support for multiple environments (test, staging, prod)

Example environment variables:
```bash
BASE_URL= https://api.github.com
TIMEOUT= 10
PAT_KEY= your_github_token_here
```
---

## 🧪 Test Execution (Pytest)

- Pytest is used as the test runner
- Fixtures manage shared dependencies like the API client
- Tests focus on:
  - Status code validation
  - Response structure verification
  - Basic content checks

### Run tests
```bash
  pytest -v
```
---

## 🧠 Validation Strategy

Planned validation layers include:
- Status code checks
- Response schema validation
- Business rule assertions
- Negative and edge-case scenarios
- Rate-limit and error handling tests
---

## 🧩 Logging & Observability

The framework is designed to support:
- Structured request/response logging
- Debug-level tracing
- Failure diagnostics
- Optional integration with reporting tools
(Current logging is intentionally minimal and will evolve.)
---

## 🚀 Execution & Scalability Roadmap

The framework roadmap includes:
- Parallel test execution
- Environment-based test selection
- Retry mechanisms
- Tag-based execution
- CI/CD integration
- Report generation
---

## 🛣️ Development Roadmap (High Level)

- Phase 1 – Core foundation & API client abstraction
- Phase 2 – Validation layers & test organization
- Phase 3 – Reliability (retries, logging, reporting)
- Phase 4 – CI/CD & scalability
- Phase 5 – Advanced features (contract testing, observability)
---

## 🚧 Project Status

- Development: Active
- Documentation: Stable (long-term)
---

## 📄 Disclaimer

- This project is built for architectural learning and professional growth.
It is developed incrementally to reflect how real-world automation frameworks evolve, rather than presenting a prematurely “complete” solution.
---

## 🙌 Author

Prasad Helaskar </br>
Automation Tester | Python | API & UI Automation
