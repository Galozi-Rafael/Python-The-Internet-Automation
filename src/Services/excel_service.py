import pandas as pd

# Serviço para salvar dados em um arquivo Excel
class ExcelService:

    # Método para salvar dados em um arquivo Excel
    @staticmethod
    def save_to_excel(data, file_name):

        df = pd.DataFrame(data)

        df.to_excel(file_name, index=False)

        print(f"Tabela salva em {file_name} com sucesso!")