from Services.browser_service import BrowserService

def run():

    # Criar uma instância do BrowserService e iniciar o navegador
    browser = BrowserService(headless=False)
    page = browser.start_browser()
    browser.goto("https://the-internet.herokuapp.com/dynamic_loading")

    # Clicar no link "Example 1: Element on page that is hidden"
    example_1_link_selector = 'a[href="/dynamic_loading/1"]'
    browser.click(example_1_link_selector)

    # Clicar no botão "Start" para iniciar o carregamento do conteúdo
    start_button_selector = "#start button"
    browser.click(start_button_selector)

    # Esperar até que o conteúdo carregado seja exibido
    page.wait_for_selector("#finish", state="visible")
    
    # Extrair o texto do conteúdo carregado
    loaded_content = page.locator("#finish").inner_text().strip()
    print(f"Loaded content: {loaded_content}")

    # Voltar para a página anterior
    page.go_back()

    # Clicar no link "Example 2: Element rendered after the fact"
    example_2_link_selector = 'a[href="/dynamic_loading/2"]'
    browser.click(example_2_link_selector)

    # Clicar no botão "Start" para iniciar o carregamento do conteúdo
    browser.click(start_button_selector)

    # Esperar até que o conteúdo carregado seja exibido
    page.wait_for_selector("#finish", state="visible")
    # Extrair o texto do conteúdo carregado
    loaded_content_example_2 = page.locator("#finish").inner_text().strip()
    print(f"Loaded content (Example 2): {loaded_content_example_2}")