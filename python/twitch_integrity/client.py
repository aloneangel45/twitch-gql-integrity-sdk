import requests
from typing import Dict, Any

class TwitchIntegrityClient:
    """Enterprise client for Twitch GQL Client-Integrity Tokens."""
    
    def __init__(self, rapidapi_key: str, host: str = "twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com"):
        self.rapidapi_key = rapidapi_key
        self.host = host
        self.base_url = f"https://{host}/api/v1/twitch"

    def get_integrity_token(self) -> Dict[str, Any]:
        """Fetch fresh Twitch Client-Integrity token for stream playback & GQL."""
        headers = {
            "x-rapidapi-host": self.host,
            "x-rapidapi-key": self.rapidapi_key,
            "Content-Type": "application/json"
        }
        response = requests.post(f"{self.base_url}/integrity", headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
