from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)

@app.route('/')
def index():
    # Đọc file CSV
    df = pd.read_csv('C:\\Users\\My Laptop\\Desktop\\học máy và ứng dụng(TH)\\lab2\\drug.csv')

    # Xử lý dữ liệu
    label_encoder_sex = LabelEncoder()
    df['Sex'] = label_encoder_sex.fit_transform(df['Sex'])

    label_encoder_BP = LabelEncoder()
    df['BP'] = label_encoder_BP.fit_transform(df['BP'])

    label_encoder_chol = LabelEncoder()
    df['Cholesterol'] = label_encoder_chol.fit_transform(df['Cholesterol'])

    # Tạo tập dữ liệu huấn luyện và kiểm tra
    X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']]
    y = df['Drug']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Gaussian Naive Bayes
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Độ chính xác và báo cáo phân loại
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Trả về kết quả cho template
    return render_template('index_g.html', accuracy=accuracy, report=report)

if __name__ == '__main__':
    app.run(debug=True)
