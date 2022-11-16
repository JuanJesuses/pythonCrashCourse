# Utiliza el código de favorite_languages.py.
#
#     • Haz una lista de las personas que han hecho la encuesta.
#     Incluye algunos nombres que ya estén en el diccionario y otros que no lo estén.
#     • Recorre la lista de personas que han hecho la encuesta.
#     Si la han hecho, imprime un mensaje de agradecimiento por responder,
#     si no lo han hecho, imprime un mensaje invitándolas a hacerla.

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

persons = ['jen', 'guido', 'sarah', 'edward', 'richard', 'phil']

for person in persons:
    if person in favorite_languages.keys():
        print(f"Hey {person.title()}, thanks for responding the poll.")
    else:
        print(f"{person.title()}, what are you waiting for to respond fucking guy!")