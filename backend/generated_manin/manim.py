from manim import *
import numpy as np

class LSTMScene(Scene):
    def construct(self):
        # Scene 1
        subtitle1 = Text("Breaking down a vector")
        subtitle1.to_edge(UP)
        axes1 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False},
        )
        vector1 = Vector([2, 2], color=YELLOW)
        dashed_line1_x = DashedLine([2, 2], [2, 0], color=YELLOW)
        dashed_line1_y = DashedLine([2, 2], [0, 2], color=YELLOW)
        self.add(subtitle1, axes1, vector1, dashed_line1_x, dashed_line1_y)
        self.wait(5)
        self.clear()

        # Scene 2
        subtitle2 = Text("Vector components as directions")
        subtitle2.to_edge(UP)
        compass = Circle(radius=2, color=YELLOW)
        center = Dot([0, 0], color=YELLOW)
        north = Arrow([0, 0], [0, 2], color=YELLOW)
        east = Arrow([0, 0], [2, 0], color=YELLOW)
        northeast = DashedLine([0, 0], [2, 2], color=YELLOW)
        north_label = Text("N").next_to(north, UP)
        east_label = Text("E").next_to(east, RIGHT)
        self.add(subtitle2, compass, center, north, east, northeast, north_label, east_label)
        self.wait(5)
        self.clear()

        # Scene 3
        subtitle3 = Text("Projections onto axes")
        subtitle3.to_edge(UP)
        axes3 = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            z_length=6,
            axis_config={"include_tip": False},
        )
        vector3 = Vector([2, 2, 1], color=YELLOW)
        dashed_line3_x = DashedLine([2, 2, 1], [2, 0, 0], color=YELLOW)
        dashed_line3_y = DashedLine([2, 2, 1], [0, 2, 0], color=YELLOW)
        dashed_line3_z = DashedLine([2, 2, 1], [0, 0, 1], color=YELLOW)
        self.add(subtitle3, axes3, vector3, dashed_line3_x, dashed_line3_y, dashed_line3_z)
        self.wait(5)
        self.clear()

        # Scene 4
        subtitle4 = Text("x and y components")
        subtitle4.to_edge(UP)
        axes4 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False},
        )
        vector4 = Vector([2, 2], color=YELLOW)
        dashed_line4_x = DashedLine([2, 2], [2, 0], color=YELLOW)
        dashed_line4_y = DashedLine([2, 2], [0, 2], color=YELLOW)
        x_component = Text("x-component").next_to(dashed_line4_x, DOWN)
        y_component = Text("y-component").next_to(dashed_line4_y, LEFT)
        self.add(subtitle4, axes4, vector4, dashed_line4_x, dashed_line4_y, x_component, y_component)
        self.wait(5)
        self.clear()

        # Scene 5
        subtitle5 = Text("Calculating vector components")
        subtitle5.to_edge(UP)
        axes5 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False},
        )
        vector5 = Vector([2, 2], color=YELLOW)
        dashed_line5_x = DashedLine([2, 2], [2, 0], color=YELLOW)
        dashed_line5_y = DashedLine([2, 2], [0, 2], color=YELLOW)
        x_value = Text("x = 2").next_to(dashed_line5_x, DOWN)
        y_value = Text("y = 2").next_to(dashed_line5_y, LEFT)
        vector_components = Text("Vector components").above(axes5)
        self.add(subtitle5, axes5, vector5, dashed_line5_x, dashed_line5_y, x_value, y_value, vector_components)
        self.wait(5)
        self.clear()

        # Scene 6
        subtitle6 = Text("Comparing vector components")
        subtitle6.to_edge(UP)
        axes6 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False},
        )
        vector6_1 = Vector([2, 2], color=YELLOW)
        vector6_2 = Vector([3, 1], color=YELLOW)
        dashed_line6_1_x = DashedLine([2, 2], [2, 0], color=YELLOW)
        dashed_line6_1_y = DashedLine([2, 2], [0, 2], color=YELLOW)
        dashed_line6_2_x = DashedLine([3, 1], [3, 0], color=YELLOW)
        dashed_line6_2_y = DashedLine([3, 1], [0, 1], color=YELLOW)
        self.add(subtitle6, axes6, vector6_1, vector6_2, dashed_line6_1_x, dashed_line6_1_y, dashed_line6_2_x, dashed_line6_2_y)
        self.wait(5)
        self.clear()

        # Scene 7
        subtitle7 = Text("Understanding vector components")
        subtitle7.to_edge(UP)
        axes7 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False},
        )
        vector7 = Vector([2, 2], color=YELLOW)
        dashed_line7_x = DashedLine([2, 2], [2, 0], color=YELLOW)
        dashed_line7_y = DashedLine([2, 2], [0, 2], color=YELLOW)
        vector_components_7 = Text("Vector components are projections").above(axes7)
        self.add(subtitle7, axes7, vector7, dashed_line7_x, dashed_line7_y, vector_components_7)
        self.wait(5)
        self.clear()

        # Scene 8
        subtitle8 = Text("Reviewing vector components")
        subtitle8.to_edge(UP)
        axes8 = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": False},
        )
        vector8 = Vector([2, 2], color=YELLOW)
        dashed_line8_x = DashedLine([2, 2], [2, 0], color=YELLOW)
        dashed_line8_y = DashedLine([2, 2], [0, 2], color=YELLOW)
        x_component_8 = Text("x-component").next_to(dashed_line8_x, DOWN)
        y_component_8 = Text("y-component").next_to(dashed_line8_y, LEFT)
        vector_8 = Text("Vector").above(axes8)
        self.add(subtitle8, axes8, vector8, dashed_line8_x, dashed_line8_y, x_component_8, y_component_8, vector_8)
        self.wait(5)