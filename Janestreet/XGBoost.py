# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import dask_cudf as cd
from pathlib import Path

# %%
import janestreet
env = janestreet.make_env() # initialize the environment
iter_test = env.iter_test() # an iterator which loops over the test set

# %%
import xgboost as xgb
print("XGBoost version:", xgb.__version__)

# %%
train_path = Path("/shared_data/kaggle/train.csv")
feature_meta_path = Path("/shared_data/kaggle/features.csv")
train = pd.read_csv(str(train_path))
features = pd.read_csv(str(feature_meta_path))
example_test = pd.read_csv("/shared_data/kaggle/example_test.csv")
sample_prediction_df = pd.read_csv("/shared_data/kaggle/example_sample_submission.csv")
print ("Data is loaded!")

# %%
train = train[train['weight'] != 0]
train['action'] = (train['resp'].values > 0).astype('int')
X_train = train.loc[:, train.columns.str.contains('feature')]
y_train = train.loc[:, 'action'
