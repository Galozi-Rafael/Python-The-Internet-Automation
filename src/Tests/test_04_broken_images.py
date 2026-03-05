from Services.browser_service import BrowserService
from Services.http_service import HttpService
from urllib.parse import urljoin
def run():

    browser = BrowserService(headless=False)
    http = HttpService()

    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/broken_images")

    images = page.locator("img")

    total_images = images.count()
    print(f"Total de imagens encontradas: {total_images}")

    broken_images = []
    valid_images = []

    for i in range(total_images):
        src = images.nth(i).get_attribute("src")

        #full_url = page.url + src if src.startswith("/") else src
        full_url = urljoin("https://the-internet.herokuapp.com/", src)
        status_code = http.get_status_code(full_url)

        if status_code == 200:
            print(f"Imagem válida: {full_url} (Status Code: {status_code})")
            valid_images.append(full_url)
        else:
            print(f"Imagem quebrada encontrada: {full_url} (Status Code: {status_code})")
            broken_images.append(full_url)
            #print(f"Imagem quebrada encontrada: {full_url} (Status Code: {status_code})")

    print("\n====== RESULTADO FINAL ======")

    print(f"Total de imagens: {total_images}")
    print(f"Imagens válidas: {len(valid_images)}")
    print(f"Imagens quebradas: {len(broken_images)}")

    if broken_images:
        print("\nLista de imagens quebradas:\n")

        for img in broken_images:
            print(f"Imagem quebrada: {img}")
    else:
        print("Nenhuma imagem quebrada encontrada.")