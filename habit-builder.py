import datetime

# 🧾 Decorator to log habit tracking
def log_habit(func):
    def wrapper(*args, **kwargs):
        print(f"\n🕒 [{datetime.datetime.now()}] Logging your habit...")
        result = func(*args, **kwargs)
        print("✅ Habit logged successfully!\n")
        return result
    return wrapper

# 🎯 Closure to generate messages
def habit_response_generator():
    messages = {
        "exercise": "Awesome! Keep your body strong and your mind sharper 🏋️‍♀️🧠",
        "study": "You're building your future, one session at a time 📚🌟",
        "read": "Books are your brain's best friends 📖💡",
        "meditate": "Peace within brings peace outside 🧘‍♀️🌼",
        "journal": "Writing clears your mind and boosts clarity 📝✨"
    }

    def get_message(habit):
        return messages.get(habit.lower(), "That's a valuable habit! Keep going 💪")
    
    return get_message

# 🧱 OOP: Class for Habit Tracking
class HabitTracker:
    def __init__(self, name):
        self.name = name
        self.habit_log = []

    @log_habit
    def track(self, habit):
        self.habit_log.append((habit, datetime.datetime.now()))
        response_func = habit_response_generator()
        print(f"{self.name}, {response_func(habit)}")

    def show_history(self):
        if not self.habit_log:
            print("📭 No habits logged yet.")
            return
        print(f"\n📜 Habit History for {self.name}:")
        for habit, timestamp in self.habit_log:
            print(f"🔹 {habit.title()} at {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

# 🚀 Main Program
if __name__ == "__main__":
    print("🌟 Welcome to Habit Builder with OOP 🌟")
    name = input("👤 Enter your name: ")
    tracker = HabitTracker(name)

    while True:
        action = input("\n🔹 Type a habit to log, 'history' to view log, or 'exit' to quit: ")
        if action.lower() == 'exit':
            print("👋 Keep growing, one habit at a time. See you again!")
            break
        elif action.lower() == 'history':
            tracker.show_history()
        else:
            tracker.track(action)
