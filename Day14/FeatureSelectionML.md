### 8. Feature Selection For Machine Learning
----

The data features that you use to train your machine learning models have a huge inﬂuence on the performance you can achieve. Irrelevant or partially relevant features can negatively impact model performance. You will discover automatic feature selection techniques that you can use to prepare your machine learning data in Python with scikit-learn.
1. Univariate Selection.
2. Recursive Feature Elimination.
3. Principle Component Analysis.
4. Feature Importance.

--- 
#### 8.1 Feature Selection
---
Feature selection is a process where you automatically select those features in your data that contribute most to the prediction variable or output in which you are interested. Having irrelevant features in your data can decrease the accuracy of many models, especially linear algorithms like linear and logistic regression. Three beneﬁts of performing feature selection before modeling your data are:
* Reduces Overﬁtting: Less redundant data means less opportunity to make decisions based on noise.
* Improves Accuracy: Less misleading data means modeling accuracy improves.
* Reduces Training Time: Less data means that algorithms train faster.

You can learn more about feature selection with scikit-learn in the article Feature selection. Each feature selection recipes will use the Pima Indians onset of diabetes dataset. [Feature Selection](1http://scikit-learn.org/stable/modules/feature_selection.html)

---
#### 8.2 Univariate Selection
----
Statistical tests can be used to select those features that have the strongest relationship with the output variable. The scikit-learn library provides the SelectKBest class2 that can be used with a suite of diﬀerent statistical tests to select a speciﬁc number of features. The example below uses the chi-squared (chi2) statistical test for non-negative features to select 4 of the best features from the Pima Indians onset of diabetes dataset.

![unvariate](../Imgs/unvariate.PNG)    

You can see the scores for each attribute and the 4 attributes chosen (those with the highest scores): plas, test, mass and age. I got the names for the chosen attributes by manually mapping the index of the 4 highest scores to the index of the attribute names.

![unvariate2](../Imgs/unvariate2.PNG)

---
#### 8.3 Recursive Feature Elimination   
----

The Recursive Feature Elimination (or RFE) works by recursively removing attributes and building a model on those attributes that remain. It uses the model accuracy to identify which attributes (and combination of attributes) contribute the most to predicting the target attribute. You can learn more about the RFE class3 in the scikit-learn documentation. The example below uses RFE with the logistic regression algorithm to select the top 3 features. The choice of algorithm does not matter too much as long as it is skillful and consistent. [RFE](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest)

![rfe1](../Imgs/rfe1.PNG)

You can see that RFE chose the top 3 features as preg, mass and pedi. These are marked True in the support array and marked with a choice 1 in the ranking array. Again, you can manually map the feature indexes to the indexes of attribute names.

![rfe2](../Imgs/rfe2.PNG)

---
#### 8.4 Principal Component Analysis
----

Principal Component Analysis (or PCA) uses linear algebra to transform the dataset into a compressed form. Generally this is called a data reduction technique. A property of PCA is that you can choose the number of dimensions or principal components in the transformed result. In the example below, we use PCA and select 3 principal components. Learn more about the PCA class in scikit-learn by reviewing the API. [Analysis](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html) [Analysis2](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

![PCA](../Imgs/PCA.png)

---
#### 8.5 Feature Importance
----

Bagged decision trees like Random Forest and Extra Trees can be used to estimate the importance of features. In the example below we construct a ExtraTreesClassifier classiﬁer for the Pima Indians onset of diabetes dataset. You can learn more about the ExtraTreesClassifier class5 in the scikit-learn API.

![featImp](../Imgs/featImp.PNG)

You can see that we are given an importance score for each attribute where the larger the score, the more important the attribute. The scores suggest at the importance of plas, age and mass.

![featImp2](../Imgs/featImp2.PNG)






