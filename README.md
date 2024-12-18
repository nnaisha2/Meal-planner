# Cameroon Meal Planner Application

This meal planner application is designed to recommend meals based on user inputs. Django powers the web application's backend, whereas the meal recommendation algorithm is handled by a K-Nearest Neighbors (KNN) model from the sklearn library.

The application has been developed to consider both the weight and ease of a meal in its recommendation. The meals' data is stored in an Excel file (`CMR.xlsx`), which is read by pandas' DataFrame before fitting into the KNN model. 

## Set Up 

You need to have Django, sklearn, pandas, and Python installed on your machine to run this application. After ensuring these installations, you can add the project directory to your Python path and set up Django with the project settings module. You're all set!

## KNN Model for Meal Recommendation

The KNN model, initialized with five neighbors, uses features such as `Weight` and `Ease` from our dataset to predict and recommend meals based on the user's preferences.

## Django Models
In Django, the `Meal` model is used for creating meal objects. This model contains fields like `name`, `description`, `image`, `recipe_link`, `main_ingredient`, `weight`, and `ease`.

## Using the Application
To get recommendations, call the function `recommend_meals(user_weight, user_ease, k)` by passing the user's desired weight, ease of meal, and the number of recommendations you'd like. 

The function returns a list of recommended meals based on user preferences provided with the KNN model.

## Future Scope
In the near future, expect more features such as adding custom meals, storing user preferences, offering dietary advice, and much more. Stay tuned!

## About
The Cameroon Meal Planner app has been designed to recommend meals commonly found in Cameroon based on users' inputs. This application stems from the rich and diverse food culture that exists in Cameroon, which is often referred to as 'Africa in miniature' due to its cultural and geographical diversity. With an array of dishes featuring a variety of flavors, ingredients, and techniques, Cameroonian cuisine is a culinary adventure worth exploring.
Recognizing this rich culinary landscape, our application aims to make Cameroonian meals more accessible to food lovers worldwide. By recommending meals based on factors such as ease of preparation and the nutritional value (represented by `Weight`), we hope to bring the unique tastes of Cameroonian meals to kitchens around the globe. 
Whether you're Cameroonian looking to revisit the familiar taste of home meals or a food enthusiast wishing to try new cuisines, our application will guide you on this exciting culinary journey. By matching your personal preferences to the features of our diverse meal options, we make the selection process much easier and enjoyabl
