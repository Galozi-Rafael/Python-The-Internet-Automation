import requests

class HttpService:

    def get_status_code(self, url:str) -> int:
        try:
            response = requests.get(url)
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {url}: {e}")
            return None