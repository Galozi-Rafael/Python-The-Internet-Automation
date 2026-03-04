from Services.browser_service import BrowserService

# Metodo para executar o teste de A/B Test
def run():
    
    # Cria uma instância do BrowserService com headless=False para visualizar o navegador
    browser = BrowserService(headless=False)

    # Inicia o navegador e obtém a página para interagir
    page = browser.start_browser()

    # Navega para a página de teste de A/B Test
    page.goto("https://the-internet.herokuapp.com/abtest")

    # Obtém o texto do heading da página
    heading = page.locator("h3").inner_text()

    print(f"O texto do heading é: {heading}")

    # Verifica se o heading é um dos esperados para o teste de A/B Test
    if heading in ["A/B Test Control", "A/B Test Variation 1"]:
        print("Teste passou: O heading é um dos esperados.")
    else:
        print("Teste falhou: O heading não é um dos esperados.")

    browser.close_browser()