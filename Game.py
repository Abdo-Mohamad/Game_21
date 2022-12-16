import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4

option= input("Hola y bienvenido al juego del 21, selecciona s para jugar, r para ver las reglas o q para salir: ")


def deal(deck,numCards):
    hand = []
    if numCards== 2 :
        random.shuffle(deck)
        for i in range(numCards):
                card = deck.pop()
                if card == 11:card = "J"
                if card == 12:card = "Q"
                if card == 13:card = "K"
                if card == 14:card = "A"
                hand.append(card)
        return hand
    else:
        for i in range(numCards):
                    card = deck.pop()
                    if card == 11:card = "J"
                    if card == 12:card = "Q"
                    if card == 13:card = "K"
                    if card == 14:card = "A"
                    hand.append(card)
        return hand
while option:
    if option == "s":

        
        while True:
                print("Has seleccionado jugar")
                # time.sleep(1)
                print("Mezclando baraja.")
                # time.sleep(1)
                print("Mezclando baraja..")
                # time.sleep(1)
                print("Mezclando baraja...")
                # time.sleep(1)
                print("Terminado")
                player_hand = deal(deck,2)
                print(player_hand)
                
                

                # reserva = str(numero) + str(deal(deck))
                # numero = 0
                # # time.sleep(2)

                seguir = input("Si quieres robar pulsa r, si te quieres rendir pulsa f: ")
                if seguir == "r" :
                    print("aqui estamos")
                    test = deal(deck,1)
                    print(player_hand)
                    test.append(player_hand)
                    print(test)

                    break
                elif seguir == "f":
                    print("la consola ")
                    break
                else:
                    print("exet")
                exit()
        break    
    elif option == "r":

            print("Estas son las reglas: ")
            break
    elif option == "q":
            print("Hasta luego")
            exit()

    else:
        option = input(
            "Lo siento, las unicas opciones son s para jugar, r para ver las reglas o q para salir, selecciona 1: ")