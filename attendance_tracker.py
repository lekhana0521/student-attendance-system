import csv

# Step 1: Read file
def get_file_data():
    try:
        with open("attendance.txt", "r") as file:
            data = file.readlines()
            print("DEBUG: Data read from file ↓")
            print(data)   # 👈 THIS WILL SHOW IF FILE IS READ
            return data
    except Exception as e:
        print("❌ Error reading file:", e)
        return []

# Step 2: Process attendance
def process_attendance(lines):
    attendance = {}

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if " - " in line:   # 👈 IMPORTANT (space dash space)
            name, date = line.split(" - ")

            if name not in attendance:
                attendance[name] = set()

            attendance[name].add(date)

    print("DEBUG: Processed attendance ↓")
    print(attendance)   # 👈 CHECK DATA

    return attendance

# Step 3: Generate report
def generate_report(attendance):
    if not attendance:
        print("❌ No attendance data found!")
        return

    all_dates = set()
    for dates in attendance.values():
        all_dates.update(dates)

    total_days = len(all_dates)

    with open("attendance_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student Name", "Days Present", "Attendance %"])

        for student, days in attendance.items():
            present = len(days)
            percentage = (present / total_days) * 100 if total_days > 0 else 0

            writer.writerow([student, present, f"{percentage:.2f}%"])

    print("✅ Attendance Report Generated Successfully!")

# Main
if __name__ == "__main__":
    data = get_file_data()
    attendance = process_attendance(data)
    generate_report(attendance)