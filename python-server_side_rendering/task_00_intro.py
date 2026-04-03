#!/usr/bin/python3

def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees."""

    # Validate template type
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Validate attendees type
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Validate each attendee item
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # List of placeholders
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Generate one file per attendee
    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(output)
        except Exception as e:
            print(f"Error writing {filename}: {e}")
