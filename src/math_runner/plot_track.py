#------------------------------------------------------------------------------#

import numpy      as np
import pyqtgraph  as pg

from meta import BoundaryFunctions

PLOT_MAX_X = 100
PLOT_MAX_F = 100

#------------------------------------------------------------------------------#
class PlotTrack:

    #--------------------------------------------------------------------------#
    def __init__(self, plot, color, boundary: BoundaryFunctions) -> None:

        self.boundary = boundary

        plot.setBackground(color)
        plot.setTitle('Fronteiras' )
        plot.setLabel('left',   'Fronteiras (porcentagem da tela)')
        plot.setLabel('bottom', 'Porcentagem da tela')
        plot.showGrid(x=True, y=True)

        plot.setXRange(0, PLOT_MAX_X, padding=0)
        plot.setYRange(0, PLOT_MAX_F, padding=0)

        pen_raw = pg.mkPen(color=(255, 0,   0), width=1.5)
        pen_min = pg.mkPen(color=(  0, 0, 255), width=2.0)
        pen_max = pg.mkPen(color=(255, 0, 255), width=2.0)
        pen_aux = pg.mkPen(None)
        brush   = pg.mkBrush(color=(100, 100, 160))

        p_min_raw = pg.PlotDataItem(np.array((0, PLOT_MAX_X)), np.array((10, 10)), pen=pen_raw)
        p_max_raw = pg.PlotDataItem(np.array((0, PLOT_MAX_X)), np.array((90, 90)), pen=pen_raw)
        p_min     = pg.PlotDataItem(np.array((0, PLOT_MAX_X)), np.array((10, 10)), pen=pen_min)
        p_max     = pg.PlotDataItem(np.array((0, PLOT_MAX_X)), np.array((90, 90)), pen=pen_max)
        p_aux     = pg.PlotDataItem(np.array((0, PLOT_MAX_X)), np.array((90, 90)), pen=pen_aux)
        pfill     = pg.FillBetweenItem(p_min, p_aux, brush=brush)

        plot.addItem(p_min_raw)
        plot.addItem(p_max_raw)
        plot.addItem(p_min)
        plot.addItem(p_max)
        plot.addItem(p_aux)
        plot.addItem(pfill)

        self.plot_boundary_min_data_raw = p_min_raw
        self.plot_boundary_max_data_raw = p_max_raw
        self.plot_boundary_min_data     = p_min
        self.plot_boundary_max_data     = p_max
        self.plot_boundary_aux_data     = p_aux

        plot.sigRangeChanged.connect(self.on_range_changed)

    #--------------------------------------------------------------------------#
    def on_range_changed(self, plot, view_range) -> None:

        x_min, x_max = view_range[0]

        if x_min < 0:
            x_min = 0
            x_max = max(x_max, 1)

            plot.sigRangeChanged.disconnect(self.on_range_changed)
            plot.setXRange(x_min, x_max, padding=0)
            plot.sigRangeChanged.connect(self.on_range_changed)

        self.update_data(x_min, x_max)

    #--------------------------------------------------------------------------#
    def update_boundary(self, boundary: BoundaryFunctions) -> None:

        self.boundary = boundary
        self.update_data(0, PLOT_MAX_X)

    #--------------------------------------------------------------------------#
    def update_data(self, x_min: float, x_max: float) -> None:

        xx = np.linspace(x_min, x_max, 1000)

        fmin_raw = self.boundary.eval_min_raw(xx)
        fmax_raw = self.boundary.eval_max_raw(xx)
        fmin     = self.boundary.eval_min    (xx)
        fmax     = self.boundary.eval_max    (xx)

        self.plot_boundary_min_data_raw.setData(xx, fmin_raw)
        self.plot_boundary_max_data_raw.setData(xx, fmax_raw)
        self.plot_boundary_min_data.    setData(xx, fmin    )
        self.plot_boundary_max_data.    setData(xx, fmax    )

        xx = self.plot_boundary_min_data.xData

        y_aux = np.maximum(self.plot_boundary_min_data.yData,
                           self.plot_boundary_max_data.yData)

        self.plot_boundary_aux_data.setData(xx, y_aux)

#------------------------------------------------------------------------------#
