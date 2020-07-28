T = int(input())
for i in range(T):
    no_of_activity, origin = input().split()
    no_of_laddu = 0
    for i in range(int(no_of_activity)):
        contest = input().split()
        if(contest[0] == 'CONTEST_WON'):
            if (int(contest[1])>20):
                no_of_laddu = no_of_laddu + 300
            else:
                no_of_laddu = no_of_laddu + 300 + 20 - int(contest[1])
        if(contest[0] == 'TOP_CONTRIBUTOR'):
            no_of_laddu = no_of_laddu + 300
        if(contest[0] == 'BUG_FOUND'):
            no_of_laddu = no_of_laddu + int(contest[1])
        if(contest[0] == 'CONTEST_HOSTED'):
            no_of_laddu = no_of_laddu + 50
            
    if(origin == 'INDIAN'):
        print( no_of_laddu // 200)
    else:
        print( no_of_laddu // 400)
