from random import randint as ri

def get_candy_bot(total: int, mode: bool):
    if mode == False:
        if total > 28:
            get_candies = ri(1,28)
            return get_candies
        else:
            get_candies = total
            return get_candies
    else:
        if total > 28:
            splitting = total//29
            if splitting == 1 and total < 58:
                if total > 29: get_candies = total-29
                else: get_candies = ri(1,28)
            else:
                get_candies = total - splitting*29
                if get_candies <= 0: get_candies += 28
            return get_candies
        else:
            get_candies = total
            return get_candies

def get_mode(mode):
    if mode == False: return 'простого'
    else: return 'сложного'