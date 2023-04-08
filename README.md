Here is my code:
python
python HousePricing.py

The model that I chose to use perform the SHAP interpretation of the house price prediction was the xgboost model. This is kown as Extreme Gradient boosting algorithm.
For our case, it used a decision tree a checked the difference between the actual and predicted values. In additon to that, it also handled any missing values that occured in the data. The one other feature is does is prevent overfitting.

Article that helped me understand what XGBoost is
https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/

For my shap values, I generated a summary plot consisting of all the features that are int and float data type and they are ordered by their shap values. There are multiples points on the graph and each point is basaically an instance in the data. There is also a vertical line included which shows the where the most important features are. The blue dots are known as low values and the red dots are known as high values. If you see purple then thats what is in the middle values. Also the horizontal axis shows the SHAP values for each feature.

Summary Plot
![Screenshot 2023-04-08 111650](https://user-images.githubusercontent.com/123338238/230729110-a6cb33bf-7b62-49b6-ad15-7e2fb5aeb34a.png)

For SHAP Values, I generated another graph known as a waterfall plot which basically shows the effects of a feature to the model which could be positive or negative. If the features line is red, that means the features is going to increase the prediction and a blue line shows that a feature is decreasing the prediction. As you can see in my graph, I am using all the features that are int and float data types. Just know that the Y-axis of the graph is the featuers and the x-axis of graph is the features contribution to that prediction.

Waterfall Plot
![Screenshot 2023-04-08 114055](https://user-images.githubusercontent.com/123338238/230730485-4508eedc-9914-47d2-a022-ac7213bee57f.png)


For shap interaction values, I created a dependence plot using the shap library. In this dependance plot, I am extracting one feature in the dataset and will see what effects will it to the models prediction. In many case, I used the 'OverallQual' feature in my dependance plot and I could see the differences it makes to the model's prediction. We are comparing the prediction that has the 'OverallQual' Feature with the prediction that does not have the 'OverallQual' Feature. From my plot, we can see that the value of 'OverallQual' feature increases in the plot. This indicates that this feature is an important predictor of the model's output because of the high predictions values it produces.


Dependance plot
![Screenshot 2023-04-08 112745](https://user-images.githubusercontent.com/123338238/230729730-b6b880c1-0c14-47a4-b886-92510fab88e7.png)
