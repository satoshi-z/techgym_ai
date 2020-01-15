#AI-TECHGYM-3-14-A-1
#回帰問題と分類問題

#インポート
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

#シグモイド関数定義
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#シグモイド関数描画
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.title('sigmoid function')

#データロード
cancer = load_breast_cancer()

#格納データの確認
#print(cancer.keys())

#必要なら表示
#print(cancer.DESCR)

#特徴量の表示
#print(cancer.feature_names)
#print(cancer.target_names)

#学習データ、テストデータ
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, stratify = cancer.target,test_size=0.2,random_state=0)

#学習、モデル
model = LogisticRegression(solver='liblinear')
model.fit(X_train,y_train)

#表示
print('正解率(train):{:.3f}'.format(model.score(X_train, y_train)))
print('正解率(test):{:.3f}'.format(model.score(X_test, y_test)))
