# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:16:36 2022

@author: aaron
"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class HCDefaultFeatureEngineer(BaseEstimator, TransformerMixin):
    
    def __init__(self, featengineer):
        self.featengineer = featengineer
        self.feature_set = ''
    
        
    def fit(self, X, y=None):
        return(self)
    
    
    def transform(self, X, y=None):
        
        out = X.copy()
        
        def edu_code(education):
                if education == 'Academic degree':
                    return 1
                elif education == 'Higher education':
                    return 2
                elif education == 'Incomplete higher':
                    return 3
                elif education == 'Secondary / secondary special':
                    return 4
                elif education == 'Lower secondary':
                    return 5
                else:
                    return 6
                
        def marital_code(marital_status):
            if marital_status == 'Widow':
                return 1
            elif marital_status == 'Married':
                return 2
            elif marital_status == 'Separated':
                return 3
            elif marital_status == 'Civil marriage':
                return 4
            elif marital_status == 'Single / not married':
                return 5
            else:
                return 6
        
        if self.featengineer == 'experiment_a':
        
        
            out['ind_cash_loan'] = out['name_contract_type'].apply(lambda x: 1 if x == 'Cash loans' else 0)
            out['ind_male'] = out['code_gender'].apply(lambda x: 1 if x == 'M' else 0)
            out['ind_own_car'] = out['flag_own_car'].apply(lambda x: 1 if x == 'Y' else 0)
            out['ind_own_realty'] = out['flag_own_realty'].apply(lambda x: 1 if x == 'Y' else 0)
            out['age'] = out.days_birth / -365
            out['credit_income_ratio'] = out.amt_credit / out.amt_income_total
            out['credit_amt_goods_diff'] = out.amt_credit - out.amt_goods_price
            out['years_employed'] = out.days_employed / -365
            out['years_employed'] = out.years_employed.apply(lambda x: x if x > 0 else np.NaN)
            out['age_started_at_job'] = out.age - out.years_employed
            out['perc_life_at_job'] = out.years_employed / out.age
            out['days_birth_registration_diff'] = out.days_birth - out.days_registration
            out['days_birth_employed_diff'] = out.days_birth - out.days_employed
            out['days_birth_id_publish_diff'] = out.days_birth - out.days_id_publish
            out['education_level'] = out.name_education_type.apply(lambda x: edu_code(x))
            out['marital_status'] = out.name_family_status.apply(lambda x: marital_code(x))
            

            
            incl = ['ind_cash_loan', 'ind_male', 'ind_own_car', 
                    'ind_own_realty', 'cnt_children', 'amt_income_total', 'amt_credit',
                    'amt_goods_price', 'age', 'flag_phone', 'flag_email',
                    'cnt_fam_members', 'region_rating_client', 'region_rating_client_w_city',
                    'reg_city_not_live_city', 'ext_source_2', 'days_last_phone_change',
                    'flag_document_3', 'flag_document_6', 'credit_income_ratio',
                    'credit_amt_goods_diff', 'days_employed', 'age_started_at_job',
                    'days_id_publish', 'days_registration', 'days_birth_registration_diff',
                    'days_birth_employed_diff', 'days_birth_id_publish_diff', 
                    'education_level', 'marital_status']
            
            self.feature_set = incl
            out = out[incl]
            
        if self.featengineer == 'experiment_b':
            
        
            out['ind_cash_loan'] = out['name_contract_type'].apply(lambda x: 1 if x == 'Cash loans' else 0)
            out['ind_male'] = out['code_gender'].apply(lambda x: 1 if x == 'M' else 0)
            out['ind_own_car'] = out['flag_own_car'].apply(lambda x: 1 if x == 'Y' else 0)
            out['ind_own_realty'] = out['flag_own_realty'].apply(lambda x: 1 if x == 'Y' else 0)
            out['age'] = out.days_birth / -365
            out['credit_income_ratio'] = out.amt_credit / out.amt_income_total
            out['credit_amt_goods_diff'] = out.amt_credit - out.amt_goods_price
            out['years_employed'] = out.days_employed / -365
            out['years_employed'] = out.years_employed.apply(lambda x: x if x > 0 else np.NaN)
            out['age_started_at_job'] = out.age - out.years_employed
            out['perc_life_at_job'] = out.years_employed / out.age
            out['days_birth_registration_diff'] = out.days_birth - out.days_registration
            out['days_birth_employed_diff'] = out.days_birth - out.days_employed
            out['days_birth_id_publish_diff'] = out.days_birth - out.days_id_publish
            out['education_level'] = out.name_education_type.apply(lambda x: edu_code(x))
            out['marital_status'] = out.name_family_status.apply(lambda x: marital_code(x))
            

            
            incl = ['ind_cash_loan', 'ind_male', 'ind_own_car', 
                    'ind_own_realty', 'cnt_children', 'amt_income_total', 'amt_credit',
                    'amt_goods_price', 'age', 'flag_phone', 'flag_email',
                    'cnt_fam_members', 'region_rating_client', 'region_rating_client_w_city',
                    'reg_city_not_live_city', 'ext_source_2', 'days_last_phone_change',
                    'flag_document_3', 'flag_document_6', 'credit_income_ratio',
                    'credit_amt_goods_diff', 'days_employed', 'age_started_at_job',
                    'days_id_publish', 'days_registration', 'days_birth_registration_diff',
                    'days_birth_employed_diff', 'days_birth_id_publish_diff', 
                    'education_level', 'marital_status', 'obs_60_cnt_social_circle',
                    'def_60_cnt_social_circle']
            
            self.feature_set = incl
            out = out[incl]
            
        return out
    
    
    # Failed Experiments
    # flag_emp_phone (actually does offer some performance gain but it's minimal)
    # number of address mismatches
    