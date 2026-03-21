class ScraperService:

    @staticmethod
    def extract_table(page, table_selector="table"):
        
        table_data = []

        headers = page.locator(f"{table_selector} thead tr th")

        header_row = []

        for i in range(headers.count()):
            header_text = headers.nth(i).inner_text().strip()
            header_row.append(header_text)

        if header_row:
            table_data.append(header_row)

        rows = page.locator(f"{table_selector} tbody tr")

        for i in range(rows.count()):

            cells = rows.nth(i).locator("td")

            row_data = []

            for j in range(cells.count()):

                cell_text = cells.nth(j).inner_text().strip()

                row_data.append(cell_text)

            table_data.append(row_data)

        return table_data
    

    # Função para extrair texto dinâmico de um elemento usando um seletor
    @staticmethod
    def extract_dynamic_text(page, selector, locator):
        # Localiza o elemento usando o seletor e extrai o texto
        elements = page.locator(selector)
        
        content_data = []

        for i in range(elements.count()):

            element = elements.nth(i)

            img_src = element.locator("img").first.get_attribute("src") if element.locator("img").count() > 0 else None
            text_content = element.locator(locator).inner_text().strip() if element.locator(locator).count() > 0 else None

            content_data.append({
                "text": text_content,
                "image_src": img_src
            })

        return content_data
