from flask import Flask
from flask import jsonify
from resources.city import City

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