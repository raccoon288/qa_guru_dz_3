import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setup_teardown():
    browser.config.window_height = 1280
    browser.config.window_width = 720
    browser.open('https://google.com/ncr')
    yield
    browser.quit()
