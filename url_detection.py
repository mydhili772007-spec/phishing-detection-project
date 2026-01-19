def detect_phishing_url(url):
    if not url.startswith("https"):
        return " Unsafe Website (No HTTPS)"

    suspicious_words = ["login", "verify", "bank", "secure", "update", "account", "password",
                        "confirm", "alert", "suspend", "urgent", "immediate", "action", "request",
                        "access", "identity", "protection", "notification", "reset", "unauthorized",
                        "warning", "safeguard", "compromise", "threat", "fraud", "scam", "danger",
                        "risk", "breach", "malware", "virus", "spyware", "phishing", "hijack",
                        "exploit", "attack", "infiltrate", "theft", "loss", "expose", "vulnerability",
                        "intrusion", "deception", "manipulate", "impersonate", "masquerade", "spoof",
                        "clone", "fake", "forged", "counterfeit", "bogus", "fraudulent", "illegitimate",
                        "unauthenticated", "unverified", "suspicious", "dubious"]
    for word in suspicious_words:
        if word in url.lower():
            return "Possible Phishing Website"

    return " Legitimate Website"


url = "http://secure-bank-login.net"
print(detect_phishing_url(url))
