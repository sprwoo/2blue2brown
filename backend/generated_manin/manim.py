from manim import *
import numpy as np

class LSTMScene(Scene):
    def construct(self):
        subtitle = Text("Defining a vector in 2D space", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True},
        )
        self.play(Create(axes), run_time=2)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        vector_label = Text("Vector", font_size=24)
        vector_label.next_to(vector, UP, buff=0.5)
        self.play(Write(vector_label), run_time=1)

        self.wait(3)

        self.clear()

        subtitle = Text("Finding vector components", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        dashed_x = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=YELLOW)
        dashed_y = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=YELLOW)
        self.play(Create(dashed_x), Create(dashed_y), run_time=2)

        x_label = Text("2", font_size=24)
        x_label.next_to(dashed_x, DOWN, buff=0.2)
        y_label = Text("2", font_size=24)
        y_label.next_to(dashed_y, LEFT, buff=0.2)
        self.play(Write(x_label), Write(y_label), run_time=1)

        self.wait(3)

        self.clear()

        subtitle = Text("Understanding vector component relationships", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        triangle = Polygon(ORIGIN, [2, 0, 0], [2, 2, 0], stroke_color=WHITE, fill_opacity=0)
        self.play(Create(triangle), run_time=2)

        x_label = Text("x-component", font_size=24)
        x_label.next_to(Line(ORIGIN, [2, 0, 0]), DOWN, buff=0.2)
        y_label = Text("y-component", font_size=24)
        y_label.next_to(Line(ORIGIN, [0, 2, 0]), LEFT, buff=0.2)
        self.play(Write(x_label), Write(y_label), run_time=1)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        self.wait(3)

        self.clear()

        subtitle = Text("Visualizing the x-component", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        dashed_x = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=YELLOW)
        dashed_y = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=YELLOW)
        self.play(Create(dashed_x), Create(dashed_y), run_time=2)

        x_component = Line(ORIGIN, [2, 0, 0], stroke_color=GREEN)
        self.play(Create(x_component), run_time=2)

        x_label = Text("x-component", font_size=24)
        x_label.next_to(x_component, UP, buff=0.2)
        self.play(Write(x_label), run_time=1)

        self.wait(3)

        self.clear()

        subtitle = Text("Visualizing the y-component", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        dashed_x = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=YELLOW)
        dashed_y = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=YELLOW)
        self.play(Create(dashed_x), Create(dashed_y), run_time=2)

        y_component = Line(ORIGIN, [0, 2, 0], stroke_color=GREEN)
        self.play(Create(y_component), run_time=2)

        y_label = Text("y-component", font_size=24)
        y_label.next_to(y_component, RIGHT, buff=0.2)
        self.play(Write(y_label), run_time=1)

        self.wait(3)

        self.clear()

        subtitle = Text("Combining vector components", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        x_component = Line(ORIGIN, [2, 0, 0], stroke_color=GREEN)
        self.play(Create(x_component), run_time=2)

        x_label = Text("x-component", font_size=24)
        x_label.next_to(x_component, UP, buff=0.2)
        self.play(Write(x_label), run_time=1)

        y_component = Line(ORIGIN, [0, 2, 0], stroke_color=GREEN)
        self.play(Create(y_component), run_time=2)

        y_label = Text("y-component", font_size=24)
        y_label.next_to(y_component, RIGHT, buff=0.2)
        self.play(Write(y_label), run_time=1)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        vector_label = Text("Resultant Vector", font_size=24)
        vector_label.next_to(vector, UP, buff=0.5)
        self.play(Write(vector_label), run_time=1)

        self.wait(3)

        self.clear()

        subtitle = Text("Resolving vectors into components", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        triangle = Polygon(ORIGIN, [2, 0, 0], [2, 2, 0], stroke_color=WHITE, fill_opacity=0)
        self.play(Create(triangle), run_time=2)

        x_label = Text("x-component", font_size=24)
        x_label.next_to(Line(ORIGIN, [2, 0, 0]), DOWN, buff=0.2)
        y_label = Text("y-component", font_size=24)
        y_label.next_to(Line(ORIGIN, [0, 2, 0]), LEFT, buff=0.2)
        self.play(Write(x_label), Write(y_label), run_time=1)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        vector_label = Text("Resultant Vector", font_size=24)
        vector_label.next_to(vector, UP, buff=0.5)
        self.play(Write(vector_label), run_time=1)

        dashed_x = DashedLine([2, 2, 0], [2, 0, 0], stroke_color=YELLOW)
        dashed_y = DashedLine([2, 2, 0], [0, 2, 0], stroke_color=YELLOW)
        self.play(Create(dashed_x), Create(dashed_y), run_time=2)

        self.wait(3)

        self.clear()

        subtitle = Text("Visualizing vector addition", font_size=36)
        subtitle.to_edge(DOWN)
        self.add(subtitle)

        vector = Line(ORIGIN, [2, 2, 0], stroke_color=RED)
        self.play(Create(vector), run_time=2)

        vector_label = Text("Resultant", font_size=24)
        vector_label.next_to(vector, UP, buff=0.5)
        self.play(Write(vector_label), run_time=1)

        x_component = Line(ORIGIN, [2, 0, 0], stroke_color=GREEN)
        self.play(Create(x_component), run_time=2)

        x_label = Text("x-component", font_size=24)
        x_label.next_to(x_component, UP, buff=0.2)
        self.play(Write(x_label), run_time=1)

        y_component = Line(ORIGIN, [0, 2, 0], stroke_color=GREEN)
        self.play(Create(y_component), run_time=2)

        y_label = Text("y-component", font_size=24)
        y_label.next_to(y_component, RIGHT, buff=0.2)
        self.play(Write(y_label), run_time=1)

        self.wait(3)