import requests

def load_payloads():
    with open("payloads.txt", "r") as f:
        return f.read().splitlines()

def scan_xss(url):
    payloads = load_payloads()
    vulnerable = False

    print("\n[*] Starting XSS Scan...\n")

    for payload in payloads:
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)
            if payload in response.text:
                print(f"[VULNERABLE] XSS Found with payload: {payload}")
                vulnerable = True
        except Exception as e:
            print(f"[ERROR] {e}")

    if not vulnerable:
        print("[SAFE] No XSS vulnerability found")

if __name__ == "__main__":
    target = input("Enter target URL (example: ?q=): ")
    scan_xss(target)