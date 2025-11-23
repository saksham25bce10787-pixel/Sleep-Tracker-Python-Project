from datetime import datetime

# Take time in HH:MM
def take_time(msg):
    t = input(msg + " (HH:MM): ")
    h, m = t.split(":")
    return datetime.strptime(t, "%H:%M")

# Calculate sleep hours
def sleep_hours(s, w):
    if w < s:
        w = w.replace(day=w.day + 1)
    return round((w - s).total_seconds() / 3600, 2)

# Decide quality
def quality(h):
    if h <= 4: return "Very Poor"
    if h <= 6: return "Poor"
    if h <= 7: return "Good"
    if h <= 8: return "Excellent"
    return "Over Sleeping"

# Save record
def save(h, q):
    today = datetime.now().date()
    f = open("sleep_history.txt", "a")
    f.write(f"{today} | {h} hrs | {q}\n")
    f.close()

# Show history
def show_history():
    print("\n----- Sleep History -----")
    f = open("sleep_history.txt", "r")
    data = f.read()
    f.close()
    if data.strip() == "":
        print("No history yet!")
    else:
        print(data)

# Main program
print("=== Sleep Tracker ===")
s = take_time("Sleep time")
w = take_time("Wake time")

hrs = sleep_hours(s, w)
q = quality(hrs)

save(hrs, q)

print("\nTotal Sleep:", hrs, "hours")
print("Sleep Quality:", q)
print("History saved!")

see = input("\nDo you want to See your sleep history? (y/n): ")
if see.lower() == "y":
    show_history()
else:
    print(" Okay Goodbye! Sweet dreams.")
