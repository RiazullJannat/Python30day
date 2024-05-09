def provideAccess(user):
    return {
        "username": user,
        "password": "admin"
    }
def runmatch():
    user = str(input("Write your username -: "))
    match user:
        case "RJ":
            print("Jannat do not have access to the database "
                  "only for the api code.")
        case 'Rk':
            print('Rk do not have access to the database '
                  'only for the frontend code.')

        case "rjannat":
            print('RJannat have the access to the database')
            print(provideAccess('Rjannat'))
        case _:
            print("You do not have any access to the code.")
if __name__ == '__main__':
    for _ in range(3):
        runmatch()