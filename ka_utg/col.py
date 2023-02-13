# coding=utf-8
"""Koskya Utilities Module
contains the Kosakya Utilitiy Classes
"""


class Col:
    """Colour Class
    """
    # esc = "\033"
    esc = "\u001b"
    check_mark = u'\u2705'
    heavy_check_mark = u'\u2713'
    heavy_check_mark_ = u'\u2714'

    class style:
        reset = '0'
        bold = '1'
        disable = '2'
        negative1 = '3'
        underline = '4'
        negative2 = '5'
        reverse = '7'
        invisible = '8'
        strikethrough = '9'

    class fg:
        black = '30'
        red = '31'
        green = '32'
        yellow = '33'
        blue = '34'
        magenta = '35'
        cyan = '36'
        white = '37'
        reset = '39'

    class bg:
        black = '40'
        red = '41'
        green = '42'
        yellow = '43'
        blue = '44'
        magenta = '45'
        cyan = '46'
        white = '47'
        reset = '49'

    @classmethod
    def show(cls, text, fg, bg=bg.reset, style=style.reset, esc=esc):
        return f"{esc}[{style};{fg};{bg}m{text}{esc}[0m"

    @classmethod
    def sh_red(cls, text):
        return cls.show(text, fg=cls.fg.red)

    @classmethod
    def sh_green(cls, text, ):
        return cls.show(text, fg=cls.fg.green)

    @classmethod
    def sh_yellow(cls, text):
        return cls.show(text, fg=cls.fg.yellow)

    @classmethod
    def sh_blue(cls, text):
        return cls.show(text, fg=cls.fg.blue)

    @classmethod
    def sh_magenta(cls, text):
        return cls.show(text, fg=cls.fg.magenta)

    @classmethod
    def sh_bold(cls, text):
        return cls.show(text, fg=cls.fg.red, style=cls.style.bold)

    @classmethod
    def sh_bold_red(cls, text):
        return cls.show(text, fg=cls.fg.red, style=cls.style.bold)

    @classmethod
    def sh_bold_green(cls, text):
        return cls.show(text, fg=cls.fg.green, style=cls.style.bold)

    @classmethod
    def sh_bold_light_green(cls, text):
        return cls.show(text, fg='92', style=cls.style.bold)

    @classmethod
    def sh_bold_yellow(cls, text):
        return cls.show(text, fg=cls.fg.yellow, style=cls.style.bold)

    @classmethod
    def sh_bold_blue(cls, text):
        return cls.show(text, fg=cls.fg.blue, style=cls.style.bold)

    @classmethod
    def sh_bold_magenta(cls, text):
        return cls.show(text, fg=cls.fg.magenta, style=cls.style.bold)

    @classmethod
    def sh_bold_cyan(cls, text):
        """light blue
        """
        return cls.show(text, fg=cls.fg.cyan, style=cls.style.bold)
