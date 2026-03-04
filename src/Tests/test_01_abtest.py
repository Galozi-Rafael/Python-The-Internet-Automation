from Services.browser_service import BrowserService

def run_TC01():
    
    browser = BrowserService(headless=False)

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/abtest")

    heading = page.locator("h3").inner_text()

    print(f"O texto do heading é: {heading}")

    if heading in ["A/B Test Control", "A/B Test Variation 1"]:
        print("Teste passou: O heading é um dos esperados.")
    else:
        print("Teste falhou: O heading não é um dos esperados.")

    browser.close_browser()