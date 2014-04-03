from selenium import webdriver
import time
from login_details import loginDetails


def open_o2_in_browser():
    browser = webdriver.Firefox()
    browser.get('http://o2.ie')
    return browser


def find_and_click_login_button(browser):
    button = browser.find_element_by_link_text("Login")
    button.click()


def go_to_iFrame(browser):  # meld this in
    browser.switch_to_frame(browser.find_element_by_tag_name("iframe"))


def ask_for_username_and_password():
    print("please enter the username")
    username = input(">")

    print("please enter the password")
    password = input(">")

    return username, password


def ask_for_message():
    print("please enter message")
    message = input(">")
    # put in check if over 140 characters
    return message


def enter_username_and_password_and_hit_login(browser, username, password):
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_tag_name("button").click()
    return browser


def go_to_webtext_page(browser):
    while True:
        try:
            browser.find_element_by_class_name("myO2Webtext").click()
        except webdriver.NoSuchElementException:
            time.sleep(1)
            continue
        break


def enter_message(browser, message):
    try:
        browser.switch_to_frame(browser.find_element_by_tag_name("frame"))
    except:
        pass
        # in the long term we can put a note into a log saying we didn't need
        # to switch"
    browser.find_element_by_tag_name("textarea").send_keys(message)


# put in loop around known values


if __name__ == '__main__':

    browser = open_o2_in_browser()

    #loginDetails = {"0863799601": "Bhaa9601"}
    message = ask_for_message()
    for username in loginDetails:
        password = loginDetails[username]
        find_and_click_login_button(browser)
        browser.implicitly_wait(3)
        go_to_iFrame(browser)
        #username, password = ask_for_username_and_password()
        enter_username_and_password_and_hit_login(browser, username, password)
        # replace with looping and trying
        input("hit enter when it stops loading")
        go_to_webtext_page(browser)
        for partial_link_text in ("1st", "2nd", "3rd", "4th", "5th"):
        # for partial_link_text in ("1st","2nd"):
            #ditto
            blah = input("hit enter when the text message thing is available")
            enter_message(browser, message)
            try:
                browser.find_element_by_class_name("all").click()
                #input ("in try")
            except:
                browser.find_element_by_id("imgOpenContacts").click()
                browser.find_element_by_class_name("all").click()
                #input ("in except")
            input("hit enter when names appear")
            try:
                browser.find_element_by_partial_link_text(
                    partial_link_text).click()
                input("change to own number and hit enter")
                browser.find_element_by_id("imgSendYourText").click()
                print("sent to " + partial_link_text)
            except:
                print(
                    username + " doesn't seem to have a " + partial_link_text)
                break  # some of the users don't have all 5 groups
        # browser.find_element_by_partial_link_text("logout.php").click()
        # browser.find_element_by_partial_link_text("Logout").click()
        print("all sent using " + username)
        input("logout manually")

        """
    username = "0863799442"
    password = "Bhaa3799"
    input ("hit enter when done with SAP stuff")
    find_and_click_login_button(browser)
    browser.implicitly_wait(3)
    go_to_iFrame(browser)
    message = ask_for_message()
        #username, password = ask_for_username_and_password()
    browser = enter_username_and_password_and_hit_login(browser,username,password)
    browser.implicitly_wait(20)
    #this line works in the interpreter but not here
    #I don't know why, and I'm going to bed
    input ("hang on")
    go_to_webtext_page(browser)
    blah = input("hang on a sec")"""

        # enter_message(browser,message)
        # can't finish without being able to send texts
        # right now it's midnight
        # these will be useful though

        # click on the all link under contacts
        # browser.find_element_by_class_name("all").click()

        # click on the '1st' link
        # browser.find_element_by_partial_link_text("1st").click()
    browser.quit()
