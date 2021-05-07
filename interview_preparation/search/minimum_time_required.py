def minTime(machines, goal):
    num_of_machines = len(machines)
    l = min(machines) * goal // num_of_machines
    r = max(machines) * goal // num_of_machines
    
    while l < r:
        days = (l + r) // 2
        
        if sum(days // m for m in machines) < goal:
            l = days + 1
        else:
            r = days
    
    return r


if __name__ == '__main__':

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)
    
    print(ans)