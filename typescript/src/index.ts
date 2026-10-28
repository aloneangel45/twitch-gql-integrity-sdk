export class TwitchIntegrityClient {
  private rapidApiKey: string;
  private host: string;

  constructor(apiKey: string, host = "twitch-gql-integrity-ad-free-stream-api.p.rapidapi.com") {
    this.rapidApiKey = apiKey;
    this.host = host;
  }

  async getIntegrityToken() {
    const res = await fetch(`https://${this.host}/api/v1/twitch/integrity`, {
      method: "POST",
      headers: {
        "x-rapidapi-host": this.host,
        "x-rapidapi-key": this.rapidApiKey,
        "Content-Type": "application/json"
      }
    });

    if (!res.ok) {
      throw new Error(`Twitch API error: ${res.status} ${res.statusText}`);
    }
    return await res.json();
  }
}
