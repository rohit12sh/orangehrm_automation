# OrangeHRM Automation Framework

A professional test automation framework for OrangeHRM using Playwright and Python.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install
```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_login.py
```

Run smoke tests:
```bash
pytest -m smoke
```

Generate Allure report:
```bash
allure serve reports/allure-results
```

## Project Structure

- `tests/`: Test cases organized by feature
- `pages/`: Page Object Models
- `components/`: Reusable UI components
- `utils/`: Helper functions and configurations
- `reports/`: Test execution reports and screenshots
