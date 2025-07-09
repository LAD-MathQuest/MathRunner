#------------------------------------------------------------------------------#

import numpy      as np
import pyqtgraph  as pg
import parameters as par

#------------------------------------------------------------------------------#
class PlotTrack:

    #--------------------------------------------------------------------------#
    def __init__(self, plot, color):

        plot.setBackground(color)
        plot.setTitle('Boundary' )
        plot.setLabel('left',   'Boundary (screen fraction)')
        plot.setLabel('bottom', 'Time (seconds)'            )
        plot.showGrid(x=True, y=True)
        plot.setXRange(0, par.PLOT_MAX_X, padding=0)
        plot.setYRange(0, 1,              padding=0)

        pen_min = pg.mkPen(color=(  0, 0, 255), width=2)
        pen_max = pg.mkPen(color=(255, 0, 255), width=2)
        pen_aux = pg.mkPen(None)
        brush   = pg.mkBrush(color=(100, 100, 160))

        p_min = pg.PlotDataItem(np.array((0,par.PLOT_MAX_X)), np.array((0.1, 0.1)), pen=pen_min)
        p_max = pg.PlotDataItem(np.array((0,par.PLOT_MAX_X)), np.array((0.9, 0.9)), pen=pen_max)
        p_aux = pg.PlotDataItem(np.array((0,par.PLOT_MAX_X)), np.array((0.9, 0.9)), pen=pen_aux)
        pfill = pg.FillBetweenItem(p_min, p_aux, brush=brush)

        plot.addItem(p_min)
        plot.addItem(p_max)
        plot.addItem(p_aux)
        plot.addItem(pfill)

        self.plot_boundary_min_data = p_min
        self.plot_boundary_max_data = p_max
        self.plot_boundary_aux_data = p_aux

    #--------------------------------------------------------------------------#
    def update(self, boundary):

        xx     = np.arange(0, par.PLOT_MAX_X, 0.1)
        mm, MM = boundary.eval(xx)

        self.plot_boundary_min_data.setData(xx, mm)
        self.plot_boundary_max_data.setData(xx, MM)

        xx = self.plot_boundary_min_data.xData

        y_aux = np.maximum(self.plot_boundary_min_data.yData,
                           self.plot_boundary_max_data.yData)

        self.plot_boundary_aux_data.setData(xx, y_aux)

#------------------------------------------------------------------------------#
