import pandas as pd

class TratamentoDados:

    def __init__(self, path):
        self.dataFrame = pd.read_csv(path)

    def showColumns(self):
        return self.dataFrame.columns.tolist()

    def header(self):
        return self.dataFrame.head()

    def removeEmpysValues(self, *args):
        self.alterDataFrame = self.dataFrame.copy()

        for element in args:
            self.alterDataFrame[element].dropna(inplace=True)
                
        return self.alterDataFrame

    def changInvalidToMean(self, *args):
        self.alterDataFrame = self.dataFrame.copy()

        for element in args:
            if element in self.alterDataFrame.columns:
                self.alterDataFrame[element] = self.alterDataFrame[element].fillna(self.alterDataFrame[element].mean())
            else:
                print("invalid column")

        return self.alterDataFrame
    
