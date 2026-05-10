# Automation Infrastructure Showcase

Welcome to the **Automation Infrastructure Showcase** repository! 🚀

This repository contains a robust, scalable, and fully functional Test Automation Framework designed to test WEB and API applications (with structure ready for Mobile). It demonstrates advanced industry practices including **Page Object Model (POM)**, **Data-Driven Testing (DDT)**, **Action-driven Workflows**, and **Database Validation**, built using modern Python automation tools.

## 🛠️ Technology Stack
- **Language**: Core logic written in **Python 3**.
- **Test Runner**: **Pytest** (with `pytest-playwright` plugin).
- **Web Automation Engine**: **Playwright** 🎭 for fast, reliable, and headless browser automation.
- **API Testing**: **Playwright APIRequestContext** and **Requests** library mapping.
- **Reporting**: **Allure Reports** 📊 for interactive and comprehensive test execution history.
- **Database**: **SQLite3** for direct database state validation and mapping.
- **Other Utilities**: Contains implementations for smart assertions, AI visual testing capabilities, and JSON-driven dynamic configurations.

## 📂 Project Structure
```text
Automation/final_project
├── .env                  # Environment Variables (Secrets mapping)
├── .github/              # CI/CD Workflows (e.g., GitHub Actions)
├── config/               # Generic framework configuration files (JSON format)
├── conftest.py           # Pytest fixtures, browser setup/teardown, and global hooks
├── data/                 # Hardcoded test data, database files (.db), and DDT (Data-Driven Testing) payloads
├── extensions/           # Custom extensions like Database actions (`db_actions.py`) or UI helpers 
├── page_objects/         # Core UI locators and basic page level interactions (Web, API, Mobile)
├── tests/                # Test suites grouped by domain:
│   ├── api/              # Complete API test scenarios
│   ├── mobile/           # Mobile App testing scenarios directory
│   └── web/              # E2E Web UI test scenarios
├── utils/                # Common utility scripts (Browser initialization, config loaders, helper ops)
├── workflows/            # High-level business logic chaining multiple Page Object interactions
└── requirements.txt      # Python Dependencies list
```

## 🏗️ Architecture Design Principles
The framework was built with scalability, readability, and maintenance in mind:
1. **Separation of Concerns**: Test logic (`tests/`) is strictly separated from business operations (`workflows/`) and element locators (`page_objects/`).
2. **Page Object Model (POM)**: Core mapping ensures UI element reusability and drastically reduces code duplication when application states change.
3. **Workflow Logic Layer**: Groups several singular page operations into a logical application workflow block (e.g., `brains_flows.sign_in()`, `brains_flows.add_all_products_to_cart()`). This keeps test files clean and action-oriented.
4. **Data-Driven Testing (DDT)**: Driving complex UI/API test validations using parametrization rather than duplicating test functions.
5. **Fixture-based Execution**: Leverages `@pytest.fixture` scoping (session, class, function) and yield patterns in `conftest.py` ensuring reliable state management and dynamic browser setup.

## 💻 Included Testing Coverage
- **Web UI E2E**: End-to-end user journeys including Authentication, Shopping Cart interactions, Checkout processes, and dynamic UI component handling.
- **API Contract & Integration**: REST endpoints validation handling standard HTTP verbs (GET, POST).
- **Database Verification**: Direct SQL query execution mapping backend state variations directly against SQLite.
- **AI Vision Checks**: Next-generation layout validation using AI visual models incorporated into Playwright UI scripts.

## 🚀 Getting Started

### Prerequisites
Make sure you have installed:
- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation Steps
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository_url>
   cd final_project
   ```

2. Create and activate a virtual environment (Recommended):
   ```bash
   # Windows
   python -m venv .venv
   source .venv/Scripts/activate 

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install requirements using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright core browser binaries:
   ```bash
   playwright install
   ```

## 🏃 Running the Tests

To run the complete framework test suite:
```bash
pytest tests/
```

To run only the Web UI suite:
```bash
pytest tests/web/
```

To run only the API suite:
```bash
pytest tests/api/
```

### 📊 Generating Allure Reports
The framework uses Allure for detailed HTML reporting natively bound to pytest fixtures.

1. Execute tests while specifying the generated output directory:
   ```bash
   pytest --alluredir=allure-results
   ```
2. Serve the generated Allure report locally:
   ```bash
   allure serve allure-results
   ```

## ⚙️ Configuration
The core runtime configurations sit inside `config/config.json`. These handle overarching settings such as target browser types (`BROWSER_TYPE` to map Chrome, Firefox, or WebKit).

---
*Developed with modern Continuous Testing practices in mind.* 🥂
