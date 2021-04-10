from selenium import webdriver
import settings

if __name__ == '__main__':
    driver = webdriver.Chrome(settings.CHROME_BIN)
    # driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("http://park.mail.ru/")
    driver.quit()