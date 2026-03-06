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