# KLTN
GIÁM SÁT ENTROPY CHUẨN HÓA CỦA LƯU LƯỢNG MẠNG ĐỂ PHÁT HIỆN TẤN CÔNG DDOS TRONG P4

LỜI CẢM ƠN
Lời đầu tiên, tôi xin bày tỏ lời cảm ơn, từ tận đáy lòng, với cơ hội, cũng như những kiến thức mà các Thầy, Cô trong khoa Điện tử - Viễn Thông, trường Đại học Khoa học Tự nhiên đã cho tôi trong suốt bốn năm học vừa qua, đồng thời đã trao cho tôi nhiều cơ hội để được tiếp xúc với các thử thách trong suốt khoảng thời gian ấy.
Tôi cũng xin gửi lời cảm ơn tới thầy Nguyễn Minh Trí, vì những sự góp ý chuyên môn, chuyên sâu về kiến thức, đồng thời là những sự hỗ trợ hết mình của thầy trong quá trình định hướng và hoàn thiện khóa luận: Giám sát Entropy Chuẩn hóa của Lưu lượng Mạng để Phát hiện Tấn công DDoS trong P4. Sự chỉ dạy tận tình của thầy là động lực lớn giúp tôi đã hoàn thiện bài khóa luận này.
Đồng thời, tôi cũng xin cảm ơn những người bạn, những “đồng nghiệp” trong quá trình làm bài khóa luận này, đã chia sẻ, góp ý, xây dựng, và hoàn thiện bài báo cáo của tôi.
Cuối cùng, tôi xin cảm ơn gia đình – những người hậu phương, đã luôn động viên, hỗ trợ tôi, không chỉ về mặt tài chính, mà còn cả mặt tinh thần, giúp tôi vượt qua được những khó khăn trong quá trình hoàn thiện bài khóa luận này.
Tuy đã cố gắng hết sức, nhưng với sự hạn chế về kiến thức cũng như là thiết bị, bài khóa luận này không thể tránh khỏi sự thiếu sót. Tôi rất mong nhận được những góp ý chuyên môn của thầy, cô trong hội đồng để tôi có thể hoàn thiện bài khóa luận này hơn.

Trịnh Hải Sơn

TÓM TẮT
Các cuộc tấn công từ chối dịch vụ phân tán (DDoS) ngày càng gia tăng về tần suất và mức độ tinh vi, gây ra nhiều mối đe dọa nghiêm trọng cho hệ thống mạng. Trong năm 2024, hệ thống bảo mật VNIS của VNETWORK ghi nhận và xử lý thành công hơn 360.000 cuộc tấn công DDoS, tăng khoảng 20% so với năm 2023, với đỉnh tấn công đạt 1,7 Tbps, đặc biệt tập trung vào ngành tài chính – chứng khoán.
Phương pháp phát hiện truyền thống chủ yếu dựa vào tầng điều khiển hoặc thiết bị phần cứng chuyên dụng, gây độ trễ cao và chi phí lớn. Sự xuất hiện của ngôn ngữ lập trình P4 cho phép xử lý và phân tích lưu lượng trực tiếp tại tầng dữ liệu, giúp giảm độ trễ và tăng hiệu quả.
Khóa luận này đề xuất phương pháp phát hiện DDoS dựa trên việc ước lượng entropy chuẩn hóa của địa chỉ IP nguồn trong các gói tin IPv4 bằng ngôn ngữ P4. Mỗi gói tin được băm và ánh xạ vào cấu trúc LogLog để ước lượng số lượng IP nguồn duy nhất. Định kỳ, hệ thống sẽ tính toán entropy, chuẩn hóa kết quả và lưu vào thanh ghi riêng.
Hệ thống sử dụng thuật toán Trung bình động EWMA để theo dõi xu hướng entropy theo thời gian. Nếu giá trị EWMA giảm dưới một ngưỡng xác định, hệ thống sẽ kích hoạt cảnh báo tấn công DDoS bằng cách cập nhật vào thanh ghi trạng thái.
Kết quả thực nghiệm cho thấy phương pháp có khả năng phát hiện hiệu quả các hành vi bất thường với chi phí xử lý thấp. Các giá trị như bộ đếm, entropy, EWMA và cảnh báo đều được lưu vào thanh ghi và có thể truy xuất thời gian thực. Hệ thống cũng được so sánh với các phương pháp hiện đại (SOTA) để đánh giá hiệu quả và khả năng triển khai thực tế.

Các bước thực hiện tấn công
Lần lượt chạy các file sau: P4LogLog -> P4NEntropy -> P4DDoS

Các bước chạy của các file đã có các file liên quan, nằm ở các file tôi đã để ở trong
