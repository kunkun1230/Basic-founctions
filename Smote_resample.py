# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#生成不平衡样本

from sklearn.datasets import make_classification
from collections import Counter
# 使用imlbearn库中上采样方法中的SMOTE接口
from imblearn.over_sampling import SMOTE
#调用下采样模型
from imblearn.under_sampling import RandomUnderSampler

#---------------------------------------------生成样本-----------------------------------------------
# 生成一组0和1比例为9比1的样本，X为特征，y为对应的标签
X, y = make_classification(n_classes=2, class_sep=2,
                           weights=[0.9, 0.1], n_informative=3, 
                           n_redundant=1, flip_y=0,
                           n_features=20, n_clusters_per_class=1, 
                           n_samples=1000, random_state=10)


# 查看所生成的样本类别分布，0和1样本比例9比1，属于类别不平衡数据
print('y的数量是：',Counter(y))


#------------------------------------------生成模型，调整参数------------------------------------------
# 定义SMOTE模型，random_state相当于随机数种子的作用，增加少量样本的样本点
smo = SMOTE(random_state=42)
X_smo, y_smo = smo.fit_sample(X, y)

print('y_smo的数量是：',Counter(y_smo))

#smo = SMOTE(ratio={1: 300 },random_state=42)
## 生成0和1比例为3比1的数据样本
#X_smo, y_smo = smo.fit_sample(X, y)
#print(Counter(y_smo))


#-------------------------------------------进行下采样重新生成样本数据------------------------------------
# 同理，也可使用ratio来指定下采样的比例
rus = RandomUnderSampler(ratio={0: 600,1:400}, random_state=0)
X_rus, y_rus = rus.fit_sample(X_smo, y_smo)
print('y_rus的数量是：',Counter(y_rus))
# Counter({0: 500, 1: 300})


from sklearn.linear_model import LogisticRegression
import numpy as np

lr = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X,y)

sample = np.random.rand(20).reshape(1,-1)
 
res = lr.predict(sample)

print(res)
