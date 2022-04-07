from cmath import phase
from PIL import Image, ImageDraw

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        minx, maxx = (x1,x2) if x1 < x2 else (x2,x1)
        miny, maxy = (y1,y2) if y1 < y2 else (y2,y1)
        self.min = Point(minx, miny)
        self.max = Point(maxx, maxy)

    width  = property(lambda self: self.max.x - self.min.x)
    height = property(lambda self: self.max.y - self.min.y)

class Frame:
    def __init__(self):
        self.gradient_palette = []
        self.phases = []
        self.region = Rect(0, 0 , 300, 50)
        self.width = self.region.max.x
        self.height = self.region.max.y
        self.image = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        
    #add gradient color to Image
    def add_gradient_color(self, rgb_color, phase_size):
        self.gradient_palette.append(tuple(rgb_color))
        self.phases.append(phase_size)
    
    def gradient(self, blur_factor):
        for c, color in enumerate(self.gradient_palette):
            try:
                next_color = self.gradient_palette[c+1]
            except IndexError:
                next_color = None
            
            try:
                previous_color = self.gradient_palette[c-1]
            except IndexError:
                previous_color = None
                
            
            if not c:
                x_range = int(self.phases[c] * self.width)
                blur_range = int(x_range * blur_factor)
                if not blur_range:
                    blur_range = 1
                for x in range(x_range):
                    if x < (x_range - blur_range):
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=color)
                    else:
                        blur = ((x - (x_range - blur_range))/blur_range) / 2
                        mixed_color = tuple([int(c1 * (1-blur) + c2 * blur) for c1, c2 in zip(color, next_color)])
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=mixed_color)
            
            elif not next_color:
                x_range = int(self.phases[c] * self.width)
                blur_range = int(x_range * blur_factor)
                offset = int(sum(self.phases[:c] * self.width))
                if not blur_range:
                    blur_range = 1
                for x in range(offset, offset+x_range):
                    if x > (offset + blur_range):
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=color)
                    else:
                        blur = 0.5 + ((x - offset)/blur_range)/2
                        mixed_color = tuple([int(c1 * blur + c2 * (1-blur) ) for c1, c2 in zip(color, previous_color)])
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=mixed_color)

            else:
                x_range = int(self.phases[c] * self.width)+1
                offset = int(sum(self.phases[:c] * self.width))
                blur_range = int(x_range * blur_factor/2)
                if not blur_range:
                    blur_range = 1
                for x in range(offset, offset+x_range):
                    if x < (offset + blur_range):
                        blur = 0.5 + ((x - offset)/blur_range)/2
                        mixed_color = tuple([int(c1 * blur + c2 * (1-blur) ) for c1, c2 in zip(color, previous_color)])
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=mixed_color)
                    elif x > (offset + x_range - blur_range):
                        blur = ((x - (offset + x_range - blur_range))/blur_range) / 2
                        mixed_color = tuple([int(c1 * (1-blur) + c2 * blur) for c1, c2 in zip(color, next_color)])
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=mixed_color)
                    else:
                        self.draw.line([(x, self.region.min.y), (x, self.region.max.y)], fill=color)
    
    def fill(self, color):
        color = tuple(color)
        self.image.paste(color, [0,0,self.image.size[0],self.image.size[1]])
    
    def save(self, path):
        self.image.save(path)
        
class Gif:
    def __init__(self):
        self.frames = list()
    
    def add_frame(self, image):
        self.frames.append(image)
    
    def save(self, path):
        self.frames[0].save(
            path,
            format = "GIF",
            append_images = self.frames,
            save_all = True,
            loop = 0
        )
        
            
    
    