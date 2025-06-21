def detect_mood(text):
    text = text.lower()
    if any(word in text for word in ["happy", "joy", "glad", "great", "cheerful", "awesome"]):
        return "😊 Happy"
    elif any(word in text for word in ["sad", "upset", "depressed", "crying", "down"]):
        return "😔 Sad"
    elif any(word in text for word in ["angry", "mad", "furious", "irritated"]):
        return "😡 Angry"
    elif any(word in text for word in ["anxious", "worried", "nervous", "tense"]):
        return "😟 Anxious"
    elif any(word in text for word in ["tired", "exhausted", "sleepy"]):
        return "🥱 Tired"
    else:
        return "😐 Neutral"