# -*- coding: utf-8 -*-
"""FPSD_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gy6qc-thd4BT9R7sLR1IbHASl0ZgvQwQ
"""

from datetime import date

def TotalScore(NameOfMovie, RelDate, Lng, Bdg, Aud, IntScore, HighestBdg):
    NormBdg = (Bdg /HighestBdg)*30
    Today = date.today()
    Interest =0
    if Lng == 'Tamil':
        Interest=Interest+10
    elif Lng == 'English':
        Interest=Interest+9
    elif Lng == 'Hindi':
        Interest=Interest+8
    elif Lng == 'Telugu':
        Interest=Interest+7
    elif Lng == 'Malayalam':
        Interest=Interest+6.5
    else:
        Interest=Interest+5

    RelDate = date(int(RelDate[0:4]), int(RelDate[5:7]), int(RelDate[8:10]))
    
    Difference = Today - RelDate
    if (Difference.days) < 7:
        Interest=Interest+10
    elif (Difference.days) < 14:
        Interest=Interest+7
    elif (Difference.days) < 21:
        Interest=Interest+5
    else:
        Interest=Interest+2

    if (Aud=='U' or Aud=='U/A'):
        Interest=Interest+20
    else:
        Interest=Interest+10

    Interest=Interest+IntScore
    TotalScore= (Interest+NormBdg)/10
    return round(TotalScore, 4)


def TotalNoOfShows(MovieNames, Scores, TotalScreens):
    sum_of_scores= sum(Scores)
    ratio_factor =TotalScreens/sum_of_scores
    MaxNoOfShows=[]
    for j in range(len(MovieNames)):
      MaxNoOfShows.append(round(Scores[j]*ratio_factor))

    if sum(MaxNoOfShows) > TotalScreens:
      minimum=Scores.index(min(Scores))
      MaxNoOfShows[minimum]=MaxNoOfShows[minimum]-1
      
    elif sum(MaxNoOfShows) < TotalScreens:
      maximum=Scores.index(max(Scores))
      MaxNoOfShows[maximum]=MaxNoOfShows[maximum]+1

    return MaxNoOfShows

from itertools import product

def Maximisation(TimeTables, ScreenScore, MovieScore):
    for i in TimeTables:
        BestScore=1
        s=0
        BestTimeTable=dict()
        
        for screening,movie in i.items():
           
            s=s+MovieScore[movie]*ScreenScore[screening]
        if s>BestScore:
                BestScore=s
                BestTimeTable=i
    
    return(BestTimeTable)

def BruteTimeTables(Screens,Movies,MaxNoOfShows):
    temp = product(Movies, repeat = len(Screens))
    TimeTables = [{key : val for (key , val) in zip(Screens, ele)} for ele in temp]
    i=0;f=0

    while i< len(TimeTables):
        l=list(TimeTables[i].values())
        l2=[]
        j=0
        while j<len(Movies):
             l2.append(l.count(Movies[j]))
             j=j+1
        if l2 != MaxNoOfShows:
            del TimeTables[i]
        else:
            i=i+1
        
    return(TimeTables)
"""
MovieNames = ['Mov_1', 'Mov_2', 'Mov_3', 'Mov_4']
RelDate = ['2022-07-01', '2022-06-20', '2022-06-30', '2022-07-07']
Lng = ['Tamil', 'English', 'Hindi', 'Telugu']
Bdg=[40000000, 20000000, 30000000, 10000000]
Aud = ['U', 'U/A', 'U', 'A']
IntScore = [10, 14 , 29, 21]
HighestBdg = max(Bdg)

MovieScore={}
for i in range(len(MovieNames)):
    
    MovieScore[MovieNames[i]]=TotalScore(MovieNames[i], RelDate[i], Lng[i], Bdg[i], Aud[i], IntScore[i], HighestBdg)
  
print(MovieScore)
TotalScreens = 9
MaxNoOfShows = TotalNoOfShows(MovieNames, list(MovieScore.values()), TotalScreens)
print(MaxNoOfShows)
Screens = ["Scr1_m", "Scr1_a","Scr1_e","Scr2_m","Scr2_a","Scr2_e", "Scr3_m", "Scr3_a", "Scr3_e"]
TimeTables=BruteTimeTables(Screens,MovieNames,MaxNoOfShows)
ScreenScore= {'Scr1_m':5,'Scr1_a':6,'Scr1_e':9,'Scr2_m':4,'Scr2_a':5,'Scr2_e':8, 'Scr3_m': 7, 'Scr3_a': 8, 'Scr3_e': 9}
Bt=Maximisation(TimeTables, ScreenScore, MovieScore)
print(Bt)"""
