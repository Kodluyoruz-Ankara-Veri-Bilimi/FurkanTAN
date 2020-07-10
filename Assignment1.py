#
#  Created by Furkan TAN
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Data:

    def __init__(self, filePath):
        self.data = pd.read_csv(filePath)

    def getHead(self):
        return self.data.head()

    def getShape(self):
        return self.data.shape

    def getInfo(self):
        return self.data.info()

    def getDescribe(self):
        return self.data.describe()

    def showScatterPlot(self, labelX, labelY):
        sns.scatterplot(data=self.data, x=labelX, y=labelY)
        plt.show()

    def showCorrelationMap(self):
        sns.heatmap(self.data.corr(), annot=True)
        plt.show()
