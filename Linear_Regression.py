import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# عدد ساعات الدراسة
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# الدرجات
y = np.array([2, 3, 6, 8, 10])

# إنشاء النموذج
model = LinearRegression()

# تدريب النموذج على البيانات
model.fit(X, y)

# معامل الميل (Slope)
print("Slope (β1):", model.coef_[0])

# الثابت (Intercept)
print("Intercept (β0):", model.intercept_)

# التنبؤ للمدخل 4 ساعات
hours = np.array([[4]])
predicted_score = model.predict(hours)
print("Predicted score for studying 4 hours:", predicted_score[0])

# رسم البيانات
plt.scatter(X, y, color='blue')

# رسم خط الانحدار
plt.plot(X, model.predict(X), color='red')

# إضافة تسميات للمحاور وعنوان
plt.xlabel('Number of Study Hours')
plt.ylabel('Scores')
plt.title('Study Hours vs Scores')

# عرض الرسم
plt.show()
