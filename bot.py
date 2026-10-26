# Business-Bot - General version for any business
def reply_to_customer(message, business_name="Our Store"):
 msg = message.lower()
 
 if "price" in msg or "بكام" in msg or "سعر" in msg:
 return f"Hello! Thanks for contacting {business_name}. Please send the product name and we will send you the price + shipping to your city."
 elif "location" in msg or "فين" in msg or "عنوان" in msg:
 return f"{business_name} offers delivery to all governorates. Where are you located?"
 else:
 return f"Welcome to {business_name}! How can I help you today?"

# Test
print(reply_to_customer("بكام؟", "Hamada Store"))
