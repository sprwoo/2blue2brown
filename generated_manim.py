<think>
Okay, I need to create a Manim scene that shows the relationship between sine and cosine on a unit circle. Let me start by breaking down the problem.

First, the main elements required are a unit circle, a point moving along its circumference, and projections of that point onto the x and y axes for both sine and cosine. Also, the projections should be dynamically drawn as the point moves, and there should be labels and smooth transitions to show the changing values.

Hmm, so the unit circle is straightforward. I can use the Circle class in Manim. Then, a moving point can be represented by a Dot. To animate the movement along the circumference, I can use a ParametricFunction or perhaps update the position of the dot over time using a ValueTracker for the angle.

Next, the projections. For cosine, which is the x-component, I need a line from the point to the y-axis. Similarly, for sine (y-component), a line from the point to the x-axis. These lines should change as the point moves. So maybe using always_redraw to keep updating the lines as the dot moves.

Also, the dynamic drawing of the sine and cosine curves over time. Wait, the problem says "dynamically drawing the sine and cosine projections onto the x- and y-axes." Maybe they mean drawing the sine and cosine waves as the point moves? Or perhaps just the vertical and horizontal lines from the point to the axes, which represent the projections. The wording says "projections," so I think it's the lines from the point to the axes. But the user also mentions "evolving values," so maybe labels showing the current sine and cosine values as the point moves.

So, step by step:

1. Create the unit circle centered at the origin.
2. Add axes (x and y) to the scene.
3. Create a moving dot on the circumference of the circle. This can be done by using a ValueTracker for the angle (theta) and updating the dot's position as (cos(theta), sin(theta), 0).
4. Draw horizontal and vertical lines from the dot to the axes. These lines will represent the projections (cos(theta) on x-axis and sin(theta) on y-axis).
5. Labels for sine and cosine values, positioned near the axes. These labels should update as theta changes.
6. Animate the movement of the dot and the corresponding lines and labels.

Wait, but how to handle the dynamic drawing of the projections? For example, as the dot moves, the lines from the dot to the axes should update their length and position. Using always_redraw for these lines would work. Similarly, the labels can be updated using always_redraw with a lambda function that takes the current theta value.

Also, the axes need to be present. Maybe create them with Axes or NumberLine. But since it's a unit circle, the axes should extend a bit beyond -1 and 1. So perhaps using NumberPlane or just two perpendicular lines with ticks.

Alternatively, use the standard Axes class and set the x_range and y_range from -1.5 to 1.5 to give some space.

Another thing: the dynamic drawing of the sine and cosine curves. Wait, the problem says "dynamically drawing the sine and cosine projections onto the x- and y-axes." Maybe they want to plot the sine and cosine functions as the point moves, like tracing out the curves over time. For example, as the point moves around the circle, a sine wave is drawn on the y-axis side and a cosine wave on the x-axis side. That would require creating another set of axes next to the unit circle and plotting the functions as theta increases.

But that might complicate the scene. The original description mentions "projections onto the x- and y-axes," so maybe just the vertical and horizontal lines from the moving point to the axes. However, the user also says "dynamically drawing the sine and cosine projections," which might imply that both the lines and the actual graphs are being drawn over time.

Wait, let's re-read the problem statement: "Animate a point moving along the circle’s circumference while dynamically drawing the sine and cosine projections onto the x- and y-axes. Use labels and smooth transitions to highlight the evolving values as the point moves."

So the projections are the lines from the point to the axes, and perhaps the actual graphs of sine and cosine being plotted as functions of the angle. Hmm, maybe not. The wording is a bit ambiguous. But since the user mentions "projections onto the axes," it's more likely referring to the lines that show the current sine and cosine values on the axes.

Alternatively, it could be that they want to draw the sine and cosine curves as the point moves, with the x-coordinate being the angle and the y-coordinate being sin(angle) or cos(angle). But in that case, the axes would need to be different. For example, the horizontal axis would be the angle theta, and the vertical axis would be the value of sine or cosine. But that requires a separate plot next to the unit circle.

But given the problem statement, perhaps the intended approach is to have the unit circle, the moving point, and the projections (lines) to the x and y axes. Then, labels indicating the current sine and cosine values. The "dynamically drawing" part could mean that as the point moves, the lines are drawn in real-time, and maybe the labels update smoothly.

So, to proceed:

