## Playwright Python pytest_bdd example
- Depends on [pytest-playwright](https://github.com/microsoft/playwright-pytest) 

To install project packages

```
pip install -r requirements.txt
```

## Command Line Example
Use "pytest" to run all the tests

Other examples
Use "pytest tests/test_pytest_bdd.py" to run specific file test
Use "pytest tests/without_bdd/test_ui_validation.py::test_handle_alert_boxes" to run the test_handle_alert_boxes test 

## Playwright Documentation

[https://playwright.dev/python/docs/intro](https://playwright.dev/python/docs/intro)

## pytest-bdd Documentation

See [https://pypi.org/project/pytest-bdd/](https://pypi.org/project/pytest-bdd/) for reporting options.
 


## Page Object example
This test is using a standard page object model, where the selectors 
and functions are group inside a class.

Alternative format that uses files instead of objects to group the pages can be found
[here](https://github.com/cmoir/playwright-pytest-pagefile-example)

## Recommended plugins:
pytest-xdist - used to run multiple tests at the same time
pytest-html - for nice simple html report

