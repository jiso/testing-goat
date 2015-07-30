from selenium import webdriver

driver = webdriver.Remote(
   command_executor='http://192.168.99.100:4444/wd/hub',
   desired_capabilities={
            "browserName": "firefox"
        })

driver.get('http://192.168.99.100:8000')

assert 'Django' in driver.title
driver.quit()