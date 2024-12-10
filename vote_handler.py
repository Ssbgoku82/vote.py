import csv

def check_and_update_vote(user_id, selected_mascot):
    try:
        with open("IDlist.csv", mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        user_data = None
        for row in rows:
            if row['ID Number'].strip() == user_id.strip():
                user_data = row
                break

        if user_data is None:
            return f"ID {user_id} not found. Please register."

        if user_data['Voted'] == 'Yes':
            return f"User {user_id} has already voted."
        else:
            for row in rows:
                if row['ID Number'].strip() == user_id.strip():
                    row['Voted'] = 'Yes'
                    row['Selected Mascot'] = selected_mascot
                    break

            with open("IDlist.csv", mode='w', newline='', encoding='utf-8-sig') as file:
                fieldnames = ['ID Number', 'Voted', 'Selected Mascot']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            return f"User {user_id} can vote and selected {selected_mascot}."

    except Exception as e:
        return f"Error reading CSV file: {e}"