- Create the unit circle.
- Create x and y axes.
- Create a ValueTracker for theta, ranging from 0 to 2*PI.
- The moving point is at (cos(theta), sin(theta), 0).
- The horizontal projection line is from the point to (cos(theta), 0, 0), which is the projection on the x-axis (cosine). Similarly, the vertical projection line is from the point to (0, sin(theta), 0) (sine).
- These lines can be created as DashedLines or regular Lines, colored differently for sine and cosine.
- Labels for "sin(θ)" and "cos(θ)" positioned near the respective axes, showing the current value. These can be DecimalNumber objects that track the values of sin(theta) and cos(theta), updating as theta changes.
- To animate the movement, use ValueTracker and updaters.

Now, for the animation:

Start by drawing the circle and axes. Then, create the dot and projection lines. Animate the dot moving around the circle, with the projection lines updating in real-time. The labels should also update their numerical values as theta changes.

Additionally, maybe add an arc to indicate the angle theta, with a label showing θ. But the problem statement doesn't explicitly mention that, but it could enhance the visualization.

Smooth transitions: perhaps when starting the animation, the dot begins moving, and the lines and labels smoothly follow.

So, putting this into code:

First, import necessary Manim modules.

Then, create a class that extends Scene (or maybe MovingCameraScene if needed, but probably Scene is enough).

In the construct method:

1. Create the unit circle.
2. Create x and y axes. Let's use Axes for better control. Or maybe two NumberLines positioned horizontally and vertically.

Wait, in Manim, the Axes class can create x and y axes, but for simplicity, maybe create two lines: x_axis from (-1.5, 0, 0) to (1.5, 0, 0), and y_axis from (0, -1.5, 0) to (0, 1.5, 0). Then add them to the scene.

Alternatively, use the NumberPlane but only show the x and y axes. But perhaps using simple Line objects is easier.

Alternatively, use the CoordinateSystem, but maybe that's overcomplicating. Let's go with simple Axes.

Wait, using Axes with x_range and y_range from -1.5 to 1.5.

But maybe for the projections, the axes need to be at the edge of the unit circle. Alternatively, position the axes outside the circle.

Wait, perhaps it's better to have the unit circle centered, and the x and y axes passing through the center. So standard coordinate system.

So:

circle = Circle(radius=1, color=WHITE)
axes = Axes(
    x_range=[-1.5, 1.5, 1],
    y_range=[-1.5, 1.5, 1],
    x_length=3,
    y_length=3,
    axis_config={"color": BLUE},
)
self.add(circle, axes)

Then, create a ValueTracker for theta:

theta = ValueTracker(0)

dot = always_redraw(lambda: Dot(point=[np.cos(theta.get_value()), np.sin(theta.get_value()), 0], color=YELLOW))

Then, the horizontal projection line (cosine):

cos_line = always_redraw(
    lambda: Line(
        start=dot.get_center(),
        end=[dot.get_center()[0], 0, 0],
        color=RED,
        stroke_width=2,
    )
)

Similarly, the vertical projection line (sine):

sin_line = always_redraw(
    lambda: Line(
        start=dot.get_center(),
        end=[0, dot.get_center()[1], 0],
        color=GREEN,
        stroke_width=2,
    )
)

Then, add labels for sin and cos values:

cos_label = always_redraw(
    lambda: MathTex(r"\cos(\theta) = ").next_to([cos_line.get_end()[0], 0, 0], DOWN).shift(UP*0.2)
)
cos_value = always_redraw(
    lambda: DecimalNumber(cos(theta.get_value())).next_to(cos_label, RIGHT)
)

Similarly for sin:

sin_label = always_redraw(
    lambda: MathTex(r"\sin(\theta) = ").next_to([0, sin_line.get_end()[1], 0], LEFT).shift(RIGHT*0.2)
)
sin_value = always_redraw(
    lambda: DecimalNumber(sin(theta.get_value())).next_to(sin_label, RIGHT)
)

Wait, but positioning the labels next to the projection lines might be tricky. For the cosine label, it can be placed below the x-axis near the end of the cos_line. Similarly, the sine label can be to the left of the y-axis near the end of the sin_line.

But maybe using VGroup or aligning them properly.

Alternatively, position the cosine label below the x-axis projection point, and the sine label to the left of the y-axis projection point.

For example:

cos_label = always_redraw(
    lambda: MathTex(r"\cos(\theta)").scale(0.8).next_to(cos_line.get_end(), DOWN)
)
cos_value = always_redraw(
    lambda: DecimalNumber(np.cos(theta.get_value()), num_decimal_places=2).scale(0.8).next_to(cos_label, DOWN)
)

