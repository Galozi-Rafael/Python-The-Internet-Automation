from Services.browser_service import BrowserService

def run():
    
    browser = BrowserService(headless=False)

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/disappearing_elements")

    # Conta o número de elementos "Menu" presentes na página
    menu_elements_count = browser.count_elements("ul li a")

    print(f"Número de elementos 'Menu' presentes: {menu_elements_count}")

    # Verifica se o número de elementos "Menu" é igual a 5
    if menu_elements_count == 5:
        print("Teste passou: O número de elementos 'Menu' é igual a 5.")
    else:
        print("Teste falhou: O número de elementos 'Menu' não é igual a 5.")

    inner_text = []
    # Obtém o texto de cada elemento "Menu" presente na página
    for i in range(menu_elements_count):
        inner_text.append(page.locator("ul li a").nth(i).inner_text())
    print(f"Texto dos elementos 'Menu': {inner_text}")
