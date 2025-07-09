#------------------------------------------------------------------------------#

import numpy      as np
import pyqtgraph  as pg
import parameters as par

#------------------------------------------------------------------------------#
class PlotVelocity:

    #--------------------------------------------------------------------------#
    def __init__(self, plot, color):

        plot.setBackground(color)
        plot.setTitle('Velocity')
        plot.setLabel('left',   'Velocity (screens/second)')
        plot.setLabel('bottom', 'Time (seconds)'           )
        plot.showGrid(x=True, y=True)
        plot.setXRange(0, par.PLOT_MAX_T, padding=0)
        plot.setYRange(0, 1,              padding=0)

        pen = pg.mkPen(color=(0, 0, 255), width=2)

        self.plot_velocity_data = plot.plot(
            (0, par.PLOT_MAX_T),
            (0.5, 0.5),
            pen=pen
        )

    #--------------------------------------------------------------------------#
    def update(self, velocity):

        tt = np.arange(0, par.PLOT_MAX_T, 0.1)
        vv = velocity.eval(tt)

        self.plot_velocity_data.setData(tt, vv)

#------------------------------------------------------------------------------#
