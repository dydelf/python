Project Population

This is a simple project intended to be grown into a full web application over
time. New functionalities will be added in the future.


Idea:
Constantly increasing population in the world is creating more and more
problems globally leading to unsustainable situation on our planet. Is this
growth constant or is it going to stop at some point in time?

Using basic correlations between population number, fertility rate and GDP we
are going to explore how they influence each other. What is the gradient over
time? Why in some regions gradient is lower and others higher? How the 
situation is going to look like in the next years? Using machine learning and
data visualisation techniques we are going to answer this questions and a lot
more.


Functions:
1. program will connect to DataHub API and download relevant data
2. data will be then cleaned and saved in a separate file
3. functions will make necessary calculations on the data
4. using machine learning program will predict future outcomes based on the
   data provided
5. data will be visualized for easier interpretation


Assumptions:
Fertility rate is correlated to GDP and differs for each country. Over time it
slows down and even drops below 2.0 in some cases. At some point assuming that
all countries are going to grow economically at the rate countable using 
machine learning we will have situation where FR will be going closer and 
closer to 2.0. This will give us a measurable stable population number with a 
little variance. Our aim is to calculate when this will happen and what will be
the number of people living in the world at this point in time.

This model does not include probability for any major event like war, crisis or
pandemia. Assumption is that the growth will stay at the stable rate in the
next years. This makes the model more and more unpredictable over time but
quite accurate for the nearest years.

The model by no means include all the data that could be taken into account
creating the prediction. They can be added in the future creating more and
more accurate prediction.


Logic:
GDP / up - fertility rate \ down - population \ down
years / up - gradient population \ down
with time population striving to one number with little variance

