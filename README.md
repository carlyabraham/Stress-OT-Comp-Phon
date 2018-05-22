# Stress-OT-Comp-Phon
Stress Optimality Theory scripts to be used with the Phonology software OTSoft.

## stressot-makeinput.py
A Python adaptation of the original Perl code written by Juliet Stanton (NYU).
Takes user-given constraints to generate a list of stress inputs, then evaluates their feature constraint values. Outputs a txt file of this data that is formatted to be used as the input to [OTSoft](http://linguistics.ucla.edu/people/hayes/otsoft/). Meant to be used in full OT analyses on surface representations of stress in words.

To run: 
* Save file locally, and locate in your directory (using the command line)
* Run 
'''
python stressot-makeinput.py
'''
* Answer the given prompts in the command line - min and max word size, and number of stresses.
* The resulting input.txt (file to be used with OTSoft) will be located in that same directory.
