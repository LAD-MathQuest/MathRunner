size(16cm, 8cm, IgnoreAspect);

import "./utils.ah" as utils;

pen text = black + fontsize(14pt);

real x_min = -1;
real x_max =  5;
real y_min = -10;
real y_max =  80;

draw_axes(x_min, x_max, 1, y_min, y_max, 10);

real f(real x) { return 40 + 20*sin(x); }

draw(graph(f, 0, x_max), pens[0]);

label("$v(t) = 40 + 20\,\mbox{sen}(t)$ \texttt{= 40 + 20*sen(t)}", (0.1, 72), align=NE, p=text );

clip_to_axis();
