import random
import time
import math
def player_draw(Deck,player_hand): #for debug
    values = {'2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':1}
    player_random_point = random.randrange(0,len(Deck)-1)
    player_true_point = values[Deck[player_random_point]] 
    player_hand.append(Deck[player_random_point])
    del Deck[player_random_point]
    return player_true_point

def dealer_draw(Deck,dealer_hand):  #for debug
    values = {'2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':1}
    dealer_random_point = random.randrange(0,len(Deck)-1)
    dealer_true_point = values[Deck[dealer_random_point]]
    dealer_hand.append(Deck[dealer_random_point])
    del Deck[dealer_random_point]
    return dealer_true_point

def End_game(Deck,dealer_point,dealer_hand):
    if dealer_point < 16:
        dealer_point += dealer_draw(Deck,dealer_hand)
        return End_game(Deck,dealer_point,dealer_hand)
    else:
        return dealer_point

def check_point(player_point,dealer_point,dealer_hand,challenge,Deck):
    values = {'2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':1}
    
    #เปิด Hide card และแสดงการเทียบแต้ม
    time.sleep(1)
    if challenge == "Black Jack":
        return f"<Action!> player Black Jack!🎯 >> bonus x1.5 of bet\n>> $ player Black Jack! |"
    elif challenge == "in": 
        if dealer_hand[0] == ('🔟' or'Jack' or 'Queen' or 'King'):
            return f"<Action!> player Insurance!🤝 >> dealer Black Jack! $ bonus+ x2 of bet\n>> $ Insurance! |"
        else:
            return f"<Action!> player Insurance!🤝 >> dealer no Black Jack! $ pay bet + 0.5 of bet\n>> $ Insurance! |"
    elif challenge == "sd":
        return f"<Action!> Surrender!🏳 >> Surrender and pay 1/2 of bet\n>> $ Surrender! |"
    elif challenge == "dd":
        if player_point > 21:   
            return f"<Action!> Double Down!📌 >> add last card and bet x2\n>> $ player busted! |"
        elif dealer_point > 21:    
            return f"<Action!> Double Down!📌 >> add last card and bet x2\n>> $ dealer busted! |"
        elif player_point > dealer_point:
            return f"<Action!> Double Down!📌 >> add last card and bet x2\n>> $ player win! |"
        elif dealer_point > player_point:
            return f"<Action!> Double Down!📌 >> add last card and bet x2\n>> $ dealer win! |"
        elif dealer_point == player_point:
            return f"<Action!> Double Down!📌 >> add last card and bet x2\n>> $ player and dealer push! |"
    elif challenge == "s" or challenge == "h":
        if player_point > 21:   
            return f">> $ player busted! |"
        elif dealer_point > 21:    
            return f">> $ dealer busted! |"
        elif player_point > dealer_point:
            return f">> $ player win! |"
        elif dealer_point > player_point:
            return f">> $ dealer win! |"
        elif dealer_point == player_point:
            return f">> $ player and dealer push! |"

