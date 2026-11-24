import math
import turtle
screen = turtle.Screen()
screen.setup(width=750, height=700)
screen.bgcolor("#F5F4F0") 
screen.title("IIEST Shibpur Logo")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
DEEP_BLUE = "#000080"
GOLD_YELLOW = "#F7C815"
BG_COLOR = "#F5F4F0"
def draw_poly(points, fill_color, border_color=None, pen_size=1):
    t.penup()
    t.goto(points[0])
    t.pencolor(border_color if border_color else fill_color)
    t.fillcolor(fill_color)
    t.pensize(pen_size)
    t.pendown()
    t.begin_fill()
    for pt in points[1:]:
        t.goto(pt)
    t.goto(points[0])
    t.end_fill()
    t.penup()


def draw_sunburst_arc():
    # Draws the semicircular ring of yellow gear-like rays behind the tower
    inner_r = 148
    outer_r = 175
    y_base = -85
    num_rays = 37  # Spanning from 0 to 180 degrees

    for i in range(num_rays):
        angle_deg = i * (180 / (num_rays - 1))
        # Skip rays completely hidden behind the central tower body
        if 64 < angle_deg < 116:
            continue

        a_start = math.radians(angle_deg - 1.5)
        a_end = math.radians(angle_deg + 1.5)

        pts = [
            (inner_r * math.cos(a_start), y_base + inner_r * math.sin(a_start)),
            (outer_r * math.cos(a_start), y_base + outer_r * math.sin(a_start)),
            (outer_r * math.cos(a_end), y_base + outer_r * math.sin(a_end)),
            (inner_r * math.cos(a_end), y_base + inner_r * math.sin(a_end)),
        ]
        draw_poly(pts, GOLD_YELLOW)


def draw_clock_tower():
    # 1. Main lower tower body (two pillars connected below the roof)
    draw_poly([(-68, -85), (68, -85), (68, 92), (-68, 92)], DEEP_BLUE)

    # 2. Pointed Gothic archway cutout in the center
    arch_pts = [(-22, -85), (-22, 25)]
    # Left curve of pointed arch
    for step in range(11):
        frac = step / 10
        x = -22 + 22 * (frac**1.3)
        y = 25 + 32 * math.sin(frac * math.pi / 2)
        arch_pts.append((x, y))
    # Right curve of pointed arch
    for step in range(10, -1, -1):
        frac = step / 10
        x = 22 - 22 * (frac**1.3)
        y = 25 + 32 * math.sin(frac * math.pi / 2)
        arch_pts.append((x, y))
    arch_pts.append((22, -85))
    draw_poly(arch_pts, BG_COLOR)

    # 3. Horizontal eave/ledge separating tower body and clock housing
    draw_poly([(-84, 98), (84, 98), (62, 122), (-62, 122)], DEEP_BLUE)

    # 4. Middle clock section
    draw_poly([(-52, 122), (52, 122), (52, 165), (-52, 165)], DEEP_BLUE)

    # 5. Upper roof eave and gable peak
    draw_poly([(-66, 165), (66, 165), (32, 198), (-32, 198)], DEEP_BLUE)

    # 6. White/cream triangle inside the top gable
    draw_poly([(-28, 168), (28, 168), (0, 193)], BG_COLOR)

    # 7. Circular clock face cutout
    t.penup()
    t.goto(0, 118)
    t.setheading(0)
    t.pencolor(BG_COLOR)
    t.fillcolor(BG_COLOR)
    t.pendown()
    t.begin_fill()
    t.circle(21)
    t.end_fill()
    t.penup()


def draw_text():
    t.pencolor(DEEP_BLUE)

    # Year 1856 in English (left) and Devanagari (right)
    t.goto(-96, -86)
    t.write("1856", align="center", font=("Times New Roman", 13, "bold"))

    t.goto(96, -86)
    t.write("१८५६", align="center", font=("Nirmala UI", 13, "bold"))

    # Line 1: Sanskrit Motto
    t.goto(0, -118)
    t.write(
        "उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत",
        align="center",
        font=("Nirmala UI", 19, "bold"),
    )

    # Line 2: English Institute Name
    t.goto(0, -142)
    t.write(
        "INDIAN INSTITUTE OF ENGINEERING SCIENCE AND TECHNOLOGY, SHIBPUR",
        align="center",
        font=("Arial Narrow", 11, "bold"),
    )

    # Line 3: Hindi Institute Name
    t.goto(0, -168)
    t.write(
        "भारतीय अभियांत्रिकी विज्ञान एवं प्रौद्योगिकी संस्थान, शिबपुर",
        align="center",
        font=("Nirmala UI", 15, "bold"),
    )


# Execute drawing in layers (back to front)
draw_sunburst_arc()
draw_clock_tower()
draw_text()

turtle.done()
