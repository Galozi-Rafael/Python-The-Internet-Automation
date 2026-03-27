from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()
    page.goto("https://the-internet.herokuapp.com/login")

    # Esperar que a página fique visível
    page.wait_for_selector("#username", state="visible")

    # Declarando as credenciais
    user_name = "tomsmith"
    password = "SuperSecretPassword!"

    # Preenchendo os campos de login e click em submit
    page.get_by_label("Username").fill(user_name)
    page.get_by_label("password").fill(password)
    page.locator('[type="submit"]').click()

    # Capturando mensagem de login
    login_message = "You logged into a secure area!"
    message = page.locator("#flash").inner_text()
    clean_message = message.split("\n")[0].strip()

    # Verificando se o login foi efetuado corretamente
    if login_message in message:
        print(clean_message)
    else:
        print("Login não foi bem sucedido!")

    # Clicando em logout
    page.locator('[href="/logout"]').click()



