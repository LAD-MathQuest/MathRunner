#------------------------------------------------------------------------------#

import numpy      as np
import pyqtgraph  as pg

from meta import VelocityFunction

PLOT_MAX_T = 5
PLOT_MAX_V = 80

#------------------------------------------------------------------------------#
class PlotVelocity:

    #--------------------------------------------------------------------------#
    def __init__(self, plot, color, velocity: VelocityFunction):

        
        self.plot = plot

        self.velocity = velocity
        self.securityValue = 0.00000000000000000000000000000000000000000000000001

        plot.setBackground(color)
        plot.setTitle('Velocidade')
        plot.setLabel('left',   'Velocidade (porcentagem da tela/segundo)')
        plot.setLabel('bottom', 'Tempo (segundos)')
        plot.showGrid(x=True, y=True)

        plot.setXRange(0, PLOT_MAX_T, padding=0)
        plot.setYRange(0, PLOT_MAX_V, padding=0)

        pen_raw = pg.mkPen(color=(255, 0, 0), width=1.5)
        pen_vel = pg.mkPen(color=(0, 0, 255), width=2.0)

        p_raw = pg.PlotDataItem(np.array((self.securityValue, PLOT_MAX_T)), np.array((5, 5)), pen=pen_raw)
        p_vel = pg.PlotDataItem(np.array((self.securityValue, PLOT_MAX_T)), np.array((5, 5)), pen=pen_vel)

        plot.addItem(p_raw)
        plot.addItem(p_vel)

        self.plot_raw_data = p_raw
        self.plot_vel_data = p_vel

        plot.sigRangeChanged.connect(self.on_range_changed)

    #--------------------------------------------------------------------------#
    def on_range_changed(self, plot, view_range) -> None:

        t_min, t_max = view_range[0]

        if t_min < 0:
            t_min = 0
            t_max = max(t_max, 1)

            plot.sigRangeChanged.disconnect(self.on_range_changed)
            plot.setXRange(t_min, t_max, padding=0)
            plot.sigRangeChanged.connect(self.on_range_changed)

        self.update_data(t_min, t_max)

    #--------------------------------------------------------------------------#
    def update_velocity(self, velocity: VelocityFunction) -> None:

        self.velocity = velocity
        self.update_data(0, PLOT_MAX_T)

    #--------------------------------------------------------------------------#
    def update_data(self, t_min: float, t_max: float) -> None:

        start = max(t_min, self.securityValue)
        tt = np.linspace(start, t_max, 1000)

        raw = self.velocity.eval_raw(tt)
        vel = self.velocity.eval    (tt)

        self.plot_raw_data.setData(tt, raw)
        self.plot_vel_data.setData(tt, vel)

    #--------------------------------------------------------------------------#
    def reset_scales(self) -> None:
        #Reseta os intervalos da visualização para os padrões e atualiza os dados
        #desconecta os sinais temporariamente para evitar ajustes recursivos
        try:
            self.plot.sigRangeChanged.disconnect(self.on_range_changed)
        except Exception:
            pass

        self.plot.setXRange(0, PLOT_MAX_T, padding=0)
        self.plot.setYRange(0, PLOT_MAX_V, padding=0)

        #reconnecta os sinais e atualiza os dados
        self.plot.sigRangeChanged.connect(self.on_range_changed)
        self.update_data(0, PLOT_MAX_T)

#------------------------------------------------------------------------------#
