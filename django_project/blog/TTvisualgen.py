
def VisualTT(timetable,screens,slots):
    Visualtt=[]
    for i in range(len(screens)):
        Visualtt.append([])
        for j in range(len(slots)):
            x=screens[i]+'_'+slots[j]
            Visualtt[i].append(timetable[x])
    return Visualtt



