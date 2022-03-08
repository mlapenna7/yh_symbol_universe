# yh_symbol_universe
Retrieves all the symbols available on Yahoo Finance and stores in a file. 

Written in python 3.9.

Currently retrieves just symbol and listing name for each available ticker.

Takes quite a few hours to run.  It's brute force but works.

Output file name is yhallsym.txt stored in the same folder you launched python script from.

File format is a python dictionary:
{ 'ticket1':'name1', 'ticker2':'name2', ... }  

Here 's a sample:

{'BA': 'Boeing Company (The)', 'MA': 'Mastercard Incorporated', 'AAL': 'American Airlines Group, Inc.', 'AA': 'Alcoa Corporation', 'APA': 'APA Corporation', 'AI': 'C3.ai, Inc.', 'AG': 'First Majestic Silver Corp.', 'AR': 'Antero Resources Corporation', 'PAA': 'Plains All American Pipeline, L', 'AU': 'AngloGold Ashanti Limited', 'UA': 'Under Armour, Inc.', 'AM': 'Antero Midstream Corporation', 'AB': 'AllianceBernstein Holding L.P.', 'UAA': 'Under Armour, Inc.', 'EA': 'Electronic Arts Inc.', 'HA': 'Hawaiian Holdings, Inc.', 'A': 'Agilent Technologies, Inc.', 'AAP': 'Advance Auto Parts Inc.', 'AL': 'Air Lease Corporation', 'AY': 'Atlantica Sustainable Infrastru', 'SA': 'Seabridge Gold, Inc.', 'RA': 'Brookfield Real Assets Income F', 'AN': 'AutoNation, Inc.', 'AE': 'Adams Resources & Energy, Inc.', 'AAU': 'Almaden Minerals, Ltd.', 'TA': 'TravelCenters of America Inc.', 'MAA': 'Mid-America Apartment Communiti', 'AIR': 'AAR Corp.', 'AX': 'Axos Financial, Inc.', 'AVA': 'Avista Corporation', 'AKA': 'a.k.a. Brands Holding Corp.', 'AADI': 'Aadi Bioscience, Inc.', 'ASA': 'ASA  Gold and Precious Metals L', 'AAON': 'AAON, Inc.', 'AAC.ST': 'AAC Clyde Space AB', 'AAN': 'Aarons Holdings Company, Inc.', 'IAA': 'IAA, Inc.', 'AAVE-USD': 'Aave USD', 'AOA': 'iShares Core Aggressive Allocat', 'ASME.DE': 'ASML Holding N.V. Aandelen op n', 'ACA': 'Arcosa, Inc.', 'AARTIIND.NS': 'AARTI IND LTD', 'AALB.AS': 'AALBERTS N.V.', '2018.HK': 'AAC TECH', 'AAT': 'American Assets Trust, Inc.', 'AIA': 'iShares Asia 50 ETF', 'AC': 'Associated Capital Group, Inc.', 'AZ': 'A2Z Smart Technologies Corp.', 'AP': 'Ampco-Pittsburgh Corporation', 'ARL.DE': 'Aareal Bank AG Inhaber-Aktien o', 'FA': 'First Advantage Corporation', 'AAC': 'Ares Acquisition Corporation', 'AAA': 'Listed Funds Trust AAF First Pr', 'AAK.ST': 'AAK AB', 'SPDV': 'AAM S&P 500 High Dividend Value', 'AARTIDRUGS.NS': 'AARTI DRUGS LTD', '5238.KL': 'AAX', 'ATA': 'Americas Technology Acquisition', 'SAA': 'ProShares Ultra SmallCap600' }
