def callback(path, layout):
    if path == "/":
        return layout.home.content()
    elif path == "/led":
        return layout.led.content()
    else:
        return layout.not_found()