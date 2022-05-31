import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_check_addtobasket_btn(browser):
    browser.get(link)
    time.sleep(30)
    add_btn = browser.find_elements_by_css_selector("button.btn-primary")
    add_btn_text = "Add to basket"
    assert add_btn != None,\
        f"Elements '{add_btn_text}' not found in page. Expected found"

