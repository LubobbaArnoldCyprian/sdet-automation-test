import time
import allure
import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:
    all_menu_id = "nav-hamburger-menu"
    arts_crafts_xpath = "//div[normalize-space()='Arts & Crafts']"
    beading_jewelery_partial_link_text = "Beading & Jewelry Making"
    crafts_sewing_xpath = "//span[contains(text(),'Arts, Crafts & Sewing')]"
    engraving_machinery_tools_id = "n/12896151"
    sort_css_selector = ".a-dropdown-container"
    drop_down_selection_id = "s-result-sort-select_2"
    third_product_css_selector = "div[data-index='4']"
    review_score_css_selector = ".a-icon.a-icon-star-medium"
    review_score_id = "acrPopover"
    add_to_cart_button_id = "submit.add-to-cart"
    price_element = "a-price-whole"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )

    def click_all_menu(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.all_menu_id).click()

# locate the element, compare its text with the expected value, print the results, and click on the
# element if the text matches the expected value.

    def click_open_arts_and_crafts(self, assertArtsCrafts):
        arts_element = self.wait_for_element((By.XPATH, self.arts_crafts_xpath))
        open_arts_text = arts_element.text
        print(f"Actual Text: {open_arts_text}, Expected Text: {assertArtsCrafts}")
        assert open_arts_text == assertArtsCrafts
        arts_element.click()

# wait up to 10 seconds until the "Beading & Jewelry Making" link is present, get the text of the found element
# print actual and expected text for verification, assert that the actual text matches the expected text.

    def click_beading_and_crafts(self, assertBeadingJewelry):
        self.driver.implicitly_wait(10)
        beading_element = beading_jewelry = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Beading & Jewelry Making"))
        )
        open_beading_text = beading_element.text
        print(f"Actual Text: {open_beading_text}, Expected Text: {assertBeadingJewelry}")
        assert open_beading_text == assertBeadingJewelry
        self.driver.execute_script("arguments[0].click();", beading_jewelry)

# locate the element, compare its text with the expected value, print the results, and click on the
# element if the text matches the expected value.
    def click_crafts_and_sewing(self, assertCraftsSewing):
        crafts_element = self.driver.find_element(By.XPATH, self.crafts_sewing_xpath)
        open_crafts_text = crafts_element.text
        print(f"Actual Text: {open_crafts_text}, Expected Text: {assertCraftsSewing}")
        assert open_crafts_text == assertCraftsSewing
        crafts_element.click()

    def click_engraving_machines_and_tools(self):
        self.driver.find_element(By.ID, self.engraving_machinery_tools_id).click()

    def sort_price(self):
        self.driver.find_element(By.CSS_SELECTOR, self.sort_css_selector).click()
        self.driver.find_element(By.ID, self.drop_down_selection_id).click()

    def click_third_product(self):
        self.driver.implicitly_wait(10)
        click_product = self.driver.find_element(By.CSS_SELECTOR, self.third_product_css_selector)
        third_product = WebDriverWait(self.driver, 10).until(EC.visibility_of(click_product))
        third_product.click()

# Find review elements, get the text from the second one, extract the numeral from review_score_text, remove whitespace
# Assert error is raised if the review score is less than 4, print message if the review score is 4 or higher
# A value error is raised if no numeric review scores are found in the element text

    def get_review_score(self):
        #
        review_score_elements = self.driver.find_elements(By.ID, self.review_score_id)
        review_score_element = review_score_elements[1]
        review_score_text = review_score_element.get_attribute('textContent')

        review_score_text = review_score_text.strip()
        review_score_numbers = [float(s) for s in review_score_text.split() if s.replace('.', '', 1).isdigit()]

        if review_score_numbers:
            review_score = review_score_numbers[0]
            if review_score < 4:
                raise AssertionError(f"Review score is less than 4: {review_score}")
            else:
                print(f"Test passed. Review score is: {review_score}")
        else:
            raise ValueError("No numeric review scores found in the element text.")

# Check if price exceeds $4000, raise exception if true, Raise exception if the price element is not found on the page
    def check_price(self):
        try:
            price_element = self.wait_for_element((By.CLASS_NAME, self.price_element))
            price_fraction_element = self.driver.find_element(By.CLASS_NAME, "a-price-fraction")
            item_price = float(f"{price_element.text.replace(',', '')}.{price_fraction_element.text}")
            if item_price > 4000:
                raise ValueError(f"Item price is greater than $4000: ${item_price}")
        except NoSuchElementException:
            raise NoSuchElementException("Price element not found on the page.")
