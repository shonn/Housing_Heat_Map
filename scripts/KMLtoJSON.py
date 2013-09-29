'''
Created on Sep 25, 2013
Grabs the data we want from the KML and converts it into a format friendly to mysqlimport
Polygons are defined in JSON arrays
@author: hehahohee
'''

from pykml import parser
from os import path
import re

kml_file = path.join("/Applications/XAMPP/htdocs/CS157A/HousingPriceHeatMap/zipcodes.kml")
with open(kml_file) as f:
    doc = parser.parse(f)
root = doc.getroot()
outf = open('zipJSON.txt','w')
for placemark in root.Document.Folder.Placemark:
    if(re.match('^\\d+$', placemark.name.text)):
        print placemark.name.text;
        jsonShapePath = "["
        if(hasattr(placemark,"Polygon")):
            jsonShapePath += "[[" + placemark.Polygon.outerBoundaryIs.LinearRing.coordinates.text.replace(",", "],[") +"]]"
            jsonShapePath = jsonShapePath.replace(" ", ",")
        elif(hasattr(placemark, "MultiGeometry")):
            for polygon in placemark.MultiGeometry.Polygon:
                jsonShapePath += "[[" + polygon.outerBoundaryIs.LinearRing.coordinates.text.replace(",", "],[") +"]]"
        jsonShapePath += "]"
        outf.write(placemark.name.text + '\t' + jsonShapePath +'\n');
outf.close()