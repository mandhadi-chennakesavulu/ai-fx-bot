import requests

OANDA_API_KEY = '0ec10b3425bf3c7cd8d5c7bcd9f2d880-576ac8bd3c585ae8cfd018ab15b2c542'
ACCOUNT_ID = '101-001-35008001-001'
OANDA_URL = 'https://api-fxpractice.oanda.com/v3/instruments/EUR_USD/candles'

HEADERS = {
    'Authorization': f'Bearer {OANDA_API_KEY}',
}

def get_latest_candle():
    params = {
        'count': 2,
        'granularity': 'M1',
        'price': 'M'
    }
    try:
        response = requests.get(OANDA_URL, headers=HEADERS, params=params)
        response.raise_for_status()
        candles = response.json().get('candles', [])
        if candles:
            return {
                'open': float(candles[-1]['mid']['o']),
                'high': float(candles[-1]['mid']['h']),
                'low': float(candles[-1]['mid']['l']),
                'close': float(candles[-1]['mid']['c']),
                'volume': int(candles[-1]['volume'])
            }
    except Exception as e:
        print(f"Error fetching candle: {e}")
    return None