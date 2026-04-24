import random 

def dice_roll():
    "Dice roll function - repeats when 6 is rolled, returns the sum of rolls"
    sum = 0
    while True:
        roll = random.randint(1, 6)
        sum += roll
        if roll != 6:
            break
    return sum

def teleports_generate(N):
    "Generates teleports for the game board"
    pair_sum = N // 2
    "valid positions for teleports are 2(start) to (N*N)-1 (finish)"
    valid_pos = list(range(2, N*N))
    random.shuffle(valid_pos)

    teleports = {}
    visual = {}

    # positive teleports (A,B,C...)
    for i in range(pair_sum):
        p1,p2 = valid_pos.pop(), valid_pos.pop()
        start, end = min(p1, p2), max(p1, p2)
        teleports[start] = end
        visual[start] = chr(65 + i)
    
    # negative teleports (a,b,c...)
    for i in range(pair_sum):
        p1,p2 = valid_pos.pop(), valid_pos.pop()
        start, end = min(p1, p2), max(p1, p2)
        teleports[start] = end
        visual[start] = chr(97 + i)
    
    return teleports, visual

def print_board(N, players_pos, tp_visual):
    "prints the game board with players and teleports"
    print("\n" + "=" * (N*5))

    for r in range(N):
        row_str = ""
        for i in range(N):
            # even rows go left to right, odd rows go right to left (snake pattern)
            if r % 2 == 0:
                pos = r * N + i + 1
            else:
                pos = r * N + (N - 1 - i) + 1
            
            players_here = [str(idx + 1) for idx, p in enumerate(players_pos) if p == pos]

            if players_here:
                symbol = ",".join(players_here) # if multiple players are on the same spot
            elif pos == 1:
                symbol = '+' # start
            elif pos == N * N:
                symbol = '*' # finish
            elif pos in tp_visual:
                symbol = tp_visual[pos] # teleport symbol
            else:
                symbol = '.'

            row_str += f"{symbol:>4}"
        print(row_str)
    print("=" * (N*5))

def game():
    # inputs
    size = int(input("Enter parameter N between 5-10 for board size (N*N)  : "))
    if size < 5 or size > 10:
        print("Invalid board size. Please enter a number between 5 and 10.")
        return
    
    num_players = int(input("Enter parameter K for number of players: "))
    if num_players < 1:
        print("There must be at least one player.")
        return
    
    finish = size * size
    players_pos = [1] * num_players # all players start at position 1
    teleports, visual = teleports_generate(size)

    print_board(size, players_pos, visual)

    # game loop
    for round in range(1, 101):
        for i in range(num_players):
            dice = dice_roll()
            new_pos = players_pos[i] + dice

            print(f"\nPlayer {i+1} rolled {dice}!")

            if new_pos > finish:
                print(f"Player {i+1} cannot move, needs exactly {finish - players_pos[i]} to win.")
                continue

            players_pos[i] = new_pos
            print(f"Player {i+1} moves to position {new_pos}.")

            if new_pos in teleports:
                to = teleports[new_pos]
                type = "positive" if visual[new_pos].isupper() else "negative"
                print(f"Player {i+1} hit a {type} teleport '{visual[new_pos]}' and moves to position {to}!")
                players_pos[i] = to
            
            print_board(size, players_pos, visual)

            if players_pos[i] == finish:
                print(f"Player {i+1} wins the game in round {round}!!! Congratulations!")
                return
    print("Game over! No winner after 100 rounds.")

if __name__ == "__main__":
    game()



