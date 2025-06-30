#!/usr/bin/env python3
"""
CSV to JSON conversion module.

This module provides functionality to convert CSV data to JSON format,
demonstrating data format conversion and serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save to data.json.

    Args:
        csv_filename (str): The filename of the input CSV file

    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Read CSV data
        json_data = []

        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Convert each row to a dictionary and add to list
            for row in csv_reader:
                json_data.append(row)

        # Write JSON data to file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)

        return True

    except FileNotFoundError:
        print(f"Error: CSV file {csv_filename} not found")
        return False
    except csv.Error as e:
        print(f"Error reading CSV file {csv_filename}: {e}")
        return False
    except json.JSONEncodeError as e:
        print(f"Error encoding JSON data: {e}")
        return False
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        return False
