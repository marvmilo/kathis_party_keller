from dash import html
import marvmiloTools as mmt

from . import gif

__preview_style__ = {
    "height": "2rem",
    "width": "100%",
    "maxWidth": "25rem",
    "minWidth": "15rem",
    "borderRadius": "0.25rem"
}

def __path__(format):
    return f"./assets/previews/{mmt.dash.random_ID(32)}.{format}"


def __return__(path):
    return html.Img(
        src = path,
        style = __preview_style__
    )


def single(input_vals):
    path = __path__("jpg")
    
    frame = gif.Frame()
    frame.fill(input_vals.color[0])
    frame.save(path)
    
    return __return__(path)


def two_color(input_vals):
    path = __path__("jpg")
    
    frame = gif.Frame()
    for color in input_vals.color:
        frame.add_gradient_color(color, 0.5)
    frame.gradient(blur_factor = input_vals.blur_factor)
    frame.save(path)
    
    return __return__(path)
    

def pulse(input_vals):
    path = __path__("gif")
    
    n_frames = int(input_vals.interval * 100)
    if n_frames < 2:
        n_frames = 2
    turn_point = n_frames/2
    gif_file = gif.Gif()
    
    for i in range(n_frames):
        if i < turn_point:
            blur = i/turn_point
        else:
            blur = 1 - ((i - turn_point)/turn_point)
        mixed_color = [int(c1 * (1-blur) + c2 * blur) for c1, c2 in zip(*input_vals.color)]
        frame = gif.Frame()
        frame.fill(mixed_color)
        gif_file.add_frame(frame.image)
    
    gif_file.save(path)
    
    return __return__(path)
            

def shoot(input_vals):
    path = __path__("gif")
    step_width = input_vals.interval
    if not step_width:
        step_width = 0.01
    colors = list()
    phases = list()
    c1 = input_vals.color[0]
    c2 = input_vals.color[1]
    current_color = c1
    gif_file = gif.Gif()
    
    n = 0
    while True:
        colors.append(current_color)
        phases.append(step_width)
        
        if current_color == c1:
            current_color = c2
        else:
            current_color = c1
        
        n += step_width
        if n >= 1:
            break
    
    if step_width == 1:
        colors.append(c2)
        phases.append(0)
        
    gif_file = gif.Gif()
    frame = gif.Frame()
    for i in range(len(colors)):
        frame.add_gradient_color(colors[i], phases[i])
    frame.gradient(input_vals.blur_factor, connect_ends = True)
    gif_file.add_frame(frame.image)
    
    max_chunks = 150
    try:
        speed = int(frame.width / (max_chunks * (1-input_vals.fade_out)))
    except ZeroDivisionError:
        speed = max_chunks
    for i in range(0, frame.width, speed):
        frame.move_right(speed)
        gif_file.add_frame(frame.image)
        
    gif_file.save(path)
    return __return__(path)  


def rainbow(input_vals):
    path = __path__("gif")
    colors = [
        [255, 0, 0],
        [255, 255, 0],
        [0, 255, 0],
        [0, 255, 255],
        [0, 0, 255],
        [255, 0, 255],
    ]
    
    frame = gif.Frame()
    for c in colors:
        frame.add_gradient_color(c, 1/len(colors))
    frame.gradient(input_vals.blur_factor, connect_ends = True)
    
    frame.save(path)
    return __return__(path)
    

functions = {
    "single": single,
    "two_color": two_color,
    "pulse": pulse,
    "shoot": shoot,
    "rainbow": rainbow,
}