# Selenium тесты
для проекта MoneyCat (softree.group) и Todo (todo.mail.ru)

## SetUp
requirement python version - 3.7.x  

Нужно указать в settings.py  
- CHROME_BIN - путь на бинарник http://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/
- FIREFOX_BIN - путь на бинарник https://github.com/mozilla/geckodriver/releases
- SELENIUM_BIN - путь на jar файл селениума http://selenium-release.storage.googleapis.com/index.html?path=3.141/

## Usage
```bash
python manage.py run_selenium
python manage.py test
```

*run_selenium* - запустить сервер селениума  
*test* - запустить тесты  

**Переменные окружения**  
*LOGIN* - логин  
*PASS* - пароль  
*LOCALE* - локаль (ENG или ничего)
