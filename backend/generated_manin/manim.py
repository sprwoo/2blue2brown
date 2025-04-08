from manim import *
import numpy as np

class LSTMScene(Scene):
    def construct(self):
        subtitle = Text("Defining a vector in 2D space").to_edge(DOWN)
        self.add(subtitle)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True},
        )
        self.play(Create(axes))
        vector = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW).add_tip()
        self.play(Create(vector))
        self.wait(3)
        self.clear()

        subtitle = Text("Finding vector components").to_edge(DOWN)
        self.add(subtitle)
        vector = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW).add_tip()
        self.play(Create(vector))
        dashed_line_x = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=YELLOW)
        dashed_line_y = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=YELLOW)
        self.play(Create(dashed_line_x), Create(dashed_line_y))
        x_label = Text("2").next_to([2, 0, 0], DOWN)
        y_label = Text("2").next_to([0, 2, 0], LEFT)
        self.play(Write(x_label), Write(y_label))
        self.wait(3)
        self.clear()

        subtitle = Text("Understanding component relationships").to_edge(DOWN)
        self.add(subtitle)
        triangle = Polygon(ORIGIN, [2, 0, 0], [2, 2, 0], stroke_color=YELLOW, fill_opacity=0.5)
        self.play(Create(triangle))
        x_component = Text("x-component").next_to([1, 0, 0], DOWN)
        y_component = Text("y-component").next_to([0, 1, 0], LEFT)
        self.play(Write(x_component), Write(y_component))
        self.wait(3)
        self.clear()

        subtitle = Text("Representing vectors as components").to_edge(DOWN)
        self.add(subtitle)
        vector = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW).add_tip()
        self.play(Create(vector))
        x_vector = Line(ORIGIN, [2, 0, 0], stroke_color=YELLOW).add_tip()
        y_vector = Line(ORIGIN, [0, 2, 0], stroke_color=YELLOW).add_tip()
        self.play(Create(x_vector), Create(y_vector))
        self.wait(3)
        self.clear()

        subtitle = Text("Visualizing vector components").to_edge(DOWN)
        self.add(subtitle)
        grid = NumberPlane(x_range=[-4, 4, 1], y_range=[-4, 4, 1])
        self.play(Create(grid))
        vector = Line(ORIGIN, [2, 2, 0], stroke_color=YELLOW).add_tip()
        self.play(Create(vector))
        x_highlight = Rectangle(width=1, height=0.1, stroke_color=YELLOW, fill_color=YELLOW, fill_opacity=0.5).move_to([2, 0, 0])
        y_highlight = Rectangle(width=0.1, height=1, stroke_color=YELLOW, fill_color=YELLOW, fill_opacity=0.5).move_to([0, 2, 0])
        self.play(Create(x_highlight), Create(y_highlight))
        self.wait(3)