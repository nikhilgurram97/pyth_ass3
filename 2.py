from sklearn import datasets,metrics
from sklearn import cross_validation as cv
from sklearn import svm

model = svm.SVC(kernel='linear')                         
bc = datasets.load_breast_cancer()
x=bc.data
y=bc.target
x_train,x_test,y_train,y_test=cv.train_test_split(x,y,test_size=0.4)

model.fit(x_train, y_train)
y_pred=model.predict(x_test)
print("Accuracy :", metrics.accuracy_score(y_test,y_pred))