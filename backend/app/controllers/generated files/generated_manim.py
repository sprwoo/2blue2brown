# New manim
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

