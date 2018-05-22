# Stress-OT-Comp-Phon
Stress Optimality Theory scripts to be used with the Phonology software OTSoft.

## stressot-makeinput.py
A Python adaptation of the original Perl code written by Juliet Stanton (NYU).
Takes user-given constraints to generate a list of stress inputs, then evaluates their constraint violations. Outputs a txt file of this data that is formatted to be used as the input to [OTSoft](http://linguistics.ucla.edu/people/hayes/otsoft/). Meant to be used in full OT analyses on surface representations of stress in words.

####Currently evaluates violations of the following constraints:
* OneStress: assign \* for every non-primary stress.
* StressLeft: assign \* for every stress separating a stressed syll from the left boundary.
* StressRight: assign \* for every stress separating a stressed syll from the right boundary.
* MainStressLeft: assign \* for every stress between the primary stress and the left edge.
* MainStressRight: assign \* for every stress between the primary stress and the right edge.
* NonFinality: assign \* if a stress is on the final syllable.
* \*Lapse: assign \* for every distinct sequence of two unstressed syllables.
* \*ExtLapse: assign \* for every distinct sequence of three unstressed syllables.
* \*Clash: assign \* for every distinct sequence of two stressed syllables.

####To run: 
* Save file locally, and locate in your directory (using the command line)
* Run 
```
python stressot-makeinput.py
```
* Answer the given prompts in the command line - min and max word size, and number of stresses.
* The resulting input.txt (file to be used with OTSoft) will be located in that same directory.
