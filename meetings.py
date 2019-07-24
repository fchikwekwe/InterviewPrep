meetings= [(1, 4), (2, 3), (5, 7)]
# assume that times are ints 
# return int with num of meetings 

# at time 2.5: 2 meetings
# at time 4.5: 0 meetings
# at time 5.5: 1 meetings

# print('Hello')
# list of meetings (start, end)
# query different time and know how many meetings

"""
psuedocode: 
meetings = 0 
loop over the list of times
compare with start and end to see if its between 
    if yes, then increment meetings
return meetings 

pseudocode: 
start list
end list

start [1, 2, 3, 4], before, two values 
end [2, 3, 4, 5], after, two values

2.5 

6

start [1, 2, 5], two
end [4, 3, 7], 

[(1, start), (2, start), (3, end), (4, end), (5, start), (7, end)]

global count: 
1 - 1
2 - 2
5 - 1

[(1, 4), (2, 3), (5, 7)]

all_times = []
pseudocode: 
loop over the list of meetings
    first value = (time, start)
    second value =(time, end)
    append those to all_times 

target 
count = 0 
loop over all times: 
    check if time is greater than target: 
    if it is return count 
    if not: 
        if start: 
            increment count
        if end: 
            decrement count 
"""

def get_all_times(meetings):
    all_times = []
    for meeting in meetings:
        all_times.append((meeting[0], "start"))
        all_times.append((meeting[1], "end"))
    
    all_times = sorted(all_times) # n log n 
    
def num_meetings(times, target):    
    count = 0 
    for time in times: 
        if time[0] > target:
            return count
        else: 
            if time[1] == "start":
                count += 1
            else: 
                count -= 1
    return count

examples = # a list of targets
times = get_all_times(meetings)
for example in examples: 
    print(num_meetings(times, example))

