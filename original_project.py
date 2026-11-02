#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:25:48 2024

@author: aaraizkazmi
"""
# %%
#Demography of New Jersey
# %%


#source - worldpopulationreview


population = 9320860 # Global Variable of NJ 2024 population from source


def yourAge(y): 
 #creates yourAge function which takes input yourGroup(what choice age was in) and prints results based on choice
    
    if y == "1": #if yourGroup chocie was 1
        print(f" Demography of Ages 0-15 : around {round(0.1791 * population):,} people")
    
    if y == "2":#if yourGroup chocie was 2
        print(f" Demography of Ages 15-29 : around {round(0.1893 * population):,} people")
    
    if y == "3":#if yourGroup chocie was 3
        print(f" Demography of Ages 30-64 : around {round(0.4660 * population):,} people")
        
    if y == "4":#if yourGroup chocie was 4
        print(f" Demography of Ages 65-84 : around {round(0.1439 * population):,} people")
    
    if y == "5":#if yourGroup chocie was 5
        print(f" Demography of Ages 84-older : around {round(0.0217 * population):,} people")
    
    
def career(x):
    #creates career function which takes input careerchoice(what choice career was in) and prints results based on choice
    if x == "1":#if careerchoice chocie was 1
        print(f" Demography of STEM,Business,Management,and Health: around {round(0.40 * population):,} people")
    
    if x == "2":#if careerchoice chocie was 2
        print(f" Demography of Service occupations: around {round(0.2546 * population):,} people")
    
    if x == "3":#if careerchoice chocie was 3
        print(f" Demography of Construction,labor,agriculture: around {round(0.1679 * population):,} people")
        
    if x == "4":#if careerchoice chocie was 4
        print(f" Demography of Production,Transportation: around {round(0.11 * population):,} people")
    
eduGroup = {
        "High School Graduate": round(0.2606 * population),
        "Bachelors Degree": round(0.2546 * population),
        "Graduate Degree": round(0.1679 * population),
        "Associates Degree": round(0.669 * population),
    }
#creates tuple with keys "education groups" and its values.Also rounds the values since its number of people


print("Welcome! These are 5 demographic categories of the state of New Jersey(source-worldpopulationreview)") #welcomes user and tell them demography choices

while True: #Program will keep repeating until there is a break
    
    print("1. Total State Population") #choice 1
    
    print("2. Subtotal by Age") #choice 2
    
    print("3. By Gender") #choice 3
    
    print("4. By Highest Education attained") #choice 4
    
    print("5. By Type of Career") #choice 5
    
    DemG = input("Select which demographic you want to know:(1-5) ") 
    #collects number input from user for what choice they want to pick
         
    
    if DemG == "1": #if user picks choice 1
        
        print(f"The Total State Population is {population:,} people") #prints out total population from global variable population
        
      
    elif DemG == "2": #if user picks choice 2
        
        print("Subtotal By Age") #prints type of demography
        
        agechoices=print("Choice 1:(0-15),Choice 2:(15-29),Choice 3:(30-64),Choice 4:(65-84), Choice 5:(85-older)")
        #agechoices prints out the 5 choice of age groups spanning from 0 to 85 and above
        yourGroup = input("what age group do you belong in?(1-5) ")
        #asks user what age group they belong in based on their age, then user has to pick the number of the their choice
        yourAge(yourGroup)
        #uses function yourage and takes yourGroup where the user inputted their choice. YourAge will turn into a set of demography based on the choice
        
        
    
    elif DemG == "3": #if user picks choice 3
        
        print("By Gender") #prints type of demography
        
        male = round(0.4926* population) #Male population is 49.26 percent of nj population, so decimal is multipled by population total 
        female = round(0.5074 * population)#Female population is 50.74 percent of nj population, so decimal is multipled by population total 
        
        print(f"The population by gender is approximately {male:,} men and {female:,} women")
        #prints out men and women population in nj and formatted
        
    elif DemG == "4":
        print("by highest education") #prints type of demography
        
        for i in eduGroup.items(): #repeats 4 times since there 4 groups with items in the tuple eduGroup
            print(f"  Max Education level {i[0]}: {i[1]:,} people")
            #i[0] represents first element and [1] is second element of tuple list. It will give iterating until no more elements. elemnts will paired like 1:2, 2:3, etc.
            
    elif DemG == "5":
        print("by Career")#prints type of demography
        print("Choice 1:(STEM,Business,Management,and Health),Choice 2:(Service occupations),Choice 3:(Constructio,labor,agriculture),Choice 4:(Production,Transportation)")
        #prints out the 4 choice of career categoroes 
        careerchoice = input("What choice is your career in or want to know about?(1-4) ")
        #asks user what choice career is in, if no career user can still find about choices. User has to answer a number between 1-4
        career(careerchoice)
        #uses function career and takes careerchoice where the user inputted their choice. career will turn into a set of demography based on the choice
   
    
   
    
   
    issues = input("Do you want to know two of the most prevelant health concerns?(y/n): ")
#asks user if want to know 2 health concerns as listed in prompt     
    if issues == "y": #if user answers y then it will state 2 health concerns
        print("1.Hearth Disease - risks include high blood pressure, high cholesterol, smoking, diabetes, overweight and obesity, unhealthy diet, physical inactivity, and excessive alcohol use")
        print("2.Cancer - risks include smoking, your weight, your diet, how active you are, sun exposure and sunbed use, and how much alcohol you drink")
        
    
    
    
    
    again = input("Do you want to learn another demographic?(y/n):")#asks user if they want to find another demographic
    
    if again != "y": #If user enters anything but Y, program ends
        break
        
         
    
 

    
    
    
        
    
        

    
    
    