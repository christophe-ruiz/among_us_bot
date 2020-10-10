from PIL import ImageGrab
from pynput.keyboard import Listener, Key

from task.electrical.wiring.wire import Wire


class Engine:
    """
    Runs the engine
    """
    def __init__(self):
        print("Running bot.")
        self.key_pressed = False
        # Listens keyboard events
        listener = Listener(self.on_press, self.on_release)
        listener.start()
        listener.join()
        print("Listening to key pressed...")

    """
    Checks if the correct key triggered the event
    """
    def on_press(self, key):
        try:
            if key == Key.up:
                self.key_pressed = True
        except AttributeError as ex:
            print(ex)
    """
    Does the action when the correct key is pressed.
    """
    def on_release(self, key):
        if self.key_pressed:
            print("Solving...")
            self.key_pressed = not self.key_pressed
            self.action()

    """
    Founds wires on screen and connects them.
    """
    def action(self):
        # Contains wires on the left of the screen
        left_wires = []
        # Contains wires on the right of the screen
        right_wires = []
        # Fullscreen screenshot
        screen = ImageGrab.grab()

        # Y axis position of wires (from top to bottom)
        y_values = [275, 460, 646, 833]
        # X position of wires (left then right)
        x_values = [570, 1310]

        # Fill left and right wires list with the good wires.
        for x in x_values:
            for y in y_values:
                pos = [x, y]
                # Gets the color of the pixel at position (x, y)
                color = screen.getpixel((x, y))
                wire = Wire(pos, color)
                if x == 1310:
                    right_wires.append(wire)
                else:
                    left_wires.append(wire)

        # Associating corresponding wire for left wires.
        for wire in left_wires:
            wire.find_corresponding_wire(right_wires)
            wire.connect_to_corresponding_wire()
