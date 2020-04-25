import fiona
import shapely
from pathlib import Path
print(Path.cwd())

data_path = "/home/navneet/Documents/shapely_fiona_tutorial/data/all.shp" 
#read the data 
vector_file = fiona.open(data_path)
#show the driver(in which format the file is )
driver = vector_file
print("the  driver of the file is " + str(driver))
#now to show the schema of the file(schema - > tabel attribute)
schema=vector_file.schema
print("schema of the vector file")
print(schema)
#show the coordinate system of the vector file
crs=vector_file.crs
print("coordiate system of the vector file")
print(crs)

#shapely example

#how to write a vector file suppose we have a csv file 
from shapely.geometry import Point, mapping

#for write a vector file form csv file we have two step 
#1step create the scheme
#2step crete the coordinate system

#1step

schema={'geometry':'point',
       'properties':{'labe':'str',
                    'easting_xcord':'float',
                    'notherning':'float',
                    'elevation':'float'}}

#from_epsg('crs code')
crs=from_epsg(32643)

import csv
with open('demo_test_data.csv', 'r') as file:  #read the csv file
    csv_file = csv.reader(file)
    for row in csv_file:
        print(row)#print every row of csv file

#open the csv file  in reading mode
with open('demo_test_data.csv', 'r') as file:
    csv_file = csv.reader(file)
    with fiona.open('output.shp', 'w', driver='shapefile', crs=crs, schema=schema) as soource:#output file with writing mode
        for row in csv_file:
            Point = Point(float(row[1]), float(row[2]))#row[1]->column1 and similarly row[2] -> col2
            source.write('geometry':mapping[point],
                        'properties':{'label':row[0],
                                     'easting_xcord':float(row[1]),
                                     'northing_ycord':float(row[2]),
                                     'elevation':float(row[3])})
            
#after this a output file is created in shape format
#you can see these file in qgis