"""
    Module for basic stocks info filtering.
    Analyzed basic information based on current stock info retrieved from YF.

    Required:
        Dict_create_fr_text
        

"""
import os, sys, re, time, datetime
import pandas
from Dict_create_fr_text import DictParser

class InfoBasicFilter(object):
    """ Basic info filter by getting the curr stocks information for filtering.

    """
    def __init__(self, fname):
        """ Pass in the basic stock info for the analysis.

        """
        # file path
        self.data_fname = fname
        self.criteria_fname = r'C:\pythonuserfiles\Stocks_data_filter\basic_filter_criteria.txt'
        self.modified_fname = r'c:\data\modifiedoutput.csv'

        # parameters
        # will str away get all the criteria
        self.dictparser = DictParser(self.criteria_fname)
        self.criteria_dict = self.dictparser.dict_of_dict_obj
        self.data_df = pandas.read_csv(self.data_fname)
        self.modified_df = self.data_df

    def get_all_criteria_fr_file(self):
        """ Created in format of the dictparser.
            Dict parser will contain the greater, less than ,sorting dicts for easy filtering.
            may not need as str away create the critiera
        """

    def process_criteria(self):
        """ Process the different criteria generated.
            Present only have more and less
        """
        # for greater
        greater_dict =  self.criteria_dict['greater']
        less_dict =  self.criteria_dict['less']

        for n in greater_dict.keys():
            self.modified_df = self.modified_df[self.modified_df[n] > float(greater_dict[n][0])]

        for n in less_dict.keys():
            self.modified_df = self.modified_df[self.modified_df[n] < float(less_dict[n][0])]

    def send_modified_to_file(self):
        """ Save the modified df to csv.

        """
        self.modified_df.to_csv(self.modified_fname, index = False)


if __name__ == '__main__':
    print
    ss =  InfoBasicFilter(r'c:\data\full1.csv')
    print ss.dictparser.dict_of_dict_obj
    ss.process_criteria()
    ss.send_modified_to_file()
    
    