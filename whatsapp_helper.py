import requests

# UltraMsg Account Credentials
INSTANCE_ID = "instance186765"  # Apni UltraMsg Instance ID yahan dalein
TOKEN = "gi55vbaimdxsi2ro"      # Apna UltraMsg Token yahan dalein
ULTRAMSG_URL = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

def send_whatsapp_message(phone_number, message):
    """
    Sends an automated WhatsApp message to the given phone number using UltraMsg API.
    """
    # Clean phone number (remove spaces, plus sign, dashes)
    clean_phone = str(phone_number).replace("+", "").replace(" ", "").replace("-", "")
    
    payload = {
        "token": TOKEN,
        "to": clean_phone,
        "body": message
    }
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    try:
        response = requests.post(ULTRAMSG_URL, data=payload, headers=headers)
        result = response.json()
        print(f"✅ WhatsApp Message Sent to {clean_phone}:", result)
        return result
    except Exception as e:
        print(f"❌ Error sending WhatsApp message: {e}")
        return None