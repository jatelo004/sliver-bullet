def simp_alert(money_spent, texts_sent, texts_replied, dates_asked, dates_accepted):
    # Avoid division by zero
    reply_rate = texts_replied / texts_sent if texts_sent > 0 else 0
    date_rate = dates_accepted / dates_asked if dates_asked > 0 else 0
    
    score = (reply_rate + date_rate) / 2
    
    if score >= 0.5:
        return "She likes you"
    elif score >= 0.2:
        return "Lukewarm"
    else:
        return "You are simping"

# Three test calls
print(simp_alert(5000, 40, 28, 6, 4))   # High engagement
print(simp_alert(3000, 50, 15, 8, 2))   # Medium engagement
print(simp_alert(8000, 60, 5, 10, 1))   # Low engagement