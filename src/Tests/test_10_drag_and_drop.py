from Services.browser_service import BrowserService

def run():

    browser = BrowserService(headless=False)

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/drag_and_drop")

    box_a_selector = "#column-a"
    box_b_selector = "#column-b"

    print("Arrastando o Box A para o Box B...")
    print(f"Antes do arraste: Box A - {page.locator(box_a_selector).inner_text()}, Box B - {page.locator(box_b_selector).inner_text()}")

    page.wait_for_timeout(1000)  # Aguarda um curto período para garantir que a página esteja pronta para a ação de arrastar e soltar
    
    page.drag_and_drop(box_a_selector, box_b_selector)

    page.wait_for_timeout(1000)  # Aguarda um curto período para garantir que a ação de arrastar e soltar seja concluída

    print(f"Depois do arraste: Box A - {page.locator(box_a_selector).inner_text()}, Box B - {page.locator(box_b_selector).inner_text()}")

    print("Arrastando o Box B para o Box A...")
    print(f"Antes do arraste: Box A - {page.locator(box_a_selector).inner_text()}, Box B - {page.locator(box_b_selector).inner_text()}")

    page.drag_and_drop(box_b_selector, box_a_selector)

    page.wait_for_timeout(1000)  # Aguarda um curto período para garantir que a ação de arrastar e soltar seja concluída

    print(f"Depois do arraste: Box A - {page.locator(box_a_selector).inner_text()}, Box B - {page.locator(box_b_selector).inner_text()}")