Similarly for sine:

sin_label = always_redraw(
    lambda: MathTex(r"\sin(\theta)").scale(0.8).next_to(sin_line.get_end(), LEFT)
)
sin_value = always_redraw(
    lambda: DecimalNumber(np.sin(theta.get_value()), num_decimal_places=2).scale(0.8).next_to(sin_label, LEFT)
)

But maybe the labels should be grouped with the values. Alternatively, use a single label that combines the text and value. But using separate labels for text and numbers allows more flexibility.

Alternatively, use a VGroup for each label and value. But maybe it's easier to create a MathTex that includes the value. However, since the value is changing, using DecimalNumber is better.

Wait, Manim has a way to combine text and numbers using Tex and DecimalNumber. For example:

cos_label = VGroup(
    MathTex(r"\cos(\theta) = "),
    DecimalNumber(np.cos(theta.get_value())),
).arrange(RIGHT, buff=0.2)
cos_label.add_updater(lambda m: m[1].set_value(np.cos(theta.get_value())))
cos_label.add_updater(lambda m: m.next_to(cos_line.get_end(), DOWN))

But then, need to create this VGroup and add the updaters. This way, both the label and the value are grouped and move together.

Similarly for sin_label.

Alternatively, use the following approach:

cos_tex = MathTex(r"\cos(\theta)").scale(0.8)
cos_num = DecimalNumber(0, num_decimal_places=2).scale(0.8)
cos_group = VGroup(cos_tex, cos_num).arrange(RIGHT, buff=0.2)
cos_group.add_updater(lambda m: m.next_to(cos_line.get_end(), DOWN))
cos_num.add_updater(lambda m: m.set_value(np.cos(theta.get_value())))

Same for sin_group:

sin_tex = MathTex(r"\sin(\theta)").scale(0.8)
sin_num = DecimalNumber(0, num_decimal_places=2).scale(0.8)
sin_group = VGroup(sin_tex, sin_num).arrange(RIGHT, buff=0.2)
sin_group.add_updater(lambda m: m.next_to(sin_line.get_end(), LEFT))
sin_num.add_updater(lambda m: m.set_value(np.sin(theta.get_value())))

This way, the labels and numbers are grouped and update their positions and values as theta changes.

Now, putting it all together:

In the construct method:

- Create circle and axes.
- Create theta tracker.
- Create dot, cos_line, sin_line.
- Create cos_group and sin_group with updaters.
- Animate theta from 0 to 2*PI.

But need to add all these elements to the scene.

So:

self.add(circle, axes)
self.add(dot, cos_line, sin_line)
self.add(cos_group, sin_group)

Then, animate theta with:

self.play(theta.animate.set_value(2 * PI), run_time=5, rate_func=linear)

But before that, maybe create the initial elements with Create animations. For example, first draw the circle and axes, then add the dot and lines with FadeIn, then start the animation.

Alternatively, since Manim will show all elements added to the scene at the start of the play call. But using the ValueTracker and always_redraw ensures that everything updates during the animation.

Wait, no. If we use always_redraw, then the objects are added once, and their positions are updated each frame. So the code would be:

In the construct method:

circle = Circle(radius=1, color=WHITE)
axes = Axes(
    x_range=[-1.5, 1.5, 1],
    y_range=[-1.5, 1.5, 1],
    x_length=3,
    y_length=3,
    axis_config={"color": BLUE},
)
self.add(circle, axes)

theta = ValueTracker(0)

dot = always_redraw(lambda: Dot(point=[np.cos(theta.get_value()), np.sin(theta.get_value()), 0], color=YELLOW))
cos_line = always_redraw(lambda: Line(dot.get_center(), [dot.get_center()[0], 0, 0], color=RED))
sin_line = always_redraw(lambda: Line(dot.get_center(), [0, dot.get_center()[1], 0], color=GREEN))

cos_tex = MathTex(r"\cos(\theta)").scale(0.8)
cos_num = DecimalNumber(0, num_decimal_places=2).scale(0.8)
cos_group = VGroup(cos_tex, cos_num).arrange(RIGHT, buff=0.2)
cos_group.add_updater(lambda m: m.next_to(cos_line.get_end(), DOWN))
cos_num.add_updater(lambda m: m.set_value(np.cos(theta.get_value())))

