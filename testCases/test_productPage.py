import pytest
from selenium import webdriver
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
import allure


@pytest.mark.usefixtures("setup", "log_on_failure")
class Test_001_Product:
    baseURL = ReadConfig.getApplicationURL()
    assertArtsCrafts = ReadConfig.getArtsCraftsAssertions()
    assertBeadingJewelry = ReadConfig.getBeadingJewelryAssertions()
    assertCraftsSewing = ReadConfig.getCraftSewingAssertions()

    def test_product(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.product = ProductPage(self.driver)
        self.product.click_all_menu()
        self.product.click_open_arts_and_crafts(self.assertArtsCrafts)
        self.product.click_beading_and_crafts(self.assertBeadingJewelry)
        self.product.click_crafts_and_sewing(self.assertCraftsSewing)
        self.product.click_beading_and_crafts(self.assertBeadingJewelry)
        self.product.click_engraving_machines_and_tools()
        self.product.sort_price()
        self.product.click_third_product()
        self.product.get_review_score()
        self.product.check_price()
