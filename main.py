from FizzBuzz import ArgumentError, FizzBuzz

def main():
  print('Jeu du FizzBuzz')
  print()
  partieEnCours = True
  while partieEnCours:
    inputAlice = input('Alice, entrez un nombre : ("stop" pour arrêter la partie) ')
    if inputAlice == 'stop':
      partieEnCours = False
      print("Merci d'avoir joué")
    else:
      try:
        print('Bob :', FizzBuzz.NombreVerificateur(inputAlice))
      except ArgumentError as e:
        print('Bob :', e.message)

if __name__ == '__main__':
  main()