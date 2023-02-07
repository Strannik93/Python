from random import randint as ri
import text

total = {}
total_pvp = {}

def get_candy_bot(total_id: int, mode: bool):
    if mode == False:
        if total_id > 28:
            get_candies = ri(1,28)
            return get_candies
        else:
            get_candies = total_id
            return get_candies
    else:
        if total_id > 28:
            splitting = total_id//29
            if splitting == 1 and total_id < 58:
                if total_id > 29: get_candies = total_id-29
                else: get_candies = ri(1,28)
            else:
                get_candies = total_id - splitting*29
                if get_candies <= 0: get_candies += 28
            return get_candies
        else:
            get_candies = total_id
            return get_candies

def check_win(total_id, first_name):
    if total_id[0] == 0:
        new_text = text.check_win_text(first_name)
        return False, new_text
    else:
        return True, ''

def check_candy(total_id, candy, pvp = False):
    if total_id[0] < 28:
        if int(candy) <= total_id[0]:
            if pvp:
                return True, text.surplus_pvp_text(total_id[0] - int(candy),total_id[2],total_id[4],int(candy),total_id[5])
            else:
                return True, text.surplus_text(total_id[0] - int(candy))
        else:
            return False, text.error_1_max(total_id[0])
    else:
        if 0 < int(candy) < 29:
            if pvp:
                return True, text.surplus_pvp_text(total_id[0] - int(candy),total_id[2],total_id[4],int(candy),total_id[5])
            else:
                return True, text.surplus_text(total_id[0] - int(candy))
        else:
            return False, text.error_1_28