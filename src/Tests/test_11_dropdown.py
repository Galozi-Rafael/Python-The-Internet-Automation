from Services.browser_service import BrowserService

def run():
    browser = BrowserService(headless=False)

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown_selector = "#dropdown"
    option_text = "Option 2"

    print(f"Selecionando a opção '{option_text}' no dropdown...")

    page.wait_for_timeout(1000)  

    browser.select_by_text(dropdown_selector, option_text)

    selected_option = page.locator(f"{dropdown_selector} option:checked").inner_text()

    page.wait_for_timeout(1000)
    
    print(f"Opção selecionada: {selected_option}")


    
    browser.close_browser()