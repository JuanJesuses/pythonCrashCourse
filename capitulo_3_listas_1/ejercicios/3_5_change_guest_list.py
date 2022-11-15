people_dinners = ['andrés iniesta', 'arquímedes', 'aristóteles']

message1 = f'Hola {people_dinners[0]}, ¿te vienes a cenar?'
message2 = f'Hola {people_dinners[1]}, ¿te vienes a cenar?'
message3 = f'Hola {people_dinners[2]}, ¿te vienes a cenar?'

print(message1,'\n',message2,'\n',message3)

print(f'Al final, {people_dinners[1].title()} no va a poder asistir.')

people_dinners[1] = 'stephen hawkings'

message1 = f'Hola {people_dinners[0].title()}, ¿te vienes a cenar?'
message2 = f'Hola {people_dinners[1].title()}, ¿te vienes a cenar?'
message3 = f'Hola {people_dinners[2].title()}, ¿te vienes a cenar?'

print(message1,'\n',message2,'\n',message3)