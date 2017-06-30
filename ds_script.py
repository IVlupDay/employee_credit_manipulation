import numpy as np
import pandas as pd
import sklearn as skl 
import matplotlib.pyplot as plt
import os, csv, datetime, time, subprocess

from numpy import sqrt, pi, exp, linspace, loadtxt
from lmfit import Model
from scipy.optimize import curve_fit
from scipy import stats
from operator import itemgetter

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.metrics import mean_squared_error
from sklearn import svm, metrics 

from apply_ml import ApplyMethod

print "\n%%%%------------------ Loading Data -------------------%%%%\n"

csv = pd.read_csv("./credit_data_track2_part_A.csv", sep=',')
file_name = os.path.basename("./credit_data_track2_part_A.csv")

print "Data summary"
print "File name: "+file_name
print "Number of row: " +str(len(csv.values[:, 0]))
print "Number of column: "+str(csv.shape[1])
print "Total data elemnent: "+str(csv.size)+"\n"
print "Sample data on credit_amount column"
print "credit_amount: "+str(csv.values[:, 0])+"\n\n"

size_row = len(csv.values[:, 0])
size_column = csv.shape[1]

ApplyMethod(size_row)



print "\n%%%%---------------- Success Load Data ----------------%%%%\n"

