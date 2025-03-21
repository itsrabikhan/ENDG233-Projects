# records.py
# ENDG 233 F24
#
# Data is provided below to be used with analysis.py. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
# An alternate version of records data will be used to test your code.

# Assume inputs are always capitalized
# Do not hardcode the regions in your analysis.py file- they will not be the same for grading (e.g. 'AA')
regions = ['NE', 'SE', 'NW', 'SW', 'DT']

# Nested lists
# [region, price, number of bedrooms, number of bathrooms]
data = [
['NE', 674900, '4', '4'],
['NE', 585000, '3', '3'],
['SW', 1050000, '5', '4'],
['NE', 520000, '4', '4'],
['SE', 475000, '3', '2'],
['NE', 449900, '4', '3'],
['SE', 469900, '3', '2'],
['NE', 599900, '5', '4'],
['NE', 459900, '3', '3'],
['NW', 798800, '3', '3'],
['SW', 199900, '4', '2'],
['SW', 799900, '2', '2'],
['SW', 299900, '2', '2'],
['SW', 309900, '4', '4'],
['NE', 849900, '4', '3'],
['NW', 445000, '2', '2'],
['NW', 299900, '4', '2'],
['NE', 775000, '6', '5'],
['SE', 629900, '3', '1'],
['NW', 749888, '4', '4'],
['NE', 699999, '4', '4'],
['NE', 464990, '3', '2'],
['SE', 419000, '6', '2'],
['SW', 309900, '1', '1'],
['NE', 499900, '4', '2'],
['NW', 750000, '4', '3'],
['SW', 319900, '1', '1'],
['SW', 189900, '1', '1'],
['SW', 375000, '3', '2'],
['SE', 349900, '1', '1'],
['SW', 194900, '1', '1'],
['NW', 978000, '4', '4'],
['SE', 699000, '4', '4'],
['SW', 599000, '5', '4'],
['NW', 769000, '5', '2'],
['SE', 419000, '3', '3'],
['NE', 459900, '3', '2'],
['SE', 624900, '3', '4'],
['SW', 975000, '4', '4'],
['SW', 3988000, '3', '5'],
['NW', 299000, '1', '1'],
['SW', 789900, '2', '3'],
['NW', 649000, '3', '2'],
['NW', 275000, '2', '2'],
['NE', 449900, '2', '2'],
['NE', 449900, '3', '2'],
['NE', 549900, '2', '2'],
['SW', 297000, '1', '1'],
['SW', 469900, '2', '2'],
['NE', 575000, '5', '3'],
['NW', 999900, '6', '4'],
['SE', 469900, '3', '2'],
['NW', 379000, '2', '2'],
['NE', 554900, '5', '2'],
['SW', 289900, '2', '2'],
['SW', 585000, '4', '3'],
['NE', 479900, '4', '3'],
['NW', 775000, '4', '3'],
['SW', 1495000, '5', '5'],
['NE', 329800, '1', '1'],
['SW', 839000, '8', '4'],
['NE', 474500, '3', '3'],
['SE', 499000, '4', '2'],
['SW', 1299900, '8', '4'],
['SE', 715000, '4', '4'],
['SE', 220000, '1', '1'],
['NE', 649900, '4', '4'],
['SW', 779000, '4', '4'],
['NW', 735000, '4', '3'],
['SE', 360000, '2', '2'],
['NE', 639900, '5', '4'],
['SW', 649900, '5', '3'],
['SE', 669900, '4', '4'],
['SW', 1795000, '3', '4'],
['NE', 239900, '1', '1'],
['NW', 975000, '4', '4'],
['NE', 235000, '1', '1'],
['SW', 689900, '4', '3'],
['NE', 499000, '5', '2'],
['SE', 925000, '8', '4'],
['NE', 345000, '3', '3'],
['NE', 275000, '2', '2'],
['NW', 674900, '5', '4'],
['SW', 699900, '4', '3'],
['SW', 775000, '4', '3'],
['NE', 639900, '5', '4'],
['NW', 750000, '3', '3'],
['SW', 985000, '5', '2'],
['NE', 485000, '4', '2'],
['NW', 799900, '3', '3'],
['SW', 899900, '2', '3'],
['SW', 490000, '4', '3'],
['NE', 499900, '4', '3'],
['SW', 349900, '2', '2'],
['NE', 1098000, '5', '5'],
['SE', 535000, '4', '3'],
['SE', 749900, '4', '4'],
['NE', 279888, '2', '2'],
['SW', 315000, '1', '1'],
['SE', 499900, '3', '3'],
['SW', 499900, '2', '3'],
['SW', 474900, '2', '2'],
['SE', 499900, '4', '3'],
['NE', 549900, '3', '2'],
['SW', 355000, '2', '2'],
['SE', 634900, '3', '3'],
['SW', 628000, '4', '2'],
['SE', 700000, '4', '3'],
['SW', 195000, '1', '1'],
['NW', 245000, '1', '1'],
['SW', 649900, '3', '4'],
['SW', 679900, '5', '2'],
['NW', 199000, '1', '1'],
['NW', 319000, '2', '2'],
['NE', 265000, '1', '1'],
['NW', 849900, '3', '4'],
['SE', 439000, '2', '2'],
['SE', 499900, '3', '3'],
['SE', 339000, '2', '2'],
['NW', 425000, '2', '2'],
['SE', 229900, '2', '1'],
['NW', 649900, '4', '2'],
['SW', 1649900, '6', '5'],
['SE', 549900, '4', '3'],
['SW', 4750000, '3', '5'],
['SW', 1188000, '4', '3'],
['NW', 885000, '4', '4'],
['SE', 419900, '2', '3'],
['NW', 765000, '2', '3'],
['SW', 739000, '4', '2'],
['SW', 649900, '4', '4'],
['NE', 389900, '3', '4'],
['NW', 1175000, '3', '4'],
['NE', 825000, '6', '4'],
['SW', 875000, '4', '4'],
['SE', 659900, '4', '4'],
['SW', 699999, '4', '3'],
['SW', 259000, '2', '1'],
['SE', 475000, '5', '3'],
['SE', 238800, '1', '1'],
['SE', 385000, '3', '3'],
['SW', 949000, '4', '3'],
['SE', 271000, '2', '2'],
['NE', 824999, '6', '4'],
['NE', 620900, '7', '4'],
['NW', 429000, '3', '2'],
['NE', 774999, '7', '6'],
['SW', 200000, '1', '1'],
['NE', 544500, '3', '3'],
['SE', 625000, '5', '4'],
['SW', 749900, '2', '3'],
['NW', 649900, '3', '3'],
['NW', 439900, '2', '3'],
['NW', 749000, '4', '3'],
['SW', 250000, '1', '1'],
['NW', 335000, '2', '2'],
['SW', 729900, '3', '3'],
['SW', 319900, '2', '2'],
['SW', 229900, '1', '1'],
['SW', 399900, '2', '2'],
['NW', 629900, '4', '4'],
['NW', 300000, '2', '1'],
['NW', 549900, '3', '3'],
['NW', 549900, '3', '3'],
['NW', 848800, '4', '4'],
['SW', 299999, '2', '2'],
['NW', 589000, '5', '2'],
['NE', 544900, '3', '3'],
['NW', 1049900, '4', '4'],
['NE', 580000, '5', '3'],
['NW', 525000, '5', '3'],
['SW', 1199999, '4', '3'],
['NE', 300000, '2', '2'],
['SW', 980000, '4', '3'],
['NW', 529000, '3', '3'],
['NW', 519000, '3', '3'],
['NW', 775000, '3', '3'],
['NE', 469900, '3', '3'],
['SW', 384900, '2', '1'],
['NW', 599900, '3', '3'],
['NW', 750000, '4', '2'],
['SW', 274900, '1', '1'],
['SE', 399000, '2', '2'],
['SE', 724950, '4', '3'],
['NW', 834900, '4', '4'],
['SE', 549900, '3', '2'],
['NW', 899900, '4', '4'],
['SW', 370000, '1', '1'],
['NW', 849900, '4', '2'],
['SW', 375000, '3', '2'],
['SE', 550000, '4', '2'],
['SE', 449900, '3', '2'],
['SE', 599800, '5', '3'],
['NW', 580000, '2', '1'],
['SW', 579999, '3', '3'],
['NW', 459900, '5', '2'],
['NE', 335000, '3', '2'],
['SE', 499900, '4', '4'],
['NE', 599900, '3', '1'],
['NE', 225000, '2', '1'],
['SW', 549900, '5', '4'],
['SW', 299900, '2', '2'],
['NW', 729000, '3', '3'],
['SW', 925000, '3', '3'],
['NW', 599900, '3', '3'],
['SE', 680000, '6', '3'],
['SE', 675000, '3', '4'],
['NE', 579900, '4', '4'],
['NW', 239900, '1', '1'],
['SW', 514900, '3', '3'],
['SW', 199900, '1', '1'],
['NE', 279900, '2', '1'],
['NE', 594900, '5', '3'],
['SW', 1387000, '5', '4'],
['SW', 349900, '2', '1'],
['NE', 615000, '5', '3'],
['SW', 245000, '2', '1'],
['NW', 699900, '3', '3'],
['NE', 665000, '6', '2'],
['SW', 1595000, '4', '5'],
['SE', 280000, '2', '1'],
['SE', 389000, '3', '1'],
['NW', 789777, '4', '5'],
['SW', 409900, '4', '3'],
['SW', 435000, '2', '2'],
['NW', 859000, '3', '3'],
['SE', 659800, '4', '4'],
['NW', 449900, '2', '3'],
['NW', 599800, '3', '2'],
['SW', 159900, '1', '1'],
['SE', 499000, '3', '3'],
['SE', 675000, '4', '4'],
['NE', 324900, '4', '2'],
['SW', 429900, '3', '3'],
['NW', 295000, '2', '2'],
['NE', 299000, '2', '2'],
['SW', 799900, '2', '3'],
['NE', 1150000, '1', '1'],
['NE', 469000, '3', '3'],
['SW', 1150000, '4', '3'],
['SW', 1499000, '4', '4'],
['SW', 299000, '2', '1'],
['NW', 1049900, '4', '4'],
['NW', 399900, '2', '2'],
['SW', 799900, '5', '2'],
['SW', 769900, '3', '4'],
['NE', 285000, '3', '1'],
['NE', 429900, '5', '3'],
['NE', 634900, '4', '3'],
['NE', 225000, '1', '1'],
['SW', 1089000, '4', '4'],
['SE', 829988, '5', '4'],
['NE', 359900, '2', '2'],
['SW', 250000, '2', '1'],
['SW', 1225000, '3', '3'],
['NW', 629900, '4', '4'],
['SW', 899900, '5', '3'],
['NE', 799142, '4', '3'],
['NW', 749900, '3', '3'],
['SE', 735000, '3', '3'],
['SE', 344900, '2', '2'],
['NE', 369900, '2', '2'],
['SW', 550000, '3', '3'],
['NE', 215000, '1', '1'],
['SW', 619900, '5', '4'],
['NE', 524900, '4', '3'],
['NW', 724800, '4', '2'],
['NE', 349900, '3', '2'],
['SE', 310000, '2', '2'],
['SE', 599888, '4', '3'],
['SW', 760000, '4', '2'],
['NW', 649900, '4', '4'],
['SW', 899900, '5', '4'],
['SE', 599888, '4', '3'],
['NW', 649900, '4', '4'],
['SW', 899900, '5', '4'],
['SW', 2950000, '3', '3'],
['NE', 1350000, '4', '4'],
['SW', 628800, '3', '3'],
['NE', 310000, '2', '2'],
['SE', 459000, '4', '3'],
['NE', 304777, '2', '2'],
['NE', 388900, '3', '3'],
['NE', 560000, '3', '3'],
['NW', 650000, '4', '3'],
['SE', 269900, '2', '2'],
['SW', 314900, '2', '2'],
['SE', 399900, '3', '2'],
['SW', 735000, '4', '2'],
['NE', 559900, '5', '4'],
['SE', 1498000, '4', '4'],
['NW', 428000, '2', '2'],
['NW', 259900, '2', '1'],
['SW', 598800, '2', '4'],
['SW', 445000, '2', '3'],
['NE', 730000, '3', '2'],
['NW', 1189000, '4', '4'],
['SW', 325900, '2', '1'],
['NW', 620000, '4', '3'],
['SW', 339000, '2', '2'],
['NW', 459900, '2', '2'],
['NE', 575000, '4', '3'],
['NE', 489900, '5', '3'],
['NE', 325000, '2', '2'],
['SE', 465000, '2', '3'],
['SW', 650000, '4', '3'],
['SE', 389900, '2', '2'],
['NW', 914900, '5', '4'],
['SW', 935000, '4', '4'],
['SW', 1995000, '4', '4'],
['SW', 990000, '2', '2'],
['SE', 1199000, '2', '2'],
['NE', 400000, '3', '2'],
['NW', 538500, '4', '4'],
['SE', 1999000, '5', '5'],
['SW', 939900, '4', '2'],
['NW', 675000, '3', '2'],
['SW', 549000, '3', '2'],
['NW', 439900, '3', '2'],
['NE', 699900, '4', '4'],
['NE', 624900, '4', '4'],
['NE', 319000, '2', '2'],
['NE', 699900, '6', '4'],
['SW', 439800, '2', '2'],
['SW', 294900, '1', '1'],
['NE', 594900, '4', '4'],
['SW', 1475000, '5', '4'],
['SE', 289900, '3', '2'],
['SE', 574999, '3', '3'],
['SW', 1599900, '4', '3'],
['NW', 214900, '2', '1'],
['NE', 295000, '2', '2'],
['NE', 594900, '5', '3'],
['SW', 279900, '2', '2'],
['SW', 529900, '2', '2'],
['SE', 269900, '2', '2'],
['SE', 720000, '3', '3'],
['SW', 259900, '2', '1'],
['SW', 472000, '2', '2'],
['SW', 359900, '2', '2'],
['SW', 999999, '5', '4'],
['NW', 319900, '2', '2'],
['SE', 325000, '2', '1'],
['NW', 929900, '5', '2'],
['NE', 249900, '2', '3'],
['SW', 965000, '4', '3'],
['NW', 245000, '2', '1'],
['SW', 700000, '3', '3'],
['NW', 475000, '5', '3'],
['SW', 399900, '2', '2'],
['SW', 919900, '4', '4'],
['SW', 2495000, '4', '4'],
['SE', 539900, '2', '2'],
['NW', 259900, '1', '1'],
['NW', 1359999, '3', '4'],
['NW', 1050000, '6', '4'],
['SW', 299900, '1', '1'],
['SW', 668000, '2', '2'],
['SW', 249900, '5', '4'],
['NE', 550000, '3', '3'],
['SW', 379900, '2', '2'],
['NE', 399900, '2', '3'],
['NW', 420000, '3', '3'],
['NE', 619900, '4', '3'],
['NE', 1000000, '5', '4'],
['SE', 340000, '3', '2'],
['SE', 439000, '4', '2'],
['SW', 279990, '1', '1'],
['SW', 360000, '2', '2'],
['NE', 539000, '4', '3'],
['NE', 479900, '3', '2'],
['SE', 389900, '1', '1'],
['NW', 219900, '2', '1'],
['SW', 2350000, '5', '6'],
['NW', 275000, '2', '1'],
['NW', 474900, '3', '3'],
['SE', 324000, '1', '1'],
['NW', 445000, '4', '4'],
['NE', 459900, '2', '2'],
['SW', 439000, '2', '2'],
['SW', 849000, '5', '3'],
['NW', 639000, '5', '4'],
['SE', 520000, '3', '2'],
['NW', 318813, '2', '2'],
['SW', 370000, '2', '1'],
['NE', 549900, '3', '3'],
['SE', 720000, '2', '1'],
['NW', 574990, '3', '3'],
['NE', 629999, '4', '3'],
['NE', 819900, '4', '4'],
['SW', 289900, '2', '1'],
['SW', 359000, '2', '2'],
['NW', 849900, '3', '4'],
['SE', 395000, '2', '3'],
['SE', 729900, '3', '3'],
['SW', 730000, '2', '2'],
['NE', 979888, '4', '5'],
['NW', 254000, '2', '1'],
['NW', 614900, '4', '4'],
['NW', 769900, '6', '4'],
['SW', 310000, '2', '2'],
['NW', 749900, '5', '2'],
['NW', 542500, '2', '3'],
['SW', 359000, '1', '1'],
['NE', 320000, '3', '2'],
['SE', 159000, '3', '2'],
['NE', 525000, '2', '1'],
['NE', 340000, '2', '2'],
['NW', 879900, '3', '3'],
['SW', 537000, '2', '3'],
['NW', 475000, '3', '2'],
['NW', 749900, '3', '4'],
['SW', 1995000, '4', '5'],
['NW', 849900, '6', '4'],
['NE', 319900, '2', '2'],
['NE', 639900, '4', '3'],
['SW', 229900, '1', '1'],
['SW', 215000, '1', '1'],
['NW', 369900, '2', '2'],
['NE', 199900, '2', '2'],
['NE', 389900, '3', '2'],
['SE', 260000, '3', '1'],
['SE', 439900, '4', '2'],
['SW', 525000, '3', '3'],
['NE', 549900, '4', '3'],
['SW', 1775000, '4', '4'],
['SW', 219000, '1', '1'],
['SW', 184900, '1', '1'],
['NW', 699900, '5', '4'],
['SW', 364900, '2', '1'],
['NE', 319900, '2', '2'],
['NW', 315000, '1', '1'],
['NW', 339900, '2', '2'],
['NW', 413900, '3', '2'],
['SW', 249999, '2', '1'],
['SW', 1299900, '4', '4'],
['NW', 270000, '2', '1'],
['SW', 349800, '1', '1'],
['NW', 785000, '5', '4'],
['NE', 1098000, '7', '4'],
['NE', 730000, '6', '4'],
['NE', 870000, '4', '4'],
['SW', 329900, '2', '1'],
['NE', 599888, '3', '3'],
['SW', 1259000, '4', '5'],
['NE', 329900, '2', '1'],
['SW', 2350000, '4', '5'],
['NE', 969900, '5', '4'],
['NW', 895000, '5', '4'],
['SE', 649900, '4', '3'],
['SW', 645000, '3', '2'],
['SW', 1684900, '5', '4'],
['SW', 1499900, '4', '3'],
['NE', 499900, '5', '2'],
['NW', 529999, '3', '3'],
['NW', 724900, '4', '4'],
['SE', 399900, '2', '2'],
['SW', 252900, '2', '1'],
['NW', 499900, '3', '2'],
['NE', 949900, '6', '5'],
['SE', 439900, '1', '1'],
['NE', 550000, '4', '4'],
['NW', 589900, '4', '2'],
['NE', 734900, '4', '4'],
['SW', 234900, '1', '1'],
['SW', 919800, '4', '4'],
['NE', 325000, '2', '2'],
['NE', 299999, '3', '2'],
['SE', 275000, '1', '1'],
['NE', 539999, '3', '2'],
['NW', 130000, '3', '1'],
['NW', 569900, '2', '2'],
['NW', 234900, '1', '1'],
['SW', 329900, '2', '2'],
['SE', 450000, '2', '2'],
['NW', 769900, '3', '2'],
['NE', 337000, '2', '1'],
['NW', 745000, '4', '4'],
['NE', 609000, '2', '2'],
['SE', 779000, '3', '2'],
['SW', 749000, '5', '4'],
['SE', 329900, '3', '1'],
['SW', 645000, '2', '1'],
['NW', 194000, '4', '4'],
['SE', 899500, '3', '2'],
['SW', 599900, '4', '4'],
['NW', 649900, '5', '3'],
['NW', 674900, '5', '4'],
['NE', 455000, '2', '1'],
['SE', 570000, '4', '3'],
['NE', 659900, '3', '3'],
['SW', 975000, '4', '4'],
['NE', 400000, '2', '2'],
['NW', 59900, '2', '2'],
['NE', 335000, '3', '3'],
['SE', 274900, '3', '3'],
['NE', 699900, '4', '4'],
['SW', 258800, '1', '1'],
['NW', 2980000, '5', '7'],
['NE', 438000, '3', '3'],
['NE', 460000, '3', '2'],
['NW', 350000, '4', '2'],
['NE', 289900, '3', '1'],
['SE', 614900, '3', '3'],
['NW', 779900, '4', '3'],
['NE', 350000, '3', '3'],
['NE', 529900, '4', '3'],
['SE', 509000, '4', '2'],
['NE', 774999, '3', '3'],
['SE', 575000, '3', '3'],
['NE', 399900, '2', '3'],
['NE', 449900, '4', '3'],
['SW', 249900, '2', '1'],
['NW', 785000, '3', '4'],
['NE', 469000, '3', '3'],
['NE', 529999, '3', '3'],
['NE', 661500, '3', '3'],
['NE', 809900, '2', '2'],
['NE', 249900, '2', '1'],
['SE', 359900, '1', '1'],
['NE', 559000, '3', '2'],
['SE', 549900, '5', '2'],
['SW', 759900, '4', '3'],
['SW', 305000, '2', '2'],
['SW', 800000, '2', '1'],
['NW', 869900, '5', '3'],
['NW', 339900, '2', '2'],
['NW', 679900, '3', '3'],
['SW', 1695000, '4', '5'],
['SW', 599000, '4', '2'],
['SE', 759999, '4', '3'],
['SW', 824900, '4', '4'],
['SW', 341000, '2', '1'],
['SE', 376845, '4', '3'],
['SE', 790000, '3', '2'],
['NE', 395000, '3', '3'],
['SW', 565000, '4', '4'],
['SW', 1128000, '2', '1'],
['SW', 240000, '3', '2'],
['SW', 484900, '4', '4'],
['NW', 1198000, '4', '4'],
['NW', 1249900, '2', '1'],
['NW', 625000, '4', '3'],
['SW', 799900, '5', '2'],
['SW', 1320000, '4', '5'],
['NW', 699000, '4', '4'],
['NW', 415000, '3', '2'],
['NW', 450000, '4', '2'],
['SE', 589900, '3', '3'],
['SW', 849999, '5', '4'],
['NW', 659900, '3', '3'],
['NW', 574900, '4', '4'],
['SE', 525000, '3', '3'],
['SW', 684900, '4', '3'],
['SW', 900000, '5', '4'],
['NW', 484900, '3', '3'],
['SE', 270000, '2', '1'],
['NW', 732000, '4', '3'],
['NE', 475000, '4', '3'],
['NE', 549900, '4', '3'],
['SW', 370000, '2', '2'],
['NW', 699900, '3', '3'],
['SE', 629900, '3', '3'],
['SE', 624900, '3', '1'],
['NW', 719000, '3', '3'],
['SW', 1275000, '3', '3'],
['SW', 630000, '5', '4'],
['NW', 599900, '3', '3'],
['NW', 249900, '1', '1'],
['SW', 589900, '3', '3'],
['SW', 699900, '3', '3'],
['NW', 750000, '5', '4'],
['NE', 1099000, '4', '5'],
['SW', 324900, '2', '2'],
['SW', 785000, '4', '4'],
['NW', 350000, '2', '2'],
['NW', 969900, '4', '4'],
['SW', 599900, '3', '2'],
['SW', 1099900, '6', '4'],
['NE', 489900, '4', '3'],
['NE', 1049900, '8', '6'],
['NE', 335000, '3', '3'],
['SW', 400000, '2', '2'],
['SE', 314900, '2', '1'],
['SW', 999900, '3', '4'],
['SE', 283000, '2', '1'],
['NE', 398088, '2', '2'],
['SW', 774900, '5', '2'],
['SW', 1450000, '5', '5'],
['SE', 283000, '2', '1'],
['NE', 398088, '2', '2'],
['SW', 999900, '3', '4'],
['SW', 3850000, '5', '6'],
['NE', 425000, '3', '3'],
['NW', 549500, '3', '2'],
['NW', 815000, '5', '3'],
['NE', 499000, '3', '3'],
['NE', 394900, '2', '2'],
['NE', 538888, '2', '2'],
['NE', 599990, '4', '3'],
['NE', 825000, '4', '4'],
['NE', 839900, '4', '4'],
['SW', 879900, '3', '3'],
['SE', 510000, '5', '2'],
['NW', 920000, '3', '2'],
['SW', 799900, '4', '3'],
['NW', 920000, '3', '2'],
['SW', 199900, '1', '1'],
['SW', 169000, '1', '1'],
['NW', 535000, '4', '3'],
['SE', 899000, '2', '2'],
['SE', 999900, '3', '3'],
['SW', 629900, '2', '2'],
['SW', 529900, '5', '4'],
['NE', 349900, '3', '2'],
['SE', 868900, '2', '4'],
['NE', 3300000, '6', '4'],
['SW', 574900, '2', '3'],
['SW', 484500, '4', '2'],
['SE', 819900, '3', '2'],
['NE', 690000, '2', '1'],
['SW', 439900, '2', '3'],
['NE', 264999, '1', '1'],
['SW', 1100000, '2', '2'],
['NW', 364900, '1', '1'],
['NW', 500000, '3', '2'],
['NW', 449900, '4', '2'],
['SW', 229000, '2', '1'],
['NE', 499900, '3', '3'],
['NW', 920000, '5', '2'],
['NE', 647000, '5', '4'],
['NE', 458200, '3', '2'],
['NW', 574900, '4', '3'],
['NW', 574900, '4', '3'],
['NE', 539000, '5', '3'],
['NE', 365000, '3', '2'],
['SE', 448888, '3', '2'],
['NW', 728000, '3', '4'],
['SE', 759900, '4', '4'],
['SE', 593500, '4', '3'],
['SW', 1325000, '3', '4'],
['SW', 699900, '2', '2'],
['NE', 459900, '3', '3'],
['SW', 537500, '4', '3'],
['SE', 629900, '4', '3'],
['SW', 450000, '2', '3'],
['NW', 949900, '5', '4'],
['SW', 399900, '3', '3'],
['NE', 559000, '3', '2'],
['SW', 549900, '4', '3'],
['SE', 559000, '4', '3'],
['NE', 654900, '5', '2'],
['SW', 425000, '2', '2'],
['NW', 610000, '3', '4'],
['SE', 669000, '3', '4'],
['SE', 519900, '3', '3'],
['SW', 499900, '4', '2'],
['SW', 549800, '2', '3'],
['SE', 469900, '3', '3'],
['SE', 675000, '3', '3'],
['NE', 579900, '5', '2'],
['NW', 889999, '6', '5'],
['SE', 650000, '3', '3'],
['SE', 540000, '3', '2'],
['SE', 850000, '4', '3'],
['SW', 610000, '3', '3'],
['SW', 420000, '3', '3'],
['SE', 325000, '1', '1'],
['NE', 675000, '4', '3'],
['NE', 664900, '3', '3'],
['NW', 485000, '3', '3'],
['SW', 429900, '3', '3'],
['NE', 699900, '4', '4'],
['NE', 679000, '4', '2'],
['NW', 630000, '3', '3'],
['NE', 565000, '6', '4'],
['NW', 399900, '2', '2'],
['NW', 599900, '3', '3'],
['NE', 347500, '1', '1'],
['SW', 929000, '4', '4'],
['SW', 1049000, '4', '5'],
['SW', 649900, '3', '3'],
['SW', 554903, '3', '2'],
['SW', 219900, '1', '1'],
['NW', 609900, '2', '2'],
['NW', 799000, '4', '4'],
['NW', 899900, '5', '4'],
['NE', 768000, '6', '3'],
['SE', 579900, '3', '1'],
['SE', 429900, '1', '1'],
['SW', 1325000, '3', '4'],
['SW', 269000, '1', '1'],
['SE', 499900, '3', '4'],
['NW', 309000, '2', '1'],
['NW', 649900, '3', '3'],
['SW', 779900, '4', '3'],
['SW', 820000, '3', '3'],
['NW', 699900, '3', '3'],
['NE', 795000, '5', '4'],
['SE', 576345, '2', '2'],
['SW', 465000, '2', '2'],
['SW', 779900, '4', '3'],
['SW', 820000, '3', '3'],
['NW', 309000, '2', '1'],
['NE', 379900, '2', '2'],
['SE', 449900, '4', '2'],
['SE', 298000, '2', '1'],
['NE', 728888, '6', '4'],
['SW', 650000, '3', '4'],
['SE', 268000, '1', '1'],
['SE', 539000, '4', '2'],
['NW', 379900, '2', '2'],
['SW', 429900, '1', '1'],
['SW', 738800, '3', '3'],
['SE', 519900, '3', '3'],
['NW', 775000, '3', '2'],
['SW', 250000, '1', '1'],
['SW', 659900, '3', '3'],
['NE', 569900, '3', '3'],
['SE', 2780000, '4', '5'],
['NE', 299900, '2', '1'],
['SW', 2695000, '6', '7'],
['NW', 889000, '4', '4'],
['NE', 649000, '4', '4'],
['SE', 1388800, '4', '5'],
['SW', 440000, '2', '2'],
['NE', 755000, '4', '4'],
['NW', 699900, '3', '3'],
['NW', 654900, '3', '3'],
['NW', 649000, '5', '2'],
['NE', 519900, '3', '3'],
['SE', 1265000, '5', '3'],
['NW', 595000, '2', '3'],
['NW', 429999, '3', '2'],
['SW', 799900, '4', '4'],
['NW', 999000, '3', '3'],
['SW', 599900, '3', '3'],
['SE', 364900, '2', '2'],
['SW', 675000, '3', '2'],
['SE', 539900, '4', '3'],
['SW', 899000, '4', '4'],
['NW', 768000, '6', '4'],
['NE', 699999, '3', '3'],
['SE', 279900, '2', '1'],
['SW', 599900, '3', '4'],
['NE', 578500, '4', '4'],
['SW', 225000, '3', '2'],
['NE', 499900, '6', '3'],
['NE', 549900, '5', '3'],
['NW', 474900, '3', '3'],
['SW', 1169900, '4', '4'],
['NE', 450000, '3', '2'],
['SE', 639990, '3', '2'],
['SE', 590000, '4', '3'],
['NE', 589999, '4', '4'],
['NW', 685000, '3', '3'],
['NE', 579900, '4', '4'],
['NE', 519900, '3', '2'],
['SE', 389900, '2', '3'],
['NW', 632988, '2', '1'],
['NW', 899800, '4', '4'],
['NE', 284900, '3', '2'],
['NE', 824900, '4', '3'],
['NE', 679000, '4', '3'],
['SW', 749900, '3', '3'],
['NW', 759900, '3', '3'],
['SE', 1295000, '5', '4'],
['SW', 629900, '2', '2'],
['SW', 324900, '2', '1'],
['NW', 1245000, '3', '4'],
['NE', 335000, '2', '1'],
['NE', 299000, '0', '1'],
['SW', 899000, '4', '4'],
['NE', 890000, '4', '4'],
['SW', 1200000, '5', '4'],
['NE', 399900, '3', '2'],
['SE', 379900, '2', '2'],
['SW', 1399000, '5', '4'],
['NW', 750000, '3', '4'],
['NE', 1299900, '5', '4'],
['NW', 800000, '3', '3'],
['SW', 534900, '4', '3'],
['NE', 890000, '4', '4'],
['NW', 849900, '2', '2'],
['NW', 549900, '2', '3'],
['NW', 265000, '2', '2'],
['NE', 699000, '5', '4'],
['NW', 550000, '3', '3'],
['NE', 700000, '3', '3'],
['NW', 940000, '5', '3'],
['NE', 519900, '3', '3'],
['SW', 799900, '4', '3'],
['NE', 549888, '3', '3'],
['SW', 229900, '2', '1'],
['NW', 675000, '3', '3'],
['NW', 669500, '5', '2'],
['NW', 528888, '2', '1'],
['SW', 339000, '2', '1'],
['NW', 749900, '5', '3'],
['NW', 1650000, '4', '4'],
['NE', 539900, '3', '3'],
['NW', 749900, '5', '3'],
['NW', 799900, '3', '3'],
['SE', 542900, '2', '3'],
['SW', 1399900, '5', '4'],
['NW', 1249900, '6', '5'],
['SW', 2250000, '5', '5'],
['SW', 959999, '1', '1'],
['SE', 299900, '2', '2'],
['SW', 1388000, '2', '3'],
['NE', 639777, '4', '4'],
['NE', 599888, '4', '3'],
['NE', 599000, '3', '3'],
['SE', 625000, '3', '3'],
['SW', 722888, '3', '3'],
['NW', 589900, '5', '3'],
['SW', 624900, '3', '3'],
['NE', 420000, '3', '3'],
['NE', 629900, '3', '3'],
['SE', 564900, '2', '3'],
['SE', 579900, '4', '2'],
['SW', 699000, '2', '2'],
['NE', 549900, '4', '3'],
['NW', 500000, '3', '3'],
['NW', 499800, '3', '3'],
['SE', 595000, '4', '4'],
['SW', 649900, '3', '2'],
['NE', 779900, '3', '3'],
['NW', 689000, '3', '4'],
['NW', 539900, '2', '2'],
['SW', 949900, '3', '4'],
['SW', 364777, '2', '2'],
['NW', 899900, '4', '2'],
['SE', 475000, '2', '2'],
['SE', 355000, '2', '2'],
['SW', 527900, '2', '3'],
['SW', 335000, '1', '1'],
['SW', 319900, '2', '1'],
['SE', 550000, '3', '2'],
['SW', 318800, '1', '1'],
['NE', 340000, '3', '1'],
['NE', 1620000, '3', '3'],
['SE', 755895, '2', '2'],
['SW', 1365000, '5', '3'],
['SE', 834645, '2', '2'],
['SE', 629900, '4', '2'],
['SW', 559000, '2', '2'],
['SW', 549000, '2', '2'],
['NE', 649000, '4', '3'],
['NW', 475000, '3', '3'],
['SE', 675000, '3', '3'],
['SW', 2095000, '6', '7'],
['NW', 779900, '5', '4'],
['SW', 579777, '3', '3'],
['SW', 1259000, '5', '4'],
['SW', 1299000, '3', '4'],
['SW', 219999, '1', '1'],
['NW', 1100000, '4', '4'],
['SE', 199900, '2', '1'],
['SE', 274900, '1', '1'],
['SE', 446145, '1', '1'],
['NW', 569900, '5', '2'],
['SW', 765000, '4', '3'],
['NE', 299900, '2', '2'],
['SW', 199900, '0', '1'],
['NE', 869000, '3', '3'],
['NW', 510000, '3', '3'],
['NE', 489900, '5', '2'],
['SW', 825000, '3', '5'],
['NW', 719999, '5', '4'],
['SE', 375000, '2', '3'],
['SW', 450000, '2', '2'],
['NE', 419900, '3', '4'],
['SW', 649000, '2', '2'],
['NW', 549999, '4', '2'],
['NE', 549900, '4', '4'],
['SE', 239500, '1', '1'],
['NE', 489000, '4', '3'],
['NW', 742900, '3', '2'],
['NW', 939900, '4', '4'],
['SW', 365000, '1', '1'],
['NE', 312900, '2', '1'],
['SW', 365000, '2', '1'],
['SE', 499900, '3', '2'],
['NE', 199000, '2', '2'],
['NW', 889000, '6', '3'],
['SE', 499000, '4', '4'],
['NE', 819786, '5', '4'],
['SW', 768000, '3', '4'],
['SE', 235000, '2', '1'],
['NE', 860000, '5', '4'],
['SW', 384900, '2', '2'],
['SE', 60000, '2', '1'],
['SW', 935900, '4', '2'],
['NE', 549900, '4', '2'],
['SW', 1299000, '4', '4'],
['NE', 589900, '5', '3'],
['SW', 1199000, '4', '4'],
['NE', 724900, '4', '2'],
['NE', 329000, '3', '2'],
['SW', 498900, '3', '4'],
['NW', 795000, '3', '4'],
['NW', 595000, '2', '2'],
['NW', 595000, '3', '4'],
['SE', 459786, '4', '2'],
['NE', 475000, '6', '4'],
['SW', 526800, '3', '1'],
['NW', 365000, '2', '2'],
['SE', 484900, '2', '3'],
['NE', 555000, '4', '2'],
['SW', 248000, '1', '1'],
['SW', 320000, '1', '1'],
['NE', 489000, '3', '2'],
['SW', 298555, '1', '1'],
['NE', 387500, '2', '2'],
['SE', 459900, '2', '2'],
['SE', 464786, '4', '2'],
['NW', 699900, '3', '4'],
['NW', 212500, '1', '1'],
['SE', 1469000, '4', '4'],
['NW', 759900, '3', '3'],
['SW', 339900, '2', '1'],
['SW', 580000, '1', '1'],
['NW', 301442, '3', '3'],
['NW', 597000, '8', '4'],
['NE', 929000, '6', '4'],
['SW', 699900, '5', '4'],
['NE', 374900, '4', '3'],
['SE', 549999, '2', '2'],
['SW', 559900, '5', '4'],
['NW', 1849000, '5', '2'],
['NW', 734900, '2', '3'],
['NW', 449000, '6', '3'],
['NE', 1225000, '3', '3'],
['NW', 399900, '4', '4'],
['SW', 759900, '4', '3'],
['NW', 825000, '1', '1'],
['SE', 153900, '2', '3'],
['NE', 979888, '4', '5'],
['NE', 499900, '4', '3'],
['NW', 699900, '4', '2'],
['SE', 550000, '4', '2'],
['NW', 865000, '5', '3'],
['NW', 688800, '4', '3'],
['SE', 475000, '3', '2'],
['SW', 629900, '4', '3'],
['NE', 849000, '6', '4'],
['SW', 389000, '2', '2'],
['NE', 649999, '4', '3'],
['SW', 969900, '5', '4'],
['SW', 684900, '3', '3'],
['NE', 629900, '4', '2'],
['NW', 849900, '4', '4'],
['SW', 575000, '4', '3'],
['SE', 699900, '4', '4'],
['SE', 549900, '3', '3'],
['NW', 877000, '5', '4'],
['SE', 549900, '3', '3'],
['NW', 315000, '3', '1'],
['SW', 839999, '3', '3'],
['NW', 779000, '3', '2'],
['SW', 380000, '2', '2'],
['SW', 849900, '5', '2'],
['SW', 799988, '4', '3'],
['NE', 289900, '3', '2'],
['NW', 1550000, '5', '5'],
['NW', 598000, '3', '3'],
['NW', 849900, '5', '4'],
['SE', 398800, '3', '2'],
['NW', 950000, '3', '4'],
['SW', 1800000, '4', '3'],
['NE', 585000, '3', '3'],
['NE', 399900, '2', '2'],
['SE', 599900, '5', '3'],
['NE', 290000, '2', '2'],
['NE', 520000, '5', '3'],
['SW', 630000, '5', '3'],
['NW', 649900, '4', '3'],
['SW', 460000, '3', '1'],
['NE', 549900, '3', '3'],
['SW', 615000, '5', '3'],
['NE', 575000, '5', '3'],
['SE', 525000, '4', '2'],
['NE', 495000, '4', '3'],
['NW', 794800, '3', '3'],
['SW', 468000, '2', '2'],
['SW', 335000, '1', '1'],
['NE', 250000, '2', '1'],
['NW', 619900, '3', '3'],
['NE', 229900, '3', '1'],
['NW', 639900, '4', '4'],
['SE', 1650000, '2', '3'],
['NW', 550000, '2', '2'],
['NW', 1249000, '5', '2'],
['NE', 339900, '2', '2'],
['SE', 680000, '5', '4'],
['SW', 839000, '3', '3'],
['NE', 344900, '2', '1'],
['SW', 1149900, '2', '3'],
['SW', 575000, '4', '3'],
['SE', 1169999, '4', '3'],
['SW', 949900, '4', '4'],
['SW', 1299900, '3', '3'],
['NE', 849900, '4', '2'],
['NE', 740000, '6', '5'],
['SW', 1000000, '4', '3'],
['SW', 238800, '2', '1'],
['NW', 1350000, '4', '4'],
['NW', 515000, '3', '3'],
['NW', 1049999, '5', '3'],
['NW', 1499000, '5', '4'],
['NW', 1249900, '5', '5'],
['NE', 269000, '2', '1'],
['NW', 499000, '3', '3'],
['NW', 749900, '4', '4'],
['NE', 515000, '4', '2'],
['NW', 819900, '5', '5'],
['SE', 569900, '4', '4'],
['NW', 481900, '3', '4'],
['NW', 997500, '3', '3'],
['SE', 775900, '4', '4'],
['NW', 1599900, '5', '5'],
['NW', 799000, '4', '4'],
['SW', 1299900, '5', '3'],
['NW', 725000, '5', '4'],
['NW', 769900, '3', '3'],
['NW', 2299990, '5', '5'],
['NW', 749900, '3', '3'],
['NE', 699000, '6', '3'],
['NE', 495000, '3', '3'],
['SW', 925000, '4', '3'],
['NW', 715000, '3', '4'],
['SW', 4450000, '5', '6'],
['NW', 550000, '3', '3'],
['SW', 566500, '3', '3'],
['NW', 725000, '4', '4'],
['NW', 874900, '4', '4'],
['SW', 399900, '3', '2'],
['NW', 789000, '4', '4'],
['SE', 339000, '4', '4'],
['NE', 284900, '4', '4'],
['NW', 520000, '4', '4'],
['NW', 674900, '3', '2'],
['NE', 499900, '3', '3'],
['NE', 489000, '4', '2'],
['SE', 399900, '2', '3'],
['SE', 420000, '3', '1'],
['NW', 559000, '3', '3'],
['NE', 339900, '4', '4'],
['SW', 639900, '4', '3'],
['SE', 585000, '4', '4'],
['NE', 585000, '4', '4'],
['NE', 799999, '4', '3'],
['NE', 500000, '3', '3'],
['SW', 629900, '4', '3'],
['SE', 395000, '3', '3'],
['SW', 759990, '5', '2'],
['NE', 549900, '3', '3'],
['NW', 599900, '3', '3'],
['SW', 449000, '2', '2'],
['SW', 4500000, '5', '9'],
['SW', 799900, '3', '4'],
['SE', 525000, '3', '3'],
['NW', 869900, '5', '4'],
['SE', 489999, '3', '2'],
['SW', 269000, '2', '1'],
['NW', 828000, '4', '4'],
['NE', 1388000, '6', '5'],
['SE', 699900, '4', '4'],
['NE', 579000, '4', '3'],
['NW', 799900, '4', '4'],
['NE', 329500, '2', '2'],
['NE', 300000, '2', '1'],
['NW', 774900, '4', '3'],
['NE', 499000, '3', '2'],
['NW', 1388800, '4', '4'],
['SW', 538900, '4', '3'],
['NE', 669000, '5', '5'],
['SW', 799900, '4', '3'],
['NW', 1110000, '6', '4'],
['SW', 1165000, '3', '4'],
['SW', 1099900, '4', '4'],
['NW', 895000, '3', '2'],
['SE', 633000, '4', '2'],
['SE', 519900, '5', '4'],
['SW', 799999, '4', '2'],
['NW', 575000, '4', '5'],
['NE', 619000, '4', '4'],
['NW', 748000, '3', '4'],
['NW', 319900, '2', '1'],
['NW', 634900, '2', '3'],
['SE', 550000, '5', '2'],
['NW', 439900, '2', '3'],
['SE', 469900, '4', '1'],
['SW', 629900, '3', '4'],
['SE', 349900, '1', '1'],
['NE', 539900, '3', '2'],
['NE', 849000, '6', '5'],
['SW', 1150000, '4', '4'],
['SE', 349000, '3', '1'],
['NW', 749999, '5', '3'],
['SW', 729900, '2', '2'],
['SW', 1150000, '4', '3'],
['SE', 660000, '2', '2'],
['SE', 700000, '4', '4'],
['NW', 1199900, '5', '4'],
['NW', 539900, '2', '2'],
['SW', 590000, '2', '3'],
['SW', 899000, '2', '2'],
['SW', 359000, '1', '1'],
['NW', 880000, '4', '4'],
['SW', 269900, '1', '1'],
['SE', 514900, '3', '2'],
['NE', 1450000, '4', '4'],
['NW', 2199000, '6', '8'],
['NW', 314900, '2', '2'],
['NE', 495000, '3', '3'],
['NW', 600000, '3', '3'],
['NW', 775000, '3', '3'],
['NE', 324900, '3', '2'],
['SW', 784900, '4', '4'],
['NW', 697200, '3', '3'],
['SW', 1280000, '4', '4'],
['NW', 324900, '4', '4'],
['SW', 998500, '2', '1'],
['SW', 194999, '1', '1'],
['SW', 314900, '1', '1'],
['NW', 839000, '5', '3'],
['SW', 962560, '4', '4'],
['NE', 1100000, '5', '3'],
['NE', 599000, '3', '3']
]
