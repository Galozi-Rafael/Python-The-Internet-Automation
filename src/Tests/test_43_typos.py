from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()
    browser.goto("https://the-internet.herokuapp.com/typos")

    # Esperar até que o parágrafo esteja visível
    page.wait_for_selector("#content > div > p:nth-child(3)", state="visible")

    # Extrair o texto do parágrafo
    paragraph_text = page.locator("#content > div > p:nth-child(3)").inner_text().strip()
    print(f"Paragraph text: {paragraph_text}")

    # Verificar se o texto contém o erro de digitação esperado
    expected_typo = "won't"

    if expected_typo in paragraph_text:
        print("Typo found in the paragraph.")
    else:
        print("Typo not found in the paragraph.")