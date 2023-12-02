"""
Hex Colour Codes
Estimate: 20 minutes
Actual: 15 minutes

COLOUR_TO_HEX = {
    'aliceblue': '#f0f8ff',
    'antiquewhite': '#faebd7',
    'aqua': '#00ffff',
    'aquamarine': '#7fffd4',
    'azure': '#f0ffff',
    'beige': '#f5f5dc',
    'bisque': '#ffe4c4',
    'black': '#000000',
    'blanchedalmond': '#ffebcd',
    'blue': '#0000ff',
    'blueviolet': '#8a2be2'
}

def get_hex_code(colour_name)
    return COLOUR_TO_HEX.get(colour_name.lower(), None)

get colour_name
while colour_name
    hex_code = get_hex_code(colour_name)
    if hex_code
        print The code for {colour_name} is {hex_code}
    else
        print Invalid colour name
    get colour_name
"""
COLOUR_TO_HEX = {
    'aliceblue': '#f0f8ff',
    'antiquewhite': '#faebd7',
    'aqua': '#00ffff',
    'aquamarine': '#7fffd4',
    'azure': '#f0ffff',
    'beige': '#f5f5dc',
    'bisque': '#ffe4c4',
    'black': '#000000',
    'blanchedalmond': '#ffebcd',
    'blue': '#0000ff',
    'blueviolet': '#8a2be2'
}

def get_hex_code(colour_name):
    return COLOUR_TO_HEX.get(colour_name.lower(), None)

colour_name = input("Enter a colour name: ").strip()
while colour_name:
    hex_code = get_hex_code(colour_name)
    if hex_code:
        print(f"The code for {colour_name} is {hex_code}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").strip()
