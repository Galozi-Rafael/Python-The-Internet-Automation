from Services.browser_service import BrowserService

def run():
    
    # Cria uma instância do BrowserService com headless=False para visualizar o navegador
    browser = BrowserService(headless=False)

    # Inicia o navegador e obtém a página para interagir
    page = browser.start_browser()

    # Navega para a página de teste de A/B Test
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")

    # Clica no botão "Add Element" 5 vezes para adicionar 5 elementos
    for _ in range(5):
        browser.click("button[onclick='addElement()']")

    # Conta o número de elementos "Delete" presentes na página
    delete_buttons_count = browser.count_elements("button[onclick='deleteElement()']")
    
    print(f"Número de botões 'Delete' presentes: {delete_buttons_count}")

    # Verifica se o número de botões "Delete" é igual a 5
    if delete_buttons_count == 5:
        print("Teste passou: O número de botões 'Delete' é igual a 5.")
    else:
        print("Teste falhou: O número de botões 'Delete' não é igual a 5.")

    for i in range(delete_buttons_count):
        browser.click("button[onclick='deleteElement()']")

    final_count = browser.count_elements("button[onclick='deleteElement()']")
    print(f"Número de botões 'Delete' após clicar para remover: {final_count}")

    if final_count == 0:
        print("Teste passou: Todos os botões 'Delete' foram removidos.")
    else:
        print("Teste falhou: Nem todos os botões 'Delete' foram removidos.")

    browser.close_browser()