The model that I chose to use perform the SHAP interpretation of the house price prediction was the xgboost model. This is kown as Extreme Gradient boosting algorithm.
For our case, it used a decision tree a checked the difference between the actual and predicted values. In additon to that, it also handled any missing values that occured in the data. The one other feature is does is prevent overfitting.

For my shap values, I generated a summary plot consisting of all the features that are int and float data type and they are ordered by their shap values. There are multiples points on the graph and each point is basaically an instance in the data. There is also a vertical line included which shows the where the most important features are. The blue dots are known as low values and the red dots are known as high values. If you see purple then thats what is in the middle values. Also the horizontal axis shows the SHAP values for each feature.


![Screenshot 2023-04-08 111650](https://user-images.githubusercontent.com/123338238/230729110-a6cb33bf-7b62-49b6-ad15-7e2fb5aeb34a.png)




For shap interaction values, I created a dependence plot using the shap library. In this dependance plot, I am extracting one feature in the dataset and will see what effects will it to the models prediction. In many case, I used the 'OverallQual' feature in my dependance plot and I could see the differences it makes to the model's prediction. From my ploy, we can see that the value of 'OverallQual' feature increases in the plot. This indicates that this feature is an important predictor of the model's output because of the high predictions values it produces.



![Screenshot 2023-04-08 112745](https://user-images.githubusercontent.com/123338238/230729730-b6b880c1-0c14-47a4-b886-92510fab88e7.png)
