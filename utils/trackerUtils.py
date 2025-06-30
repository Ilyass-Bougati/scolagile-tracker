from notifypy import Notify
from bs4 import BeautifulSoup


def send_init_notification():
    """
        This function send the first notification when the application runs
    """
    notification = Notify()
    notification.title = "The app is running"
    notification.application_name = "Scolagile tracker"
    notification.message = "It'll be running smoothly in the background"
    notification.icon = "icon/icon.png"
    notification.urgency = "critical"
    notification.send()

def send_change_notification():
    """
        This function notifies the user that the page has changed
    """
    notification = Notify()
    notification.title = "Scolagile Notes Changed!!"
    notification.message = "Someone changed your notes on scolagile, enter to check them"
    notification.application_name = "Scolagile tracker"
    notification.icon = "icon/icon.png"
    notification.urgency = "critical"
    notification.send()

def get_notes(page: str) -> list[float]:
    """
        This function takes the page html and returns the notes
    """
    original_page = BeautifulSoup(page, 'html.parser')
    exclusion = ["", "CT", "CC"]
    notes = []
    for td in original_page.find_all('td', {'rowspan': '1'}):
        note = td.get_text(strip=True)
        if note not in exclusion:
            notes.append(float(note))

    return sorted(notes)

def compare_notes(original_notes: list[float], new_notes: list[float]) -> bool:
    """
        The notes must be sorted beforehand
    """
    if len(original_notes) != len(new_notes):
        return False
    
    for i in range(len(original_notes)):
        if original_notes[i] != new_notes[i]:
            return False

    return True