'''
Created on Sep 29, 2013
Uses Well Known Text so that polygons can be imported as Geometry by MySQL
@author: hehahohee
'''
from pykml import parser
from os import path
import re

kml_file = path.join("/Applications/XAMPP/htdocs/CS157A/HousingPriceHeatMap/zipcodes.kml")
with open(kml_file) as f:
    doc = parser.parse(f)
root = doc.getroot()
outf = open('zipGeometry.txt','w')
for placemark in root.Document.Folder.Placemark:
    if(re.match('^\\d+$', placemark.name.text)):
        print placemark.name.text
        output = "GeomFromText('"
        if(hasattr(placemark,"Polygon")):
            output += "POLYGON((" + placemark.Polygon.outerBoundaryIs.LinearRing.coordinates.text +"))"
        elif(hasattr(placemark, "MultiGeometry")):
            output += "MULTIPOYGON("
            for polygon in placemark.MultiGeometry.Polygon:
                output += "((" + polygon.outerBoundaryIs.LinearRing.coordinates.text +")),"
            output = output[:-1]
            output +=')'
        output += "')"
        outf.write(placemark.name.text + '\t' + output +'\n');
outf.close()