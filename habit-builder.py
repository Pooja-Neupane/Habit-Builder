import datetime
import logging
import json
from typing import Callable, List, Tuple, Optional

# Configure logging for habit tracking (to file and console)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("habit_tracker.log"),
        logging.StreamHandler()
    ]
)

def log_habit(func: Callable) -> Callable:
    """
    Decorator to log habit tracking actions.
    """
    def wrapper(self, habit: str) -> None:
        logging.info(f"User '{self.name}' is logging habit: {habit}")
        func(self, habit)
        logging.info("Habit logged successfully.")
    return wrapper

def habit_response_generator() -> Callable[[str], str]:
    """
    Closure to generate motivational messages based on habit type.
    """
    messages = {
        "exercise": "Awesome! Keep your body strong and your mind sharper 🏋️‍♀️🧠",
        "study": "You're building your future, one session at a time 📚🌟",
        "read": "Books are your brain's best friends 📖💡",
        "meditate": "Peace within brings peace outside 🧘‍♀️🌼",
        "journal": "Writing clears your mind and boosts clarity 📝✨"
    }

    def get_message(habit: str) -> str:
        return messages.get(habit.lower(), "That's a valuable habit! Keep going 💪")

    return get_message

class HabitTracker:
    """
    Class to track user habits with timestamp and persistence.
    """
    def __init__(self, name: str, data_file: Optional[str] = "habit_data.json") -> None:
        self.name: str = name
        self.habit_log: List[Tuple[str, str]] = []  # Store habit and ISO timestamp string
        self.data_file: Optional[str] = data_file
        self._load_habits()

    @log_habit
    def track(self, habit: str) -> None:
        """
        Track a new habit with current timestamp.
        """
        timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
        self.habit_log.append((habit, timestamp))
        self._save_habits()
        response_func = habit_response_generator()
        print(f"{self.name}, {response_func(habit)}")

    def show_history(self) -> None:
        """
        Display the history of logged habits.
        """
        if not self.habit_log:
            print("📭 No habits logged yet.")
            return
        print(f"\n📜 Habit History for {self.name}:")
        for habit, timestamp in self.habit_log:
            print(f"🔹 {habit.title()} at {timestamp}")

    def _save_habits(self) -> None:
        """
        Save habit log to a JSON file.
        """
        if not self.data_file:
            return
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.habit_log, file, indent=4)
        except IOError as e:
            logging.error(f"Failed to save habits: {e}")

    def _load_habits(self) -> None:
        """
        Load habit log from a JSON file if it exists.
        """
        if not self.data_file:
            return
        try:
            with open(self.data_file, "r") as file:
                self.habit_log = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.habit_log = []

def get_non_empty_input(prompt: str) -> str:
    """
    Helper function to get non-empty input from the user.
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("⚠️ Input cannot be empty. Please try again.")

def main() -> None:
    print("🌟 Welcome to Habit Builder with OOP 🌟")
    name = get_non_empty_input("👤 Enter your name: ")
    tracker = HabitTracker(name)

    while True:
        action = input("\n🔹 Type a habit to log, 'history' to view log, or 'exit' to quit: ").strip().lower()
        if action == 'exit':
            print("👋 Keep growing, one habit at a time. See you again!")
            break
        elif action == 'history':
            tracker.show_history()
        elif action:
            tracker.track(action)
        else:
            print("⚠️ Please enter a valid command or habit.")

if __name__ == "__main__":
    main()
