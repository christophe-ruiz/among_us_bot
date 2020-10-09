from pynput.mouse import Button, Controller
import time


class Wire:
    """
    Creates a wire.
    """
    def __init__(self, pos, color):
        # This wire's position
        self.__pos = pos
        # This wire's color
        self.__color = color
        # This wire's corresponding wire.
        self.__corresponding_wire = self
    """
    Returns this wire's position
    :return
        list - [0] is X-axis position and [1] is Y-axis position.
    """
    def get_pos(self):
        return self.__pos
    """
    Returns the color of this wire.
    :return
        list - [0] is red color, [1] is green color, [2] is blue color.
    """
    def get_color(self):
        return self.__color
    """
    Returns the corresponding wire.
    :return
        Wire - the corresponding wire.
    """
    def get_corresponding_wire(self):
        return self.__corresponding_wire
    """
    Sets a corresponding wire.
    """
    def set_corresponding_wire(self, wire):
        self.__corresponding_wire = wire

    """
    Checks if the given wire is of the same color as this wire.
    :param
        wire - a wire to compare with.
    """
    def is_of_same_color(self, wire):
        if not isinstance(wire, Wire):
            return False
        else:
            return self.get_color() == wire.get_color()

    """
    Founds a wire with se same color as this wire.
    :param
        wires - a list within the corresponding wire might be found
    """
    def find_corresponding_wire(self, wires):
        for wire in wires:
            if not isinstance(wire, Wire):
                print(f"{wire} is not a wire.")
            else:
                if wire.is_of_same_color(self):
                    self.set_corresponding_wire(wire)
                    return

    """
    Clicks on this wire and drags it to it's corresponding wire.
    """
    def connect_to_corresponding_wire(self):
        # This wire's position as a tuple
        my_pos = tuple(self.__pos)
        # The other wire's position as a tuple
        other_pos = tuple(self.__corresponding_wire.get_pos())

        print(f"{my_pos} is connecting to {other_pos}.")
        # Object used to control mouse movements and actions
        mouse = Controller()

        # Initial position is this wire's position
        mouse.position = my_pos
        # Left button is pressed
        mouse.press(Button.left)
        print("> button pressed")

        # Wait a bit so the movement is correctly considered
        time.sleep(0.032)
        # Move to mouse to the other wire's position while pressing the left button
        mouse.move(other_pos[0] - my_pos[0], other_pos[1] - my_pos[1])
        print("> mouse moved")

        # Wait a bit so the movement is correctly considered
        time.sleep(0.032)

        # Release the left button
        mouse.release(Button.left)
        print("> button released")

        # Wait a bit so the movement is correctly considered
        time.sleep(0.032)
