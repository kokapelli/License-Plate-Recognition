from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib3

WEBDRIVER_PATH = 'C:/Users/Kukus/chromeDriver/chromedriver.exe'

def lookup_license_plate(license_plates):
    print(license_plates)
    for license_number in license_plates:
        url = "https://biluppgifter.se/fordon/"+license_number
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options, executable_path=WEBDRIVER_PATH)
        driver.get(url)
    
if __name__ == "__main__":
    license_test = ['ABC 786', 'ÅÄÖ 123']
    license_number_test= 'ABC 786'
    lookup_license_plate(license_test)