#!/usr/bin/env python
import Quandl
import string

"""This script pulls real estate data"""

count = 0
with open('zipcodes.bak', 'r') as zipfile, open('dataset5.txt', 'w') as datafile:
  for zipcode in zipfile:
    zipcode = zipcode.rstrip()
    if count == 9000:
      break
    print zipcode
    try:
      data_object = Quandl.get('ZILLOW/ZIP_ALLHOMES_' + zipcode, collapse='annual', rows=17)
    except:
      print (zipcode + " skipped.\n")
      continue
    count += 1
    dataset = str(data_object)
    dataset = string.split(dataset, '\n')
    for data in dataset:
      if "Value" in data or "Date" in data:
        continue
      datafile.write(zipcode + " " + data + "\n")
zipfile.close()
datafile.close()

