import json
from resources.city import City
class State:    
    """city details"""
    def all(self):
        try:
            with open('api_data/state.json') as f:
                data = json.load(f)
                return data
        except Exception as e:
            return []

    def get_state(self, state_id):
        try:
            with open('api_data/state.json') as f:
                data = json.load(f)
                for state in data:
                    if(state["id"] == state_id):
                        return state
                return {}
        except Exception as e:
            return {}

    def get_cities_of_state(self, state_id):
        try:
            with open('api_data/state_city_map.json') as f:
                data = json.load(f)
                city_id_list = data[str(state_id)]
                city_list = []
                city = City()
                for city_id in city_id_list:
                    city_list.append(city.get_city(city_id))
                return city_list
        except Exception as e:
            return []