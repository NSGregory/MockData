import pandas as pd
from data_reader import dataReader
from data_faker import Faker
from gui import selectFile

class dfCompiler():

    def __init__(self, wkbk):
        self.default_mean = 100
        self.default_stdev = 15
        self.default_percentage = 67
        self.default_n = 200
        self.wkbk = wkbk
        self.filled_dataframe = self.build_random_dataset()

    def build_random_dataset(self):
        wkbk = self.wkbk
        filled_dataset = pd.DataFrame()
        columns = wkbk.columns
        faker = Faker(self.default_n)
        for entry in columns:
            pd_column = wkbk[entry]
            if pd_column[0] == 'Nominal':
                #print("add nominal dataset")
                filled_dataset[entry]=faker.synthesize_strings()
            elif pd_column[0] == 'Continuous' or pd_column[0] == 'Continous':
                #print("adding continuous dataset")
                if len(pd_column) > 1 and type(pd_column[1]) == str:
                    #print(f"{pd_column[1]} content for {entry}")
                    args = pd_column[1].split()
                    if len(args) == 2:
                        #clean up args
                        args = [x.strip() for x in args]
                        args = [x.replace(',','') for x in args]
                        args = [float(x) for x in args]
                        print(f"{args} for {entry}")
                        filled_dataset[entry]=faker.synthesize_continuous(*args)
                    else:
                        print(f"Incorrect number of arguments supplied for: {entry}")
                        print("Using default values")
                        filled_dataset[entry] = faker.synthesize_continuous(self.default_mean, self.default_stdev)
                else:
                    filled_dataset[entry] = faker.synthesize_continuous(self.default_mean, self.default_stdev)
            elif pd_column[0] == 'Categorical':
                if len(pd_column) > 2 and pd_column[1] > 0:
                    args = pd_column[1]
                    if args:
                        filled_dataset[entry]=faker.synthesize_boolean(args)
                    else:
                        print(f"Incorrect number of arguments supplied for: {entry}")
                        print("Using default values")
                        filled_dataset[entry] = faker.synthesize_boolean(self.default_percentage)
                else:
                    filled_dataset[entry] = faker.synthesize_boolean(self.default_percentage)
            else:
                print(f"{entry} has type {pd_column[0]} which is not supported")
                print("Currently 'Nominal', 'Continuous', and 'Categorical' are supported")

        return filled_dataset







if __name__=='__main__':
    # more legible feedback using the rich library
    from rich.traceback import install
    install(show_locals=True)

    #skipping gui here to make development faster
    #reinstate for ease of use post development
    from gui import selectFile
    file = selectFile.byGui()
    faker = Faker(200)
    data = dataReader(file)
    wkbk = data.wkbk

    df = dfCompiler(wkbk)

