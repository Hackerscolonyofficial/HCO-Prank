# 📱 HCO-Prank

A terrifying browser-based phone lock prank tool made for **fun, ethical testing, and entertainment only**.  
Once opened, the page appears to **hack the victim’s phone**, vibrates, plays a scary voice, and flashes red background — simulating a realistic browser freeze attack.

---

## ⚙️ Features

- 🔒 Fullscreen phone lock simulation
- 🚫 Disables back, scroll, long press, and inspect
- 📳 Auto vibration on loop
- 🎧 Voice playback: “Your phone has been hacked by Hackers Colony team”
- ⚡ Flashing red screen background
- ✅ Works in any mobile browser

---

## 🛠 Termux Setup Instructions

```bash
# 1. Update and install essentials
pkg update && pkg install python git -y

# 2. Install cloudflared
pkg install cloudflared -y

# 3. Clone the HCO-Prank repo
git clone https://github.com/Hackerscolonyofficial/HCO-Prank.git
cd HCO-Prank

# 4. Install dependencies
pip install -r requirements.txt

# 5. Make the script executable and run
chmod +x start.sh
bash start.sh
```

👉 In a new session, start Cloudflare tunnel:
```bash
cloudflared tunnel --url http://127.0.0.1:8080
```

> Send the generated link to the target. Once opened, the prank will begin instantly.

---

## 📡 Connect with Hackers Colony

[![Instagram](https://img.shields.io/badge/Instagram-%40hackers__colony__official-red?logo=instagram)](https://www.instagram.com/hackers_colony_official)  
[![Telegram](https://img.shields.io/badge/Telegram-HackersColony-blue?logo=telegram)](https://t.me/hackersColony)  
[![Facebook](https://img.shields.io/badge/Facebook-HackersColony-1877F2?logo=facebook)](https://www.facebook.com/share/1AY25it2Em/)  
[![YouTube](https://img.shields.io/badge/YouTube-HackersColonyTech-FF0000?logo=youtube)](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)  
[![Discord](https://img.shields.io/badge/Discord-HackersColony-5865F2?logo=discord)](https://discord.gg/Xpq9nCGD)  
[![Website](https://img.shields.io/badge/Visit%20Website-Blogspot-black?logo=google)](https://hackerscolonyofficial.blogspot.com/?m=1)

---

## 📜 Disclaimer

This project is made for **educational and ethical testing purposes** only.  
We are not responsible for any misuse. Do **not** use this on others without clear permission.

---

## 🧠 Hacker Quote

> _“Hackers are the artists of the digital age — we break things, not to destroy, but to rebuild better.”_

---

### 👨‍💻 Code by **Azhar** — Hackers Colony 👑
