import random


def sum_cards(people):
    sum1_ = 0
    ka = 0
    for i_ in people:
        if 's' in i_:
            continue
        else:
            if 'J' in i_ or 'Q' in i_ or 'K' in i_:
                sum1_ += 10
            elif 'A' not in i_:
                sum1_ += int(i_[:-1])
            else:
                ka += 1
        if people.index(i_) == len(people) - 1:
            for j in range(ka):
                if sum1_ < 10:
                    sum1_ += 11
                else:
                    sum1_ += 2
    return sum1_


def new_card(people, silent=False):
    suit_ = random.randint(0, 3)
    while len(deck[suit_]) == 0:
        suit_ = random.randint(0, 3)
    value_ = random.randint(0, len(deck[suit_]) - 1)
    people.append(deck[suit_][value_])
    deck[suit_].pop(value_)
    if silent:
        people[0] += 's'


def draw():
    print(f'денег: {money}')
    print(f'ставка: {bet}')
    for i_ in dealer:
        if 's' in i_:
            print('## ', end='')
        else:
            print(f'{i_} ', end='')
    print(f'\tsum:', sum_d)
    for i_ in player:
        print(f'{i_} ', end='')
    print(f'\tsum:', sum_p)


# =============================== #
# свой код с блекджеком и.. Кхем  #
#           правила:              #
#   при принятии ставок           #
# a - поставить все               #
#   при игре                      #
# h - еще карту                   #
# s - стоп                        #
# =============================== #

# deck = [
#     ['2 @', '3 @', '4 @', '5 @', '6 @', '7 @', '8 @', '9 @', '10 @', 'j @', 'q @', 'k @', 'a @'],
#     ['2 #', '3 #', '4 #', '5 #', '6 #', '7 #', '8 #', '9 #', '10 #', 'j #', 'q #', 'k #', 'a #'],
#     ['2 $', '3 $', '4 $', '5 $', '6 $', '7 $', '8 $', '9 $', '10 $', 'j $', 'q $', 'k $', 'a $'],
#     ['2 %', '3 %', '4 %', '5 %', '6 %', '7 %', '8 %', '9 %', '10 %', 'j %', 'q %', 'k %', 'a %']
# ]
GameOver = False
s1 = '♠'
s2 = '♥'
s3 = '♣'
s4 = '♦'

money = input('сколько вы взяли с собой в казино?\n')
while not money.isdigit():
    print('введите целое число')
    money = input('сколько вы взяли с собой в казино?\n')
money = int(money)

while not GameOver:
    deck = [
        [f'2{s1}', f'3{s1}', f'4{s1}', f'5{s1}', f'6{s1}', f'7{s1}', f'8{s1}', f'9{s1}', f'10{s1}',
         f'J{s1}', f'Q{s1}', f'K{s1}', f'A{s1}'],

        [f'2{s2}', f'3{s2}', f'4{s2}', f'5{s2}', f'6{s2}', f'7{s2}', f'8{s2}', f'9{s2}', f'10{s2}',
         f'J{s2}', f'Q{s2}', f'K{s2}', f'A{s2}'],

        [f'2{s3}', f'3{s3}', f'4{s3}', f'5{s3}', f'6{s3}', f'7{s3}', f'8{s3}', f'9{s3}', f'10{s3}',
         f'J{s3}', f'Q{s3}', f'K{s3}', f'A{s3}'],

        [f'2{s4}', f'3{s4}', f'4{s4}', f'5{s4}', f'6{s4}', f'7{s4}', f'8{s4}', f'9{s4}', f'10{s4}',
         f'J{s4}', f'Q{s4}', f'K{s4}', f'A{s4}']

    ]
    dealer = []
    player = []
    inp = ''

    # print(f'денег: {money}')
    # bet = input('ваша ставка:\n')
    # while not bet.isdigit() and bet != 'a' and bet != '0':
    #     print('некорректный ввод')
    #     print(f'денег: {money}')
    #     bet = input('ваша ставка:\n')
    # if bet == 'a':
    #     bet = money
    # else:
    #     bet = int(bet)
    # money -= bet

    print(f'денег: {money}')
    bet = input('ваша ставка:\n')
    while 1:
        if bet == 'a':
            bet = money
            break
        elif bet.isdigit():
            bet = int(bet)
            if bet < 0 or bet > money:
                bet = ''
                while not (bet.isdigit() or bet == 'a'):
                    print('некорректный ввод')
                    print(f'денег: {money}')
                    bet = input('ваша ставка:\n')
                else:
                    continue
            else:
                break
        else:
            while not (bet.isdigit() or bet == 'a'):
                print('некорректный ввод')
                print(f'денег: {money}')
                bet = input('ваша ставка:\n')
            else:
                continue
        print(f'денег: {money}')
        bet = input('ваша ставка:\n')
    money -= bet

    new_card(dealer, True)
    new_card(dealer)
    new_card(player)
    new_card(player)

    sum_p = sum_cards(player)
    sum_d = sum_cards(dealer)

    draw()
    if sum_p == 21:
        money += 1.5 * bet
        print('BLACKJACK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('')
        continue

    # ход игрока
    inp = input()
    while inp != 's':
        if inp == 'h':
            new_card(player)
        sum_p = sum_cards(player)
        draw()
        if sum_p > 21:
            # print('у вас перебор')
            break
        inp = input()

    # ход диллера
    dealer[0] = dealer[0][:-1]
    sum_d = sum_cards(dealer)
    if sum_p <= 21:
        while sum_d < 17:
            new_card(dealer)
            sum_d = sum_cards(dealer)
            if sum_d > 21:
                # print('у диллера перебор')
                break
        draw()

    if sum_p <= 21:
        if sum_d <= 21:
            if sum_p > sum_d:
                print('вы выиграли')
                money += bet * 2
            elif sum_p == sum_d:
                print('ничья')
                money += bet
            else:
                print('вы проиграли')
        else:
            print('вы выиграли из за перебора диллера')
            money += bet * 2
    else:
        print('вы проиграли из за перебора')

    if money == 0:
        print('вас вышвырнули из казино')
        break
        # вставить ту пикчу гд чела выпинывают из казино
print('''
у вас кончились деньги? от вас ушла жена? вы погрязли в долгах?
                        !!! НЕ БЕДА !!!
вы можете просто перевести как залог деньги нашей организации
и получить бесплатный беспроцентный бонус 9999999999999 тугриков на баланс
''')
