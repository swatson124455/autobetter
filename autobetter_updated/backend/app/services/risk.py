def kelly_bet_size(edge, fraction=1.0):
    odds = edge != 0 and (edge / (1 - edge)) or 0
    return max(0, fraction * edge / odds) if odds else 0
