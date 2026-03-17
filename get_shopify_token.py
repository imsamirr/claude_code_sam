"""
Quick script to complete Shopify OAuth and get an access token.
1. Starts a local server on port 12345
2. Opens the Shopify auth URL
3. Catches the callback with the `code` parameter
4. Exchanges it for a permanent access token
"""

import http.server
import urllib.parse
import requests
import threading
import sys

SHOP = "ortho-wears.myshopify.com"
CLIENT_ID = "2950875a7389c3574d7e8139272a22ce"
CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:12345/callback"
SCOPES = "read_orders,read_products,read_customers"

access_token_result = None


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global access_token_result
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if "code" in params:
            code = params["code"][0]
            print(f"\n[+] Received authorization code: {code[:10]}...")

            # Exchange code for access token
            token_url = f"https://{SHOP}/admin/oauth/access_token"
            payload = {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": code,
            }
            resp = requests.post(token_url, json=payload, timeout=30)

            if resp.status_code == 200:
                data = resp.json()
                access_token_result = data.get("access_token", "")
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Success! You can close this tab.</h1><p>Access token retrieved. Check your terminal.</p>")
                print(f"\n{'='*50}")
                print(f"ACCESS TOKEN: {access_token_result}")
                print(f"{'='*50}")
                print(f"\nAdd this to your .env file:")
                print(f"SHOPIFY_ACCESS_TOKEN={access_token_result}")
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                error_msg = resp.text
                self.wfile.write(f"<h1>Error</h1><pre>{error_msg}</pre>".encode())
                print(f"\n[!] Token exchange failed: {resp.status_code}")
                print(resp.text)

            # Shutdown server after handling
            threading.Thread(target=self.server.shutdown).start()
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>No code parameter found</h1>")

    def log_message(self, format, *args):
        pass  # Suppress default logging


def main():
    auth_url = (
        f"https://{SHOP}/admin/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        f"&scope={SCOPES}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
    )

    print(f"Starting local server on port 12345...")
    server = http.server.HTTPServer(("localhost", 12345), CallbackHandler)

    print(f"\nOpen this URL in your browser to authorize:\n")
    print(f"  {auth_url}\n")
    print("Waiting for callback...")

    server.serve_forever()

    if access_token_result:
        print("\nDone! Token saved above.")
    else:
        print("\nFailed to get token.")
        sys.exit(1)


if __name__ == "__main__":
    main()
