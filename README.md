# VnExpress 

Đây là một project Python để lấy tin tức từ VnExpress (chuyên mục công nghệ). Nó tự động lấy các bài viết từ trang `VnExpress`, lấy thông tin tiêu đề, mô tả, hình ảnh và nội dung rồi lưu vào file Excel

## Cài đặt

Trước khi chạy chương trình, bạn cần cài vài thư viện Python:


***pip install selenium pandas openpyxl schedule***

Cách chạy

Mở file main.py trong visual code 


Thay đổi giờ trong dòng này nếu muốn thử (ví dụ thay "14:46" thành giờ hiện tại của bạn):
sau đó nhấn lệnh chạy ***python main.py***
đợi trang web tải lấy xong bài viết
Sau khi chạy xong, sẽ thấy file TinTuc_VnExpress.xlsx tự động được tạo, ở đó có chứa các bài viết được lấy từ trang web. 



