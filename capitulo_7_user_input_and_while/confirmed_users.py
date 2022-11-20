# Start whit users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each users until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    curren_users = unconfirmed_users.pop()

    print(f'Verfiying user: {curren_users.title()}')
    confirmed_users.append(curren_users)

# Display all confirmed users.
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())