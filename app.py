import json
from flask import Flask, render_template
from driver import find_lexical_match, find_closest_cities

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)

# list of city data (as a list)
# dictionary of city data (indexed by city id)
data_list = []
data_dict = {}

'''
Loads webpage
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    parse_file('cities1000.txt')
    return render_template('index.html')

'''
Returns lexical matches by city name
'''
@app.route('/findLexicalMatch/<word>', methods=['GET', 'POST'])
def find_match(word):
    return find_lexical_match(word, data_dict, data_list)

'''
Returns closest k cities by distance 
'''
@app.route('/findClosestCities/<cityId>/<numCities>', methods=['GET', 'POST'])
def find_cities(cityId, numCities):
    print(cityId, int(numCities));
    closest_cities = find_closest_cities(cityId, int(numCities), data_dict, data_list)
    return json.dumps(closest_cities)

def parse_file(filename):
	'''
	The main 'geoname' table has the following fields :
	---------------------------------------------------
	geonameid         : integer id of record in geonames database
	name              : name of geographical point (utf8) varchar(200)
	asciiname         : name of geographical point in plain ascii characters, varchar(200)
	alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
	latitude          : latitude in decimal degrees (wgs84)
	longitude         : longitude in decimal degrees (wgs84)
	feature class     : see http://www.geonames.org/export/codes.html, char(1)
	feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
	country code      : ISO-3166 2-letter country code, 2 characters
	cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
	admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
	admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80) 
	admin3 code       : code for third level administrative division, varchar(20)
	admin4 code       : code for fourth level administrative division, varchar(20)
	population        : bigint (8 byte int) 
	elevation         : in meters, integer
	dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
	timezone          : the iana timezone id (see file timeZone.txt) varchar(40)
	modification date : date of last modification in yyyy-MM-dd format
	'''
	with open(filename) as f:
		lines = f.readlines()
		for line in lines: 
			line_list = line.split('\t')
			data_list.append(line_list)
			city_id = line_list[0]
			data_dict[city_id] = line_list


if __name__ == '__main__':
    app.run()
