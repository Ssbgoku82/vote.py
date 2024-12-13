import csv

def check_and_update_vote(user_id, selected_mascot) -> str:
    """
    Checks for user ID voted and will update if no vote has been casted.
    """
    try:
        # Reads CSV File to confirm ID
        with open("IDlist.csv", mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Looks for User ID in row name "ID Number"
        user_data = None
        for row in rows:
            if row['ID Number'].strip() == user_id.strip():
                user_data = row
                break

        user_data = None
        # Find the user in the CSV
        for row in rows:
            if row['ID Number'].strip() == user_id.strip():
                user_data = row
                break

        # If user ID is not found
        if user_data is None:
            return f"ID {user_id} not found. Please register."

        # Check if the user has already voted
        if user_data['Voted'] == 'Yes':
            return f"User {user_id} has already voted."

        # Update the user's voting status and selected mascot
        for row in rows:
            if row['ID Number'].strip() == user_id.strip():
                row['Voted'] = 'Yes'
                row['Selected Mascot'] = selected_mascot
                break

        # Write the updated data back to the CSV file
        with open("IDlist.csv", mode='w', newline='', encoding='utf-8-sig') as file:
            fieldnames = ['ID Number', 'Voted', 'Selected Mascot']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        return f"User {user_id} can vote and selected {selected_mascot}."

    except Exception as e:
        return f"Error reading CSV file: {e}"