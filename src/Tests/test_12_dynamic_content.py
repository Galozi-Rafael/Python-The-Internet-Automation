from Services.browser_service import BrowserService
from Services.scraper_service import ScraperService

def run():
    browser_service = BrowserService(headless=False)
    page = browser_service.start_browser()

    page.goto("https://the-internet.herokuapp.com/dynamic_content")

    scraper_service = ScraperService()
    content_data = scraper_service.extract_dynamic_text(page, "#content > .row", "div.large-10.columns")

    for item in content_data:
        print(f"Text: {item['text']}")
        print(f"Image Source: {item['image_src']}")
        print("-" * 40)

    page.reload()

    content_data_after_reload = scraper_service.extract_dynamic_text(page, "#content > .row", "div.large-10.columns")
    
    for item in content_data_after_reload:
        print(f"Text: {item['text']}")
        print(f"Image Source: {item['image_src']}")
        print("-" * 40)

    if content_data != content_data_after_reload:
        print("O conteúdo dinâmico mudou após o reload da página.")
    else:
        print("O conteúdo dinâmico permaneceu o mesmo após o reload da página.")

    browser_service.close_browser()