people_dinners = ['andrés iniesta', 'arquímedes', 'aristóteles']

message1 = f'Hola {people_dinners[0]}, ¿te vienes a cenar?'
message2 = f'Hola {people_dinners[1]}, ¿te vienes a cenar?'
message3 = f'Hola {people_dinners[2]}, ¿te vienes a cenar?'

print(f'Hola {people_dinners[0].title()}, {people_dinners[1].title()} y {people_dinners[2].title()}.'
      f'\nHe encontrado una mesa más grande para cenar, así que vamos a ser tres invitados más.')

people_dinners.insert(0, 'stephen hawkings')
people_dinners.insert(2, 'richard stallman')
people_dinners.append('alan turing')

message1 = f'Hola {people_dinners[0].title()}, ¿te vienes a cenar?'
message2 = f'Hola {people_dinners[1].title()}, ¿te vienes a cenar?'
message3 = f'Hola {people_dinners[2].title()}, ¿te vienes a cenar?'
message4 = f'Hola {people_dinners[3].title()}, ¿te vienes a cenar?'
message5 = f'Hola {people_dinners[4].title()}, ¿te vienes a cenar?'
message6 = f'Hola {people_dinners[5].title()}, ¿te vienes a cenar?'

print('Siento mucho deciros que sólo puedo invitar a dos personas.')

invitado1 = people_dinners.pop(0)
print(f'Lo siento mucho {invitado1.title()}, no puedes venir a cenar.')
invitado2 = people_dinners.pop(1)
print(f'Lo siento mucho {invitado2.title()}, no puedes venir a cenar.')
invitado3 = people_dinners.pop(3)
print(f'Lo siento mucho {invitado3.title()}, no puedes venir a cenar.')
invitado4 = people_dinners.pop(2)
print(f'Lo siento mucho {invitado4.title()}, no puedes venir a cenar.')

print(f'Vosotros dos, {people_dinners[0].title()} y {people_dinners[1].title()}, podéis venir a la cena de mierda.')

del people_dinners[0]
del people_dinners[0]

print(people_dinners)
