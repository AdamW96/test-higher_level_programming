#!/usr/bin/python3
"""
Task 00 for server side rendering
"""

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.

    Args:
        template (str): Template string with placeholders {name}, {event_title},
                       {event_date}, {event_location}
        attendees (list): List of dictionaries containing attendee information

    Returns:
        None: Creates output files or logs error messages
    """

    # ========================================================================
    # Step 1: Input Type Validation
    # ========================================================================

    # Check if template is a string
    if not isinstance(template, str):
        print(f"Error: Template must be a string, received {type(template).__name__}")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, received {type(attendees).__name__}")
        return

    # Check if attendees is a list of dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: All attendees must be dictionaries, found {type(attendee).__name__} at index {i}")
            return

    # ========================================================================
    # Step 2: Empty Input Validation
    # ========================================================================

    # Check if template is empty
    if not template.strip():  # strip() removes whitespace
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # ========================================================================
    # Step 3: Process Each Attendee
    # ========================================================================

    print(f"Processing {len(attendees)} attendees...")

    for index, attendee in enumerate(attendees, start=1):
        try:
            # Start with the original template
            processed_template = template

            # Define the placeholders we need to replace
            placeholders = ["name", "event_title", "event_date", "event_location"]

            # Replace each placeholder with actual data or "N/A"
            for placeholder in placeholders:
                placeholder_key = "{" + placeholder + "}"

                # Get the value from attendee dictionary
                value = attendee.get(placeholder)

                # If value is None or missing, use "N/A"
                if value is None:
                    value = "N/A"

                # Replace the placeholder in the template
                processed_template = processed_template.replace(placeholder_key, str(value))

            # ====================================================================
            # Step 4: Generate Output File
            # ====================================================================

            # Create filename starting from 1
            filename = f"output_{index}.txt"

            # Write the processed template to file
            with open(filename, 'w') as output_file:
                output_file.write(processed_template)

            print(f"Generated: {filename}")

        except Exception as e:
            print(f"Error processing attendee {index}: {e}")
            continue

    print("Invitation generation completed.")


# ============================================================================
# Template Creation and Testing
# ============================================================================

def create_template_file():
    """Create the template.txt file with the required content"""
    template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    with open('template.txt', 'w') as file:
        file.write(template_content)
    print("Template file 'template.txt' created successfully.")


def test_program():
    """Test the templating program with various scenarios"""

    print("=" * 80)
    print("TESTING THE TEMPLATING PROGRAM")
    print("=" * 80)

    # Create template file
    create_template_file()

    # Read the template from file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    print("Template content:")
    print("-" * 40)
    print(template_content)
    print("-" * 40)

    # Test data
    attendees = [
        {
            "name": "Alice",
            "event_title": "Python Conference",
            "event_date": "2023-07-15",
            "event_location": "New York"
        },
        {
            "name": "Bob",
            "event_title": "Data Science Workshop",
            "event_date": "2023-08-20",
            "event_location": "San Francisco"
        },
        {
            "name": "Charlie",
            "event_title": "AI Summit",
            "event_date": None,  # This will become "N/A"
            "event_location": "Boston"
        }
    ]

    print("\nTest 1: Normal execution with valid data")
    print("-" * 50)
    generate_invitations(template_content, attendees)

    print("\nTest 2: Empty template")
    print("-" * 50)
    generate_invitations("", attendees)

    print("\nTest 3: Empty attendees list")
    print("-" * 50)
    generate_invitations(template_content, [])

    print("\nTest 4: Invalid template type")
    print("-" * 50)
    generate_invitations(123, attendees)

    print("\nTest 5: Invalid attendees type")
    print("-" * 50)
    generate_invitations(template_content, "not a list")

    print("\nTest 6: Invalid attendee item type")
    print("-" * 50)
    invalid_attendees = [
        {"name": "Alice", "event_title": "Conference"},
        "not a dictionary",  # This should cause an error
        {"name": "Bob", "event_title": "Workshop"}
    ]
    generate_invitations(template_content, invalid_attendees)

    print("\nTest 7: Missing data fields")
    print("-" * 50)
    incomplete_attendees = [
        {
            "name": "David",
            "event_title": "Missing Date Event"
            # Missing event_date and event_location
        },
        {
            "event_title": "Missing Name Event",
            "event_date": "2023-09-15",
            "event_location": "Chicago"
            # Missing name
        }
    ]
    generate_invitations(template_content, incomplete_attendees)


def demonstrate_output_files():
    """Demonstrate what the output files look like"""

    print("\n" + "=" * 80)
    print("DEMONSTRATING OUTPUT FILES")
    print("=" * 80)

    import os

    # Check if output files exist and display their content
    for i in range(1, 4):  # Expecting output_1.txt, output_2.txt, output_3.txt
        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            print(f"\nContent of {filename}:")
            print("-" * 40)
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
            print("-" * 40)
        else:
            print(f"\n{filename} does not exist.")


# ============================================================================
# Advanced Features and Error Handling Demo
# ============================================================================

def advanced_templating_demo():
    """Demonstrate advanced features and edge cases"""

    print("\n" + "=" * 80)
    print("ADVANCED TEMPLATING FEATURES")
    print("=" * 80)

    # Custom template with additional placeholders
    advanced_template = """Dear {name},

