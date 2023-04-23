import redis

# Connexion à Redis via Docker
r = redis.Redis(host='173.18.0.4', port=6379)

# Importer des clés et leurs valeurs
r.set('cle5', 'valeur5')
