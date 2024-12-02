from selenium import webdriver
from selenium.webdriver.chrome.service import Service;

from selenium.webdriver.common.by import By;

from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;

cookie_id = 'bigCookie';

cookies_id = 'cookies';

product_price_prefix = 'productPrice';

product_prefix = 'product';

service = Service(executable_path="chromedriver.exe");

driver = webdriver.Chrome(service=service);

driver.get('https://orteil.dashnet.org/cookieclicker/');

# WebDriverWait(driver=driver, timeout=5).until(
#     EC.presence_of_element_located((By.ID, cookie_id))
# )

WebDriverWait(driver=driver, timeout=15).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "English")]'))
)

language = driver.find_element(By.XPATH, '//*[contains(text(), "English")]');
language.click();

WebDriverWait(driver=driver, timeout=15).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id);

# print(cookie);
# print(cookie.tag_name);

# time.sleep(5);

while True:
    cookie.click();

    cookies = driver.find_element(By.ID, cookies_id);
    
    # print(cookies.text);
    cookies_count = cookies.text.split(" ")[0];
    cookies_count = int(cookies_count.replace(",", ""));
    print("The Cookies Count Is: ", cookies_count);

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i));
        print("The Product Price Text Is: ", product_price.text);

        if product_price.text == '' or product_price.text is None:
            continue;

        product_price = int(product_price.text.replace(',', ''));
        # print(product_price);

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i));
            product.click();
            print("We Have Buy Product With Name: ", product.text);
            break;

# driver.quit();