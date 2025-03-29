from manim import *

class MainScene(Scene):
    def construct(self):
        # Create right triangle
        triangle = Polygon([-2, -1, 0], [1, -1, 0], [1, 2, 0], color=WHITE)
        right_angle = Square(side_length=0.2, color=YELLOW).move_to([1, -1, 0]).shift(LEFT*0.1 + UP*0.1)
        
        # Create squares on sides
        a_square = Square(side_length=2, color=BLUE).next_to(triangle, LEFT, buff=0)
        b_square = Square(side_length=3, color=RED).next_to(triangle, DOWN, buff=0)
        c_square = Square(side_length=np.sqrt(13), color=GREEN).rotate(np.arctan(3/2)).move_to([-0.5, 0.5, 0])
        
        # Labels
        a_label = MathTex("a^2").move_to(a_square)
        b_label = MathTex("b^2").move_to(b_square)
        c_label = MathTex("c^2").move_to(c_square)
        theorem = MathTex("a^2 + b^2 = c^2").to_edge(UP)
        
        # Animations
        self.play(Create(triangle), Create(right_angle))
        self.wait(0.5)
        self.play(FadeIn(a_square), Write(a_label))
        self.wait(0.5)
        self.play(FadeIn(b_square), Write(b_label))
        self.wait(0.5)
        self.play(FadeIn(c_square), Write(c_label))
        self.wait(0.5)
        self.play(Write(theorem))
        self.wait(2)