from selenium import webdriver
from time import sleep

if __name__=='__main__':
    url = 'https://www.codewars.com/users/NieetycznyPa%C5%BAdzierz%20/completed'

    browser = webdriver.Firefox()
    browser.get(url)
    while True:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)
        new_height = browser.execute_script("return document.body.scrollHeight")
        try:
            if last_height and new_height == last_height:
                break
        except NameError:
            pass
        last_height = new_height
        
    html = browser.page_source

    print([x[-1] for x in html.split(' kyu') if x[-1].isnumeric()])
    browser.quit()