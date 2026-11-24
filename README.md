# Python Test Automation Framework — pytest

[![tests](https://github.com/yanivi71/python-test-automation-framework/actions/workflows/tests.yml/badge.svg)](https://github.com/yanivi71/python-test-automation-framework/actions/workflows/tests.yml)

A test automation framework built from scratch in Python, covering **UI**, **API** and **unit-level** tests
from a single `pytest` run.

```
pytest -v
```

```
tests/api/test_posts.py ....                    [ 25%]
tests/test_exercises.py ..........              [ 87%]
tests/test_web_form.py ..                       [100%]
16 passed
```

---

## What this framework demonstrates

| Area | Implementation |
|---|---|
| Test infrastructure | `conftest.py` — external config, driver lifecycle, failure capture |
| UI testing | Selenium 4 + Page Objects, locators stored as data |
| API testing | `requests` with a session-scoped `Session` fixture |
| Data-driven testing | `@pytest.mark.parametrize` with explicit case ids |
| Non-deterministic output | Invariant assertions + repeated-run statistical checks |
| Test isolation | Guaranteed starting state before every test |
| Reporting | Automatic screenshot on UI failure |

---

## Project structure

```
PytestPort/
├── conftest.py          # fixtures, hooks, config loader
├── config.json          # browser, URLs, timeout — no values hardcoded in tests
├── pages/               # page objects
│   └── web_form_page.py
├── tests/
│   ├── api/             # API tests
│   ├── test_web_form.py # UI tests
│   └── test_exercises.py
└── requirements.txt
```

---

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
pytest -v
```

Chrome is required for the UI tests. Selenium Manager resolves the driver automatically — no manual
driver download.

Run a single category:

```bash
pytest tests/api -v
pytest tests/test_web_form.py -v
```

---

## Implementation notes

### Locators are data, not elements

Page objects store the *instruction to find* an element rather than the element itself:

```python
class WebFormPage:
    TXT_INPUT = (By.NAME, "my-text")
    BTN_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_text(self, value):
        self.driver.find_element(*self.TXT_INPUT).send_keys(value)
```

Nothing is cached between page states, so `StaleElementReferenceException` cannot occur.

### Test isolation is enforced, not assumed

The browser is shared across a test class for speed, which makes order-dependence possible. Rather than
cleaning up after each test, every test is given a known starting state before it runs:

```python
@pytest.fixture(autouse=True)
def start_at_home(request):
    if "driver" in request.fixturenames:
        request.getfixturevalue("driver").get(get_data("url"))
    yield
```

The `fixturenames` check means unit and API tests never launch a browser — they run in ~0.1s and cannot
fail because of WebDriver.

### Screenshots on failure

A `pytest_runtest_makereport` hook attaches each test's result to the test item; an autouse fixture reads
it during teardown and captures the browser state — while the session is still alive.

### Testing non-deterministic output

Output that changes between runs cannot be asserted by value. The suite separates two kinds of claim:

```python
def test_shuffled_words_keeps_all_words():          # invariant — every run
    assert sorted(result) == sorted(source.split())

def test_shuffled_words_order_varies():             # statistical — across runs
    orders = {tuple(shuffled_words(text)) for _ in range(20)}
    assert len(orders) > 1
```

Asserting "the order changed" in a *single* run would be flaky: a shuffle may legitimately return the
original order. The same separation applies to validating LLM output — structural invariants per call,
quality measured across a dataset.

---

## Background

Ported from a Java/TestNG/Selenium framework I built during my automation studies, rebuilt layer by layer
in Python to map the concepts across:

| Java / TestNG | Python / pytest |
|---|---|
| `@BeforeClass` / `@AfterClass` | fixture code before / after `yield` |
| `ITestListener` | `pytest_runtest_makereport` hook + autouse fixture |
| `@FindBy` + PageFactory | locator tuples resolved at use time |
| `DataProvider` | `@pytest.mark.parametrize` |
| `DataConfig.xml` | `config.json` |
| RestAssured | `requests` |
