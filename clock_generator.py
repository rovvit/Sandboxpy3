import cairo
import math

hours, minutes = 15, 45

width =  256
with cairo.SVGSurface("clock.svg", width, width) as surface:
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(2.0)

    border = 2
    ctx.rectangle(border, border, width - 2 * border, width - 2 * border)  # отступы по краям
    ctx.stroke()



    center = width / 2
    radius = width * 0.95 / 2

    ctx.set_source_rgba(0, 0, 0, 1)
    ctx.arc(center, center, radius, 0, 2.0 * math.pi)
    ctx.stroke()

    ctx.arc(center, center, 5, 0, 2 * math.pi)
    ctx.fill()

    for i in range (12):
        tick_length = radius * 0.95
        tick_offset = radius * 0.75

        tick_x_outer = center + tick_length * math.sin(2 * math.pi * (i / 12))
        tick_y_outer = center - tick_length * math.cos(2 * math.pi * (i / 12))

        tick_x_inner = center + tick_offset * math.sin(2 * math.pi * (i / 12))
        tick_y_inner = center - tick_offset * math.cos(2 * math.pi * (i / 12))

        ctx.move_to(tick_x_inner, tick_y_inner)
        ctx.line_to(tick_x_outer, tick_y_outer)
        ctx.set_line_width(1)

        ctx.stroke()

    h_length = radius * 0.64
    ctx.set_line_width(7)
    offset = radius * 0.08

    hx_outer = center + h_length * math.sin(2 * math.pi * (hours / 12 + minutes / 60 / 12)  )
    hy_outer = center - h_length * math.cos(2 * math.pi * (hours / 12 + minutes / 60 / 12))

    hx_inner = center + offset * math.sin(hours * 2 * math.pi / 12)
    hy_inner = center - offset * math.cos(hours * 2 * math.pi / 12)
    ctx.move_to(hx_outer, hy_outer)
    ctx.line_to(hx_inner, hy_inner)
    ctx.stroke()

    m_length = radius * 0.8
    ctx.set_line_width(4)

    mx_outer = center + m_length * math.sin(minutes * 2 * math.pi / 60)
    my_outer = center - m_length * math.cos(minutes * 2 * math.pi / 60)

    mx_inner = center + offset * math.sin(minutes * 2 * math.pi / 60)
    my_inner = center - offset * math.cos(minutes * 2 * math.pi / 60)
    ctx.move_to(mx_outer, my_outer)
    ctx.line_to(mx_inner, my_inner)
    ctx.stroke()