sin_tex = MathTex(r"\sin(\theta)").scale(0.8)
sin_num = DecimalNumber(0, num_decimal_places=2).scale(0.8)
sin_group = VGroup(sin_tex, sin_num).arrange(RIGHT, buff=0.2)
sin_group.add_updater(lambda m: m.next_to(sin_line.get_end(), LEFT))
sin_num.add_updater(lambda m: m.set_value(np.sin(theta.get_value())))

self.add(dot, cos_line, sin_line, cos_group, sin_group)

self.play(theta.animate.set_value(2 * PI), run_time=5, rate_func=linear)

Wait, but adding the updaters after creating the VGroups and before adding them to the scene. Also, when using add_updater, the objects must be in the scene already, otherwise the updater might not be called. But in this case, the updaters are added before adding to the scene. However, Manim's updaters work as long as the Mobject is on the screen. So perhaps the code is okay.

Alternatively, create the VGroups, add the updaters, then add them to the scene.

But let's test the code in mind. When theta is animated to 2*PI over 5 seconds, the dot moves around the circle, the lines update, and the labels update their positions and values.

Potential issues:

- The labels might overlap with the axes or other elements. Maybe adjusting the positioning. For example, shifting the cos_group a bit down and to the side. Using .next_to(..., DOWN, buff=0.1) for cos_group.

Alternatively, use:

cos_group.add_updater(lambda m: m.next_to(cos_line.get_end(), DOWN, buff=0.1))

Similarly for sin_group:

sin_group.add_updater(lambda m: m.next_to(sin_line.get_end(), LEFT, buff=0.1))

Also, the DecimalNumbers might have a lot of decimal places. Limiting to 2 decimal places.

Another consideration: the lines (cos_line and sin_line) can be dashed for better visibility. So in the Line constructor, add stroke_opacity=0.5 or dash_length=0.1.

For example:

cos_line = always_redraw(lambda: DashedLine(
    dot.get_center(), [dot.get_center()[0], 0, 0],
    color=RED,
    dash_length=0.1,
))

Similarly for sin_line.

This makes the projection lines dashed, which might look better.

Also, the dot's size can be adjusted with radius=0.08.

Putting all together:

The code would look something like this:

from manim import *

class SineCosineUnitCircle(Scene):
    def construct(self):
        # Create the unit circle
        circle = Circle(radius=1, color=WHITE)
        axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3,
            y_length=3,
            axis_config={"color": BLUE},
        )

        # Value tracker for the angle theta
        theta = ValueTracker(0)

        # Moving dot on the circle
        dot = always_redraw(lambda: Dot(
            point=[np.cos(theta.get_value()), np.sin(theta.get_value()), 0],
            color=YELLOW,
            radius=0.08,
        ))

        # Projection lines
        cos_line = always_redraw(lambda: DashedLine(
            dot.get_center(), [dot.get_center()[0], 0, 0],
            color=RED,
            dash_length=0.1,
        ))
        sin_line = always_redraw(lambda: DashedLine(
            dot.get_center(), [0, dot.get_center()[1], 0],
            color=GREEN,
            dash_length=0.1,
        ))

        # Labels for cosine and sine values
        cos_tex = MathTex(r"\cos(\theta)").scale(0.8)
        cos_num = DecimalNumber(0, num_decimal_places=2).scale(0.8)
        cos_group = VGroup(cos_tex, cos_num).arrange(RIGHT, buff=0.2)
        cos_group.add_updater(lambda m: m.next_to(cos_line.get_end(), DOWN, buff=0.1))
        cos_num.add_updater(lambda m: m.set_value(np.cos(theta.get_value())))

        sin_tex = MathTex(r"\sin(\theta)").scale(0.8)
        sin_num = DecimalNumber(0, num_decimal_places=2).scale(0.8)
        sin_group = VGroup(sin_tex, sin_num).arrange(RIGHT, buff=0.2)
        sin_group.add_updater(lambda m: m.next_to(sin_line.get_end(), LEFT, buff=0.1))
        sin_num.add_updater(lambda m: m.set_value(np.sin(theta.get_value())))

        # Adding all elements to the scene
        self.add(circle, axes)
        self.add(dot, cos_line, sin_line)
        self.add(cos_group, sin_group)

        # Animate theta from 0 to 2*PI
        self.play(theta.animate.set_value(2 * PI), run_time=5, rate_func=linear)

        # Keep the final frame displayed
        self.wait(2)

