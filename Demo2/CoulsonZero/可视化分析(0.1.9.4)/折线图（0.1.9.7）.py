from pyecharts import Line, Grid
# 0.1.9.7

import random

attr = ["{}天".format(i) for i in range(1, 31)]
line_top = Line("折线图示例")
line_top.add(
    "最高气温",
    attr,
    [random.randint(20, 100) for i in range(30)],
    mark_point=["max", "min"],
    mark_line=["average"],
    legend_pos="38%",
)
line_bottom = Line()
line_bottom.add(
    "最低气温",
    attr,
    [random.randint(20, 100) for i in range(30)],
    mark_point=["max", "min"],
    mark_line=["average"],
    is_yaxis_inverse=True,
    xaxis_pos="top",
)

grid = Grid() #width=1200,height=700
grid.add(line_top, grid_bottom="60%")
grid.add(line_bottom, grid_top="50%")
grid.render()
