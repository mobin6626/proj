import math
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon

def draw_square(PDwg: Drawing, left: float, top: float, side: float,
                fill_color: str, stroke_color: str) -> None:
    """Draw a square."""
    PDwg.add(Rect(
        insert=(left, top),
        size=(side, side),
        fill=fill_color,
        stroke=stroke_color,
        stroke_width=2
    ))

def draw_circle(PDwg: Drawing, center_x: float, center_y: float, radius: float,
                fill_color: str, stroke_color: str) -> None:
    """Draw a circle."""
    PDwg.add(Circle(
        center=(center_x, center_y),
        r=radius,
        fill=fill_color,
        stroke=stroke_color,
        stroke_width=2
    ))

def draw_hexagon(PDwg: Drawing, center_x: float, center_y: float,
                 apothem: float, fill_color: str, stroke_color: str) -> None:
    """Draw a regular hexagon."""
    # Calculate circumradius from apothem
    # apothem = circumradius * cos(30°) = circumradius * (√3/2)
    circumradius = apothem / (math.sqrt(3) / 2)
    
    # Calculate side length (optional: side = circumradius)
    side_length = circumradius
    
    # Calculate all 6 points (starting from top-right, moving clockwise)
    points = []
    
    for i in range(6):
        # Angle for each corner (starting at 30° for top-right)
        # 30°, 90°, 150°, 210°, 270°, 330°
        angle_deg = 30 + (i * 60)
        angle_rad = math.radians(angle_deg)
        
        # Calculate point coordinates
        x = center_x + circumradius * math.cos(angle_rad)
        y = center_y + circumradius * math.sin(angle_rad)
        
        # Round to integers as specified
        points.append((round(x), round(y)))
    
    # Add polygon to drawing
    PDwg.add(Polygon(
        points=points,
        fill=fill_color,
        stroke=stroke_color,
        stroke_width=2
    ))

def save_svg(PDwg: Drawing, filename: str) -> bool:
    """Save the SVG drawing to a file."""
    try:
        PDwg.saveas(filename, pretty=True, indent=2)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False