import csv
import gmplot

    
import csv
with open('heritage_sites.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        heritagesite = [row['Address'], row['Latitude'], row['Longitude']]
        coordinates = [heritagesite[1], heritagesite[2]]
        print(coordinates)
