from flask import Flask, send_from_directory
import os
import time  # ✅ Add this line

app = Flask(__name__)

def redirect_to_youtube():
    os.system("clear")
    banner = """
\033[1;32m╭────────────────────────────────────────────────────────────╮
│                                                            │
│      🔐 This tool is part of the Hackers Colony arsenal.   │
│                                                            │
│  ⚠️  Access is restricted to verified users only.           │
│                                                            │
│  🔗 Please subscribe to our YouTube channel to unlock it.   │
│                                                            │
│       ⏳ Redirecting in 10 seconds... Stand by.             │
│                                                            │
╰────────────────────────────────────────────────────────────╯\033[0m
"""
    print(banner)
    time.sleep(10)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    input("\n\033[1;32m[✔] After subscribing, press Enter to continue...\033[0m\n")

@app.route('/')
def serve_prank():
    return send_from_directory('.', 'prank.html')

@app.route('/hackervoice.mp3')
def serve_audio():
    return send_from_directory('.', 'hackervoice.mp3')

if __name__ == '__main__':
    redirect_to_youtube()
    print("\033[1;34m[✔] Flask server running at http://127.0.0.1:8080\033[0m")
    print("\033[1;36m[>] Run: cloudflared tunnel --url http://127.0.0.1:8080\033[0m")
    app.run(host='127.0.0.1', port=8080)
