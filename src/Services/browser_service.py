from playwright.sync_api import sync_playwright, Page

# Classe responsável por gerenciar o navegador usando Playwright
class BrowserService:

    def __init__(self, headless=True, username=None, password=None):
        self.headless = headless
        self.username = username
        self.password = password

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_browser(self) -> Page:
        # Inicia o motor do Playwright
        self.playwright = sync_playwright().start()
        # Lança o navegador chromium
        self.browser = self.playwright.chromium.launch(headless=self.headless)

        # Verifica se as credenciais de autenticação HTTP foram fornecidas
        if self.username and self.password:
            # Cria um contexto de navegador com autenticação HTTP se as credenciais forem fornecidas
            self.context = self.browser.new_context(
                http_credentials={"username": self.username, "password": self.password}
            )
        else:
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
        self.page.locator(selector).first.click()

    def right_click(self, selector):
        #Executa clique com botão direito no elemento.
        self.page.locator(selector).first.click(button="right")

    def count_elements(self, selector) -> int:
        # Conta o número de elementos que correspondem ao seletor
        return self.page.locator(selector).count()
    
    def drag_and_drop(self, source_selector, target_selector):
        # Realiza a ação de arrastar e soltar do elemento de origem para o elemento de destino
        self.page.locator(source_selector).drag_to(self.page.locator(target_selector))

    def close_browser(self):
        # Fecha o navegador e o motor do Playwright
        self.context.close()
        self.browser.close()
        self.playwright.stop()