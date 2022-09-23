from confluent_kafka import Producer
import json
import ccloud_lib # Library not installed with pip but imported from ccloud_lib.py
import time
import pickle
import json
import requests
import pandas as pd
import io

CONF = ccloud_lib.read_ccloud_config("python.config")
TOPIC = "my_lime_07_16_topic" 

producer_conf = ccloud_lib.pop_schema_registry_params_from_config(CONF)
producer = Producer(producer_conf)

ccloud_lib.create_topic(CONF, TOPIC)

url_nb = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=1000&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes&refine.nom_arrondissement_communes=Paris"
r_nb = requests.get(url_nb)
velib_nb = r_nb.json()
try:
	while True:
		gathered = []
		for i in range(velib_nb['nhits']):
			code_station = velib_nb['records'][i]['fields']['stationcode']
			name = velib_nb['records'][i]['fields']['name']
			lat = velib_nb['records'][i]['fields']['coordonnees_geo'][0]
			lon = velib_nb['records'][i]['fields']['coordonnees_geo'][1]
			velos_dispo = velib_nb['records'][i]['fields']['numbikesavailable']
			quais_dispo = velib_nb['records'][i]['fields']['numdocksavailable']
			total = velib_nb['records'][i]['fields']['capacity']
			time_gmt = velib_nb['records'][i]['record_timestamp']    
			info =  {i: ''}
			info[i] = [code_station, name, lat, lon, velos_dispo, quais_dispo, total, time_gmt]
			gathered.append(info)
		df = pd.concat([pd.DataFrame(l) for l in gathered], axis=1).T#.reset_index()
		dictionary = {0: 'code_station', 1: 'name', 2:'latitude', 3:'longitude', 4:'velos_dispo', 5:'quais_dispo', 6:'total', 7: 'time_gmt'}
		df.rename(columns=dictionary, inplace=True)
		df['percentage_used'] = df.apply(lambda row: 0 if row['velos_dispo'] == 0\
			else 100 - round((row['velos_dispo'] / row['total'])*100,1), axis=1)
		df = df.astype({'code_station': 'int64', 'name': 'string', 'latitude': 'float64', 'longitude': 'float64', 'velos_dispo': 'int64', 'quais_dispo': 'int64', 'total':'int64','time_gmt':'datetime64[ns]', 'percentage_used':'float64'})
		dfjson = df.to_json(orient="split", force_ascii=False, index=False)

		record_key = "stations_availability"
		record_value = dfjson
		print("Producing record: {}\t{}".format(record_key, record_value), '\n\n')

		producer.produce(
		    TOPIC,
		    key=record_key,
	    	value=record_value,
		)
		time.sleep(1.2)

except KeyboardInterrupt:
    pass
finally:
    producer.flush() # Finish producing the latest event before stopping the whole script
