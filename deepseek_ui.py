#!/usr/bin/env python3
"""一键启动 DeepSeek 去除 AI 痕迹 UI

使用方式（单行命令）：
    python e:/workplace/deepseek-anti-ai-agent/deepseek_ui.py
"""
import http.server
import socketserver
import threading
import webbrowser
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PORT = 8000

class SilentHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def serve():
    os.chdir(BASE_DIR)
    with socketserver.TCPServer(("127.0.0.1", PORT), SilentHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=serve, daemon=True).start()
    url = f"http://127.0.0.1:{PORT}/ui.html"
    webbrowser.open(url)
    print(f"DeepSeek UI 已启动 → {url}")
    print("按 Ctrl+C 关闭服务器。")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n服务器已关闭。")
        sys.exit(0)
