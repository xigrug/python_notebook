#!/usr/bin/env python
# coding: utf-8
# # Python中的因子分析简介
# 
# https://www.datacamp.com/community/tutorials/introduction-factor-analysis
# 
# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt


# ## 加载数据

df= pd.read_csv("avg_CCNnew41.8-spss.csv")
print(df.columns)
# Dropping unnecessary columns
# NOTICE BJC is Time value
df.drop(['FAC1', 'FAC2', 'FAC3', 'FAC4', 'FAC5', 'FAC6', 'FAC7', 'FAC8'],axis=1,inplace=True)
df.drop(['CCN_1.0_cm3'],axis=1,inplace=True)
print(df.shape)
# Dropping missing values rows
df.dropna(inplace=True)
print(df.shape)
print(df.info())
print(df.head())
# ## 充分性测试
# 在执行因子分析之前，您需要评估数据集的“可用性”。Factorability意味着“我们能找到数据集中的因子吗？”。有两种方法可以检查可行性或抽样充分性：
# 
# * 巴特利特的考验
# * Kaiser-Meyer-Olkin测试
# 
# **Bartlett**对球形度的检验使用观察到的相对矩阵对照单位矩阵检查观察到的变量是否完全相互关联。如果测试发现统计上不显着，则不应使用因子分析。

from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value=calculate_bartlett_sphericity(df)
print(chi_square_value, p_value)

# 在该Bartlett检验中，p值为0.该检验具有统计学意义，表明观察到的相关矩阵不是单位矩阵。

# **Kaiser-Meyer-Olkin（KMO）测试**测量数据在因子分析中的适用性。它确定了每个观测变量和完整模型的充分性。
# KMO估计所有观测变量之间的方差比例。较低的比例id更适合因子分析。KMO值介于0和1之间.KMO小于0.6的值被认为是不合适的。

# In[12]:


from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)

print(kmo_model)

# 我们数据的总体KMO为0.84，非常好。此值表示您可以继续进行计划的因子分析。

# ### 选择因素数量
# 要选择因子数，可以使用Kaiser标准和scree图。两者都基于特征值。

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 25, rotation=None)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
print(ev)

# 在这里，您只能看到6个因子的特征值大于1。这意味着我们只需要选择6个因子（或未观察到的变量）。

# Create scree plot using matplotlib
plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.axhline(y=1, color='r', linestyle='-')
plt.grid()
plt.savefig("scree_plot.png")
# 碎石图方法为每个因子及其特征值绘制一条直线。特征值大于1被认为是因子的数量。
# 
# 在这里，您只能看到6个因子的特征值大于1。这意味着我们只需要选择6个因子（或未观察到的变量）。

# ## 执行因子分析

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 6 ,rotation="varimax")
print(fa.loadings)

print(fa.get_factor_variance())
#ConfirmatoryFactorAnalyzer
#print(fa.get_standard_errors())
fa_t=fa.transform(df)
print(fa_t)
