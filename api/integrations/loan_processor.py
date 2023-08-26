class RDStation:
    def __init__(self):
        self.base_url = "https://loan-processor.digitalsys.com.br/api/v1"
        self.headers = {
            'Authorization': f'Bearer {auth_response["access_token"]}',
            'Content-Type': 'application/json'
        }
        self.PARAMS = (('api_key', settings.RD_STATION_API_KEY),)