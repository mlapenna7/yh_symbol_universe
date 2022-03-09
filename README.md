# yh_symbol_universe
Retrieves all the symbols available on Yahoo Finance and stores them in a file for subsequent processing.
The last time this python program was run, it retrieved over 400,000 symbols. 
Currently just the ticker symbol and name are retrieved.  

Written in python 3.9.

_Takes a few hours to run._  It's brute force but works.

# Running the script
```
python yh_get_all_sym.py
```

If you get an error running the script, you *may* need to install python libraries.  
If so, use `pip install <library name>` .  The only ones I am using are logging and requests.

# Output
- Tickers are stored in a file with name yhallsym.txt 
- Output file format is structured as a python dictionary: { 'ticker1':'name1', 'ticker2':'name2', ... }  
- File is located in the same folder you launched python script from
- Output file size is about 16MB
- Console messages are shown while the script is executing
- Log file contains the console messages is stored in yh_get_all_sym.log

# Sample output
{'BA': 'Boeing Company (The)', 'MA': 'Mastercard Incorporated', 'AAL': 'American Airlines Group, Inc.', 'AA': 'Alcoa Corporation', 'APA': 'APA Corporation', 'AI': 'C3.ai, Inc.', 'AG': 'First Majestic Silver Corp.', 'AR': 'Antero Resources Corporation', 'PAA': 'Plains All American Pipeline, L', 'AU': 'AngloGold Ashanti Limited', 'UA': 'Under Armour, Inc.', 'AM': 'Antero Midstream Corporation', 'AB': 'AllianceBernstein Holding L.P.', 'UAA': 'Under Armour, Inc.', 'EA': 'Electronic Arts Inc.', 'HA': 'Hawaiian Holdings, Inc.', 'A': 'Agilent Technologies, Inc.'}
