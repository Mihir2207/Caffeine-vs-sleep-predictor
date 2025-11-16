# Caffeine Intake → Sleep Quality Prediction

A Machine Learning project using Simple Linear Regression and Streamlit

## Overview

This project predicts a person's sleep quality (scale 0–10) based on their daily caffeine intake (in milligrams).
It demonstrates a complete end-to-end workflow including dataset generation, model training, visualization, and deployment on an AWS EC2 instance.

## Project Structure

```
ml project/
├── app.py                 # Streamlit user interface
├── caffeine_sleep.csv     # Dataset used for training and visualization
├── generate_sleep_data.py # Script to generate synthetic caffeine–sleep dataset
├── plot_model.py          # Script to generate regression plot
├── regression_plot.png    # Generated regression line plot
├── requirements.txt       # Python dependencies
├── sleep_model.pkl        # Trained Linear Regression model
├── train_model.py         # Script to train the model
├── README.md              # Project documentation
├── LICENSE                # Optional open-source license
```

## Dataset Generation

`generate_sleep_data.py` creates a synthetic dataset that models a negative linear relationship between caffeine consumption and sleep quality. Random noise is added for realism.

Output file:

* `caffeine_sleep.csv`

Columns:

* `Caffeine_mg`
* `Sleep_Quality`

## Model Training

`train_model.py` trains a Simple Linear Regression model using scikit-learn.
The training process includes:

1. Loading the dataset
2. Separating features and labels
3. Fitting a LinearRegression model
4. Saving the trained model as `sleep_model.pkl`

The model learns an equation of the form:

```
Sleep_Quality = m × Caffeine_mg + b
```

This equation is displayed in the Streamlit application.

## Regression Plot

`plot_model.py` loads both the dataset and the trained model to generate a regression plot showing the fitted model line against actual data points.

Output:

* `regression_plot.png`

## Streamlit Application

`app.py` provides an interactive interface to:

* Input daily caffeine intake (mg)
* Predict sleep quality using the trained model
* Display the model equation
* Visualize dataset trends using a line chart
* Use a custom color palette:

  * #e23636
  * #000000
  * #504a4a
  * #518cca
  * #f78f3f

### Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Start the application:

```
streamlit run app.py
```

The app runs at:

```
http://localhost:8501
```

## Deploying on AWS EC2

This project can be deployed to an EC2 instance to make it publicly accessible.

### 1. Connect to EC2

```
ssh -i "<your-key>.pem" ec2-user@<EC2_PUBLIC_IP>
```

### 2. Install Python and required packages

```
sudo yum update -y
sudo yum install -y python3-pip
pip3 install --upgrade pip
```

### 3. Transfer project files from local machine to EC2

```
scp -i "<your-key>.pem" app.py sleep_model.pkl requirements.txt caffeine_sleep.csv ec2-user@<EC2_PUBLIC_IP>:/home/ec2-user/
```

### 4. Install dependencies on EC2

```
pip3 install streamlit pandas scikit-learn matplotlib
```

### 5. Run the application on EC2

```
streamlit run app.py --server.port 8080 --server.address 0.0.0.0
```

Access the deployed app in a browser:

```
http://<EC2_PUBLIC_IP>:8080
```

## Author

Mihir Ginde
