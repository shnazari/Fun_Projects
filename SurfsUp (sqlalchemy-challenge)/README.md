# Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data
In this section, we’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of our climate database. Specifically, we’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. 

### Precipitation Analysis
1- We will find the most recent date in the dataset.
2- Using that date, we will get the previous 12 months of precipitation data by querying the previous 12 months of data.
3- And finally we will use libraries like Pandas and Matplotlib to create a graphiocal representation of the data.

### Station Analysis
1- We will design a query to calculate the total number of stations in the dataset.
2- We will design a query to find the most-active stations (that is, the stations that have the most rows). To do so, we complete the following steps:
	- List the stations and observation counts in descending order.
	- Answer the following question: which station id has the greatest number of observations?
3- We will design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4- We will design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, we complete the following steps:
	- Filter by the station that has the greatest number of observations.
	- Query the previous 12 months of TOBS data for that station.
	- Plot the results as a histogram

## Part 2: Climate App wil Flask API
We will design a Flask API based on the queries that you just developed. To do so, we use Flask to create the routes as follows:
	- Start at the homepage.
	- List all the available routes.
	- Return the JSON representation of your dictionary.
	- Return a JSON list of stations from the dataset.
	- Return a JSON list of temperature observations for the previous year.
	- Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
	
# References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xmlLinks.