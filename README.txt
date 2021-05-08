		Angel Rating Prediction System

Description:
	
	this is basically a part of our Final Year Project which recomends angel(our representitive) based on rating. Angel help customer in 
	buying their favourite products at resonable rate and also get them quality products. And after that user will give the angel 3 ratings

	1- How much time angel spend with user to help them find their desired product
	2- How much shops are visited by angel and customer
	3- What rating would you(user) give to the angel.


	and based on these 3 things our model will give average rating to the angel.


1- Data Gathering:
	
	Since there is no dataset on internet that takes 3 things(minutes,shopsvisited,rating) we have to make our own dataset.
	
	if angel spend only 20 minutes it will count as 1 rating in minutes section.if angel spend only 20-59 minutes it will count as 2 rating in minutes section.
	and so on.
	
	Minutes
	0-20(1)
	20-50(2)
	50-80(3)
	80-110(4)
	110-140(5)

	if angel visited only 1 shop it will count as 1 rating in Shops Visited section. if angel visited only 2 shop it will count as 2 rating in Shops Visited section.
	and so on.

	Shops Visited:
	1-(1)
	2-(2)
	3-(3)
	4-(4)
	5-(5)

	if user give only 1 rating to angel it will count as 1 rating in Rating section.if user give only 2 rating to angel it will count as 2 rating in Rating section.
	and so on.


	Rating:
	1
	2
	3
	4
	5

	so we prepare our dataset accordingly

2-   Test Train Split:
	
	the dependent variable will be three columns in dataset those are (minutes,shopsvisited,rating) and non dependent variable are OverallRating(average).
	we divide our dataset into 80% train data and 20% test data.

3-   Cleaning of Dataset:


	We have around 800 rows and 6 columns and are all added manually so our data is clean without any null values, or any other bad things.

4-   Applying of algoritgm:
	

	After applying bunch of algorithms. the one with the best accuracy is Random Forest Classifier which gives us the accuracy of 99%.