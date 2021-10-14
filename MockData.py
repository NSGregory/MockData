import pandas as pd

from data_reader import dataReader
from data_faker import Faker
from gui import selectFile
from dataframe_compiler import dfCompiler
from name import Name
from excel_generator import excelGenerator

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