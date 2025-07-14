import os

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
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya")
    time.sleep(10)
    input("\n\033[1;32m[✔] After subscribing, press Enter to continue...\033[0m\n")

# Run the YouTube redirect first
redirect_to_youtube()

# Start the prank server
print("\033[1;34m[✔] Starting prank server at http://127.0.0.1:8080\033[0m")
print("\033[1;36m[>] Now run this in another Termux tab:\033[0m")
print("\033[1;33m    cloudflared tunnel --url http://127.0.0.1:8080\033[0m\n")

# Launch HTTP server
os.system("python3 -m http.server 8080")
