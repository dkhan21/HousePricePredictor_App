[House Prediction App Website](https://sites.google.com/njit.edu/houseprediction?usp=sharing)

House price prediction app
In my app, I first imported all the libraries that were need to display all the plots and design for the app. I imported the data from a csv file and put the data of 17 features into a dataframe. From here I trained a LGB model by having the data frame in the parameters of the lgbRegressor method. Then I fit the model that I have with the dataframe and the target which is the saleprice. SalePrice is what we are trying to predict. We now create sliders for the 17 features and have an option for them to  have a certain range. We then take all the data from the sliders and put it in a dataframe. Then we take an explainer object a assign the model and training data into it. Then we pass the new dataframe and compare what the price of the house would be. Given that we got the values from sliders. Our model will use information from the training data and predict a price for the new dataframe.

Results : An estimate sale price of the house was displayed based on the given features. We get to see the complexity and the accuracy that the prediction model has to predict the price. The training model gave the Overall Quality feature a major impact on the price while other features like the number of fireplaces has a low impact on the price. Each feature had a differnet impact. The quantity of the input data gave a range for the price to be predicted at. In addition to that, we see a summary plot and an interaction plot that displays the value of each feauture and how much impact it has on the house price.
