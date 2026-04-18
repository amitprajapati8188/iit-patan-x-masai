# ML Workflow Assignment

## Task 1: Label Identification and Data Leakage

* **Label:** The column **`repeat_purchase_flag`** is the label because it represents the target outcome we want the model to predict based on historical customer behavior.
* **Data Leakage:** The column **`discount_used_on_repeat_order`** introduces data leakage because it contains information about the repeat purchase itself, which would not be known at the time the model is making a prediction.

## Task 2: Recommended ML Workflow Steps

Before training a complex model like Gradient Boosting, the following two steps are crucial:

### 1. Exploratory Data Analysis (EDA)
**Why it matters:** EDA helps in understanding the distribution of data, identifying missing values, and detecting outliers. Without EDA, you might train a model on "noisy" or biased data, leading to inaccurate predictions regardless of how complex the algorithm is.

### 2. Data Cleaning and Preprocessing
**Why it matters:** This step involves handling missing values, encoding categorical variables, and scaling numerical features. Since models require clean, structured data to function, skipping this step can lead to errors or a model that fails to converge during training.