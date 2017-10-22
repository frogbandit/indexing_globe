import json
from flask import Flask, render_template
from driver import find_lexical_match, find_closest_cities

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

'''
Loads webpage
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

'''
Returns lexical matches by city name
'''
@app.route('/findLexicalMatch/<word>', methods=['GET', 'POST'])
def find_lexical_match(word):
    return find_lexical_match(word)

'''
Returns closest k cities by distance 
'''
@app.route('/findClosestCities/<cityId>/<numCities>', methods=['GET', 'POST'])
def find_closest_cities(cityId, numCities):
    return find_closest_cities(cityId, numCities)
    

if __name__ == '__main__':
    app.run()
