def detect_phishing_email(email):
    phishing_words = ["urgent", "verify", "login", "password", "bank","click","update","security"
                      ,"limited","suspend","confirm","alert","important","immediate","action","request"
                      ,"access","identity","protection","notification","reset","unauthorized","warning",
                      "safeguard","compromise","threat","fraud","scam","danger","risk","breach"
                      ,"malware","virus","spyware","phishing","hijack","exploit","attack","infiltrate",
                      "breach","theft","loss","expose","vulnerability","intrusion","deception","manipulate",
                      "impersonate","masquerade","spoof","clone","fake","forged","counterfeit","bogus",
                      "fraudulent","illegitimate","unauthenticated","unverified","suspicious","dubious",
                      "questionable","shady","untrustworthy","unreliable","dishonest","corrupt","crooked",
                      "unscrupulous","deceitful","misleading","trickery","cheat","swindle","con","scam","hoax","ruse","ploy","scheme"]
    email = email.lower()
    for word in phishing_words:
        if word in email:
            return " Phishing Email Detected"
    return " Safe Email"
email_text = "Dear User, We have detected unusual activity on your bank account. Please click the link below to verify your information immediately to avoid suspension of your account.\n\nBest regards,\nYour Bank Security Team"
print(detect_phishing_email(email_text))
