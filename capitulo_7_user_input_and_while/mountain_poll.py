responses = {}

# SEt a flag to indicate that polling is active.
pollin_active = True

while pollin_active:
    # Prompt for the person's name and response
    name = input("\n¿Cuál es tu nombre?: ")
    response = input("¿Qué montaña te gustaría escalar algún día?: ")

    # Store response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("¿Te gustaría dejar que otra persona responda (si/no)?: ")
    if repeat == 'no':
        pollin_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would you like to climb {response}")