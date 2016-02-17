"""
Download baby names from U.S. Social Security website and use historical frequency to predict gender
Feng Mai maifeng@gmail.com
2016-02-17
"""

import urllib.request
import os
from zipfile import ZipFile
import csv
import io


class simpleGenderPredictor():
    
    def __init__(self):
        self.name_dict = self.extractNamesDict()

    def downloadNames():
        urllib.request.urlretrieve(
            'https://www.ssa.gov/oact/babynames/names.zip', 'names.zip')

    def extractNamesDict(self):
        """
        download names.zip from SSA if necessary
        construct a dict from SSA name data: NAME: [number of M, number of F]
        """
        if not os.path.exists('names.zip'):
            print('names.zip does not exist, downloading from ssa.gov')
            self.downloadNames()
        else:
            print('names.zip exists, not downloading')
        zf = ZipFile('names.zip', 'r')
        filenames = zf.namelist()

        names = dict()
        genderMap = {'M': 0, 'F': 1}

        for filename in filenames:
            if filename.endswith('.txt'):
                file = zf.open(filename, 'r')
                rows = csv.reader(
                    io.TextIOWrapper(file, encoding="latin-1"), delimiter=',')

                for row in rows:
                    name = row[0].upper()
                    gender = genderMap[row[1]]
                    count = int(row[2])

                    if name not in names:
                        names[name] = [0, 0]
                    names[name][gender] = names[name][gender] + count
                file.close()
        print('name dictionary constructed')
        return names

    def predict_name(self, a_name):
        """
        Outputs a tuple: prediction, probability from historical data
        """
        freq = self.name_dict.get(a_name.upper())
        if freq is None:
            return 'Unknown'
        elif freq[0] >= freq[1]:
            return 'M', freq[0] / (freq[0] + freq[1])
        else:
            return 'F', freq[1] / (freq[0] + freq[1])
