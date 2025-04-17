## Playwright Python pytest_bdd example
- Depends on [pytest-playwright](https://github.com/microsoft/playwright-pytest) 

## Commands

To install project packages from [requirements.txt](./requirements.txt)
```
pip install -r requirements.txt
```

From root, to run all the tests
```
pytest
```

From root, to run specific file test
```
pytest tests/test_pytest_bdd.py
```

## Playwright Documentation

* [https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)

## pytest-bdd Documentation

* See [https://pypi.org/project/pytest-bdd/](https://pypi.org/project/pytest-bdd/) for reporting options.


## Practices

### Page Object Model

This test is using a standard page object model, where the selectors 
and functions are group inside a class.

### BDD
Using pytest-bdd to describe a behavior of users in plain text for better understanding of stakeholders.
This project is structured using features and test steps. 

* Feature example [order_transaction.feature](./features/order_transaction.feature) 
* Steps example [test_pytest_bdd.py](./tests/test_pytest_bdd.py)

## Recommended plugins:
* pytest-xdist - used to run multiple tests at the same time
* pytest-html - for simple html report

