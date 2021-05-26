import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from linearmodels.panel import PanelOLS
from linearmodels.iv import IV2SLS

### data = df

def load_data(path):
  """
  파일 경로 -> 좌측에서 파일에 우클릭 경록 복사해서 붙여놓으면됨
  """
  try:
    data = pd.read_excel(path)
  except:
    data = pd.read_csv(path)
  return data

def preprocess_ln(ln_cols, data):
  """
  ln_cols 에 ln() 해줘야할 컬럼들 전부 아래와 같이 입력
  ['rob', 'mur' ,'vio']
  """
  for col in ln_cols:
    data[f"ln_{col}"] = np.log(data[col])
  return data

def linear_regression(iv_lst, dv, data):
  """
  iv_lst 에 독립변수들 리스트로 입력 ['col_a', 'col_b', ...]
  dv 에 타겟변수 스트링으로 입력 "target"
  """
  formula = f"{dv} ~ {'+'.join(iv_lst)}"
  print(formula)
  model = smf.ols(formula, data)
  result = model.fit()
  print(result.summary())

def instrument_ols(iv, dv, instrument, data):
  """
  iv: 스트링 (무조건 하나)
  dv: 스트링
  instrument: 스트링
  """
  data_ = data.copy()
  dependent = data_[dv]
  data_['const'] = 1
  exog = data_['const']
  endog = data_[iv]
  instruments = data_[iv]
  model = IV2SLS(dependent=dependent, exog=exog, endog=endog, instruments=instruments)
  result = model.fit()
  print(result.summary)

def panel_ols(iv_lst, dv, data, fixed_entity=None, fixed_time=None):
  """
  iv_lst : 독립변수 리스트
  dv: 타겟변수 스트링
  ### panel data section ###
  fixed_entity: entity 변수
  fixed_time: time 변수
  """
  # data_ = data.copy()
  formula_1 = f"{dv} ~ 1 + {'+'.join(iv_lst)} + EntityEffects"
  formula_2 = f"{dv} ~ 1 + {'+'.join(iv_lst)} + TimeEffects"
  formula_3 = f"{dv} ~ 1 + {'+'.join(iv_lst)} + TimeEffects + EntityEffects"
  if fixed_entity is not None:
    data_ = data.set_index([fixed_entity, fixed_time])
    model_1 = PanelOLS.from_formula(formula=formula_1, data=data_)
    print("###### Fixed Entity Effects ######")
    print(model_1.fit())
  if fixed_time is not None:
    data_ = data.set_index([fixed_entity, fixed_time])
    model_2 = PanelOLS.from_formula(formula=formula_2, data=data_)
    print("\n ###### Fixed Time Effects ######")
    print(model_2.fit())
  if (fixed_entity is not None) and (fixed_time is not None):
    data_ = data.set_index([fixed_entity, fixed_time])
    print("\n ###### Fixed Entity & Time Effects ######")
    model_3 = PanelOLS.from_formula(formula=formula_3, data=data_)
    print(model_3.fit())
