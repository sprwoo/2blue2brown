from manim import *

class MainScene(Scene):
    def construct(self):
        # Intro: Neurons and circuits
        subtitle1 = Text("The Backbone of AI: Backpropagation", font_size=24).to_edge(DOWN)
        self.play(Write(subtitle1))
        
        # Neuron animation
        neuron = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(5)])
        neuron.arrange(RIGHT, buff=0.5)
        connectors = VGroup(*[Line(neuron[i], neuron[i+1]) for i in range(4)])
        
        self.play(
            LaggedStart(*[FadeIn(n) for n in neuron], lag_ratio=0.2),
            Create(connectors),
            run_time=2
        )
        self.wait(1)
        self.play(FadeOut(subtitle1), FadeOut(neuron), FadeOut(connectors))

        # Neural network diagram
        subtitle2 = Text("Learning Through Adjustments", font_size=24).to_edge(DOWN)
        layers = VGroup(
            VGroup(*[Circle(radius=0.15, color=GREEN) for _ in range(3)]),
            VGroup(*[Circle(radius=0.15, color=RED) for _ in range(4)]),
            VGroup(*[Circle(radius=0.15, color=BLUE) for _ in range(3)])
        )
        for i, layer in enumerate(layers):
            layer.arrange(DOWN, buff=0.4).shift(LEFT * (i - 1) * 2)
        
        connections = VGroup()
        for i in range(len(layers)-1):
            for s in layers[i]:
                for t in layers[i+1]:
                    connections.add(Line(s, t, stroke_width=1.5))
        
        self.play(Write(subtitle2))
        self.play(
            LaggedStart(*[FadeIn(layers[0]), FadeIn(layers[1]), FadeIn(layers[2])], lag_ratio=0.3),
            Create(connections),
            run_time=3
        )
        self.wait(2)
        
        # Error propagation
        error_arrow = Arrow(UP, DOWN, color=YELLOW).next_to(layers[2], RIGHT)
        error_text = Text("Error", font_size=18).next_to(error_arrow, RIGHT)
        self.play(GrowArrow(error_arrow), Write(error_text))
        self.play(
            connections.animate.set_stroke(opacity=0.3),
            layers[2].animate.set_fill(opacity=0.5),
            run_time=1.5
        )
        self.play(FadeOut(subtitle2), FadeOut(error_arrow), FadeOut(error_text))

        # Mathematical explanation
        subtitle3 = Text("The Calculus of Correction", font_size=24).to_edge(DOWN)
        equation = MathTex(r"\frac{\partial E}{\partial w} = \frac{\partial E}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w}").scale(1.2)
        self.play(Write(subtitle3), Write(equation))
        self.wait(3)
        self.play(FadeOut(equation), FadeOut(subtitle3))

        # Gradient descent visualization
        subtitle4 = Text("Navigating the Error Landscape", font_size=24).to_edge(DOWN)
        axes = Axes(x_range=[0, 5], y_range=[0, 5])
        curve = axes.plot(lambda x: 0.5*(x-2.5)**2 + 1, color=MAROON_B)
        dot = Dot(color=YELLOW).move_to(axes.c2p(4.5, 4.5))
        
        self.play(Write(subtitle4), Create(axes), Create(curve))
        self.play(dot.animate.move_to(axes.c2p(2.5, 1)), run_time=3)
        self.wait(1)
        self.play(FadeOut(axes), FadeOut(curve), FadeOut(dot), FadeOut(subtitle4))

        # Modern applications
        subtitle5 = Text("From Theory to Everyday Magic", font_size=24).to_edge(DOWN)
        icons = VGroup(
            Triangle().scale(0.5).set_color(ORANGE),
            Square().scale(0.5).set_color(PURPLE),
            Circle().scale(0.5).set_color(GOLD)
        ).arrange(RIGHT, buff=1.5)
        
        self.play(Write(subtitle5))
        self.play(
            LaggedStart(
                icons[0].animate.shift(UP),
                icons[1].animate.shift(UP*0.5),
                icons[2].animate.shift(DOWN),
                lag_ratio=0.3
            ), 
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(icons), FadeOut(subtitle5))
        
        # Final message
        final_text = Text("Errors lead to growth.\nEven for machines.", font_size=36)
        self.play(Write(final_text), run_time=2)
        self.wait(3)
        self.play(FadeOut(final_text))