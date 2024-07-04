# SELENIUM

# U need to search in the web for the drivers, and install it

# pip install selenium webdriver-manager

# Doc Selenium
# https://selenium-python.readthedocs.i

from selenium import webdriver

def make_chrome_driver(*options: str) -> webdriver.Chrome:
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    
    chrome_options = Options()
    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
            ChromeDriverManager().install()
        ) # Service that use the configs


    chrome_browser = webdriver.Chrome(
        service= chrome_service,
        options= chrome_options,
        ) # Driver

     
    return chrome_browser


def main() -> None:
    """Function used to run the main code."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # More Chrome Options
    # https://peter.sh/experiments/chromium-command-line-switches/
    # ('--headless') option make the browser run in the background
    options: tuple[str] = ('--disable-gpu')

    driver = make_chrome_driver(*options)
    
    driver.get("https://www.google.com/")

    #                          <driver>, <max_time_to_wait>
    input_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="APjFqb"]')
        )
    )
    
    input_search.send_keys("Selenium WebDriver")
    input_search.send_keys(Keys.ENTER)

    driver.quit()

if __name__ == '__main__':
    main()