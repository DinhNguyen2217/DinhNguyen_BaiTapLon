import schedule
import time
from scraper.nhandan_scraper import NhanDanScraper

def run_scraper():
    """Chạy thu thập dữ liệu"""
    scraper = NhanDanScraper()
    articles = scraper.scrape_all_pages(num_pages=5)
    scraper.save_to_csv(articles)
    scraper.save_to_excel(articles)

def schedule_scraper():
    """Lên lịch chạy tự động hàng ngày"""
    # Lên lịch chạy mỗi ngày lúc 6 giờ sáng
    schedule.every().day.at("06:00").do(run_scraper)
    
    print("Đã lên lịch thu thập dữ liệu hàng ngày lúc 6 giờ sáng")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Kiểm tra mỗi phút