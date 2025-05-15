from app.services.risk import kelly_bet_size
from app.config import settings

async def generate_signals(markets):
    signals = []
    for m in markets:
        edge = m['probabilities']['yes'] - 0.5
        size = kelly_bet_size(edge, settings.KELLY_FRACTION)
        if size > 0:
            signals.append({'market_id': m['id'], 'side': 'YES', 'fraction': size})
    return signals
