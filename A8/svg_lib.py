from svgwrite import Drawing, cm, mm
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing, left: float, top: float, side: float, 
               fill_color: str, stroke_color: str) -> None:
    """
    Draw a square (rectangle with equal sides).
    """
    PDwg.add(Rect(
        insert=(left, top),
        size=(side, side),
        fill=fill_color,
        stroke=stroke_color,
        stroke_width=2
    ))

def drawCircle(PDwg: Drawing, center_x: float, center_y: float, radius: float,
               fill_color: str, stroke_color: str) -> None:
    """
    Draw a circle.
    """
    PDwg.add(Circle(
        center=(center_x, center_y),
        r=radius,
        fill=fill_color,
        stroke=stroke_color,
        stroke_width=2
    ))

def saveSvg(PDwg: Drawing, filename: str) -> bool:
    """
    Save the drawing to an SVG file with pretty formatting.
    Returns True if saved successfully, False otherwise.
    """
    try:
        PDwg.saveas(filename, pretty=True, indent=2)
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False