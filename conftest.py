import json
import os
from datetime import datetime
from os import path

import pytest
from selenium import webdriver
from pages.web_form_page import WebFormPage

import requests

HERE = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(HERE, "config.json")

with open(CONFIG_PATH, encoding="utf-8") as f:
    CONFIG = json.load(f)


def get_data(key):
    return CONFIG[key]

@pytest.fixture(scope="class")
def driver():
    browser = get_data("browser").lower()

    if browser == "chrome":
        drv = webdriver.Chrome()
    elif browser == "firefox":
        drv = webdriver.Firefox()
    else:
        raise RuntimeError(f"Invalid browser type: {browser}")

    drv.maximize_window()
    drv.implicitly_wait(get_data("timeout"))

    yield drv

    drv.quit()

@pytest.fixture(autouse=True)
def start_at_home(request):
    if "driver" in request.fixturenames:
        request.getfixturevalue("driver").get(get_data("url"))
    yield


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield
    report = getattr(request.node, "report_call", None)
    if report is None or not report.failed:
        return
    if "driver" not in request.fixturenames:
        return

    driver = request.getfixturevalue("driver")
    shots_dir = os.path.join(HERE, "screenshots")
    os.makedirs(shots_dir, exist_ok=True)
    name = f"{request.node.name}_{datetime.now():%Y%m%d_%H%M%S}.png"
    path = os.path.join(shots_dir, name)
    driver.save_screenshot(path)
    print(f"\nScreenshot saved: {path}")

@pytest.fixture
def web_form(driver):
    return WebFormPage(driver)

@pytest.fixture(scope="session")
def api_url():
    return get_data("api_url")

@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()