"""
    Module for basic stocks info filtering.
    Analyzed basic information based on current stock info retrieved from YF.

    Setting differrnt criteria
    one for dividend
    one for high growth

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
        ## file path
        self.data_fname = fname
        self.criteria_type = '' # determine the type of criteria to use
        self.criteria_folder_path = r'C:\pythonuserfiles\Stocks_data_filter\criteria'
        self.criteria_type_path_dict = {
                                        'dividend'  : os.path.join(self.criteria_folder_path, 'dividend.txt'),
                                        'popular'   : os.path.join(self.criteria_folder_path, 'popular.txt'),
                                        'target'    : os.path.join(self.criteria_folder_path, 'target.txt'),
                                        }

        self.criteria_fname = r'C:\pythonuserfiles\Stocks_data_filter\basic_filter_criteria.txt'


        ## output -- will be catered according to the input criteria type
        self.modified_file_path = r'c:\data'
        self.modified_fname = r''

        # parameters -- create dataframe object
        self.data_df = pandas.read_csv(self.data_fname)
        
    def set_criteria_type(self, criteria_type):
        """ Set the criteria type. Criteria type must be one of the keys in the self.criteria_type_path_dict.
            Use to select the different criteria file.
            Args:
                criteria_type (str): criteria type
        """
        assert criteria_type in self.criteria_type_path_dict.keys()
        self.criteria_type =  criteria_type

    def print_all_availiable_criteria(self):
        print self.criteria_type_path_dict.keys()

    def get_all_criteria_fr_file(self):
        """ Created in format of the dictparser.
            Dict parser will contain the greater, less than ,sorting dicts for easy filtering.
            Will parse according to the self.criteria_type

            Will also set the output file name
        """
        self.dictparser = DictParser(self.criteria_type_path_dict[self.criteria_type])
        self.criteria_dict = self.dictparser.dict_of_dict_obj
        self.modified_df = self.data_df

        self.set_output_file()

    def set_output_file(self):
        """ Set the output file according to the critiera type chosen.

        """
        self.modified_fname = os.path.join(self.modified_file_path, self.criteria_type + '_data.csv')
        
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
    ss =  InfoBasicFilter(r'c:\data\full_Aug_26.csv')
    ss.set_criteria_type('popular')
    ss.get_all_criteria_fr_file()
    ss.process_criteria()
    ss.send_modified_to_file()
    
    