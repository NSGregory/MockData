"""Turns out the to_excel function of dataframes solves most of the issues here making this a small class.
   If the original file has multiple tabs being analyzed, the output file will include each of those tabs as separate
   output tabs.
    """
import pandas as pd

from data_reader import dataReader
from data_faker import Faker
from gui import selectFile
from dataframe_compiler import dfCompiler
from name import Name


class excelGenerator:

    def __init__(self, group):
        self.group = group

    def add(self, assignments):
        pass

    def save(self, filename):
        """Assumes self.group is a dict containing one ore more pandas dataframes.
        Uses pandas.ExcelWriter to save an excel file.
        If multiple keys are present in the dict, each will be assigned to a new tab in the output file. """
        writer = pd.ExcelWriter(filename+".xlsx")
        self.group.to_excel(writer)
        writer.save()

        #df.to_excel("filename.xlsx")


if __name__=='__main__':
    # more legible feedback using the rich library
    from rich.traceback import install
    install(show_locals=True)

    #skipping gui here to make development faster
    #reinstate for ease of use post development
    #from gui import selectFile
    #file = selectFile.byGui()
    faker = Faker(200)
    file = selectFile.byGui()
    out_filename = Name.outputFile(file)
    data = dataReader(file)
    wkbk = data.wkbk
    df = dfCompiler(wkbk)
    output = df.filled_dataframe
    generator = excelGenerator(output)
    generator.save(out_filename)