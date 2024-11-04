# INSURANCE COST PREDICTION

Insurance companies need to accurately predict the cost of health insurance for individuals to set premiums appropriately. The traditional methods of cost prediction often rely braod acturial tables and historical averages which may not account for the nuanced differences among individuals.

## Problem Statement

The primary need for this project arises from the challenges insurers face in pricing policies accurately while remaining competitive in the market. Inaccurate predictions can lead to losses for insurers and unfairly high premiums for policyholders.
In this project the target metric is the "**ACCURACY**"

### EDA Process

1. Glanced through the Health Insurance dataset using methods like head(), shape, info
2. Changed the data types for few variables to Object
3. Checked for null and duplicate values which were all 0
4. Separated numerical and categorical variables for easy manipulation of data
5. Created Summary Statistics for numerical and categorical variables using describe()
6. For each of the Object features, checked Unique values
7. Plotted graphs for Outliers on Age, Height, Weight and Premium Price
8. Performed **Univariate Analysis** on Distribution of customers on Age, Height, Weight and Premium Price
9. Performed **Multivariate Analysis With 2 or more variables**
          -- Relation between features Age vs Premium Price, Weight vs Premium Price, Height vs Premium Price, Number of Major Surgeries vs Premium Price, History of Cancer in Family vs Premium Price, Known
             Allergies vs Premium Price etc.
          -- Relation between features Premium Price By Age according to History Of Cancer, Premium Price by age according to Diabetes, Premium Price by age according to Any Transplants etc
10. Analysed using **Pair plot and Heatmap**.
11. Based on the analysis, got an view of important features played a role in determining premium
12. Performed **Hypothesis Testing** using **Chi Squared Test** on History of Cancer in the family, Any Chronic Disease, Diabetes and Blood Pressure
  
### Modeling 

1. Divided the data into **X** and **y** dataset with all features in X and only Premium Price in y
2. As data needed normalisation, used StandardScaler on Age, Height, Weight features
3. Split the dataset with Train as 75% and Test as 25%
4. Used **RandomForestRegressor** modeling technique to fit and train the dataset
5. Accuracy on **Training : 85% and Test : 80%**
6. Withe above model, devised to find the most Important Feature and it was  **AGE**

### Deployment

The end goal is to render this information on an UI to the client so that he can easily evaluate Premium for different customers with health information. This will be mainly useful for end users such as Acturaries, Insurance Agents.

1. Saved the model as a pickle file
2. Deployed on a **Flask**  with **post method** by providing all the important features and predicted Premium Price
3. Also deployed on **Streamlit** which gives an UI with all the required field and predict Premium Price


