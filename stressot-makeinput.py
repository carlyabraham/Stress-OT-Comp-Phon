################## 
#
# Author:	Carly Abraham. Translated from Perl script by Juliet Stanton.
# Purpose:	Makes an input csv to be used in OTSoft. Permutates all 
# 			potential syllable outputs and calculates constraint violations.
#
##################

import itertools #gets iterations of lists
import re #regex


##################
#MAKE INPUT FILE:
##################

finalInput = open("input.txt", "w") #new file to hold created input

#print column names on first row
colNames = "\t\t\tOneStress\t" + "StressL\t" + "StressR\t" + "MainStressL\t" + "MainStressR\t" + "NonFinality\t" + "*Lapse\t" + "*ExtLapse\t" + "*Clash" + "\n"
finalInput.write(colNames)
finalInput.write(colNames)


##################
#CREATE OUTPUTS: will get the word lengths and stress values used and create all possible permutations
##################

#get inputs:
minSL = int(input("Give the min syllable length:\n"))
maxSL = int(input("Give the max syllable length:\n")) #input of max syllable length
unsplitSylls = input("Give all possible stress values, separated by a space. Ex: 0 1 2\n") #input of desired stress values
sylls = unsplitSylls.split()

#permutate all possible words:
unfilteredOutputs = []
for i in range(minSL, maxSL+1):
	curr = [''.join(p) for p in itertools.product(sylls, repeat=i)] #gets permutations of the syllables for the given word length (i)
	unfilteredOutputs.append(curr) 

#filter permutations:
filteredOutputs = []
syllFormat = re.compile(r"[0,2-9]*[1]{1}[0,2-9]*")  #regex to get any word that only has one primary stress
for word in unfilteredOutputs:
	currLen = len(word[0]) #so we know what # syll word we're currently working with
	validWord =  re.findall(syllFormat, str(word)) #grabs only words that match the regex
	for v in validWord:
		if len(v) == currLen: #only append if it's the full word (not split)
			filteredOutputs.append(v) #adds each individual found word as an element in the filteredOutputs list


##################
#CREATE CONSTRAINTS: defines constraints as variables and defines relating regexs as rules
##################

oneStress = 0
stressL = 0
stressR = 0
mainStressL = 0
mainStressR = 0
nonFinality = 0
lapse = 0
extLapse = 0
lapseAtPeak = 0 #(Kager 2001)
lapseAtEnd = 0 #(Kager 2001)
clash = 0
clashAtPeak = 0 #(Kager 2001)
clashAtEnd = 0 #(Kager 2001)

os = re.compile(r"[2-9]+") #OS: assign * for every non-primary stress
sl = re.compile(r"\b(?<=)0+") #SL: assign * for every stress separating a stressed syll from the right boundary
sr = re.compile(r"0(?=0*\b)") #SR: assign * for every stress separating a stressed syll from the right boundary
msl = re.compile(r".+1") #MSL: assign * for every stress between the primary stress and the left edge
msr = re.compile(r"1.+") #MSR: assign * for every stress between the primary stress and the right edge
nf = re.compile(r"[1-9]\b") #NF: assign * if a stress is on the final syllable
l = re.compile(r"0(?=0)") #L: assign * for every distinct sequence of two unstressed syllables
el = re.compile(r"0(?=00)") #EL: assign * for every distinct sequence of three unstressed syllables
#lp = re.comile()
#le = re.compile()
c = re.compile(r"[12](?=[12])") #C: assign * for every distinct sequence of two stressed syllables
#cp = re.compile()
#ce = re.compile()


##################
#FILL INPUT FILE: calculate violations for every word and print them in rows (1 row for each word)
##################

for word in filteredOutputs:

	oneStress = len(re.findall(os, word))
	for syll in word:
		if syll == 0:
			stressL = stressL + 1
		else:
			break
	#OLD STRESSL REGEX:
		#stressL = len(re.findall(sl, word)[0]) #the sl regex only gets one match of ALL the unstressed syllables between the stressed syllable and left boundary, so get the * count from the length of the one match
	stressR = len(re.findall(sr, word))
	mainStressL = len(re.findall(msl, word))
	mainStressR = len(re.findall(msr, word))
	nonFinality = len(re.findall(nf, word))
	lapse = len(re.findall(l, word))
	extLapse = len(re.findall(el, word))
	#lapseAtPeak = len(re.findall(lp, word)) 
	#lapseAtEnd = len(re.findall(le, word))
	clash = len(re.findall(c, word))
	#clashAtPeak = len(re.findall(cp, word))
	#clashAtEnd = len(re.findall(ce, word)) 
	
	#write the word and violations to file
	finalInput.write("\t" + word + "\t" + "\t" + str(oneStress) + "\t" + str(stressL) + "\t" + str(stressR) + "\t" + str(mainStressL) + "\t" + str(mainStressR) + "\t" + str(nonFinality) + "\t" + str(lapse) + "\t" + str(extLapse) + "\t" + str(clash) + "\n")

