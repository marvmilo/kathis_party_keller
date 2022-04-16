from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import threading
import marvmiloTools as mmt

from . import gif

input_vals = None
    
class Thread(threading.Thread):
    def __init__(self, function, path):
        threading.Thread.__init__(self)
        self.function = function
        self.path = path
    def run(self):
        self.function(self.path)

def single(path):
    frame = gif.Frame()
    frame.fill(input_vals.color[0])
    frame.save(path)


def two_color(path):
    frame = gif.Frame()
    for color in input_vals.color:
        frame.add_gradient_color(color, 0.5)
    frame.gradient(blur_factor = input_vals.blur_factor)
    frame.save(path)
    

def pulse(path):
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
        gif_file.add_frame(frame.get_image())
    
    gif_file.save(path)
            

def shoot(path):
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
        phases.append(1)
        
    gif_file = gif.Gif()
    frame = gif.Frame()
    for i in range(len(colors)):
        frame.add_gradient_color(colors[i], phases[i])
    frame.gradient(input_vals.blur_factor, connect_ends = True)
    gif_file.add_frame(frame.get_image())
    
    max_speed = 25
    speed = int(max_speed * input_vals.fade_out)
    try:
        speed = int(frame.overhang_width / int(frame.overhang_width / speed))
    except ZeroDivisionError:
        speed = 1
    progress = 0
    for i in range(0, frame.overhang_width, speed):
        progress += speed
        if progress >= frame.overhang_width:
            break
        frame.move_right(speed)
        gif_file.add_frame(frame.get_image())
    
    gif_file.save(path)


def rainbow(path):
    colors = [
        [255, 0, 0],
        [255, 255, 0],
        [0, 255, 0],
        [0, 255, 255],
        [0, 0, 255],
        [255, 0, 255],
    ]
    
    gif_file = gif.Gif()
    frame = gif.Frame()
    for c in colors:
        frame.add_gradient_color(c, 1/len(colors))
    frame.gradient(input_vals.blur_factor, connect_ends = True)
    
    max_speed = 5
    speed = int(max_speed * input_vals.fade_out)
    try:
        speed = int(frame.overhang_width / int(frame.overhang_width / speed))
    except ZeroDivisionError:
        speed = 1
    progress = 0
    for i in range(0, frame.overhang_width, speed):
        progress += speed
        if progress >= frame.overhang_width:
            break
        frame.move_right(speed)
        gif_file.add_frame(frame.get_image())
    
    gif_file.save(path)

def audio_pegel(path):
    gif_file = gif.Gif()
    
    def add_frame(phases1, phases2):
        frame = gif.Frame()
        frame.add_gradient_color(input_vals.color[0], phases1)
        frame.add_gradient_color(input_vals.color[1], phases2)
        frame.gradient(blur_factor = input_vals.blur_factor)
        gif_file.add_frame(frame.get_image())
        
    max_speed = 0.5
    speed = max_speed * input_vals.fade_out
    if speed < 0.1:
        speed = 0.1
    
    for pegel in [0.5, 1]:
        add_frame(0,1)
        add_frame(pegel, 1-pegel)
        while True:
            pegel = pegel - speed
            if pegel > 0:
                add_frame(pegel, 1-pegel)
            else:
                break
    
    gif_file.save(path)

def audio_pegel(path):
    gif_file = gif.Gif()
    frame_width = 300
    
    def add_frame(phases1, phases2):
        nonlocal frame_width
        frame = gif.Frame()
        frame.add_gradient_color(input_vals.color[0], phases1)
        frame.add_gradient_color(input_vals.color[1], phases2)
        frame.gradient(blur_factor = input_vals.blur_factor)
        gif_file.add_frame(frame.get_image())
        frame_width = frame.width
        
    max_speed = 0.5
    speed = max_speed * input_vals.fade_out
    if speed < 0.1:
        speed = 0.1
    
    for pegel in [0.5, 1]:
        add_frame(0,1)
        add_frame(pegel, 1-pegel)
        while True:
            pegel = pegel - speed
            if pegel > 0:
                add_frame(pegel, 1-pegel)
            else:
                break
    
    gif_file.save(path)
    
def audio_brightness(path):
    gif_file = gif.Gif()
    
    def add_frame(pegel):
        frame = gif.Frame()
        color = [int((c1 * pegel) + (c2 * (1-pegel))) for c1,c2 in zip(input_vals.color[0], input_vals.color[1])]
        frame.fill(color)
        gif_file.add_frame(frame.get_image())
        
    max_speed = 0.5
    speed = max_speed * input_vals.fade_out
    if speed < 0.1:
        speed = 0.1
        
    for pegel in [0.5, 1]:
        add_frame(0)
        add_frame(pegel)
        while True:
            pegel = pegel - speed
            if pegel > 0:
                add_frame(pegel)
            else:
                break
    
    gif_file.save(path)
    
def audio_shoot(path):
    gif_file = gif.Gif()
    frame = gif.Frame()
    c1 = input_vals.color[0]
    c2 = input_vals.color[1]
    
    max_interval = 0.3
    interval = max_interval * input_vals.interval
    if interval < 0.1:
        interval = 0.1
    filler_interval = (1 - (interval * 2))/3
        
    frame.add_gradient_color(c1, interval)
    frame.add_gradient_color(c2, filler_interval*2)
    frame.add_gradient_color(c1, interval)
    frame.add_gradient_color(c2, filler_interval)
    
    frame.gradient(input_vals.blur_factor, connect_ends = True, hard_right = c1)
    gif_file.add_frame(frame.get_image())
    
    max_speed = 30
    min_speed = 10
    speed = int(((max_speed-min_speed) * input_vals.fade_out) + min_speed)
    try:
        speed = int(frame.overhang_width / int(frame.overhang_width / speed))
    except ZeroDivisionError:
        speed = 1
    progress = 0
    for i in range(0, frame.overhang_width, speed):
        progress += speed
        if progress >= frame.overhang_width:
            break
        frame.move_right(speed)
        gif_file.add_frame(frame.get_image())
    
    gif_file.save(path)

__functions__ = {
    "single": single,
    "two_color": two_color,
    "pulse": pulse,
    "shoot": shoot,
    "rainbow": rainbow,
    "audio_pegel": audio_pegel,
    "audio_brightness": audio_brightness,
    "audio_shoot": audio_shoot
}

def apply(func_name, loading, id):
    path = f"./assets/previews/{id}/{func_name}-{mmt.dash.random_ID(32)}.gif"
    function = __functions__[func_name]
    thread = Thread(function, path)
    thread.start()
          
    return html.Div(
        html.Div(
            children = loading(),
            id = f"led-{func_name}-gif-preview"
        ),
        style = {
            "width": "100%",
            "maxWidth": "25rem",
            "minWidth": "15rem"
        }
    )