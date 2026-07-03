import requests
import re
import html

def fetch_configs():
    # List of target channels
    channels = [
        "https://t.me/s/V2ray_Alpha",
        "https://t.me/s/ProxyMtAlpha"
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    all_configs = []
    
    for url in channels:
        try:
            response = requests.get(url, headers=headers, timeout=15)
            html_content = response.text
            
            # Fix Telegram formatting issues
            html_content = html_content.replace("<wbr>", "").replace("<wbr/>", "")
            html_content = html_content.replace("\u200b", "").replace("\u200c", "")
            html_content = html.unescape(html_content)
            
            # Extract both vless and vmess links
            configs = re.findall(r'(?:vless|vmess)://[^\s"<>\'\\]+', html_content)
            all_configs.extend(configs)
            
        except Exception as e:
            print(f"Error fetching from {url}: {e}")
            
    if all_configs:
        # Remove duplicates while preserving order
        unique_configs = list(dict.fromkeys(all_configs))
        
        # Save clean configs
        with open("configs.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(unique_configs))
        print(f"Successfully saved {len(unique_configs)} valid configs.")
    else:
        print("No configs found.")

if __name__ == "__main__":
    fetch_configs()
