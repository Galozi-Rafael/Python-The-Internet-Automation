from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()
    browser.goto("https://the-internet.herokuapp.com/forgot_password")

    # Esperar até que o campo de email esteja visível
    page.wait_for_selector("#email", state="visible")

    # Preencher o campo de email
    email = "zedascouves@couvemail.com"
    page.locator("#email").fill(email)

    # Clicar no botão "Retrieve password"
    browser.click("#form_submit")

    # Esperar até que a mensagem de sucesso seja exibida
    page.wait_for_selector("h1", state="visible")

    # Extrair o texto da mensagem de sucesso
    success_message = page.locator("h1").inner_text().strip()
    print(f"Success message: {success_message}")

    # Verificar se a mensagem de sucesso é a esperada
    expected_message = "Internal Server Error"

    if success_message != expected_message:
        print("Success message is correct.")
    else:
        print("Success message is incorrect.")
