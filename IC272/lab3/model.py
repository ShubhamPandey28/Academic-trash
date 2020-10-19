import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.preprocessing as sp
import math

class data_analysis_model(object):

    def __init__(self,dataframe):
        self.size = len(dataframe)
        self.dataframe = dataframe
        self.attributes = list(dataframe.columns)
    
    def range(self,attribute_name):

        l = list(self.dataframe[attribute_name])
        l.sort()
        q3 = l[int(0.75*(self.size))]
        q1 = l[int(0.25*(self.size))]

        iqr = q3-q1

        return [q1-1.5*iqr,q3+1.5*iqr]


    def replace_outliers_by_median(self,attribute_name):
        median = self.dataframe[attribute_name].median()
        mn, mx = self.range(attribute_name)

        for i in range(self.size):
            if self.dataframe[attribute_name][i] < mn or self.dataframe[attribute_name][i] > mx:
                self.dataframe[attribute_name][i] = median


    def boxplot(self,attribute_name,show=True,savefig=False):
        plt.boxplot(self.dataframe[attribute_name])
        plt.title(attribute_name)
        if show:
            plt.show()
        if savefig:
            plt.savefig("./plots/"+attribute_name+"_boxplot.jpeg")
    
    def boxplot_all(self,savefig=False):
        l = len(self.attributes)
        m = math.ceil(l**0.5)
        plt.figure()

        for i in range(l):
            plt.subplot(m,m,i+1)
            plt.boxplot(self.dataframe[self.attributes[i]])
            plt.title(self.attributes[i])
        
        if savefig:
            plt.savefig("./plots/all_boxplots.jpeg")

    def replace_outliers_by_median_all(self):
        for att in self.attributes:
            self.replace_outliers_by_median(att)

    def min_max_normalization(self,new_min,new_max,attribute_name):
        # v' = (v-mn)*(new_mx-new_mn)/(mx-mn) + new_mn;
        mn = min(self.dataframe[attribute_name])
        mx = max(self.dataframe[attribute_name])
        if mn != mx:
            for i in range(self.size):
                self.dataframe[attribute_name][i] = (self.dataframe[attribute_name][i]-mn)*(new_max-new_min)/(mx-mn) + new_min
    
    def standardize_attribute(self,attribute_name):
        mean = self.dataframe[attribute_name].mean()
        sigma = self.dataframe[attribute_name].std()
        for i in range(self.size):
            self.dataframe[attribute_name][i] = (self.dataframe[attribute_name][i]-mean)/sigma
    

class data_analysis_model_sklearn(object):

    def __init__(self,dataframe):
        self.dataframe = dataframe
    
    def min_max_scaler(self,attribute_name,new_min,new_max):
        scaled = sp.minmax_scale(np.array(self.dataframe[attribute_name]),feature_range=(new_min,new_max))
        return scaled

    def standardize(self,attribute_name):
        
        return sp.scale(self.dataframe[attribute_name])

