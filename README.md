# Stress-OT-Comp-Phon
Stress Optimality Theory scripts to be used with the Phonology software OTSoft.

## stressot-makeinput.py
A Python adaptation of the original Perl code written by [Juliet Stanton (NYU)](https://wp.nyu.edu/stanton/).
Takes user-given constraints to generate a list of stress inputs, then evaluates their constraint violations. Outputs a txt file of this data that is formatted to be used as the input to [OTSoft](http://linguistics.ucla.edu/people/hayes/otsoft/). Meant to be used in full OT analyses on surface representations of stress in words.

#### Currently evaluates violations of the following constraints:
* OneStress: assign \* for every non-primary stress.
* StressLeft: assign \* for every stress separating a stressed syll from the left boundary.
* StressRight: assign \* for every stress separating a stressed syll from the right boundary.
* MainStressLeft: assign \* for every stress between the primary stress and the left edge.
* MainStressRight: assign \* for every stress between the primary stress and the right edge.
* NonFinality: assign \* if a stress is on the final syllable.
* \*Lapse: assign \* for every distinct sequence of two unstressed syllables.
* \*ExtLapse: assign \* for every distinct sequence of three unstressed syllables.
* \*Clash: assign \* for every distinct sequence of two stressed syllables.

### To run: 
* Save stressot-makeinput.py locally, and using the command line, navigate to the file in your directory.
* Run the command:
```
python stressot-makeinput.py
```
* Answer the given prompts in the command line - the program will ask for min and max word size, and number of stresses.
* The resulting input.txt (file to be used with OTSoft) will be located in that same directory. When setting up OTSoft to run, select this file as your input.

## OTSoft Installation Guide

This script (and any future scripts) are intended to be used with the software OTSoft by Bruce Hayes, to run Optimality Theory analyses. To set up OTSoft, download the software and follow the set up guides [here](https://linguistics.ucla.edu/people/hayes/otsoft/). 

Note: this software unfortunately only runs on Windows currently.

## Contribution Guidelines

If you would like to improve the existing script, or have other scripts for OTSoft that would be useful, feel free to contribute! I'll base the contribution guidelines (for pull requests, bug reports, and similar contributions) off of the basic guidelines laid out [here](https://www.contribution-guide.org/). 

Some features that would be great to add:
* New constraints.
* An automatic ability to insert your own constraints for that specific analysis.
* Anything to work with the output from OTSoft.

## Community

The community guidelines are simple: be nice! (For more details on how to be a constructive, respectful member of an open source community, [TeachingOpenSource](http://teachingopensource.org/community/community-guidelines/) has a great outline. 

If there are any issues, feel free to contact me (Carly Abraham) through my profile contact info.
