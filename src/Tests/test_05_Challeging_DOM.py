from Services.browser_service import BrowserService
from Services.excel_service import ExcelService
from Services.scraper_service import ScraperService
from Services.canvas_service import CanvasService

def run():

    browser = BrowserService(headless=False)
    page = browser.start_browser()

    CanvasService.inject_canvas_listener(page)

    page.goto("https://the-internet.herokuapp.com/challenging_dom")

    canvas_text = CanvasService.get_canvas_text(page)
    print(f"Texto capturado do canvas: {canvas_text}")

    page.click(".button")

    page.click(".button.alert")

    page.click(".button.success")

    table_data = ScraperService.extract_table(page)

    excel_service = ExcelService()

    excel_service.save_to_excel(table_data, r"Data\challenging_dom_table.xlsx")

    browser.close_browser()






