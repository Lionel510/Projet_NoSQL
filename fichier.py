import csv
import uuid
import redis

r = redis.Redis(host='173.18.0.2', port=6379)

with open ("/home/lionel/Téléchargements/archive/country_health_indicators_v3.csv", newline='') as file1:
    liste_ligne = csv.reader(file1)
    for ligne in liste_ligne:
        for mot in ligne:
            r.set(str(uuid.uuid4()), str(mot))
