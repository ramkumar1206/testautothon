import pytest
from seleniumbase import BaseCase
from config.chrome_mobile import chrome_mobile


class TestMobileWeb(BaseCase):
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        self.driver = chrome_mobile()

    def test_open_google(self):
        self.open("https://www.youtube.com/")
        #self.click("#search", timeout=15)
        self.type("#search", "TestAutothon")
        self.click("button#search-icon-legacy")
        # self.click('a:contains("Sign in")')
        # self.assert_exact_text("Welcome!", "h1")
        # self.assert_element("img#image1")
        # self.highlight("#image1")
        # self.click_link("Sign out")
        # self.assert_text("signed out", "#top_message")

    def tearDown(self):
        self.driver.close()
