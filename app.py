from flask import Flask
from flask import jsonify
from resources.city import City
from resources.state import State

app = Flask(__name__)

@app.route('/city/list')
def get_cities():
    try:
        city = City()
        city_list = city.all()
        return jsonify(city_list)
    except Exception as e:
        app.logger.error('Error while city list %s', str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/city/<int:city_id>')
def get_city(city_id):
    try:
        city = City()
        city = city.get_city(city_id)
        return jsonify(city)
    except Exception as e:
        app.logger.error('Error while get city %s', str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/state/list')
def get_states():
    try:
        state = State()
        state_list = state.all()
        return jsonify(state_list)
    except Exception as e:
        app.logger.error('Error while state list %s', str(e))
        return jsonify({"error": str(e)}), 500

@app.route('/state/<int:state_id>')
def get_state(state_id):
    try:
        state = State()
        state = state.get_state(state_id)
        return jsonify(state)
    except Exception as e:
        app.logger.error('Error while get state %s', str(e))
        return jsonify({"error": str(e)}), 500