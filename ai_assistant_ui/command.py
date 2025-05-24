import threading
def update_display_with_command(cmd):
    global display_text, display_color, transcribed_text
    display_text = f"Command: {cmd}"
    display_color = (0, 255, 255)  # yellow

    # After 2 sec, reset to normal listening text
    def reset_display():
        global display_text, display_color
        display_text = transcribed_text
        display_color = (0, 255, 0)

    threading.Timer(2.0, reset_display).start()