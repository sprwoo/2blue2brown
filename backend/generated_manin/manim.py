from manim import *
import numpy as np

import numpy as np

class LSTMScene(Scene):
    def construct(self):
        # Scene 1
        subtitle1 = Text("Defining the Pythagorean Theorem").scale(0.7).to_edge(DOWN)
        self.add(subtitle1)
        self.wait(2)
        triangle1 = Polygon(ORIGIN, RIGHT*3, UP*4, color=WHITE)
        a_text = Text("a").next_to(triangle1, DOWN)
        b_text = Text("b").next_to(triangle1, LEFT)
        c_text = Text("c").next_to(triangle1, RIGHT).shift(UP*2.5)
        self.play(Create(triangle1), Write(a_text), Write(b_text), Write(c_text))
        self.wait(5)
        self.remove(subtitle1, triangle1, a_text, b_text, c_text)

        # Scene 2
        subtitle2 = Text("Geometric Interpretation of the Theorem").scale(0.7).to_edge(DOWN)
        self.add(subtitle2)
        self.wait(2)
        triangle2 = Polygon(ORIGIN, RIGHT*3, UP*4, color=WHITE)
        square_a = Square(side_length=3).next_to(triangle2, DOWN).shift(LEFT*1.5)
        square_b = Square(side_length=4).next_to(triangle2, LEFT).shift(UP*2)
        square_c = Square(side_length=5).next_to(triangle2, RIGHT).shift(UP*2.5)
        self.play(Create(triangle2), Create(square_a), Create(square_b), Create(square_c))
        self.wait(2)
        self.play(square_a.animate.shift(RIGHT*4.5), square_b.animate.shift(RIGHT*3), square_c.animate.shift(LEFT*0.5))
        self.wait(5)
        self.remove(subtitle2, triangle2, square_a, square_b, square_c)

        # Scene 3
        subtitle3 = Text("Mathematical Representation of the Theorem").scale(0.7).to_edge(DOWN)
        self.add(subtitle3)
        self.wait(2)
        equation = Text("a^2 + b^2 = c^2").scale(1.5)
        triangle3 = Polygon(ORIGIN, RIGHT*3, UP*4, color=WHITE).shift(DOWN*2)
        a_arrow = Arrow(equation[0].get_center(), triangle3[0].get_center())
        b_arrow = Arrow(equation[4].get_center(), triangle3[1].get_center())
        c_arrow = Arrow(equation[8].get_center(), triangle3[2].get_center())
        self.play(Write(equation), Create(triangle3), Create(a_arrow), Create(b_arrow), Create(c_arrow))
        self.wait(5)
        self.remove(subtitle3, equation, triangle3, a_arrow, b_arrow, c_arrow)

        # Scene 4
        subtitle4 = Text("Applying the Theorem to Solve for c").scale(0.7).to_edge(DOWN)
        self.add(subtitle4)
        self.wait(2)
        triangle4 = Polygon(ORIGIN, RIGHT*3, UP*4, color=WHITE)
        equation2 = Text("3^2 + 4^2 = c^2").scale(1.5).shift(UP*2)
        self.play(Create(triangle4), Write(equation2))
        self.wait(2)
        solution = Text("c = sqrt(3^2 + 4^2) = sqrt(25) = 5").scale(1.5).shift(UP*2)
        self.play(Transform(equation2, solution))
        self.wait(5)
        self.remove(subtitle4, triangle4, equation2)

        # Scene 5
        subtitle5 = Text("Universality of the Pythagorean Theorem").scale(0.7).to_edge(DOWN)
        self.add(subtitle5)
        self.wait(2)
        triangles = []
        for i in range(5):
            for j in range(5):
                triangle = Polygon(ORIGIN, RIGHT*(i+1), UP*(j+1), color=WHITE).scale(0.5).shift(RIGHT*i*0.5+UP*j*0.5)
                triangles.append(triangle)
        self.play(*[Create(triangle) for triangle in triangles])
        self.wait(5)
        self.remove(subtitle5, *triangles)