from manim import *
import numpy as np

class LSTMScene(Scene):
    def construct(self):
        subtitle = Text("Defining a right triangle", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        triangle = VGroup(
            Line(ORIGIN, RIGHT * 3, stroke_width=0.1),
            Line(ORIGIN, UP * 4, stroke_width=0.1),
            Line(RIGHT * 3, UP * 4, stroke_width=0.1)
        )
        a = Text("a").next_to(triangle[0], DOWN)
        b = Text("b").next_to(triangle[1], LEFT)
        c = Text("c").next_to(triangle[2], UP)
        self.play(Create(triangle), Write(a), Write(b), Write(c))
        self.wait(5)

        self.clear()
        subtitle = Text("Visualizing squares of sides", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        square_a = VGroup(
            Line(ORIGIN, RIGHT * 3, stroke_width=0.1),
            Line(ORIGIN, UP * 3, stroke_width=0.1),
            Line(RIGHT * 3, UP * 3, stroke_width=0.1),
            Line(RIGHT * 3, ORIGIN, stroke_width=0.1)
        )
        square_b = VGroup(
            Line(RIGHT * 4, RIGHT * 4 + UP * 4, stroke_width=0.1),
            Line(RIGHT * 4, RIGHT * 4 + RIGHT * 4, stroke_width=0.1),
            Line(RIGHT * 4 + UP * 4, RIGHT * 4 + UP * 4 + RIGHT * 4, stroke_width=0.1),
            Line(RIGHT * 4 + RIGHT * 4, RIGHT * 4 + RIGHT * 4 + UP * 4, stroke_width=0.1)
        )
        square_c = VGroup(
            Line(RIGHT * 9, RIGHT * 9 + UP * 5, stroke_width=0.1),
            Line(RIGHT * 9, RIGHT * 9 + RIGHT * 5, stroke_width=0.1),
            Line(RIGHT * 9 + UP * 5, RIGHT * 9 + UP * 5 + RIGHT * 5, stroke_width=0.1),
            Line(RIGHT * 9 + RIGHT * 5, RIGHT * 9 + RIGHT * 5 + UP * 5, stroke_width=0.1)
        )
        label_a = Text("a^2").next_to(square_a, DOWN)
        label_b = Text("b^2").next_to(square_b, DOWN)
        label_c = Text("c^2").next_to(square_c, DOWN)
        self.play(Create(square_a), Create(square_b), Create(square_c), Write(label_a), Write(label_b), Write(label_c))
        self.wait(5)

        self.clear()
        subtitle = Text("Relating squares to triangle sides", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        triangle = VGroup(
            Line(ORIGIN, RIGHT * 3, stroke_width=0.1),
            Line(ORIGIN, UP * 4, stroke_width=0.1),
            Line(RIGHT * 3, UP * 4, stroke_width=0.1)
        )
        square_a = VGroup(
            Line(ORIGIN, RIGHT * 3, stroke_width=0.1),
            Line(ORIGIN, DOWN * 3, stroke_width=0.1),
            Line(RIGHT * 3, DOWN * 3, stroke_width=0.1),
            Line(RIGHT * 3, ORIGIN, stroke_width=0.1)
        )
        square_b = VGroup(
            Line(ORIGIN, UP * 4, stroke_width=0.1),
            Line(ORIGIN, LEFT * 4, stroke_width=0.1),
            Line(UP * 4, LEFT * 4 + UP * 4, stroke_width=0.1),
            Line(LEFT * 4, LEFT * 4 + UP * 4, stroke_width=0.1)
        )
        square_c = VGroup(
            Line(RIGHT * 3, RIGHT * 3 + UP * 5, stroke_width=0.1),
            Line(RIGHT * 3, RIGHT * 3 + RIGHT * 5, stroke_width=0.1),
            Line(RIGHT * 3 + UP * 5, RIGHT * 3 + UP * 5 + RIGHT * 5, stroke_width=0.1),
            Line(RIGHT * 3 + RIGHT * 5, RIGHT * 3 + RIGHT * 5 + UP * 5, stroke_width=0.1)
        )
        dashed_line_a = DashedLine(square_a[1].get_start(), triangle[0].get_start(), stroke_width=0.1)
        dashed_line_b = DashedLine(square_b[1].get_start(), triangle[1].get_start(), stroke_width=0.1)
        dashed_line_c = DashedLine(square_c[1].get_start(), triangle[2].get_start(), stroke_width=0.1)
        self.play(Create(triangle), Create(square_a), Create(square_b), Create(square_c), Create(dashed_line_a), Create(dashed_line_b), Create(dashed_line_c))
        self.wait(5)

        self.clear()
        subtitle = Text("Pythagorean theorem formula", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        equation = Text("a^2 + b^2 = c^2")
        arrow_a = Arrow(LEFT * 2, ORIGIN, stroke_width=0.1)
        arrow_b = Arrow(LEFT * 4, LEFT * 2, stroke_width=0.1)
        arrow_c = Arrow(ORIGIN, RIGHT * 2, stroke_width=0.1)
        self.play(Write(equation), Create(arrow_a), Create(arrow_b), Create(arrow_c))
        self.wait(5)

        self.clear()
        subtitle = Text("Applying the theorem to triangles", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        triangle = VGroup(
            Line(ORIGIN, RIGHT * 3, stroke_width=0.1),
            Line(ORIGIN, UP * 4, stroke_width=0.1),
            Line(RIGHT * 3, UP * 4, stroke_width=0.1)
        )
        equation = Text("a^2 + b^2 = c^2").next_to(triangle, UP)
        arrow_a = Arrow(triangle[0].get_start(), equation[0].get_start(), stroke_width=0.1)
        arrow_b = Arrow(triangle[1].get_start(), equation[3].get_start(), stroke_width=0.1)
        arrow_c = Arrow(triangle[2].get_start(), equation[6].get_start(), stroke_width=0.1)
        self.play(Create(triangle), Write(equation), Create(arrow_a), Create(arrow_b), Create(arrow_c))
        self.wait(5)

        self.clear()
        subtitle = Text("Real-world application of theorem", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        building = VGroup(
            Line(ORIGIN, UP * 4, stroke_width=0.1),
            Line(UP * 4, RIGHT * 3 + UP * 4, stroke_width=0.1),
            Line(RIGHT * 3 + UP * 4, RIGHT * 3, stroke_width=0.1),
            Line(RIGHT * 3, ORIGIN, stroke_width=0.1)
        )
        dashed_line = DashedLine(building[1].get_start(), RIGHT * 3 + UP * 4 + RIGHT * 3, stroke_width=0.1)
        label = Text("5 units").next_to(dashed_line, RIGHT)
        self.play(Create(building), Create(dashed_line), Write(label))
        self.wait(5)