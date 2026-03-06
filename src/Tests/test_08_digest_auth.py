from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False, username="admin", password="admin")

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/digest_auth")

    # Obtém o texto do heading da página
    message = page.locator("p").inner_text()

    print(f"O texto da mensagem é: {message}")

    if "Congratulations" in message:
        print("Teste passou: A mensagem de sucesso foi exibida.")
    else:
        print("Teste falhou: A mensagem de sucesso não foi exibida.")
    
    browser.close_browser()
