import os
import requests
from edge_tts import communicate

# Load GOOGLE_API_KEY from .env
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

class Agent1:
    @staticmethod
    def research_jacuzzis():
        # Simulated product details retrieval using Gemini API
        products = []
        for i in range(6):
            products.append({
                'name': f'Luxury Jacuzzi {i + 1}',
                'description': f'Description of Luxury Jacuzzi {i + 1}',
                'price': f'${2000 + i * 500}',
                'video_url': f'https://video.url/luxury_jacuzzi_{i+1}',
                'image_url': f'https://image.url/luxury_jacuzzi_{i+1}.jpg'
            })
        return products

class Agent2:
    @staticmethod
    def write_report(products):
        report = "Luxury Jacuzzi Report\n\n"
        for product in products:
            report += f"{product['name']} - {product['description']} - {product['price']}\n"
        return report

class Agent3:
    @staticmethod
    def generate_html(products, report):
        html_content = '<html><head><title>Luxury Showroom</title></head><body>'
        html_content += '<h1>Luxury Jacuzzi Showroom</h1>'
        html_content += '<h2>Report</h2>'
        html_content += f'<pre>{report}</pre>'
        html_content += '<h2>Products</h2>'
        for product in products:
            html_content += f"<h3>{product['name']}</h3>\n"
            html_content += f"<p>{product['description']}</p>\n"
            html_content += f"<p>Price: {product['price']}</p>\n"
            html_content += f"<video src='{product['video_url']}' controls></video>\n"
            html_content += f"<img src='{product['image_url']}' alt='{product['name']}' />\n"
        html_content += '</body></html>'
        with open('luxury_showroom.html', 'w') as file:
            file.write(html_content)

class Agent4:
    @staticmethod
    def read_report(report):
        communicate(report)

if __name__ == '__main__':
    products = Agent1.research_jacuzzis()
    report = Agent2.write_report(products)
    Agent3.generate_html(products, report)
    Agent4.read_report(report)
