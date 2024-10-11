#Calling out the funtion to plot graph and also interact with our dataset
import matplotlib.pyplot as pp
import pandas as pd


#accesing the file containing our dataset
pp.style.use('grayscale')
datatable = pd.read_csv('Female_Population_by_Age_Group.csv')

x = datatable['Age_Group']
y = datatable['Number']

# #plotting Bar Chart
pp.figure(figsize=(13, 8))
pp.title('Graph showing distribution of females over age groups in Ghana')
pp.xlabel('Ages')
pp.ylabel('Population')
pp.bar(x,y)
pp.show()

