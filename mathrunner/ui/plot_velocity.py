#------------------------------------------------------------------------------#

import numpy      as np
import pyqtgraph  as pg
import parameters as par

#------------------------------------------------------------------------------#
class PlotVelocity:

    #--------------------------------------------------------------------------#
    def __init__(self, plot, color, velocity):
        
        self.velocity = velocity

        plot.setBackground(color)
        plot.setTitle('Velocity')
        plot.setLabel('left',   'Velocity (screens/second)')
        plot.setLabel('bottom', 'Time (seconds)'           )
        plot.showGrid(x=True, y=True)

        plot.setXRange(0, par.PLOT_MAX_T, padding=0)
        plot.setYRange(0, 50,             padding=0)

        pen_raw = pg.mkPen(color=(255, 0, 0), width=1.5)
        pen_vel = pg.mkPen(color=(0, 0, 255), width=2.0)

        p_raw = pg.PlotDataItem(np.array((0,par.PLOT_MAX_T)), np.array((5, 5)), pen=pen_raw)
        p_vel = pg.PlotDataItem(np.array((0,par.PLOT_MAX_T)), np.array((5, 5)), pen=pen_vel)

        plot.addItem(p_raw)
        plot.addItem(p_vel)

        self.plot_raw_data = p_raw
        self.plot_vel_data = p_vel

        plot.sigRangeChanged.connect(self.on_range_changed)

    #--------------------------------------------------------------------------#
    def on_range_changed(self, plot, view_range):

        t_min, t_max = view_range[0]

        if t_min < 0:
            t_min = 0
            t_max = max(t_max, 1)
            
            plot.sigRangeChanged.disconnect(self.on_range_changed)
            plot.setXRange(t_min, t_max, padding=0)
            plot.sigRangeChanged.connect(self.on_range_changed)
        
        self.update_data(t_min, t_max)

    #--------------------------------------------------------------------------#
    def update_velocity(self, velocity) -> None:

        self.velocity = velocity
        self.update_data(0, par.PLOT_MAX_T)

    #--------------------------------------------------------------------------#
    def update_data(self, t_min, t_max) -> None:
        
        tt = np.linspace(t_min, t_max, 1000)

        raw = self.velocity.eval_raw(tt)
        vel = self.velocity.eval    (tt)

        self.plot_raw_data.setData(tt, raw)
        self.plot_vel_data.setData(tt, vel)

#------------------------------------------------------------------------------#
