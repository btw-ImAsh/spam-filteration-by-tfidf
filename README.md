
# Spam Classification Using NLP

Spam classification using TF-IDF is a common Natural Language Processing (NLP) approach used to automatically detect and filter spam messages, such as unwanted emails or SMS.
## Tech Stack

- **Excel:** For data exploration.

- **Python:** For data preprocessing.

- **Pandas/Matplotlib/ScikitLearn:** Libraries for further data manupulation and cleaning and machine learning.

- **NLTK/re:** Libraries for performing texual operations.

- **Streamlit:** For frontend and UI.



## Workflow

1. Data Collection:

Gather a dataset of labeled messages (e.g., SMS or emails) marked as "spam" or "ham" (not spam).

2. Preprocessing:

Clean text by removing punctuation, converting to lowercase, removing stop words, and optionally applying stemming/lemmatization.

3. Feature Extraction (TF-IDF Vectorization):

Use a TfidfVectorizer to convert the text messages into numerical feature vectors based on the importance of each word.

This converts raw text into a sparse matrix of TF-IDF scores.

4. Model Training:

Train a classification model using the TF-IDF features. Common algorithms:

- Naive Bayes (most popular for spam detection)

- Logistic Regression

- Support Vector Machines (SVM)

- Random Forest

5. Evaluation:

Evaluate the model using metrics such as accuracy, precision, recall, and F1-score.

Use a test set or cross-validation.

6. Prediction:

Given a new message, transform it using the same TF-IDF vectorizer and classify it as spam or not spam using the trained model.
## Visuals

![Spam Classifier](https://github.com/user-attachments/assets/8ba694e7-f50e-4fcb-b804-c1aa0231035c)


## Authors

- Ashutosh Sharma
    - [Linkedin](https://www.linkedin.com/in/ashutosh-sharma28/)
    - [Github](https://github.com/btw-ImAsh)

