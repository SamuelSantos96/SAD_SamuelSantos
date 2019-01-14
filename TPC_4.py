# Import datasets, classifiers and performance metrics
from sklearn import datasets, tree, model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

# The digits dataset
digits = datasets.load_digits()

# Decision Tree
[features_train, features_test, classes_train, classes_test] = model_selection.train_test_split(digits.data, digits.target, test_size = 0.30, random_state = 100)
model = tree.DecisionTreeClassifier()

clf = model.fit(features_train, classes_train)

# Predict Test Set Labels
pred = model.predict(features_test)

score_train = model.score(features_train, classes_train)
score_test = model.score(features_test, classes_test)

# Extract Data
MyShape = digits.data

print('Shape: ', MyShape.shape)

print('\n\tDecision Tree')
print('==============================')
print("Features:", digits.target_names)
print("score_train:", score_train)
print("score_test:", score_test)
print('==============================')

# Random Forrest
model = RandomForestClassifier(n_estimators = 1000)

clf = model.fit(features_train, classes_train)

score_train = model.score(features_train, classes_train)
score_test = model.score(features_test, classes_test)

print('\n\tRandom Forrest')
print('==============================')
print("score_train:", score_train)
print("score_test:", score_test)
print('==============================')

# Naive Bayes
y_pred = gnb.fit(features_train, classes_train)

score_train = gnb.score(features_train, classes_train)
score_test = gnb.score(features_test, classes_test)

print('\n\tNaive Bayes')
print('==============================')
print("score_train:", score_train)
print("score_test:", score_test)
print('==============================')


# Test Set
def classify():
    values = []
    for i in digits.target:
        if pred.all() != digits.target[i]:
            values.append(i)

    print('Bad predictions ', values)


classify()

