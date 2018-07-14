# -*- coding: utf-8 -*-

import pygame

# ============================================================================
# =
# = Button
# =
# ============================================================================


class Button(pygame.Rect):
    """
    A button to be displayed on screen

    :param pos: position of the button
    :type pos: array of 2 elements
    :param width: width of the button
    :type width: int
    :param height: height of the button
    :type height: int
    :param text: text to display on the button
    :type text: str
    :param command: function to execute when clicked
    :type command: function
    :param state: ["disabled", "enabled"]
    :type state: str
    """

    def __init__(self, **kwargs):

        self.__validKwargs = {"pos", "width", "height", "text"}
        self.__setFromKwargs(kwargs)
        self.state = "disabled"

    def set(self, **kwargs):
        """
        Set the values

        :param pos: position of the button
        :type pos: array of 2 elements
        :param width: width of the button
        :type width: int
        :param height: height of the button
        :type height: int
        :param text: text to display on the button
        :type text: str
        :param command: function to execute when clicked
        :type command: function
        :param state: ["disabled", "enabled"]
        :type state: str
        """

        self.__setFromKwargs(kwargs)

    def execute(self):
        """
        Execute the command if it was given
        """

        if self.state == "enabled":
            self.command()

    def display(self, window):
        """
        Display the button on the window
        """

        core_font = pygame.font.Font(None, 30)
        core_text = core_font.render('>>> Press Enter to begin <<<', 2, (255, 255, 255))

        x_b, y_b = self.x, self.y
        w_b, h_b = self.width, self.height
        w_t, h_t = core_text.get_sire()

        mid_x = x_b + (w_b - w_t) // 2
        mid_y = y_b + (h_b - h_t) // 2

        window.blit(self, (self.x, self.y))
        window.blit(core_text, (mid_x, mid_y))

    def __setFromKwargs(self, kwargs: dict):
        """
        Set the values from the kwargs
        """

        self.__validateKwargs(kwargs.keys())

        if "pos" in kwargs:
            self.x, self.y = kwargs["pos"]

        if "width" in kwargs:
            self.width = kwargs["width"]

        if "height" in kwargs:
            self.height = kwargs["height"]

        if "text" in kwargs:
            self.text = kwargs["text"]
        else:
            self.text = "Button"

        if "command" in kwargs:
            self.command = kwargs["command"]
            self.state = "enabled"

        if "state" in kwargs:
            self.state = kwargs["state"]

    def __validateKwargs(self, kwargs: dict):
        """
        Parse all the kwargs and raise an error if one isn't correct
        """

        for key in kwargs:
            if key not in self.__validKwargs:
                err = "%s is not a valid argument : [%s]"
                args = ", ".join(self.__validKwargs)
                raise AttributeError(err % (key, args))

    def __str__(self):
        """
        To print the caracteristics of the Button
        """

        txt = "Button:\n"
        txt += "- pos (%d, %d)\n" % (self.x, self.y)
        txt += "- width %d\n" % self.width
        txt += "- height %d\n" % self.height
        txt += "- text %s\n" % self.text

        return txt


if __name__ == '__main__':
    btn = Button(text="Ok")
    btn.set(pos=(200, 200), width=200, height=50, command=lambda: ...)
