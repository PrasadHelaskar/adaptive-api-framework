# Adaptive API Automation Framework

### Python • Pytest • Scalable API Test Architecture

The **Adaptive API Automation Framework** is a **modular, extensible API test automation framework** built using **Python and Pytest**, designed to evolve incrementally into a **production-grade automation solution**.

Rather than focusing on quick test scripts, this framework emphasizes **long-term maintainability, clean architecture, and real-world API testing practices**.

> This repository is developed in **private mode** and follows a **phased roadmap**, with documentation intentionally kept stable to reflect professional framework evolution.

---

## 🧠 Design Philosophy

This framework is built around the following principles:

* **Architecture first, scripts later**
* Clear **separation of concerns**
* Predictable and debuggable execution
* Framework failures should never mask API failures
* Scalability without compromising readability

---

## 🏷️ Tech Stack & Status

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-green.svg)
![API Automation](https://img.shields.io/badge/API-Automation-orange.svg)
![Phase](https://img.shields.io/badge/Phase-P1--S1%20Completed-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-blue.svg)

---

## 🎯 Core Objectives

* Provide a **reusable and extensible API automation foundation**
* Abstract HTTP communication and authentication logic
* Support **multi-environment execution**
* Enable reliable, readable, and scalable test suites
* Prepare the framework for **CI/CD and parallel execution**

---

## 🧱 Architecture Principles

* Tests **never call HTTP libraries directly**
* API communication flows through a **single client abstraction**
* Authentication is **isolated from test logic**
* Environment configuration is **externalized**
* Fixtures manage lifecycle and dependencies
* Failures represent **actual API behavior**, not framework issues

---

## 🏗️ Project Structure

```
adaptive-api-framework/
│
├── core/
│   ├── api_client.py        # Centralized HTTP client
│   ├── auth_handler.py      # Authentication & headers handling
│   ├── config.py            # Application configuration
│   └── path_resolver.py     # Reliable path resolution
│
├── tests/
│   ├── conftest.py          # Pytest fixtures & setup
│   └── test_*.py            # API test cases
│
├── utils/
│   └── logger.py            # Logging utility
│
├── .config/
│   └── .env                 # Environment variables (not committed)
│
├── requirements.txt
└── README.md
```

---

## 🔌 API Client Layer

The framework uses a **single API client abstraction** responsible for:

* Executing HTTP requests
* Managing base URLs
* Injecting headers and authentication
* Handling timeouts and request configuration

**Benefits:**

* No duplicated request logic
* Easier debugging
* Clean extension points for retries, hooks, and tracing

---

## 🔐 Authentication Strategy

* Token-based authentication (e.g., GitHub Personal Access Token)
* Credentials sourced strictly from **environment variables**
* Authentication logic fully decoupled from tests

Designed for future support of:

* OAuth-based authentication
* Multiple authentication strategies per environment

---

## ⚙️ Configuration Management

* Environment variables loaded using `python-dotenv`
* Centralized configuration access via `AppConfig`
* Supports multiple environments (test, staging, production)

### Example `.env`

```bash
BASE_URL=https://api.github.com
TIMEOUT=10
PAT_KEY=your_github_token_here
```

---

## 🧪 Test Execution (Pytest)

* Pytest is used as the test runner
* Fixtures manage shared dependencies (API client, auth context)
* Tests focus on:

  * Status code validation
  * Response structure checks
  * Core content verification

### Run tests

```bash
pytest -v
```

---

## 🧠 Validation Strategy

Planned validation layers include:

* Status code assertions
* Response schema validation
* Business rule validations
* Negative and edge-case testing
* Rate-limit and error handling scenarios

---

## 🧩 Logging & Observability

The framework is structured to support:

* Structured request/response logging
* Debug-level tracing
* Failure diagnostics
* Optional integration with reporting tools

> Logging is currently minimal by design and will evolve in later phases.

---

## 🚀 Execution & Scalability Roadmap

Planned enhancements include:

* Parallel test execution
* Environment-based test selection
* Retry mechanisms
* Tag-based execution
* CI/CD pipeline integration
* Test reporting and metrics

---

## 🛣️ Development Roadmap (High Level)

* **Phase 1:** Core foundation & API client abstraction ✅
* **Phase 2:** Validation layers & test organization ✅
* **Phase 3:** Reliability (logging, reporting) ✅
* **Phase 4:** CI/CD & scalability
* **Phase 5:** Advanced features (contract testing, observability)

---

## 🚧 Project Status

* **Development:** Active
* **Documentation:** Stable (long-term)

---

## 📄 Disclaimer

This project is built for **architectural learning and professional growth**.
It evolves incrementally to mirror **real-world automation framework development**, rather than presenting a prematurely “complete” solution.

---

## 🙌 Author

**Prasad Helaskar** </br>
Automation Tester | Python | API & UI Automation
