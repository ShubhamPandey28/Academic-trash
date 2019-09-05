import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def read_data(path_to_file):
	""" Returns Pandas dataframe for given csv file
	
		Parameters
		----------
		path_to_file: string
			Given csv file
		
		Returns
		-------
		pandas.Dataframe
	"""
	data = pd.read_csv(path_to_file)
	return data

def show_box_plot(attribute_name,dataframe,save_image=False):
	""" Displays boxplot for atrribute

		Parameters
		----------
		attribute_name: string
			Attribute selected
		dataframe: pandas.Dataframe
			DataFrame for the given dataset
		save_image: bool
			For saving the plot as a jpeg image file
		Returns
		-------
		None
	"""
	plt.boxplot(list(data[attribute_name]))

	if save_image:
		plt.savefig("./plots/"+attribute_name+"_boxplot.jpeg")
	plt.show()



def replace_outliers(dataframe):
	""" Replaces the outliers in the given dataframe
	
		Parameters
		----------
		dataframe: pandas.Dataframe
			DataFrame for the given dataset
		Returns
		-------
		pandas.Dataframe
	"""

	pass
def range(dataframe,attribute_name):
	""" Gives Range of Selected Attribute
	
		Parameters
		----------
		attribute_name: string
			Attribute selected
		dataframe: pandas.Dataframe
			DataFrame for the given dataset
		Returns
		-------
		pair(float,float)
	"""
	pass
def min_max_normalization(dataframe,range=None):
	""" Returns normalized pandas dataframe
	
		Parameters
		----------
		dataframe: pandas.Dataframe
			Dataframe for the given dataset
		range: pair(float,float) 
			Normalize between range
		Returns
		-------
		pandas.Dataframe
	"""
	pass
def standardize(dataframe):
	""" Returns standardized pandas dataframe
	
		Parameters
		----------
		dataframe: pandas.Dataframe
			Dataframe for the given dataset
		Returns
		-------
		pandas.Dataframe
	"""
	pass

def main():
	""" Main Function
		Parameters
		----------
		
		Returns
		-------
		None
	"""
	path_to_file="Your_File_Path"
	dataframe=read_data(path_to_file)
	return

if __name__=="__main__":
	main()