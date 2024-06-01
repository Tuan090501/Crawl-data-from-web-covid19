1. Xây dựng được Spider để tải và bóc tách các dữ liệu cần thiết.

2. Sử dụng Spider để xử lý việc chuyển trang web để lấy được các dữ liệu từ ngày cũ hơn.

3. Lấy được dữ liệu về ngày tháng và số ca nhiễm mới vào ngày đó.

Truy vấn các phần tử để lấy các thông tin về thời gian cũng như số ca mắc mới. Ở ví dụ trên thì bạn cần lấy các thông tin như sau:

Thời gian: “06:00 12/08/2021”
Số ca mắc mới: “THÔNG BÁO VỀ 4.642 CA MẮC MỚI ”
Về cách lấy dữ liệu về số ca mắc mới, bạn có thể sử dụng regex để tách các số, hoặc sử dụng các biện pháp cắt chuỗi, thay thế chuỗi để xử lý. Sau khi xử lý thành công thì ta sẽ được dữ liệu ở dạng sau:

4. Lưu các dữ liệu thu thập được dưới dạng .json

5. (Yêu cầu nâng cao) Trích xuất được các dữ liệu về số ca nhiễm mới của từng thành phố.

Ngoài ra, để xử lý dữ liệu dễ hơn. Bạn nên xóa bỏ hết các dấu tiếng Việt ở trong chuỗi, Bạn có thể sử dụng hàm no_accent_vietnamese ở file trong phần “Tài nguyên” để thực hiện thao tác này.

 
