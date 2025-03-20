# 🚀 ClipQuick - URL Shortener 

### **Shorten. Share. Track. Repeat.**  

Tired of those **long, ugly URLs**? Say hello to **Flask URL Shortener** – a simple yet powerful way to **shorten URLs**, track clicks, and even protect them with passwords!

---

## 🎯 **Why This Exists**  
Ever wanted to:
✅ **Shorten links** without relying on third-party services?
✅ **Set expiration dates** so links die when you want?
✅ **Protect links with passwords** (because not all links are for everyone)?

If you said **yes** to any of these, this project is for you! 💡  

---

## 🔥 **Features at a Glance**  

- **Generate Short URLs**: Instantly shorten long URLs.  
- **Redirection**: Clicking a short link takes you to the original page.  
- **QR Code Generation**: Generate a QR code for every shortened URL.  
- **Password Protection**: Secure your links with passwords.  
- **REST API**: Shorten URLs programmatically.  
- **URL Expiration**: Set a time limit for your links. 

---

### 🎯 API Usage
#### Shorten a URL (POST Request)

```bash
curl -X POST http://127.0.0.1:5000/api/shorten \
     -H "Content-Type: application/json" \
     -d '{"original_url": "https://example.com"}'
```

✅ **Response:**
```json
{
  "short_url": "http://127.0.0.1:5000/abc123"
}
```

---

#### Redirect to Original URL (GET Request)

```bash
curl -X GET http://127.0.0.1:5000/abc123
```

✅ **Redirects to:** `https://example.com`
