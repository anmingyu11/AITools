# inverse dict
def inverse_mapping(dc):
    return dc.__class__(map(reversed, dc.items()))