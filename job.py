import os

token = os.getenv("SECRET_API_TOKEN")

print("Le secret est accessible :", token is not None)
print("Valeur :", token)







