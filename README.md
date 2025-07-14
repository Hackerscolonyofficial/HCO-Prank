# 📱 HCO-Prank

A terrifying browser-based phone lock prank tool. Made for **fun, ethical testing, and hacker-style pranks only**.

## ⚙️ Features
- Fullscreen fake phone lock screen
- Flashing background, auto vibration
- Audio message: “Your phone has been hacked by Hackers Colony team”
- Blocks back, scroll, dev tools, context menu
- No escape feel

## 🛠 Termux Setup

```bash
pkg update && pkg install python git -y
pkg install cloudflared -y
pip install flask
git clone https://github.com/Hackerscolonyofficial/HCO-Prank.git
cd HCO-Prank
chmod +x start.sh
./start.sh
```

Then in **another tab**:

```bash
cloudflared tunnel --url http://127.0.0.1:8080
```

## 📢 Disclaimer

This tool is for **educational and entertainment purposes** only.  
Do not use it on anyone without their **consent**.

## 👨‍💻 Code by Azhar — Hackers Colony