Event Details:
- Title: {event_title}
- Date: {event_date}
- Location: {event_location}
- RSVP By: {rsvp_date}
- Contact: {contact_email}

Special Instructions: {special_instructions}

Regards,
{organizer_name}"""

    advanced_attendees = [
        {
            "name": "Emma",
            "event_title": "Advanced Python Workshop",
            "event_date": "2023-10-15",
            "event_location": "Seattle",
            "rsvp_date": "2023-10-01",
            "contact_email": "contact@example.com",
            "special_instructions": "Please bring your laptop",
            "organizer_name": "Tech Academy"
        },
        {
            "name": "Frank",
            "event_title": "Machine Learning Conference",
            "event_date": "2023-11-20",
            "event_location": "Austin",
            # Missing several fields - should become "N/A"
        }
    ]

    print("Testing advanced template with additional placeholders:")

    # Create a function that can handle any number of placeholders
    def generate_advanced_invitations(template, attendees):
        """Enhanced version that automatically detects all placeholders"""

        # Input validation (same as before)
        if not isinstance(template, str):
            print(f"Error: Template must be a string, received {type(template).__name__}")
            return

        if not isinstance(attendees, list):
            print(f"Error: Attendees must be a list, received {type(attendees).__name__}")
            return

        for i, attendee in enumerate(attendees):
            if not isinstance(attendee, dict):
                print(f"Error: All attendees must be dictionaries, found {type(attendee).__name__} at index {i}")
                return

        if not template.strip():
            print("Template is empty, no output files generated.")
            return

        if not attendees:
            print("No data provided, no output files generated.")
            return

        # Find all placeholders in the template
        import re
        placeholders = re.findall(r'\{(\w+)\}', template)
        unique_placeholders = list(set(placeholders))

        print(f"Found placeholders: {unique_placeholders}")

        for index, attendee in enumerate(attendees, start=1):
            try:
                processed_template = template

                # Replace each placeholder
                for placeholder in unique_placeholders:
                    placeholder_key = "{" + placeholder + "}"
                    value = attendee.get(placeholder, "N/A")

                    if value is None:
                        value = "N/A"

                    processed_template = processed_template.replace(placeholder_key, str(value))

                # Write to file with prefix to avoid overwriting previous files
                filename = f"advanced_output_{index}.txt"
                with open(filename, 'w') as output_file:
                    output_file.write(processed_template)

                print(f"Generated: {filename}")

            except Exception as e:
                print(f"Error processing attendee {index}: {e}")
                continue

    generate_advanced_invitations(advanced_template, advanced_attendees)


# ============================================================================
# Main Execution
# ============================================================================

if __name__ == "__main__":
    # Run all tests and demonstrations
    test_program()
    demonstrate_output_files()
    advanced_templating_demo()

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print("""
    The templating program successfully:

    ✓ Validates input types (string template, list of dictionaries)
    ✓ Handles empty inputs gracefully
    ✓ Processes attendee data and replaces placeholders
    ✓ Handles missing data by substituting "N/A"
    ✓ Generates sequential output files (output_1.txt, output_2.txt, etc.)
    ✓ Provides comprehensive error handling and logging
    ✓ Demonstrates extensibility with advanced features

    Key Features:
    • Type validation for all inputs
    • Empty input detection
    • Missing data handling
    • Sequential file naming
    • Comprehensive error messages
    • Clean code structure with clear documentation
    """)