from Services.browser_service import BrowserService

def run():
    browser = BrowserService(headless=False)
    page = browser.start_browser()

    page.goto("https://the-internet.herokuapp.com/checkboxes")

    # Encontra todos os checkboxes e clica neles
    checkboxes = page.locator("input[type='checkbox']")

    total = checkboxes.count()

    print(f"Total de checkboxes encontrados: {total}")

    for i in range(total):
        checkbox = checkboxes.nth(i)

        inicial_state = checkbox.is_checked()

        if not inicial_state:
            checkbox.check()
            print(f"Checkbox {i+1} marcado.")

            checkbox.uncheck()
            print(f"Checkbox {i+1} desmarcado.")
        else:
            checkbox.uncheck()
            print(f"Checkbox {i+1} desmarcado.")

            checkbox.check()
            print(f"Checkbox {i+1} marcado.")

        final_state = checkbox.is_checked()

        print(f"Estado final do checkbox {i+1}: {final_state}")

    browser.close_browser()