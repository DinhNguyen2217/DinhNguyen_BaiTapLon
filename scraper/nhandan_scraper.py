import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import time
import random

class NhanDanScraper:
    def __init__(self, base_url="https://nhandan.vn"):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def get_article_links(self, page_url):
        """Lấy tất cả đường dẫn bài viết từ một trang"""
        try:
            response = requests.get(page_url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = []
            article_items = soup.find_all('article', class_='article-item')
            for item in article_items:
                link = item.find('a', href=True)
                if link and link['href']:
                    full_url = link['href'] if link['href'].startswith('http') else self.base_url + link['href']
                    links.append(full_url)
            
            return links
        except Exception as e:
            print(f"Lỗi khi lấy đường dẫn từ {page_url}: {e}")
            return []
    
    def scrape_article(self, url):
        """Thu thập thông tin chi tiết từ một bài viết"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Lấy tiêu đề
            title = soup.find('h1', class_='article-title').get_text(strip=True) if soup.find('h1', class_='article-title') else ''
            
            # Lấy mô tả
            description = soup.find('div', class_='article-sapo').get_text(strip=True) if soup.find('div', class_='article-sapo') else ''
            
            # Lấy hình ảnh
            image = ''
            image_tag = soup.find('div', class_='article-image') or soup.find('div', class_='article-content').find('img') if soup.find('div', class_='article-content') else None
            if image_tag:
                img = image_tag.find('img')
                if img and img.get('src'):
                    image = img['src']
            
            # Lấy nội dung
            content_div = soup.find('div', class_='article-body')
            if content_div:
                paragraphs = content_div.find_all('p')
                content = '\n'.join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
            else:
                content = ''
            
            return {
                'title': title,
                'description': description,
                'image_url': image,
                'content': content,
                'article_url': url,
                'scraped_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        except Exception as e:  
            print(f"Lỗi khi thu thập bài viết {url}: {e}")
            return None
    
    def scrape_all_pages(self, num_pages=5):
        """Thu thập bài viết từ nhiều trang"""
        all_articles = []
        
        for page_num in range(1, num_pages + 1):
            page_url = f"{self.base_url}/p{page_num}" if page_num > 1 else self.base_url
            print(f"Đang thu thập trang: {page_url}")
            
            article_links = self.get_article_links(page_url)
            print(f"Tìm thấy {len(article_links)} bài viết trên trang {page_num}")
            
            for link in article_links:
                article_data = self.scrape_article(link)
                if article_data:
                    all_articles.append(article_data)
                time.sleep(random.uniform(1, 3))  # Tạm dừng để tránh quá tải server
            
            time.sleep(random.uniform(2, 5))  # Tạm dừng giữa các trang
        
        return all_articles
    
    def save_to_csv(self, data, filename='nhandan_articles.csv'):
        """Lưu dữ liệu vào file CSV"""
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Dữ liệu đã lưu vào {filename}")
    
    def save_to_excel(self, data, filename='nhandan_articles.xlsx'):
        """Lưu dữ liệu vào file Excel"""
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"Dữ liệu đã lưu vào {filename}")