Chips = 1000
while True:
    values = {'2️⃣':2, '3️⃣':3, '4️⃣':4, '5️⃣':5, '6️⃣':6, '7️⃣':7, '8️⃣':8, '9️⃣':9, '🔟':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':1}
    Deck = ['2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟', 'Jack', 'Queen', 'King', 'Ace'] #เดี๋ยวเปลี่ยนไปใช้ไฟล์รูปภาพแทน
    Deck = random.sample(Deck,len(Deck))
    player_hand = []
    dealer_hand = []
    player_point = 0
    dealer_point = 0
    bet = 0
    challenge =  input("Do you want to play \"Black jack\"? plese enter < yes / no >: ") #ถามว่าเล่นไหม
    if  challenge.lower() == "yes":
        #bet = bet_func(Chips)
        print("Draw a card!")
        #สุ่มไพ่2ใบแรก
        player_point += player_draw(Deck,player_hand)
        dealer_point += dealer_draw(Deck,dealer_hand)
        player_point += player_draw(Deck,player_hand)
        dealer_point += dealer_draw(Deck,dealer_hand)

        #แสดงไพ่ในการเล่นรอบแรก
        print(f"---> Card in player's hand:",end=" ")
        for i in player_hand:
            print(i,end=" ")
        print(" ")
        print("---> Card in dealer's hand: [Hide]",end=" ")
        for i in range(1,len(dealer_hand)):
            print(dealer_hand[i],end=" ")
        print(" ")
        print(f"#Total-point# >> player : {player_point} | dealer : [Hide] + {dealer_point - values[dealer_hand[0]]}\n")
        time.sleep(1)
        
        if ('🔟' in player_hand or 'Jack' in player_hand or 'Queen' in player_hand or 'King'in player_hand) and "Ace" in player_hand: #กรณีป๊อก black jack ตั้งแต่2ใบแรกจะชนะทันที
            challenge = "Black Jack"
            dealer_point = End_game(Deck,dealer_point,dealer_hand)
            print(f"---> Card in player's hand:",end=" ")
            for i in player_hand:
                print(i,end=" ")
            print(" ")
            print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
            for i in range(1,len(dealer_hand)):
                print(dealer_hand[i],end="  ")
            print(" ")
            print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
            time.sleep(1)
            check_point(player_point,dealer_point,dealer_hand,challenge,Deck)
            #Chips = check_bet(Chips,bet,player_point,dealer_point,challenge,player_hand,dealer_hand)
            #print("💳 Chips:",Chips,"bez's chips")

        elif dealer_hand[1] == "Ace":
            print("Play decision...")
            challenge = input(f"dealer has \"Ace\" player can use <Action!> Insurance!🤝 >> if Hide card is 10 point then dealer black jack, player will take bonus+ x2 of bet\nplese enter < in / no > ")
            if  challenge.lower() == "in":
                dealer_point = End_game(Deck,dealer_point,dealer_hand)   
                print(f"---> Card in player's hand:",end=" ")
                for i in player_hand:
                    print(i,end=" ")
                print(" ")
                print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
                for i in range(1,len(dealer_hand)):
                    print(dealer_hand[i],end="  ")
                print(" ")
                print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
                time.sleep(1) 
                check_point(player_point,dealer_point,dealer_hand,challenge,Deck)
                #Chips = check_bet(Chips,bet,player_point,dealer_point,challenge,player_hand,dealer_hand)
                #print("💳 Chips:",Chips,"bez's chips")
            else:
                print("Play decision...")
                challenge = input("<Action!> Hit!🗡 >> add one card | plese enter < h >\
                    \n<Action!> Stand!🗿 >> no add | plese enter < s >\
                    \n<Action!> Double Down!📌 >> add last card and bet x2 | plese enter < dd >\
                    \n<Action!> Surrender!🏳 >> Surrender and pay 1/2 of bet | plese enter < sd >\
                    \nPlay decision >> ")
                if challenge == "dd":
                    player_point += player_draw(Deck,player_hand)
                elif challenge == "h":
                    player_point += player_draw(Deck,player_hand)
                    time.sleep(1)
                    print("")
                    print(f"---> Card in player's hand:",end=" ")
                    for i in player_hand:
                        print(i,end=" ")
                    print(" ")
                    print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
                    for i in range(1,len(dealer_hand)):
                        print(dealer_hand[i],end="  ")
                    print(" ")
                    print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
                    for i in range(999):
                        if player_point <= 21:
                            challenge = input("<Action!> Hit!🗡 >> add one card | plese enter < h >\n<Action!> Stand!🗿 >> no add | plese enter < s >\nPlay decision >> ")
                            if challenge == "h":
                                player_point += player_draw(Deck,player_hand)
                                time.sleep(1)
                                print("")
                                print(f"---> Card in player's hand:",end=" ")
                                for i in player_hand:
                                    print(i,end=" ")
                                print(" ")
                                print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
                                for i in range(1,len(dealer_hand)):
                                    print(dealer_hand[i],end="  ")
                                print(" ")
                                print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
                            elif challenge == "s":
                                break
                            else:
                                continue
                        else:
                            break
                time.sleep(1)
                dealer_point = End_game(Deck,dealer_point,dealer_hand)
                print("")   
                print(f"---> Card in player's hand:",end=" ")
                for i in player_hand:
                    print(i,end=" ")
                print(" ")
                print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
                for i in range(1,len(dealer_hand)):
                    print(dealer_hand[i],end="  ")
                print(" ")
                print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
                time.sleep(1)
                dealer_point = End_game(Deck,dealer_point,dealer_hand)
                check_point(player_point,dealer_point,dealer_hand,challenge,Deck)
                #Chips = check_bet(Chips,bet,player_point,dealer_point,challenge,player_hand,dealer_hand)
                #print("💳 Chips:",Chips,"bez's chips")
        else:
            print("Play decision...")
            challenge = input("<Action!> Hit!🗡 >> add one card | plese enter < h >\
                \n<Action!> Stand!🗿 >> no add | plese enter < s >\
                \n<Action!> Double Down!📌 >> add last card and bet x2 | plese enter < dd >\
                \n<Action!> Surrender!🏳 >> Surrender and pay 1/2 of bet | plese enter < sd >\
                \nPlay decision >> ")
            if challenge == "dd":
                player_point += player_draw(Deck,player_hand)
            elif challenge == "h":
                player_point += player_draw(Deck,player_hand)
                time.sleep(1)
                print("")
                print(f"---> Card in player's hand:",end=" ")
                for i in player_hand:
                    print(i,end=" ")
                print(" ")
                print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
                for i in range(1,len(dealer_hand)):
                    print(dealer_hand[i],end="  ")
                print(" ")
                print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
                for i in range(999):
                    if player_point <= 21:
                        challenge = input("<Action!> Hit!🗡 >> add one card | plese enter < h >\n<Action!> Stand!🗿 >> no add | plese enter < s >\nPlay decision >> ")
                        if challenge == "h":
                            player_point += player_draw(Deck,player_hand)
                            time.sleep(1)
                            print("")
                            print(f"---> Card in player's hand:",end=" ")
                            for i in player_hand:
                                print(i,end=" ")
                            print(" ")
                            print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
                            for i in range(1,len(dealer_hand)):
                                print(dealer_hand[i],end="  ")
                            print(" ")
                            print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
                        elif challenge == "s":
                            break
                        else:
                            continue
                    else:
                        break
            time.sleep(1)
            dealer_point = End_game(Deck,dealer_point,dealer_hand)   
            print("")
            print(f"---> Card in player's hand:",end=" ")
            for i in player_hand:
                print(i,end=" ")
            print(" ")
            print(f"---> Card in dealer's hand: {dealer_hand[0]}",end=" ")
            for i in range(1,len(dealer_hand)):
                print(dealer_hand[i],end="  ")
            print(" ")
            print(f"#Total-point# >> player : {player_point} | dealer : {dealer_point}")
            time.sleep(1)
            dealer_point = End_game(Deck,dealer_point,dealer_hand)
            print(check_point(player_point,dealer_point,dealer_hand,challenge,Deck))
            #Chips = check_bet(Chips,bet,player_point,dealer_point,challenge,player_hand,dealer_hand)
            #print("💳 Chips:",Chips,"bez's chips")
    elif challenge.lower() == "no": #กรณีเราตอบไม่เล่น
        print("see you later...")
    else:
        print(end="\n")#กรณีที่เราตอบนอกเหนทอจาก yes,no,y,n จะขึ้้นข้อความให้กรอกใหม่
        print("I don't understand, please enter again.")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")    