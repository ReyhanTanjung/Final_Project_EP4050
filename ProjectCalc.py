line = list()
singleElement = list()
tasks = dict()
number = -1
fhand = open('cpm.txt')

for line in fhand:
    singleElement=(line.split(','))
    number += 1
    for i in range(len(singleElement)):
        tasks['task'+ str(singleElement[0])]= dict()
        tasks['task'+ str(singleElement[0])]['id'] = singleElement[0]
        tasks['task'+ str(singleElement[0])]['name'] = singleElement[1]
        tasks['task'+ str(singleElement[0])]['duration'] = singleElement[2]
        if(singleElement[3] != "\n"):
            tasks['task'+ str(singleElement[0])]['dependencies'] = singleElement[3].strip().split(';')
        else:
            tasks['task'+ str(singleElement[0])]['dependencies'] = ['-1']
        tasks['task'+ str(singleElement[0])]['ES'] = 0
        tasks['task'+ str(singleElement[0])]['EF'] = 0
        tasks['task'+ str(singleElement[0])]['LS'] = 0
        tasks['task'+ str(singleElement[0])]['LF'] = 0
        tasks['task'+ str(singleElement[0])]['TotalFloat'] = 0
        tasks['task'+ str(singleElement[0])]['FreeFloat'] = 0
        tasks['task'+ str(singleElement[0])]['IndependentFloat'] = 0
        tasks['task'+ str(singleElement[0])]['isCritical'] = False

for taskFW in tasks:
    if('-1' in tasks[taskFW]['dependencies']):
        tasks[taskFW]['ES'] = 1
        tasks[taskFW]['EF'] = (tasks[taskFW]['duration'])
    else:
        for k in tasks.keys():
            for dependencies in tasks[k]['dependencies']:
                if(dependencies != '-1' and len(tasks[k]['dependencies']) == 1):
                    tasks[k]['ES'] = int(tasks['task'+ dependencies]['EF']) +1
                    tasks[k]['EF'] = int(tasks[k]['ES']) + int(tasks[k]['duration']) -1
                elif(dependencies !='-1'):
                    if(int(tasks['task'+dependencies]['EF']) > int(tasks[k]['ES'])):
                        tasks[k]['ES'] = int(tasks['task'+ dependencies]['EF']) +1
                        tasks[k]['EF'] = int(tasks[k]['ES']) + int(tasks[k]['duration']) -1

aList = list()
for element in tasks.keys():
    aList.append(element)

bList = list()
while len(aList) > 0:
    bList.append(aList.pop())
    
for taskBW in bList:
    if(bList.index(taskBW) == 0):
        tasks[taskBW]['LF']=tasks[taskBW]['EF']
        tasks[taskBW]['LS']=tasks[taskBW]['ES']
        
    for dependencies in tasks[taskBW]['dependencies']:
        if(dependencies != '-1'):
            if(tasks['task'+ dependencies]['LF'] == 0):
                tasks['task'+ dependencies]['LF'] = int(tasks[taskBW]['LS']) -1
                tasks['task'+ dependencies]['LS'] = int(tasks['task'+ dependencies]['LF']) - int(tasks['task'+ dependencies]['duration']) +1
                tasks['task'+ dependencies]['TotalFloat'] = int(tasks['task'+ dependencies]['LF']) - int(tasks['task'+ dependencies]['EF'])
                tasks['task'+ dependencies]['FreeFloat'] = int(tasks['task'+ dependencies]['LS']) - int(tasks['task'+ dependencies]['ES']) - int(tasks['task'+ dependencies]['duration'])
                if(tasks['task'+ dependencies]['FreeFloat'] <= 0):
                    tasks['task'+ dependencies]['FreeFloat'] = 0
                tasks['task'+ dependencies]['IndependentFloat'] = int(tasks['task'+ dependencies]['LS']) - int(tasks['task'+ dependencies]['EF']) - int(tasks['task'+ dependencies]['duration'])
                if(tasks['task'+ dependencies]['IndependentFloat'] <= 0):
                    tasks['task'+ dependencies]['IndependentFloat'] = 0

            if(int(tasks['task'+ dependencies]['LF']) >int(tasks[taskBW]['LS']) ):
                tasks['task'+ dependencies]['LF'] = int(tasks[taskBW]['LS']) -1
                tasks['task'+ dependencies]['LS'] = int(tasks['task'+ dependencies]['LF']) - int(tasks['task'+ dependencies]['duration']) +1
                tasks['task'+ dependencies]['TotalFloat'] = int(tasks['task'+ dependencies]['LF']) - int(tasks['task'+ dependencies]['EF'])
                tasks['task'+ dependencies]['FreeFloat'] = int(tasks['task'+ dependencies]['LS']) - int(tasks['task'+ dependencies]['ES']) - int(tasks['task'+ dependencies]['duration'])
                if(tasks['task'+ dependencies]['FreeFloat'] <= 0):
                    tasks['task'+ dependencies]['FreeFloat'] = 0
                tasks['task'+ dependencies]['IndependentFloat'] = int(tasks['task'+ dependencies]['LS']) - int(tasks['task'+ dependencies]['EF']) - int(tasks['task'+ dependencies]['duration'])
                if(tasks['task'+ dependencies]['IndependentFloat'] <= 0):
                    tasks['task'+ dependencies]['IndependentFloat'] = 0


print('task id, task name, duration, ES, EF, LS, LF, TotalFloat,FreeFloat,IndependentFloat, isCritical')
for task in tasks:
    if(tasks[task]['TotalFloat'] == 0):
        tasks[task]['isCritical'] = True
    print(str(tasks[task]['id']) +', '+str(tasks[task]['name']) +', '+str(tasks[task]['duration']) +', '+str(tasks[task]['ES']) +', '+str(tasks[task]['EF']) +', '+str(tasks[task]['LS']) +', '+str(tasks[task]['LF']) +', '+str(tasks[task]['TotalFloat']) +', '+str(tasks[task]['FreeFloat']) +', '+str(tasks[task]['IndependentFloat']) +', '+str(tasks[task]['isCritical']))