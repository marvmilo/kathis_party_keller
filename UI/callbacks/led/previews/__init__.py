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
    pass
    path = __path__("gif")
    step_width = input_vals.interval
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
    
    def create_frame(colors, phases):
        frame = gif.Frame()
        for i in range(len(colors)):
            frame.add_gradient_color(colors[i], phases[i])
        frame.gradient(input_vals.blur_factor)
        gif_file.add_frame(frame.image)
    create_frame(colors, phases)
    
    phases.insert(0, 0.01)
    phases[-1] -= 0.01
    if colors[0] == c1:
        colors.insert(0, c2)
    else:
        colors.insert(0, c1)
    create_frame(colors, phases)
    
    for i in range(int(step_width/0.01)):
        phases[0] += 0.01
        phases[-1] -= 0.01
        phases = [p if p > 0 else 0 for p in phases]
        create_frame(colors, phases)
    
    gif_file.save(path)
    return __return__(path)      
    

functions = {
    "single": single,
    "two_color": two_color,
    "pulse": pulse,
    "shoot": shoot,
}