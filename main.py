import phonenumbers
from phonenumbers import carrier, geocoder

def numChecker(phone):
    info = []
    numero = phonenumbers.parse(phone)
    info.append(geocoder.description_for_number(numero,"es"))
    info.append(carrier.name_for_number(numero,"es"))
    return info

phone = input("digite su numero telefonico: ")
print(numChecker(phone))
