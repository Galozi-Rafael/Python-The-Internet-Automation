from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()
    browser.goto("https://the-internet.herokuapp.com/dynamic_controls")

    # Verificar o estado inicial do checkbox
    checkbox_selector = "#checkbox"
    checkbox_count = browser.count_elements(checkbox_selector)
    print(f"Checkbox count before removal: {checkbox_count}")

    # Clicar no botão "Remove" para remover o checkbox
    remove_button_selector = "#checkbox-example button"
    browser.click(remove_button_selector)

    browser.page.wait_for_timeout(10000)  
    browser.page.wait_for_selector("#message", state="visible")
    message = page.locator("#message").inner_text().strip()

    print(f"Message after removal: {message}")

    # Verificar o estado do checkbox após a remoção
    checkbox_count_after_removal = browser.count_elements(checkbox_selector)
    print(f"Checkbox count after removal: {checkbox_count_after_removal}")

    # Clicar no botão "Add" para adicionar o checkbox novamente
    add_button_selector = "#checkbox-example button"
    browser.click(add_button_selector)

    browser.page.wait_for_timeout(10000)  
    browser.page.wait_for_selector("#message", state="visible")
    message_after_add = page.locator("#message").inner_text().strip()

    print(f"Message after add: {message_after_add}")


    # Clica no botão "Enable" para habilitar o campo de entrada
    enable_button_selector = "#input-example button"
    browser.click(enable_button_selector)

    # Espera até que a mensagem de habilitação seja exibida
    browser.page.wait_for_timeout(10000)  
    browser.page.wait_for_selector("#message", state="visible")
    message_after_enable = page.locator("#message").inner_text().strip()
    print(f"Message after enable: {message_after_enable}")

    # Verificar se o campo de entrada está habilitado
    input_selector = "#input-example input"
    input_enabled = browser.page.locator(input_selector).is_enabled()
    print(f"Input enabled: {input_enabled}")
