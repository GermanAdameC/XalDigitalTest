import json
import requests

# conection to url
response = requests.get('https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow')
data = response.json()

# Variables a usar, inicializadas
ANSWER_ID = 'accepted_answer_id'
VIEW_COUNT = 'view_count'
CREATION_DATE = 'creation_date'
REPUTATION = 'reputation'
IS_ANSWERED = 'is_answered'
OWNER = 'owner'
ID = 'id'
VAL = 'val'
ITEMS = 'items'

answered_true = 0
answered_false = 0
min_view = {VAL: data[ITEMS][0][VIEW_COUNT], ID: data[ITEMS][0][ANSWER_ID]}
old_date = {VAL: data[ITEMS][0][CREATION_DATE], ID: data[ITEMS][0][ANSWER_ID]}
new_date = {VAL: data[ITEMS][0][CREATION_DATE], ID: data[ITEMS][0][ANSWER_ID]}
high_reputation = {VAL: data[ITEMS][0][OWNER][REPUTATION], ID: data[ITEMS][0][ANSWER_ID]}
id_question = 0



def is_minor(targetValue, currectValue):
  if targetValue < currectValue:
    return True
  else: 
    return False

def is_bigger(targetValue, currectValue):
  if targetValue > currectValue:
    return True
  else: 
    return False


def equals(targetValue, currectValue):
  if targetValue == currectValue:
    return True
  else: 
    return False
 
# FOR principal

for item in data[ITEMS]:
  # 2- Obtener el número de respuestas contestadas y no contestadas
  if item[IS_ANSWERED] == True:
    answered_true += 1
  else:
    answered_false += 1
  
  # obtenemos un identificador para la "Respues"
  id_question = item[ANSWER_ID]
  
  
  # 3- Obtener la respuesta con menor número de vistas
  # asignamos el id de la pregunta para poder imprimir la "respuesta"
  if is_minor(item[VIEW_COUNT], min_view[VAL]):
    min_view[VAL] = item[VIEW_COUNT]
    min_view[ID] = id_question
  
  # 4- Obtener la respuesta más vieja y más actual
  if is_minor(item[CREATION_DATE], old_date[VAL]):
    old_date[VAL] = item[CREATION_DATE]
    old_date[ID] = id_question
  
  if is_bigger(item[CREATION_DATE], new_date[VAL]):
    new_date[VAL] = item[CREATION_DATE]
    new_date[ID] = id_question
  
  # 5- Obtener la respuesta del owner que tenga una mayor reputación
  # if is_bigger(item[OWNER][REPUTATION], high_reputation[VAL]):
  #  high_reputation[VAL] = item[OWNER][REPUTATION]
  #  high_reputation[ID] = id_question


print("Preguntas contestadas:", answered_true)
print("\nPreguntas no contestadas:", answered_false, "\n")

  
for item in data[ITEMS]:
  if equals(item[ANSWER_ID], min_view[ID]):
    print("Cantidad de vistas de la 'Respuesta' con menor número de vistas:", min_view[VAL])
    print("\n'Respuesta' con menor número de vistas", item, "\n")

  if item[ANSWER_ID] == old_date[ID]:
    print("Fecha de la 'Respuesta' mas vieja:", old_date[VAL])
    print("\n'Respuesta' mas vieja:", item, "\n")
  
  if item[ANSWER_ID] == new_date[ID]:
    print("Fecha de la 'Respuesta' mas nueva:", new_date[VAL])
    print("\n'Respuesta' mas nueva:", item, "\n")
  
  # if item[ANSWER_ID] == high_reputation[ID]:
  #  print("Reputación mas alta de un Owner", high_reputation[VAL])
  #  print("\n'Respuesta' con mayor reputación del owner", item, "\n")
