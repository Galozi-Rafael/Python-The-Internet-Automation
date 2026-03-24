from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()
    browser.goto("https://the-internet.herokuapp.com/entry_ad")

    # Esperar até que o modal seja exibido
    page.wait_for_selector("#modal", state="visible")

    # Extrair o texto do modal
    modal_text = page.locator("#modal .modal-body").inner_text().strip()
    print(f"Modal text: {modal_text}")

    # Clicar no botão "Close" para fechar o modal
    close_button_selector = "#modal .modal-footer p"
    browser.click(close_button_selector)

    # Verificar se o modal foi fechado
    modal_visible = page.locator("#modal").is_visible()

    if not modal_visible:
        print("Modal closed successfully.")
    else:
        print("Modal is still visible.")
    
    # Clicar no link "Click here" para reabrir o modal
    click_here_link_selector = 'a[id="restart-ad"]'
    browser.click(click_here_link_selector)

    # Esperar até que o modal seja exibido novamente
    page.wait_for_selector("#modal", state="visible")

    # Extrair o texto do modal novamente
    modal_text_again = page.locator("#modal .modal-body").inner_text().strip()
    print(f"Modal text after reopening: {modal_text_again}")

    # clicar no botão "Close" para fechar o modal novamente
    browser.click(close_button_selector)

    # Verificar se o modal foi fechado novamente

    if not modal_visible:
        print("Modal closed successfully.")
    else:
        print("Modal is still visible.")

    # Fechar o navegador
    browser.close_browser()
