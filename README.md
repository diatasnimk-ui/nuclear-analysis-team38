 # QUESTION: How does isotope lifetime affect nuclear safety and power production?


# DECISION LOG:
1. We decided to do the analysis country by country first so that we can have a break data down per country to find each timeline's start, then pick one common timeline for all comparisons.
   We did this as it would avoid measuring who started earliest instead of real differences. For this we used all of our 14 files that we merged into a flet.csv that only had the data needed for that analysis to be done. This was created using an algorithm that searched through all the raw data and then reconstructed it. Each team member was tasked with running it separetly and we then merged all of our results so that we can makde sure it truly runs smoothly.
2. For every program we create at least 2 members test it so that logic can be tested and we can see if it provides accurate results every time, also the peer testing helps with fixing bugs in the code that we could otherwise not spot individually. 
3. Harmonizing the data by combining all 14 files and keeping only fields filled in for all five countries. In order to produce one clean table plus supporting tables.
   Anything compared later must pass this all-five-countries test first. So that we can have a documentation of the gaps if any are found or occur. 
4. Store in SQLite and present via Flask. As we will save cleaned pandas output to a single SQLite file. A Flask app reads it, draws charts with matplotlib, and shows them on an HTML page so non-technical readers can explore without running code.
5.  Comparing the isotopes country by country so that we can have them mapped and then afterwards we will decide the linking factors through a python algorithm that will run the anlysis.
   Through this we are trying to prevent picking factors we can't measure for all five countries. Candidate factors: fleet age, load factor, burnup, reactor technology.
