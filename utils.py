from datetime import datetime


def parse_date(date_text):
    try:
        return datetime.strptime(date_text.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def days_between(start_date, end_date):
    delta = end_date - start_date
    return delta.days + 1 if delta.days >= 0 else 0


def show_error(message):
    print(f"Error: {message}")


def confirm_text(question):
    answer = input(question + " (si/no): ").strip().lower()
    return answer == "si"
