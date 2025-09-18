"""
Safe phone-number info script using `phonenumbers`.
This prints region/country, carrier, possible time zones, validity, and formatted versions.
It DOES NOT and CANNOT provide exact GPS location from just a phone number.

Install dependency:
    pip install phonenumbers
"""

import phonenumbers
from phonenumbers import geocoder, carrier, timezone, NumberParseException, PhoneNumberFormat


def get_phone_info(number_str, default_region=None, lang='en'):
    """
    Parse a phone number string and return a dictionary with
    region description, carrier name, timezones, validity and formats.
    `default_region` is a 2-letter region code (like "IN", "US") used for numbers without + prefix.
    """
    info = {'input': number_str, 'parsed': None, 'error': None}
    try:
        num = phonenumbers.parse(number_str, default_region)
        info['parsed'] = num

        # Valid number?
        info['is_valid'] = phonenumbers.is_valid_number(num)
        info['is_possible'] = phonenumbers.is_possible_number(num)

        # Region / description (city/country-level)
        info['region'] = geocoder.description_for_number(num, lang)

        # Carrier (may be generic or empty)
        info['carrier'] = carrier.name_for_number(num, lang)

        # Timezones possibly associated with the number / country-level
        info['time_zones'] = timezone.time_zones_for_number(num)

        # International and national formatted versions
        info['format_international'] = phonenumbers.format_number(num, PhoneNumberFormat.INTERNATIONAL)
        info['format_national'] = phonenumbers.format_number(num, PhoneNumberFormat.NATIONAL)
        info['e164'] = phonenumbers.format_number(num, PhoneNumberFormat.E164)

    except NumberParseException as e:
        info['error'] = str(e)

    return info


def print_info(info):
    if info['error']:
        print(f"Input: {info['input']}  -> Parse error: {info['error']}")
        return

    print(f"Input: {info['input']}")
    print(f" E.164: {info.get('e164')}")
    print(f" International: {info.get('format_international')}")
    print(f" National: {info.get('format_national')}")
    print(f" Valid number: {info.get('is_valid')}, Possible: {info.get('is_possible')}")
    print(f" Region / description: {info.get('region') or 'N/A'}")
    print(f" Carrier: {info.get('carrier') or 'N/A'}")
    t = info.get('time_zones') or []
    print(f" Timezones: {', '.join(t) if t else 'N/A'}")
    print("-" * 40)


if __name__ == "__main__":
    # Ask the user for phone number input
    number_str = input("Enter a phone number (with country code, e.g., +919876543210): ").strip()

    # Default region is fixed as None (only used when number has no + prefix)
    info = get_phone_info(number_str, default_region=None, lang='en')
    print_info(info)
