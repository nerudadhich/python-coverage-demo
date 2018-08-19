import json

class City:    
    """city details"""
    def all(self):
        try:
            with open('api_data/city.json') as f:
                data = json.load(f)
                return data
        except Exception as e:
            print e
            return []

    def get_city(self, city_id):
        pass