from scraper.utils import run_scraper, schedule_scraper
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Công cụ thu thập dữ liệu từ nhandan.vn')
    parser.add_argument('--schedule', action='store_true', help='Chạy tự động hàng ngày lúc 6h sáng')
    
    args = parser.parse_args()
    
    if args.schedule:
        schedule_scraper()
    else:
        run_scraper()