from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Options to configure ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Path to ChromeDriver (ensure it's in the PATH or specify the full path)
#webdriver_service = Service(r'C:\Users\21269\Downloads\chromedriver-win64\chromedriver.exe')
webdriver_service = Service('/usr/local/bin/chromedriver-linux64/chromedriver')

# Initialize the WebDriver with options
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Define the buttons to be tested
buttons_to_test = [
    {
        "url": "https://www.apec.fr/candidat/page-entreprise.html/detail?id=591263",
        "selector": "a.h-button[href='https://www.apec.fr/candidat/page-entreprise.html/detail?id=591263']",
        "name": "APEC Button"
    },
    {
        "url": "https://www.welcometothejungle.com/fr/companies/klanik",
        "selector": "a.h-button[href='https://www.welcometothejungle.com/fr/companies/klanik']",
        "name": "Welcome To The Jungle Button"
    }
]

# Initialize flag to track test result
test_passed = True

try:
    # Open the company's website
    driver.get('https://www.klanik.com/')

    # Wait for the page to load
    time.sleep(3)  # Adjust the sleep time as needed

    # Loop through each button and test
    for button_info in buttons_to_test:
        try:
            # Find the button by its CSS_SELECTOR and click it
            button = driver.find_element(By.CSS_SELECTOR, button_info["selector"])
            button.click()
            
            # Wait for the new tab to open
            time.sleep(3)  # Adjust the sleep time as needed
            
            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])
            
            # Verify the URL of the new tab
            assert button_info["url"] in driver.current_url
            #print(f"{button_info['name']} redirection: {driver.current_url}")
            print("{} redirection: {}".format(button_info['name'], driver.current_url))

            
        except Exception as e:
           # print(f"Test failed for {button_info['name']}: {e}")
           print("Test failed for {}: {}".format(button_info['name'], e))
           test_passed = False
        
        finally:
            # Close the new tab if opened
            if len(driver.window_handles) > 1:
                driver.close()
                # Switch back to the original tab
                driver.switch_to.window(driver.window_handles[0])

except Exception as e:
    #print(f"Test failed: {e}")
    print("Test failed: {}".format(e))
    test_passed = False

finally:
    # Close the WebDriver
    driver.quit()

# Print final test result
if test_passed:
    print("All redirection tests passed!")
else:
    print("One or more redirection tests failed!")
