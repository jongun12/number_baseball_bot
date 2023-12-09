import math

# 입력 추측한 수와 정답 출력 스트라이크 볼
def check(guess,ans):
    S = 0
    B = 0
    for i in range(len(guess)):
        if guess[i] == ans[i]:
            S += 1
        elif guess[i] in ans:
            B += 1
    return [S,B]

# 모든 숫자를 대입해 모든 결과 구하기(정보가치 정도, 가장 적합한 숫자)
def find_the_highest_value(all_num,possible_num):
    po_num_value = []
    for i in all_num:
        all_check = [0,0,0,0,0,0,0,0,0,0]
        for j in possible_num:
            ch = check(i, j)
            a = 0
            if ch[0] == 0:
                a += 0
            elif ch[0] == 1:
                a += 4
            elif ch[0] == 2:
                a += 7
            elif ch[0] == 3:
                a += 9
            a += ch[1]
            all_check[a] += 1
        E = 0
        for j in all_check:
            p = j/len(possible_num)
            if p != 0:
                E += p*math.log2(1/p)
        po_num_value.append(E)
    highst_val = max(po_num_value)
    highst_index = [i for i,v in enumerate(po_num_value) if v==highst_val]
    highst_num = []
    for i in highst_index:
        highst_num.append(all_num[i])
    highst_po_num = []
    for i in highst_num:
        if i in possible_num:
            highst_po_num.append(i)
    if highst_po_num:
        return highst_po_num[0], po_num_value
    else:
        return highst_num[0], po_num_value

# condition 추가 하기
def add_condition(condition,add_con,ans):
    S = check(add_con, ans)[0]
    B = check(add_con, ans)[1]
    condition.append([add_con,S,B])

# condition(조건)이 들어왔을 때 possible_num 업데이트
def upda_po_num(last_condition,possible_num):
    remove_num = []
    for i in possible_num:
        if check(i, last_condition[0]) != last_condition[1:3]:
            remove_num.append(i)
    for i in remove_num:
        possible_num.remove(i)


# score 리턴
def game(ans):
    condition = []
    possible_num = []
    all_num = []
    # 처음 possible_num에 모두 경우 넣기
    for i in range(1,10):
        for j in range(1,10):
            if i != j:
                for k in range(1,10):
                    if i != k and j != k:
                        all_num.append([i,j,k])
                        possible_num.append([i,j,k])
    score = 0
    while True:
        score += 1
        guess = find_the_highest_value(all_num, possible_num)[0]
        add_condition(condition,guess,ans)
        if condition[-1][1] == 3:
            return score
        upda_po_num(condition[-1], possible_num)
        