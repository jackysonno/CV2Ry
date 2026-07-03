import requests
import re

def fetch_vless():
    # Target telegram channel web version
    url = "https://t.me/s/V2ray_Alpha"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        html_content = response.text
        
        # Extract all vless links
        vless_configs = re.findall(r'vless://[^\s"<>\'\\]+', html_content)
        
        if vless_configs:
            # Remove duplicates while preserving order
            unique_configs = list(dict.fromkeys(vless_configs))
            
            # Save to configs.txt
            with open("configs.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(unique_configs))
            print(f"Successfully saved {len(unique_configs)} configs.")
        else:
            print("No configs found in recent messages.")
            
    except Exception as e:
        print(f"Error executing script: {e}")

if __name__ == "__main__":
    fetch_vless()
