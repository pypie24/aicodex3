from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located
)

from webdriver_manager.chrome import ChromeDriverManager

import unittest


class VnExpressMenuTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.page_load_strategy = "none"
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--headless")  # Run headless if needed
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.driver.get("https://vnexpress.net/")
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.wait.until(visibility_of_element_located((By.CSS_SELECTOR, "nav.main-nav")))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_menu_bar(self):
        # Locate the menu bar
        menu_bar = self.driver.find_element(By.CSS_SELECTOR, "nav.main-nav")
        
        # Verify menu items
        expected_menu_items = ["Trang chủ", "Thời sự", "Góc nhìn", "Thế giới", "Video", "Podcasts", "Kinh doanh", "Khoa học", "Giải trí", "Thể thao", "Pháp luật", "Giáo dục", "Sức khỏe", "Đời sống", "Du lịch", "Số hóa", "Xe", "Ý kiến", "Tâm sự"]
        menu_items = menu_bar.find_elements(By.TAG_NAME, "a")
        menu_texts = [item.accessible_name for item in menu_items if item.accessible_name]

        for expected_item in expected_menu_items:
            self.assertIn(expected_item, menu_texts, f"Menu item '{expected_item}' not found in the menu bar")
    
    def test_redirect_to_finnace(self):
        # Locate the finance menu item
        finance_menu_item = self.driver.find_element(By.XPATH, "//a[@href='/kinh-doanh']")
        finance_menu_item.click()
        
        # Verify the finance page
        self.assertIn("Tin kinh doanh", self.driver.title, "Failed to redirect to the finance page")


if __name__ == "__main__":
    unittest.main()
