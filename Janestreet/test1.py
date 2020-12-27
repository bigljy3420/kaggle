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
from pathlib import Path
import cudf as gd
import pandas as pd
import dask_cudf as cd

# %%
train_path = Path("/shared_data/kaggle/train.csv")
feature_meta_path = Path("/shared_data/kaggle/features.csv")
# train_df = cd.read_csv(str(train_path), chunksize = "128 MiB")
train_df = pd.read_csv(str(train_path))
feature_meta = pd.read_csv(str(feature_meta_path))

# %%
feature_meta.iloc[60]

# %%
train_df.shape[0].compute()

# %%
train_df.head()

# %%
print(list(train_df.columns))

# %%
train_df["ts_id"].max().compute()

# %%
train_df["date"].max().compute()

# %%
train_df_cumsum = train_df.cumsum()

# %%
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
sns.lineplot(train_df["ts_id"].iloc[0::1000], train_df_cumsum.iloc[0::1000]["resp"])
sns.lineplot(train_df["ts_id"].iloc[0::1000], train_df_cumsum.iloc[0::1000]["resp_1"])
sns.lineplot(train_df["ts_id"].iloc[0::1000], train_df_cumsum.iloc[0::1000]["resp_2"])
sns.lineplot(train_df["ts_id"].iloc[0::1000], train_df_cumsum.iloc[0::1000]["resp_3"])
sns.lineplot(train_df["ts_id"].iloc[0::1000], train_df_cumsum.iloc[0::1000]["resp_4"])
plt.legend(title='sampling interval 100', loc='upper left', labels=['resp', 'resp_1', 'resp_2', 'resp_3', "resp_4"])
# sns.lineplot(train_df["ts_id"].iloc[0::1000], train_df["resp"].iloc[0::1000])

# %%
train_df["feature_62"]

# %%
