from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Options to configure ChromeDriver
chrome_options = Options()
# Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to ChromeDriver (ensure it's in the PATH or specify the full path)
#webdriver_service = Service(r'C:\Users\21269\Downloads\chromedriver-win64\chromedriver.exe')
webdriver_service = Service('/usr/local/bin/chromedriver-linux64/chromedriver')
# Initialize the WebDriver with options
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:
    # Open the company's website
    driver.get('https://www.klanik.com/')

    # Wait for the page to load
    time.sleep(3)  # Adjust the sleep time as needed

    # Find the button by its CSS_SELECTOR and click it
    button = driver.find_element(By.CSS_SELECTOR, "a.h-button[href='https://www.apec.fr/candidat/page-entreprise.html/detail?id=591263']")
    button.click()

    # Wait for the new tab to open
    time.sleep(3)  # Adjust the sleep time as needed

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Verify the URL of the new tab
    assert "https://www.apec.fr/candidat/page-entreprise.html/detail?id=591263" in driver.current_url

    print(driver.current_url)

    print("Redirection test passed!")

except Exception as e:
    print(f"Test failed: {e}")

finally:
    # Close the WebDriver
    driver.quit()
