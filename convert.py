# 2025 USD-Based Currency Converter for Gemini

rates = {
    "AED": 0.272256, "AUD": 0.659402, "BRL": 0.175218, "CAD": 0.719718,
    "CHF": 1.153524, "CNY": 0.140301, "EUR": 1.080778, "GBP": 1.296946,
    "HKD": 0.128676, "IDR": 0.000064, "INR": 0.011894, "JPY": 0.006527,
    "MXN": 0.049959, "MYR": 0.22945,  "NZD": 0.59776,  "SGD": 0.75589,
    "THB": 0.029596, "ZAR": 0.05652,  "USD": 1.0,      "DKK": 0.144886,
    "TWD": 0.031162, "KRW": 0.000722, "SEK": 0.094102
}

def truncate_to_2_decimal(number):
    s = str(number)
    if "." in s:
        whole, decimal = s.split(".")
        return f"{whole}.{(decimal + '00')[:2]}"
    return f"{s}.00"

# ✏️ Replace these values with Gemini form variables when used in production
amount = 3000.00
source_currency = "USD"
target_currency = "JPY"

source = source_currency.upper()
target = target_currency.upper()

if source != "USD" and target != "USD":
    output = "❌ Only USD-based conversions are supported. Convert either from or to USD."
elif source not in rates or target not in rates:
    output = "❌ Currency code not found. Please check input."
else:
    if source == "USD":
        operation = "divide"
        rate = rates[target]
        raw = amount / rate
    else:
        operation = "multiply"
        rate = rates[source]
        raw = amount * rate

    result = truncate_to_2_decimal(raw)

    output = (
        f"📌 Convert {source} {amount} to {target}\n"
        f"✔ Rate used: {rate}\n"
        f"🧮 {amount} {'÷' if operation == 'divide' else '×'} {rate} = {raw}\n"
        f"✂️ Truncated to 2 decimal places: {result}\n\n"
        f"✅ Final result: {target} {result} NET"
    )

print(output)
