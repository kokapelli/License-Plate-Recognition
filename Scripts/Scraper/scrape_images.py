from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3
import argparse
import urllib.request
import time
import requests
import shutil
from tqdm import tqdm

WEBDRIVER_PATH = 'C:/Users/Kukus/chromeDriver/chromedriver.exe'
IMAGE_DIR = 'images/'


parser = argparse.ArgumentParser()
parser.add_argument('--search', 
    type=str,
    help='Search term', 
    default='bil')
parser.add_argument('--thumbnail', help='Download image thumbnails', action='store_true')

args = parser.parse_args()
query = args.search
thumbnail = args.thumbnail

def find_urls(url, driver, directory):
    driver.get(url)
    counter = 0
    succounter = 0
    dir_size = len([name for name in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, name))])


    print("Scrolling...")
    for _ in tqdm(range(500)):
        driver.execute_script("window.scrollBy(0,10000)")
        try:
            driver.find_element_by_css_selector('.mye4qd').click()
        except:
            continue

    print("Downloading images...")
    for imgurl in tqdm(driver.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]')):
        counter += 1
        if(thumbnail):
            try:
                img = imgurl.get_attribute('src')
                save_img(img, dir_size, directory)
                succounter += 1
                dir_size += 1
            except Exception:
                pass
        else:
            try:
                imgurl.click()
                img = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
                save_img(img, dir_size, directory)
                time.sleep(1.5)
                succounter += 1
                dir_size += 1
            except Exception:
                pass

    print(f"Total Count: {counter}")
    print(f"Successful Count: {succounter}")
    print(f"Directory currently holds {dir_size} images")

def save_img(img, i, directory):
    try:
        filename = 'image'+str(i)+'.jpg'
        response = requests.get(img,stream=True)
        image_path = os.path.join(directory, filename)
        with open(image_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    except Exception:
        pass

if __name__ == "__main__":
    url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

    print(f"Searching for: {query}...")
    driver = webdriver.Chrome(WEBDRIVER_PATH)
    driver.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    find_urls(url, driver, IMAGE_DIR)
    driver.close()