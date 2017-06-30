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

class ApplyMethod:
    def __init__(self, data):
        self.data = data
        self.apply_method(data)
    
    def apply_method(self, data):
        """
        print "ok, now appl_method with data:"
        print data
        """
        
      
        