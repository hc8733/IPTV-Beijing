# update.py
# 仅替换固定的 "192.168.123.1:23234" 为 config 中的 my_ip_port

import json
import sys
from datetime import datetime

try:
    import requests
except Exception:
    print("缺少 requests 模块，请在运行环境中安装：pip install requests")
    raise

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    cfg = load_config()
    source_url = cfg.get("source_url")
    my_ip_port = cfg.get("my_ip_port")
    out_file = cfg.get("output_filename", "IPTV.m3u")

    if not my_ip_port or ":" not in my_ip_port:
        print(f"配置错误：my_ip_port 格式不正确：{my_ip_port}")
        sys.exit(2)

    print(f"{datetime.now()} - 开始下载源文件：{source_url}")
    try:
        r = requests.get(source_url, timeout=30)
        r.encoding = r.apparent_encoding or "utf-8"
        content = r.text
    except Exception as e:
        print("下载源文件失败：", e)
        sys.exit(3)

    if not content:
        print("下载到的内容为空，退出。")
        sys.exit(4)

    # 只替换固定的 IP:端口
    target = "192.168.123.1:23234"
    if target in content:
        new_content = content.replace(target, my_ip_port)
        print(f"{datetime.now()} - 已将 {target} 替换为 {my_ip_port}")
    else:
        new_content = content
        print(f"{datetime.now()} - 源文件中未找到 {target}，未做替换。")

    try:
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"{datetime.now()} - 已写入 {out_file}")
    except Exception as e:
        print("写入输出文件失败：", e)
        sys.exit(5)

if __name__ == "__main__":
    main()
