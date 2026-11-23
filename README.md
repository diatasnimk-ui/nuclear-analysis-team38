 # QUESTION: How does isotope lifetime affect nuclear safety and power production?


# DECISION LOG:
1. We decided to do the analysis country by country first so that we can have a break data down per country to find each timeline's start, then pick one common timeline for all comparisons.
   We did this as it would avoid measuring who started earliest instead of real differences. For this we used all of our 14 files that we merged into a fleet.csv and a phase_1_baseline.csv that only had the data needed for that analysis to be done. This was created using an algorithm that searched through all the raw data and then reconstructed it. Each team member was tasked with running it separately and we then merged all of our results so that we can make sure it truly runs smoothly.
2. To keep the development organized we decided on using project phases and we do the whole development phase by phase.
   The phases are as follows:
   Phase 1: Country baselines and timelines. Each country's fleet baseline, first-construction and first-grid dates, and world fleet time series. Run by the lead, narratives written by teammates, results merged. Gate: two-member peer test.
   Phase 2: Harmonisation and common timeline. Combine all 14 files and keep only fields filled in for all five countries. Write the gap documentation and the clean table plus supporting tables. Choose the one common timeline. Create the SQLite file. Gate: every later comparison passes the all-five test.
   Phase 3: Isotope mapping per country. Run the step-by-step isotope verifier for each country and have two members verify each one. Store the results in SQLite with an assumed flag. Gate: the two members' outputs agree, or the disagreements are logged.
   Phase 4: Linking factors. Run the measurability test on fleet age, load factor, burn up and technology. Drop any that fail or are circular. A Python algorithm tests the links that remain. Gate: peer-tested code and documented exclusions.
   Phase 5: Full analysis and presentation. The Flask app reads SQLite and draws matplotlib charts on an HTML page, with the full final analysis covering the country comparison, the linking-factor results, the gaps, and limitations. Gate: a non-technical reader can follow it without running code.
4. For every program we create at least 2 members test it so that logic can be tested and we can see if it provides accurate results every time, also the peer testing helps with fixing bugs in the code that we could otherwise not spot individually. 
5. Harmonizing the data by combining all 14 files and keeping only fields filled in for all five countries. In order to produce one clean table plus supporting tables.
   Anything compared later must pass this all-five-countries test first. So that we can have a documentation of the gaps if any are found or occur. 
6. Store in SQLite and present via Flask. As we will save cleaned pandas output to a single SQLite file. A Flask app reads it, draws charts with matplotlib, and shows them on an HTML page so non-technical readers can explore without running code.
7.  Comparing the isotopes country by country so that we can have them mapped and then afterwards we will decide the linking factors through a python algorithm that will run the analysis.
   Through this we are trying to prevent picking factors we can't measure for all five countries. Candidate factors: fleet age, load factor, burn up, reactor technology.
