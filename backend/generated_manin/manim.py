from manim import *
import numpy as np

class LSTMScene(Scene):
    def construct(self):
        subtitle = Text("Defining a vector in 2D space", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True},
        )
        self.add(axes)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW, stroke_width=2)
        vector_arrow = Arrow(vector.get_start(), vector.get_end(), stroke_color=YELLOW, stroke_width=2)
        self.play(Create(vector), Create(vector_arrow))
        self.wait(3)

        self.clear()

        subtitle = Text("Breaking down a vector into components", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW, stroke_width=2)
        vector_arrow = Arrow(vector.get_start(), vector.get_end(), stroke_color=YELLOW, stroke_width=2)
        self.add(vector, vector_arrow)

        dashed_line_x = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=WHITE, stroke_width=1)
        dashed_line_y = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=WHITE, stroke_width=1)
        self.play(Create(dashed_line_x), Create(dashed_line_y))

        x_component_label = Text("x component", font_size=24)
        x_component_label.next_to(dashed_line_x, DOWN)
        y_component_label = Text("y component", font_size=24)
        y_component_label.next_to(dashed_line_y, LEFT)
        self.play(Write(x_component_label), Write(y_component_label))

        x_component_value = Text("2", font_size=24)
        x_component_value.next_to(x_component_label, DOWN)
        y_component_value = Text("2", font_size=24)
        y_component_value.next_to(y_component_label, LEFT)
        self.play(Write(x_component_value), Write(y_component_value))
        self.wait(3)

        self.clear()

        subtitle = Text("Calculating magnitude using components", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        triangle = Polygon(ORIGIN, [2, 0, 0], [2, 2, 0], stroke_color=WHITE, stroke_width=1)
        self.add(triangle)

        x_label = Text("2", font_size=24)
        x_label.next_to(triangle, DOWN)
        y_label = Text("2", font_size=24)
        y_label.next_to(triangle, LEFT)
        self.play(Write(x_label), Write(y_label))

        hypotenuse_label = Text("√(2^2 + 2^2)", font_size=24)
        hypotenuse_label.next_to(triangle, RIGHT)
        self.play(Write(hypotenuse_label))
        self.wait(3)

        self.clear()

        subtitle = Text("Understanding negative vector components", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        vector = Line(ORIGIN, [-2, 2, 0], stroke_color=YELLOW, stroke_width=2)
        vector_arrow = Arrow(vector.get_start(), vector.get_end(), stroke_color=YELLOW, stroke_width=2)
        self.add(vector, vector_arrow)

        dashed_line_x = DashedLine([-2, 2, 0], [-2, 0, 0], stroke_color=WHITE, stroke_width=1)
        dashed_line_y = DashedLine([-2, 2, 0], [0, 2, 0], stroke_color=WHITE, stroke_width=1)
        self.play(Create(dashed_line_x), Create(dashed_line_y))

        x_component_label = Text("x component", font_size=24)
        x_component_label.next_to(dashed_line_x, DOWN)
        y_component_label = Text("y component", font_size=24)
        y_component_label.next_to(dashed_line_y, LEFT)
        self.play(Write(x_component_label), Write(y_component_label))

        x_component_value = Text("-2", font_size=24)
        x_component_value.next_to(x_component_label, DOWN)
        y_component_value = Text("2", font_size=24)
        y_component_value.next_to(y_component_label, LEFT)
        self.play(Write(x_component_value), Write(y_component_value))
        self.wait(3)

        self.clear()

        subtitle = Text("Adding vectors component-wise", font_size=36)
        subtitle.to_edge(UP)
        self.add(subtitle)

        vector1 = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW, stroke_width=2)
        vector1_arrow = Arrow(vector1.get_start(), vector1.get_end(), stroke_color=YELLOW, stroke_width=2)
        self.add(vector1, vector1_arrow)

        vector2 = Line(ORIGIN, [-2, 2, 0], stroke_color=YELLOW, stroke_width=2)
        vector2_arrow = Arrow(vector2.get_start(), vector2.get_end(), stroke_color=YELLOW, stroke_width=2)
        self.add(vector2, vector2_arrow)

        dashed_line_x1 = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=WHITE, stroke_width=1)
        dashed_line_y1 = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=WHITE, stroke_width=1)
        dashed_line_x2 = DashedLine([-2, 2, 0], [-2, 0, 0], stroke_color=WHITE, stroke_width=1)
        dashed_line_y2 = DashedLine([-2, 2, 0], [0, 2, 0], stroke_color=WHITE, stroke_width=1)
        self.play(Create(dashed_line_x1), Create(dashed_line_y1), Create(dashed_line_x2), Create(dashed_line_y2))

        x_component_label1 = Text("x component", font_size=24)
        x_component_label1.next_to(dashed_line_x1, DOWN)
        y_component_label1 = Text("y component", font_size=24)
        y_component_label1.next_to(dashed_line_y1, LEFT)
        x_component_label2 = Text("x component", font_size=24)
        x_component_label2.next_to(dashed_line_x2, DOWN)
        y_component_label2 = Text("y component", font_size=24)
        y_component_label2.next_to(dashed_line_y2, LEFT)
        self.play(Write(x_component_label1), Write(y_component_label1), Write(x_component_label2), Write(y_component_label2))

        x_component_value1 = Text("2", font_size=24)
        x_component_value1.next_to(x_component_label1, DOWN)
        y_component_value1 = Text("2", font_size=24)
        y_component_value1.next_to(y_component_label1, LEFT)
        x_component_value2 = Text("-2", font_size=24)
        x_component_value2.next_to(x_component_label2, DOWN)
        y_component_value2 = Text("2", font_size=24)
        y_component_value2.next_to(y_component_label2, LEFT)
        self.play(Write(x_component_value1), Write(y_component_value1), Write(x_component_value2), Write(y_component_value2))

        highlight_x1 = SurroundingRectangle(x_component_value1, buff=0.1, stroke_color=YELLOW, stroke_width=2)
        highlight_x2 = SurroundingRectangle(x_component_value2, buff=0.1, stroke_color=YELLOW, stroke_width=2)
        self.play(Create(highlight_x1), Create(highlight_x2))
        self.wait(3)