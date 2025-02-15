# https://school.programmers.co.kr/learn/courses/30/lessons/250137
def solution(bandage, health, attacks):
    answer = 0
    end_time_of_attack = attacks[-1][0] 
    continuous_time = 0
    nums_attack = attacks.__len__()
    attack_idx = 1
    now_health = health
    for now_time in range(1,end_time_of_attack+1) :
        if now_time < attacks[attack_idx-1][0] :
            continuous_time += 1
            if continuous_time == bandage[0] :
                continuous_time = 0
                now_health = now_health + bandage[1] + bandage[2]
            else :
                now_health += bandage[1]
            
        else :
            now_health -= attacks[attack_idx-1][1]
            continuous_time = 0
            attack_idx +=1
                    
        if now_health <= 0 : 
            answer = -1
            print(f"{now_time} : health = {now_health} / continuous_time = {continuous_time} / answer = {answer}")
            break
        if now_health > health :
            now_health = health
        answer = now_health
        print(f"{now_time} : health = {now_health} / continuous_time = {continuous_time} / answer = {answer}")
    
    return answer

