---

# Install

```powershell
pip install git+https://github.com/seungwoo-h/econometrics_calculator.git
```

## Usage

```python
from econometrics_stats import load_data, preprocess_ln, linear_regression, instrument_ols, panel_ols

# Data load
df = load_data('path')

# Preprocess ln()
df_1 = preprocess_ln(['vio'], df_original)

# Linear regression
linear_regression(['shall'], 'ln_vio', df_1) # prints out OLS reg result

# Panel_ols
panel_ols(['shall', 'incarc_rate', 'density', 'avginc', 'pop', 'pb1064', 'pw1064', 'pm1029'], 'ln_vio', 'stateid', 'year', df_1)
```
