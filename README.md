# Twitch GQL Integrity Token Generator & Ad-Free Client-Integrity Stream Bypass API

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Active%20API-purple.svg?logo=rapidapi)](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/twitch-gql-integrity-ad-free-stream-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Latency](https://img.shields.io/badge/Latency-Sub--50ms-green.svg)]()

High-performance **Twitch GraphQL (GQL) Client-Integrity Token Provider**. Generates cryptographic Twitch integrity tokens (`Client-Integrity`, `Client-Session-Id`, `X-Device-Id`) required for ad-free stream playback, chat telemetry, and channel claim endpoints.

---

## 🚀 Marketplace & Live Endpoint

- **RapidAPI Hub:** [Twitch GQL Integrity API](https://rapidapi.com/aether-protocol-labs-aether-protocol-labs-default/api/twitch-gql-integrity-ad-free-stream-api)
- **Base Gateway:** `https://twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com`
- **Primary Endpoint:** `POST /api/v1/twitch/integrity`

---

## ⚡ Installation & Quickstart

### Python

```python
import requests

RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"

url = "https://twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com/api/v1/twitch/integrity"
headers = {
    "x-rapidapi-host": "twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
print("Twitch Integrity Token:", response.json())
```

---

## 🛡 Features

- **Ad-Free Stream Token Retrieval:** Bypass preroll and midroll injections via authentic client integrity headers.
- **Auto-Refreshing Spader Keys:** Handles periodic key rotations on Twitch's Edge CDN.
- **Full GQL Compatibility:** Ready to pass in `Client-Integrity` header for `PlaybackAccessToken_Template` queries.

---

## 📄 License
MIT © Aether Protocol Labs