This code should create a scene with a unit circle, axes, a moving dot, dashed projection lines for sine and cosine, and updating labels showing their current values. The animation runs for 5 seconds, making one full rotation, and then waits for 2 seconds at the end.

Potential improvements:

- Adding arrows or annotations to indicate the angle theta. For example, an arc from the positive x-axis to the dot, with a theta label.
- Differentiating the colors of sine and cosine labels to match their projection lines (red for cosine, green for sine).
- Adding a trace of the sine and cosine values over time as graphs next to the circle, but the problem statement doesn't mention that, so maybe not necessary.
- Adjusting the positioning of the labels if they overlap with other elements.

Testing this code should show the desired animation. If there are any issues, like labels not moving correctly or lines not updating, it might be due to the order of adding updaters or the way positions are calculated. Also, ensuring that the axes are properly scaled to the unit circle.
</think>

Here's a Manim scene that illustrates the relationship between sine and cosine on a unit circle with animated projections and dynamic labels:

```python
from manim import *
import numpy as np

class SineCosineUnitCircle(Scene):
    def construct(self):
        # Create the unit circle and coordinate axes
        circle = Circle(radius=1, color=WHITE)
        axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3,
            y_length=3,
            axis_config={"color": BLUE},
        )
        
        # Angle tracker and moving point
        theta = ValueTracker(0)
        dot = always_redraw(lambda: Dot(
            point=[np.cos(theta.get_value()), np.sin(theta.get_value()), 0],
            color=YELLOW,
            radius=0.08
        ))
        
        # Projection lines (cosine: red, sine: green)
        cos_line = always_redraw(lambda: DashedLine(
            dot.get_center(), [dot.get_center()[0], 0, 0],
            color=RED, dash_length=0.1
        ))
        sin_line = always_redraw(lambda: DashedLine(
            dot.get_center(), [0, dot.get_center()[1], 0],
            color=GREEN, dash_length=0.1
        ))
        
        # Dynamic labels with values
        cos_label = VGroup(
            MathTex(r"\cos(\theta)=", color=RED).scale(0.7),
            DecimalNumber(num_decimal_places=2).scale(0.7)
        ).arrange(RIGHT)
        cos_label.add_updater(lambda m: m.next_to(cos_line.get_end(), DOWN, buff=0.1))
        cos_label[1].add_updater(lambda m: m.set_value(np.cos(theta.get_value())))
        
        sin_label = VGroup(
            MathTex(r"\sin(\theta)=", color=GREEN).scale(0.7),
            DecimalNumber(num_decimal_places=2).scale(0.7)
        ).arrange(RIGHT)
        sin_label.add_updater(lambda m: m.next_to(sin_line.get_end(), LEFT, buff=0.1))
        sin_label[1].add_updater(lambda m: m.set_value(np.sin(theta.get_value())))
        
        # Angle indicator
        arc = always_redraw(lambda: Arc(
            radius=0.4,
            start_angle=0,
            angle=theta.get_value(),
            color=YELLOW
        ))
        theta_label = always_redraw(lambda: MathTex(r"\theta", color=YELLOW)
            .next_to(arc.point_from_proportion(0.5), UR, buff=0.1).scale(0.7))
        
        # Add all elements to the scene
        self.add(circle, axes, arc, theta_label)
        self.add(dot, cos_line, sin_line)
        self.add(cos_label, sin_label)
        
        # Animate the point moving around the circle
        self.play(
            theta.animate.set_value(2 * PI),
            run_time=8,
            rate_func=linear
        )
        self.wait(1)
```

This scene includes:

1. A unit circle with coordinate axes
2. A yellow dot moving around the circumference
3. Dashed projection lines (red for cosine, green for sine)
4. Real-time updating numeric labels for sine and cosine values
5. A yellow arc showing the current angle θ
6. Smooth animation lasting 8 seconds for a full rotation

The projections and labels update continuously as the point moves around the circle, demonstrating the relationship between the angle, its sine, and cosine values. The cosine value tracks the x-coordinate (horizontal projection) while the sine value tracks the y-coordinate (vertical projection).

Key features:
- Dashed projection lines that follow the moving point
- Numeric labels that update smoothly with trigonometric values
- Angle indicator showing the current θ value
- Color-coding for different elements (red for cosine, green for sine)
- Smooth animation that completes a full 2π rotation

To run this animation, save it as a Python file and execute with Manim:
```bash
manim -pql sine_cosine.py SineCosineUnitCircle
```