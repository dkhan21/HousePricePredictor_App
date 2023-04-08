import pandas as pand
import xgboost
import shap

house = pand.read_csv(r'C:/Users/dkhan/Desktop/Python VSCode/train.csv')
x =  house.drop('SalePrice', axis = 1).drop('Id', axis = 1)
x = x.select_dtypes(include = ['float64', 'int64'])
y = house["SalePrice"]

# SHAP VALUES GRAPH of Summary Plot and Waterfall Plot
mod = xgboost.XGBRFRegressor().fit(x, y)

explainer = shap.Explainer( mod)
sv = explainer(x);

#shap.summary_plot(sv, x)
shap.plots.waterfall(sv[0])

#SHAP DEPENDANCE PLOT with interaction values
model = xgboost.train({"learning_rate": 0.01}, xgboost.DMatrix(x, label=y), 100)
explain2 = shap.TreeExplainer(model)

shapInterVals = explain2.shap_interaction_values(x)
svdepend = explain2.shap_values(x)
#shap.dependence_plot('OverallQual', svdepend, x)
