import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS

def load_data(path):
  try:
    data = pd.read_excel(path)
  except:
    data = pd.read_csv(path)
  return data

def preprocess_ln(ln_cols, data):
  for col in ln_cols:
    data[f"ln({col})"] = np.log(data[col])
  return data

def linear_regression(iv_lst, dv, data):
  formula = f"{dv} ~ {'+'.join(iv_lst)}"
  model = smf.ols(formula, data)
  result = model.fit()
  print(result.summary())

def instrument_ols(iv, dv, instrument, data):
  data_ = data.copy()
  dependent = data_[dv]
  data_['const'] = 1
  exog = data_['const']
  endog = data_[iv]
  instruments = data_[iv]
  model = IV2SLS(dependent=dependent, exog=exog, endog=endog, instruments=instruments)
  result = model.fit()
  print(result.summary)

def panel_ols(iv_lst, dv, fixed_entity, fixed_time, data):
  data_ = data.copy()
  data_ = data_.set_index([fixed_entity, fixed_time])
  formula_1 = f"{dv} ~ 1 + {'+'.join(iv_lst)} + EntityEffects"
  formula_2 = f"{dv} ~ 1 + {'+'.join(iv_lst)} + EntityEffects + TimeEffects"
  model_1 = PanelOLS.from_formula(formula=formula_1, data=data_)
  model_2 = PanelOLS.from_formula(formula=formula_2, data=data_)
  print("###### Fixed Entity Effects ######")
  print(model_1.fit())
  print("\n ###### Fixed Time Effects ######")
  print(model_2.fit())
