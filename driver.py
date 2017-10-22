from math import sin, cos, sqrt, radians, asin

# to read each line of the txt file
def parse_file(filename):
	# list of city data (as a list)
	# dictionary of city data (indexed by city id)
	data_list = []
	data_dict = {}

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
	
	return [data_dict, data_list]

# returns the closest k cities by distance
def find_closest_cities(given_city_id, k, data_dict, data_list):
		given_city = data_dict[given_city_id]
		given_city_lat = float(given_city[4])
		given_city_lon = float(given_city[5])
		print(given_city[2])
		distance_list = []

		for city_list in data_list:
			city_lat = float(city_list[4])
			city_lon = float(city_list[5])
			city_id = city_list[0]
			city_name = city_list[2]
			dist = compute_distance(given_city_lat, given_city_lon, city_lat, city_lon)
			distance_list.append((dist, city_id, city_name))

		closest_k = sorted(distance_list, key=lambda x: x[0])[0:k]
		return closest_k
		
# From StackOverflow: finds distance between two latlng points using Haversine formula
def compute_distance(lat1, lon1, lat2, lon2):
	 # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

# Finds matches for the given word based on city name 
def find_lexical_match(word, data_dict, data_list):
	matches = []
	for city_list in data_list: 
		city_name = city_list[2]
		if word in city_name:
			matches.append(city_name)
	return matches

# # main program for testing purposes (uncomment to test)
# def main():
# 	# all cities with a population > 1000 or seats of adm div (ca 150.000), see 'geoname' table for columns
# 	parsed = parse_file('cities1000.txt')
# 	data_dict = parsed[0]
# 	data_list = parsed[1]
# 	print(find_closest_cities('3039154', 3, data_dict, data_list))
# 	print(find_lexical_match('North', data_dict, data_list))

# main()