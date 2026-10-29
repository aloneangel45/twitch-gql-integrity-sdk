# 🟣 Twitch GQL Integrity Token Generator & Ad-Free Stream Client API SDK

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Active%20Listing-purple.svg?logo=rapidapi)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/twitch-gql-integrity-ad-free-stream-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Latency](https://img.shields.io/badge/Latency-Sub--50ms-brightgreen.svg)]()
[![Free Tier](https://img.shields.io/badge/Free%20Plan-50%20Calls%2Fmo-green.svg)]()

> **High-performance Twitch GraphQL (GQL) Client-Integrity Token Provider. Generates authentic cryptographic Twitch integrity tokens (`Client-Integrity`, `Client-Session-Id`, `X-Device-Id`) required for ad-free stream playback, chat telemetry, and channel claim endpoints.**

---

## 🚀 Instant Free Access (50 Free Calls/Month)

Subscribe and get your live API key in 5 seconds:  
👉 **[Subscribe on RapidAPI Hub (Free Plan Available)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/twitch-gql-integrity-ad-free-stream-api)**

- **RapidAPI Host:** `twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com`
- **Base Gateway:** `https://twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com`

---

## ⚡ Why Use Twitch GQL Integrity API?

* **Ad-Free Stream Token Retrieval:** Bypass preroll and midroll ad injections via authentic client integrity headers.
* **Auto-Refreshing Spader Keys:** Handles periodic key rotations on Twitch's Edge CDN automatically.
* **Full GQL Compatibility:** Ready to pass in `Client-Integrity` header for `PlaybackAccessToken_Template` queries.
* **Sub-50ms Response:** Instant cryptographic header generation without launching Chromium or scraping frontend scripts.

---

## 💻 Quickstart Examples

### 1. cURL (Instant Terminal Test)
```bash
curl --request POST \
  --url https://twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com/api/v1/twitch/integrity \
  --header 'x-rapidapi-host: twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com' \
  --header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### 2. Python (`requests`)
```python
import requests

API_KEY = "YOUR_RAPIDAPI_KEY"

url = "https://twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com/api/v1/twitch/integrity"
headers = {
    "x-rapidapi-host": "twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com",
    "x-rapidapi-key": API_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
data = response.json()
print("Twitch Client-Integrity:", data.get("client_integrity"))
print("Client Session ID:", data.get("client_session_id"))
```

### 3. Node.js / TypeScript (`axios`)
```typescript
import axios from "axios";

async function getTwitchIntegrity() {
  const res = await axios.post(
    "https://twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com/api/v1/twitch/integrity",
    {},
    {
      headers: {
        "x-rapidapi-host": "twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com",
        "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_RAPIDAPI_KEY"
      }
    }
  );
  console.log("Twitch Integrity Headers:", res.data);
}

getTwitchIntegrity();
```

---

## 🎯 Endpoints Available

1. `POST /api/v1/twitch/integrity` — Acquire freshly signed Twitch Client-Integrity token pair.
2. `POST /api/v1/twitch/playback-token` — Retrieve pre-authenticated playback access token for any Twitch channel.

---

## 🔍 SEO & Use Cases
- **Custom Twitch Players:** VLC, MPV, Streamlink, and Kodi plugins without preroll ad interruptions.
- **Chat & Livestream Bots:** Channel points claimers, drop farmers, and chat analytics suites.
- **Automated Restreaming:** Clean HLS feed extraction for private stream archives.

---

## 📄 License
MIT © [Aether Protocol Labs](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default)
