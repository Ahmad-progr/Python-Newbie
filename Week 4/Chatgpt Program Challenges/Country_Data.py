import requests
import sys

def main():
    print("\n🌍 Country Information Finder")
    print("Type 'exit' to quit.\n")

    while True:
        country = input("Enter country name: ").strip()
        if country.lower() == "exit":
            sys.exit("\n👋 Goodbye!")

        try:
            response = requests.get(
                f"https://restcountries.com/v3.1/name/{country}?fullText=true"
            )
            data = response.json()

            if isinstance(data, dict) and data.get("status") == 404:
                print("❌ Country not found. Try again.\n")
                continue

            country_data = data[0]
            
            # Extract details safely
            capital = country_data.get("capital", ["N/A"])[0]
            population = country_data.get("population", "N/A")
            region = country_data.get("region", "N/A")
            flag = country_data.get("flag", "")
            
            currencies = []
            for code, details in country_data.get("currencies", {}).items():
                currencies.append(f"{details.get('name', 'N/A')} ({code})")
            currency_str = ", ".join(currencies) if currencies else "N/A"

            # Pretty Output
            print(f"\n{flag} {country_data['name']['common'].upper()}")
            print(f"🏛 Capital: {capital}")
            print(f"👥 Population: {population:,}")
            print(f"🌏 Region: {region}")
            print(f"💱 Currency: {currency_str}\n")

        except requests.exceptions.RequestException:
            sys.exit("🚨 Network error. Could not complete your request.")
        except (KeyError, IndexError):
            print("⚠️ Unexpected data format. Try another country.\n")

if __name__ == "__main__":
    main()