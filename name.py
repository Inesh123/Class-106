import plotly.express as px
import csv
import numpy as np
def getdatasource(data_path):
    ice_creamsales=[]
    temperature=[]
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row['Temperature']))
            ice_creamsales.append(float(row['Ice-cream']))
    return{'x':temperature,'y':ice_creamsales}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between temperature vs ice_creamsales:',correlation[0,1])
def setup():
    data_path = './Ice-cream.csv'
    datasource = getdatasource(data_path)
    findcorrelation(datasource)
setup()