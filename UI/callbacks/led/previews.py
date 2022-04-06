from dash import html
import colormap

preview_style = {
    "height": "2rem",
    "width": "100%",
    "maxWidth": "25rem",
    "minWidth": "15rem",
    "borderRadius": "0.25rem"
}

def single(input_vals, i, maximum):
    style = {
        "backgroundColor": colormap.rgb2hex(*input_vals.color[0])
    }
    return html.Div(
        style = preview_style | style
    )

def two_color(input_vals, i, maximum):
    c1 = colormap.rgb2hex(*input_vals.color[0])
    c2 = colormap.rgb2hex(*input_vals.color[1])
    perc = 50 * (1-input_vals.blur_factor)
    style = {
        "backgroundImage": f"linear-gradient(90deg, {c1} {perc}%, {c2} {100-perc}%)"
    }
    return html.Div(
        style = preview_style | style
    )

def pulse(input_vals, i, maximum):
    range = int((1-input_vals.interval)*(maximum/2))
    if not range:
        range = 1
    i = i % int(maximum/range)
    maximum = int(maximum/range)
    if i > maximum / 2:
        i = maximum - i
    perc = i/(maximum/2)
    color = [int(c1*perc + c2*(1-perc)) for c1, c2 in zip(input_vals.color[0], input_vals.color[1])]
    style = {
        "backgroundColor": colormap.rgb2hex(*color)
    }
    return html.Div(
        style = preview_style | style
    )
    

functions = {
    "single": single,
    "two_color": two_color,
    "pulse": pulse
}