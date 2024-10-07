import pandas as pd

from flask import Flask, render_template
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('C:\\Users\\My Laptop\\Desktop\\học máy và ứng dụng(TH)\\lab2\\Education.csv')


    label_encoder = LabelEncoder()
    df['Label'] = label_encoder.fit_transform(df['Label'])

    X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Label'], test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    model_multinomial = MultinomialNB()
    model_multinomial.fit(X_train_vectorized, y_train)
    y_pred_multinomial = model_multinomial.predict(X_test_vectorized)
    accuracy_multinomial = accuracy_score(y_test, y_pred_multinomial)
    report_multinomial = classification_report(y_test, y_pred_multinomial, output_dict=True)

    model_bernoulli = BernoulliNB()
    model_bernoulli.fit(X_train_vectorized, y_train)
    y_pred_bernoulli = model_bernoulli.predict(X_test_vectorized)
    accuracy_bernoulli = accuracy_score(y_test, y_pred_bernoulli)
    report_bernoulli = classification_report(y_test, y_pred_bernoulli, output_dict=True)

    return render_template('index.html',
                           accuracy_multinomial=accuracy_multinomial,
                           report_multinomial=report_multinomial,
                           accuracy_bernoulli=accuracy_bernoulli,
                           report_bernoulli=report_bernoulli)

if __name__ == '__main__':
    app.run(debug=True)
