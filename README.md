---
# Overview
This package wraps python libraries (statsmodels, pandas.. etc) for specific econometrics statistical modeling.

# Install

```powershell
pip install git+https://github.com/seungwoo-h/econometrics_calculator.git
```

## Usage

```python
from econometrics_stats import (
                            load_data, 
                            preprocess_ln, 
                            linear_regression,
                            instrument_ols, 
                            panel_ols
                              )

# Data load
df = load_data(path='path')

# Preprocess ln()
df_1 = preprocess_ln(ln_cols=['vio'], 
                     data=df_original)

# Linear regression
# prints out OLS reg result
linear_regression(iv_lst=['shall'], 
                  dv='ln_vio', 
                  data=df_1) 
                  
linear_regression(iv_lst=['shall', 'incarc_rate', 'density', 'avginc', 'pop', 'pb1064', 'pw1064', 'pm1029'], 
                  dv='ln_vio', 
                  data=df_1)

# Panel_ols
panel_ols(iv_lst=['shall', 'incarc_rate', 'density', 'avginc', 'pop', 'pb1064', 'pw1064', 'pm1029'], 
          dv='ln_vio', 
          fixed_entity='stateid', 
          fixed_time='year', 
          data=df_1)
```
