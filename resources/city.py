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
        try:
            with open('api_data/city.json') as f:
                data = json.load(f)
                for city in data:
                    print city, city_id
                    if(city["id"] == city_id):
                        return city
                return {}
        except Exception as e:
            print e
            return {}