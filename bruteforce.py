second_password = "secret123"
file_password = "filepass"

def request_secondary_password():
    attempts = 0
    while attempts < 5:
        entered_password = input("Entrez le mot de passe secondaire (tentative {}/5): ".format(attempts + 1))
        if entered_password == second_password:
            print("Mot de passe secondaire correct ! Vous pouvez maintenant accéder au fichier.")
            return True
        else:
            print("Mot de passe incorrect.")
            attempts += 1
    print("Vous avez épuisé vos tentatives pour le mot de passe secondaire.")
    return False

def request_file_password():
    attempts = 0
    while attempts < 3:
        entered_password = input("Entrez le mot de passe du fichier (tentative {}/3): ".format(attempts + 1))
        if entered_password == file_password:
            print("Mot de passe du fichier correct ! Accès accordé.")
            return True
        else:
            print("Mot de passe incorrect.")
            attempts += 1
    print("Vous avez épuisé vos tentatives pour le mot de passe du fichier.")
    return False

if request_secondary_password():
    if request_file_password():
        print("Vous avez ouvert le fichier avec succès.")
    else:
        print("Accès au fichier refusé.")
else:
    print("Accès refusé au système.")

if __name__ == '__main__':
    request_secondary_password()
    request_file_password()