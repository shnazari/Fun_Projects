# Background
The UK Food Standards Agency evaluates various establishments across the United Kingdom, and gives them a food hygiene rating. You've been contracted by the editors of a food magazine, Eat Safe, Love, to evaluate some of the ratings data in order to help their journalists and food critics decide where to focus future articles.

# Part 1
In part onw we set up the database and jupyter notebook by importing the provided .json file in Resources folder.

# Part 2
he magazine editors have some requested modifications for the database before you can perform any queries or analysis for them. Based on this requests we make the following updates on the database:
	1 - An exciting new halal restaurant just opened in Greenwich, but hasn't been rated yet. The magazine has asked you to include it in your analysis. 
	2- The magazine is not interested in any establishments in Dover, so check how many documents contain the Dover Local Authority. Then, remove any establishments within the Dover Local Authority from the database, and check the number of documents to ensure they were deleted.
	
# Part 3
Eat Safe, Love has specific questions they want you to answer, which will help them find the locations they wish to visit and avoid.
Answer the following queries by exploring the database:
	1 - Which establishments have a hygiene score equal to 20?
	2 - Which establishments in London have a RatingValue greater than or equal to 4? 
	3 - What are the top 5 establishments with a RatingValue of 5, sorted by lowest hygiene score, nearest to the new restaurant added, "Penang Flavours"?
	4 - How many establishments in each Local Authority area have a hygiene score of 0? Sort the results from highest to lowest, and print out the top ten local authority areas.
	
# References
UK Food Standards AgencyLinks to an external site. (2022). UK food hygiene rating data API. https://ratings.food.gov.uk/open-data/en-GBLinks Contains public sector information licensed under the Open Government Licence v3.0 Accessed Sept 9, 2022 and Sept 12, 2022 with the establishment settings as follows: longitude=51.5072, latitude=-0.1276, maxdistancelimit=4567, pagesize=10000, sortoptionkey=distance, pagenumber=(1,2,3,4,5,6,7,8).