
from Services.browser_service import BrowserService
from Services.dialog_service import DialogService

def run():

    browser = BrowserService(headless=False)

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/context_menu")

    page.on("dialog", DialogService().handle_dialog)

    page.wait_for_selector("#hot-spot")

    browser.right_click("#hot-spot")
