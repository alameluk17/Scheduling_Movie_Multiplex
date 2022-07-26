
from django.shortcuts import render
from django.http import HttpResponse
from . import fpsd_project as project
from . import TTvisualgen as TT
# Create your views here.

global D
global l
D=[];MovieNames=[];RelDate=[];Bdg=[];Lng=[];Aud=[];IntScore=[];l=[]

def home(request):
    d=dict(request.POST)
    print(request.POST)
    D.append(d)
    print(D) #D is a list of dictionaries(input)
    
    for i in D:
        if i!={}:
            if i['NameOfMovie'][0] not in l:
                l.append(i['NameOfMovie'][0])

    return render(request,'blog/Movie_form.html',{'l':l})

def about(request):

    d=dict(request.POST)
    print(d)
    
    return render(request,'blog/about.html')

def output(request):
    if D[0]=={}:
        D.pop(0)
    for i in D:
        MovieNames.append(i['NameOfMovie'][0])
        Lng.append(i['Language'][0])
        RelDate.append(i['ReleaseDate'][0])
        Bdg.append(float(i['Budget'][0]))
        Aud.append(i['AudienceType'][0])
        IntScore.append(int(i['IntScore'][0]))
        Screens=['Scr1','Scr2','Scr3']
        Slots=['m','a','e']
        Screenings = ["Scr1_m", "Scr1_a","Scr1_e","Scr2_m","Scr2_a","Scr2_e", "Scr3_m", "Scr3_a", "Scr3_e"]

        ScreenScore= {'Scr1_m':5,'Scr1_a':6,'Scr1_e':9,'Scr2_m':4,'Scr2_a':5,'Scr2_e':8, 'Scr3_m': 7, 'Scr3_a': 8, 'Scr3_e': 9}
        MovieScore={}
        TotalScreens = 9
        HighestBdg = max(Bdg)
        for i in range(len(MovieNames)):
            MovieScore[MovieNames[i]]=project.TotalScore(MovieNames[i], RelDate[i], Lng[i], Bdg[i], Aud[i], IntScore[i], HighestBdg)
        MaxNoOfShows = project.TotalNoOfShows(MovieNames, list(MovieScore.values()), TotalScreens)
        TimeTables=project.BruteTimeTables(Screenings,MovieNames,MaxNoOfShows)
        Bt=project.Maximisation(TimeTables, ScreenScore, MovieScore)
        print(Bt)
        vals=list(Bt.values())
        ln=len(vals)
        TimeTable=TT.VisualTT(Bt,Screens,Slots)

    return render (request, 'blog/OUTPUT.html',{'TT':TimeTable,'Screens':Screens,'Slots':Slots})
