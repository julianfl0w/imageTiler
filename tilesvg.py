import svgwrite
import xml.etree.ElementTree as ET
import sys

def get_svg_size(svg_path):
    # Parse the SVG file
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Get the 'width' and 'height' attributes from the root <svg> element
    width = root.get('width', '100')  # Default to 100 if not specified
    height = root.get('height', '100')  # Default to 100 if not specified

    # Try to convert to integer, strip 'px' if present
    try:
        width = int(width.strip('px'))
        height = int(height.strip('px'))
    except ValueError:
        # Use default size if width or height are not directly convertible to int
        width = height = 100  # Default size
    
    return width, height

def tile_svg(input_svg_path, output_svg_path, tile_count_x, tile_count_y):
    svg_width, svg_height = get_svg_size(input_svg_path)  # Get the SVG size
    
    # Create a new SVG drawing
    dwg = svgwrite.Drawing(output_svg_path, profile='tiny')

    # Tile the image
    for x in range(tile_count_x):
        for y in range(tile_count_y):
            # Calculate the position for the current tile
            pos_x = x * svg_width
            pos_y = y * svg_height
            
            # Add the SVG content as a fragment at the calculated position
            dwg.add(dwg.image(href=input_svg_path, insert=(pos_x, pos_y), size=(f"{svg_width}px", f"{svg_height}px")))
    
    # Save the resulting SVG
    dwg.save()

# Example usage
input_svg_path = sys.argv[1]  # Get the input path from command line arguments
output_svg_path = input_svg_path + '_tiled.svg'  # Append '_tiled.svg' to the input path for the output file

# Tile the image 10 times in x and y directions
tile_svg(input_svg_path, output_svg_path, 10, 10)
