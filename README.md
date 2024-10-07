**1. Công nghệ sử dụng:**

• Framework:numpy, pandas, matplotlib, io, sklearn, Flask, 


**2. Thuật toán:**

• Thuật toán Naive Bayes 
  - Một thuật toán học máy có giám sát (Supervised learning). Dự đoán xác suất sau của bất kỳ sự kiện nào dựa trên các sự kiện đã xảy ra. Naive Bayes được sử dụng để thực hiện phân loại và giả định rằng tất cả các sự kiện đều độc lập. Naive Bayes  được sử dụng để tính xác suất có điều kiện của một sự kiện, với điều kiện là một sự kiện khác đã xảy ra.

• Bernoulli Naive Bayes
  - Mô hình này được sử dụng khi các đặc trưng đầu vào chỉ nhận giá trị nhị phân 0 hoặc 1 (phân bố Bernoulli). Phù hợp để xử lý phân loại tài liệu 
  - Công thức : 
  - <img width="480" alt="Bernoulli Naive Bayes" src="https://github.com/user-attachments/assets/db490f19-88d2-4e78-8559-30f698083e57">
  
• Multinomial Naive Bayes
Mô thường được sử dụng cho các bài toán phân loại có đặc trưng là số nguyên không âm, đặc biệt phổ biến trong phân loại văn bản và mô hình phân tích tần suất của các từ trong tài liệu.

  - Công thức : 
  - <img width="480" alt="Multinomial Naive Bayes" src="https://github.com/user-attachments/assets/6e9ae11b-5906-4279-b98b-ca60933d0576">
  
  • GaussianNB Naive Bayes  
  Được sử dụng khi các features là dữ liệu liên tục, các giá trị của đặc trưng có thể nằm trên một dải rộng thay vì chỉ là nhị phân hoặc số nguyên.
  - Công thức : 
  <img width="480" alt="GaussianNB Naive Bayes" src="https://github.com/user-attachments/assets/eb5f3ee1-b2d7-4d62-bb4f-de7401dc1a4f">

  **3. Hiển thị kết quả lên website**

  - <img width="1024" alt="a1" src="https://github.com/user-attachments/assets/811d3c9f-4cd0-48b2-9490-6db3f8ac5ea4">


  - <img width="1024" alt="a2" src="https://github.com/user-attachments/assets/0b1bd10f-b061-4b2b-b51b-a56ce30f7650">

  **4. Đối với các bài toán có sự so sánh giữa 2 thuật toán thì sẽ dán kết quả dưới đây.**

  - **So sánh giữa hai mô hình Bernoulli Naive Bayes và Multinomial Naive Bayes**
  - <img width="480" alt="a3" src="https://github.com/user-attachments/assets/9671c0ef-1c57-4e27-9934-15ba7ce66f39">
  - Multinomial Naive Bayes có độ chính xác (accuracy), recall, và F1-score cao hơn so với Bernoulli Naive Bayes. Với tập dữ liệu này, Multinomial Naive Bayes có khả năng phân loại tốt hơn, đặc biệt là trong việc nhận diện 1 (True/positive).
  - Bernoulli Naive Bayes vượt trội ở chỉ số precision của 1 (True/positive) và có recall cao cho 0 (False/negative), nhưng bị hạn chế ở khả năng phát hiện các mẫu 1 với recall thấp.
  - Hiệu suất tổng thể và sự cân bằng giữa các cách tính hiệu suất, Multinomial Naive Bayes là sự lựa chọn tốt hơn

