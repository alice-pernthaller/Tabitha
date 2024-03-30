from theatre import my_constants

min_physical_x = 333
max_physical_x = 2666
min_physical_y = 20
max_physical_y = 1093

min_stage_x = 603
max_stage_x = 2403
stage_width = max_stage_x - min_stage_x
half_stage_width = stage_width / 2
center_of_stage = min_stage_x + half_stage_width

min_logical_x = min_physical_x - center_of_stage
max_logical_x = max_physical_x - center_of_stage
min_logical_y = min_physical_y
max_logical_y = max_physical_y

min_canvas_x = 50  # margin
max_canvas_x = 1340
min_canvas_y = 50  # margin
max_canvas_y = 540  # need space for widgets above

logical_width = max_logical_x - min_logical_x
logical_height = max_logical_y - min_logical_y

canvas_width = max_canvas_x - min_canvas_x
canvas_height = max_canvas_y - min_canvas_y

delta_x = min_canvas_x - min_logical_x
delta_y = min_canvas_y - min_logical_y
ky = canvas_height / logical_height
kx = ky
# All of the above calculates the scale factor by which to multiply the coordinates to fit the stage onto the GUI


def translate_x(x_coordinate):
    return kx * (x_coordinate + delta_x)


def translate_y(y_coordinate):
    return ky * (y_coordinate + delta_y)


# draws a seat on the GUI canvas
def draw_seat(seat, canvas, colour=False):
    x = translate_x(seat.x)
    y = translate_y(seat.y)

    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5

    if colour:
        seat_price = my_constants.price_list[seat.section]
        if seat.row == my_constants.front_rows[seat.section]:  # front row seats are drawn darker
            seat_price *= 1.5
        chosen = my_constants.colours[seat_price]
    else:
        chosen = "#808080"  # default is grey

    canvas.create_oval(x0, y0, x1, y1, fill=chosen, outline=chosen)


# draws the stage on the GUI canvas
def draw_stage(stage, canvas):
    x0 = translate_x(stage.x0)
    y0 = translate_y(stage.y0)
    x1 = translate_x(stage.x1)
    y1 = translate_y(stage.y1)
    canvas.create_rectangle(x0, y0, x1, y1)
