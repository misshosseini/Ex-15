from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# بارگذاری مجموعه داده
housing = fetch_california_housing()
X = housing.data[:, [0, 1, 2]]  # انتخاب ویژگی‌های MedInc, HouseAge, AveRooms
y = housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# آموزش مدل
model = LinearRegression()
model.fit(X_train, y_train)

# ذخیره مدل
joblib.dump(model, 'model.pkl')
