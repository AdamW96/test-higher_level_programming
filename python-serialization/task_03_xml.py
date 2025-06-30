#!/usr/bin/env python3
"""
XML serialization and deserialization module.

This module provides functionality to serialize Python dictionaries to XML format
and deserialize XML data back to Python dictionaries.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to file.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data

    Returns:
        bool: True if serialization successful, False otherwise
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child_element = ET.SubElement(root, key)
            child_element.text = str(value)

        # Create ElementTree and write to file
        tree = ET.ElementTree(root)

        # Write with proper formatting
        ET.indent(tree, space="    ", level=0)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

        return True

    except Exception as e:
        print(f"Error serializing dictionary to XML {filename}: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from file to recreate a Python dictionary.

    Args:
        filename (str): The filename of the input XML file

    Returns:
        dict: The deserialized Python dictionary, or None if error occurs
    """
    try:
        # Parse XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct dictionary from XML elements
        result_dict = {}

        for child in root:
            # Get tag name as key and text content as value
            key = child.tag
            value = child.text

            # Handle None values
            if value is None:
                value = ""

            result_dict[key] = value

        return result_dict

    except FileNotFoundError:
        print(f"Error: XML file {filename} not found")
        return None
    except ET.ParseError as e:
        print(f"Error: Invalid XML format in {filename}: {e}")
        return None
    except Exception as e:
        print(f"Error deserializing XML from {filename}: {e}")
        return None
