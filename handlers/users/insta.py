async def insta_bot(wait_for):
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.firefox.options import Options
    import asyncio
    from loader import db
    insta_username = "<username>"
    insta_password = "<password>"
    while True:
        await asyncio.sleep(wait_for)
        us = [j for i in db.get_all_users() for j in i]


        browser = webdriver.Firefox()
        browser.get('https://www.instagram.com/')
        await asyncio.sleep(20)
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(insta_username)
        password_input.send_keys(insta_password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        await asyncio.sleep(30)
        try:
            activity_link = browser.find_element_by_css_selector("a._0ZPOP.kIKUG")
            activity_link.click()
        except NoSuchElementException:
            main_page = browser.window_handles[0]
            browser.switch_to.window(main_page)
            browser.close()
        await asyncio.sleep(20)
        try:
            but = browser.find_element_by_css_selector("button.sqdOP.yWX7d._8A5w5")
            but.click()
        except NoSuchElementException:
            main_page = browser.window_handles[0]
            browser.switch_to.window(main_page)
            browser.close()
        names = browser.find_elements_by_css_selector("a.FPmhX.notranslate.yrJyr")
        confirm = browser.find_elements_by_xpath("//button[text()='Confirm']")
        delete = browser.find_elements_by_xpath("//button[text()='Delete']")
        for i, j, r in zip(names, confirm, delete):
            if i.text in us:
                j.click()
                await asyncio.sleep(1)

        main_page = browser.window_handles[0]
        browser.switch_to.window(main_page)

        browser.close()
