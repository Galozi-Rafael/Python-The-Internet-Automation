from Services.browser_service import BrowserService
import pyautogui
import time

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()
    browser.goto("https://the-internet.herokuapp.com/exit_intent")

    page.wait_for_timeout(2000)  

    # Fazer o mouse sair da janela para acionar o pop-up de intenção de saída
    screen_width, screen_height = pyautogui.size()
    x = screen_width // 2
    y = screen_height // 2

    pyautogui.moveTo(x, 1, duration=0.3)
    time.sleep(2)
    

    # Esperar até que o modal seja exibido
    page.wait_for_selector("#ouibounce-modal", state="visible")

    # Extrair o texto do modal
    modal_text = page.locator("#ouibounce-modal .modal-body").inner_text().strip()
    print(f"Modal text: {modal_text}")

    # Clicar no botão "Close" para fechar o modal
    close_button_selector = "#ouibounce-modal .modal-footer p"

    browser.click(close_button_selector)

    # Verificar se o modal foi fechado
    modal_visible = page.locator("#ouibounce-modal").is_visible()

    if not modal_visible:
        print("Modal closed successfully.")
    else:
        print("Modal is still visible.")

    # Fechar o navegador
    browser.close_browser()