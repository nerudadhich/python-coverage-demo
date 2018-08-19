import json

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