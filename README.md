# Nhandan.vn Scraper

## Giới thiệu
Dự án **Nhandan.vn Scraper** là một công cụ tự động thu thập dữ liệu từ trang web [nhandan.vn](https://nhandan.vn). Công cụ này được thiết kế để thu thập thông tin từ các bài viết, bao gồm tiêu đề, mô tả, hình ảnh, nội dung, và lưu trữ dữ liệu vào các tệp CSV hoặc Excel. Ngoài ra, công cụ hỗ trợ lên lịch chạy tự động hàng ngày để đảm bảo dữ liệu luôn được cập nhật.

## Tính năng chính
- **Thu thập dữ liệu bài viết**: Lấy thông tin chi tiết từ các bài viết trên trang web.
- **Lưu trữ dữ liệu**: Lưu dữ liệu thu thập được vào tệp CSV và Excel.
- **Lên lịch tự động**: Hỗ trợ lên lịch chạy tự động hàng ngày vào thời gian cố định.
- **Tạm dừng giữa các yêu cầu**: Tránh quá tải server bằng cách thêm thời gian tạm dừng giữa các yêu cầu HTTP.



### Chi tiết các tệp
- **`scraper/nhandan_scraper.py`**: Chứa lớp `NhanDanScraper` để thực hiện việc thu thập dữ liệu từ các bài viết trên trang web.
- **`scraper/utils.py`**: Chứa các hàm tiện ích để chạy thu thập dữ liệu và lên lịch tự động.
- **`run_scraper.py`**: Tệp chính để chạy công cụ thu thập dữ liệu hoặc lên lịch tự động.
- **`requirements.txt`**: Danh sách các thư viện cần thiết để chạy dự án.
- **`README.md`**: Tài liệu hướng dẫn sử dụng dự án.

---

## Hướng dẫn sử dụng

### 1. Cài đặt môi trường
Trước tiên, hãy đảm bảo bạn đã cài đặt Python 3.8 trở lên. Sau đó, cài đặt các thư viện cần thiết bằng lệnh sau:
```bash
pip install -r requirements.txt
```

### 2. Chạy thu thập dữ liệu
Để thu thập dữ liệu từ trang web, chạy lệnh sau:
```bash
python run_scraper.py
```
# Yêu cầu hệ thống
## Python 3.8 trở lên
### Các thư viện được liệt kê trong requirements.txt:
#### requests
#### beautifulsoup4
#### pandas
#### schedule
#### openpyxl
#### lxml
