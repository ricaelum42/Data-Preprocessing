import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


class data_preprocess:
    def __init__(self, X_train=None, y_train=None, X_test=None, y_test=None):
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.quality_report = None
        self.imp = None
        
    def check(self):
        print(self.X_train.head())
        
    def get_quality_report(self, lower=0.01, upper=0.99):
        
        temp = self.X_train.select_dtypes(include = ['float64', 'int64'])
        
        self.quality_report = pd.DataFrame(index=temp.columns)
        self.quality_report = self.quality_report.join(temp.mean().to_frame(name='Mean'))
        self.quality_report = self.quality_report.join(temp.median().to_frame(name='Median'))
        self.quality_report = self.quality_report.join(temp.var().to_frame(name='Std'))
        self.quality_report = self.quality_report.join(temp.isnull().sum().to_frame(name='MissingRate') / temp.shape[0])
        self.quality_report = self.quality_report.join(temp.quantile(lower).to_frame(name='LowerQuantile'))
        self.quality_report = self.quality_report.join(temp.quantile(upper).to_frame(name='UpperQuantile'))
        
        display(self.quality_report)
        return self.quality_report
    
    def fill_na(self, strategy='median', columns=None):
        if columns is None:
            temp = self.X_train.select_dtypes(include = ['float64', 'int64'])
        else:
            temp = self.X_train[columns].select_dtypes(include = ['float64', 'int64'])
            
        imp = SimpleImputer(missing_values=np.nan, strategy=strategy)        
        imp.fit(temp)  
        self.imp = imp
        self.X_train[temp.columns] = imp.transform(temp) 
        
        if self.X_test is not None:
            self.X_test[temp.columns] = imp.transform(self.X_test[temp.columns])
            
    def fill_outlier(self, columns=None):
        if columns is None:
            temp = 
            
        
