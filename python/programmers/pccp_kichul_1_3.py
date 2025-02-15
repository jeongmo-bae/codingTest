#https://school.programmers.co.kr/learn/courses/30/lessons/250135?language=python3

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    h0, m0, s0 = 0, 0, 0
    delta_h_per_hour = 360 / 12
    delta_h_per_min = 360 / (12 * 60)
    delta_h_per_sec = 360 / (12 * 60 * 60)
    delta_m_per_min = 360 / 60
    delta_m_per_sec = 360 / (60 * 60)
    delta_s_per_sec = 360 / 60
    start_degree_of_h = ((h1 - h0) * delta_h_per_hour + (m1 - m0) * delta_h_per_min + (s1 - s0) * delta_h_per_sec) % 360
    start_degree_of_m = ((m1 - m0) * delta_m_per_min + (s1 - s0) * delta_m_per_sec) % 360
    start_degree_of_s = ((s1 - s0) * delta_s_per_sec) % 360
    check_time = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)
    if start_degree_of_h == start_degree_of_s or start_degree_of_s == start_degree_of_m:
        answer += 1
    for time in range(1,check_time+1):
        before_degree_of_h = round((start_degree_of_h + (time-1) * delta_h_per_sec),10) %360
        before_degree_of_m = round((start_degree_of_m + (time-1) * delta_m_per_sec),10) %360
        before_degree_of_s = round((start_degree_of_s + (time-1) * delta_s_per_sec),10) %360
        now_degree_of_h = round((start_degree_of_h + time * delta_h_per_sec),10) %360
        now_degree_of_m = round((start_degree_of_m + time * delta_m_per_sec),10) %360
        now_degree_of_s = round((start_degree_of_s + time * delta_s_per_sec),10) %360

        if before_degree_of_h >= 354 and 354 <= before_degree_of_s < 360 :
            cond_h = (
                before_degree_of_h > before_degree_of_s
                and now_degree_of_h <= now_degree_of_s + 360
            )
        else :
            cond_h = (
                before_degree_of_h > before_degree_of_s
                and now_degree_of_h <= now_degree_of_s
            )
        if before_degree_of_m >= 354 and 354 <= before_degree_of_s < 360 :
            cond_m = (
                before_degree_of_m > before_degree_of_s
                and now_degree_of_m <= now_degree_of_s + 360
            )
        else :
            cond_m = (
                    before_degree_of_m > before_degree_of_s
                    and now_degree_of_m <= now_degree_of_s
            )
        cond_all = (
                cond_h
                and cond_m
                and (before_degree_of_h > before_degree_of_m)
                and (now_degree_of_h <= now_degree_of_m)
        )
        if cond_h:
            answer += 1
        if cond_m:
            answer += 1
        if cond_all:
            answer -= 1
#        print(f"""
#            time : {time}
#            answer : {answer}
#            before_degree_of_h : {before_degree_of_h}
#            before_degree_of_m : {before_degree_of_m}
#            before_degree_of_s : {before_degree_of_s}
#            now_degree_of_h : {now_degree_of_h}
#            now_degree_of_m : {now_degree_of_m}
#            now_degree_of_s : {now_degree_of_s}
#        """)
#        print(cond_h,cond_m,cond_all)

    return answer




