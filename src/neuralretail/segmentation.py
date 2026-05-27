
def customer_segment(score):

    if score > 80:
        return "VIP"

    elif score > 50:
        return "Loyal"

    return "Regular"