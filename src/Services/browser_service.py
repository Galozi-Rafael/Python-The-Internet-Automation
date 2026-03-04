from playwright.sync_api import sync_playwright, Page

# Classe responsável por gerenciar o navegador usando Playwright
class BrowserService:

    def __init__(self, headless=True):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self) -> Page:
        # Inicia o motor do Playwright
        self.playwright = sync_playwright().start()
        # Lança o navegador chromium
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        # Cria um novo contexto de navegador
        self.context = self.browser.new_context()
        # Abre uma nova página no contexto do navegador
        self.page = self.context.new_page()
        # Retorna a página já pronta para uso
        return self.page
    
    def goto(self, url):
        # Navega para a URL especificada
        self.page.goto(url)

    def click(self, selector):
        # Clica no elemento identificado pelo seletor
        self.page.locator.click(selector)

    def count_elements(self, selector) -> int:
        # Conta o número de elementos que correspondem ao seletor
        return self.page.locator(selector).count()

    def close_browser(self):
        # Fecha o navegador e o motor do Playwright
        self.context.close()
        self.browser.close()
        self.playwright.stop()