# from lib2to3.pgen2 import driver
import allure
from selenium import webdriver
import pytest


@pytest.fixture
def log_on_failure(request, setup):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(setup.get_screenshot_as_png(), name="failed_test", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(100)
    return driver
