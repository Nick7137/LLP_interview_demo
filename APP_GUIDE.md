# Two-App Setup Guide

This application now has **two separate interfaces**:

## 📱 Mobile App (Android/iPhone)
**For NFC card tapping**

### Access:
- URL: `http://your-server-ip:8000/mobile/`
- Or: `http://your-server-ip:8000/` (default route)

### Features:
- NFC card detection
- Automatic receipt creation
- Visual feedback when card is tapped
- Optimized for mobile screens

### How to Use:
1. Open the mobile URL on your phone (Chrome on Android or Safari on iOS)
2. Make sure you're using HTTPS (required for NFC)
3. Tap the screen once to enable NFC
4. Hold your NFC card near the phone
5. Receipt is automatically created and sent to server

---

## 💻 Desktop Viewer (Laptop)
**For viewing all receipts**

### Access:
- URL: `http://your-server-ip:8000/desktop/`

### Features:
- View all receipts sent from mobile devices
- Search and filter receipts
- Statistics dashboard (total receipts, total amount, today's receipts)
- Auto-refreshes every 5 seconds
- Click any receipt to see detailed itemized breakdown

### How to Use:
1. Open the desktop URL on your laptop/computer
2. View all receipts in a grid layout
3. Use search box to filter by merchant, receipt number, or amount
4. Click "Refresh" to manually update
5. Click any receipt card to see full details

---

## Setup Instructions

### 1. Start the Django Server

```bash
python manage.py runserver 0.0.0.0:8000
```

The `0.0.0.0` makes it accessible from other devices on your network.

### 2. Find Your Server IP Address

**Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" (e.g., 192.168.1.100)

**Mac/Linux:**
```bash
ifconfig
```
or
```bash
hostname -I
```

### 3. Access from Mobile Device

1. Make sure your phone is on the same Wi-Fi network
2. Open browser and go to: `http://YOUR_IP:8000/mobile/`
   - Example: `http://192.168.1.100:8000/mobile/`

### 4. Access from Laptop

1. Open browser and go to: `http://YOUR_IP:8000/desktop/`
   - Or use `http://localhost:8000/desktop/` if on the same machine

---

## HTTPS Setup (Required for NFC)

Web NFC API requires HTTPS. For local testing, you can use:

### Option 1: ngrok (Easiest)
```bash
# Install ngrok: https://ngrok.com/
ngrok http 8000
```
Use the HTTPS URL provided by ngrok on your mobile device.

### Option 2: Django with SSL
Use a reverse proxy like nginx with SSL certificates.

---

## URLs Summary

| Purpose | URL |
|---------|-----|
| Mobile NFC Tapper | `/mobile/` or `/` |
| Desktop Viewer | `/desktop/` |
| Receipt Detail | `/receipt/<receipt_number>/` |
| API - Create Receipt | `/api/nfc-tap/` |
| API - Get Receipts | `/api/receipts/` |

---

## Workflow

1. **Employee taps NFC card** on mobile app → Receipt created
2. **Manager opens desktop viewer** → Sees all receipts in real-time
3. **Click receipt** → View detailed itemized breakdown

---

## Troubleshooting

### Mobile app not detecting NFC:
- Make sure you're using HTTPS
- Use Chrome on Android or Safari on iOS 13+
- Check that NFC is enabled on your device
- Try tapping the screen first to enable NFC

### Desktop viewer not showing receipts:
- Check that the server is running
- Make sure API endpoint is accessible
- Check browser console for errors
- Click "Refresh" button

### Can't access from mobile device:
- Make sure both devices are on same Wi-Fi network
- Check firewall settings
- Use `0.0.0.0:8000` instead of `127.0.0.1:8000`
- Verify IP address is correct



