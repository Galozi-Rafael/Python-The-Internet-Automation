from playwright.sync_api import sync_playwright

# Classe responsável por gerenciar o navegador usando Playwright
class BrowserService:

    def __init__(self, headless=True):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self):
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