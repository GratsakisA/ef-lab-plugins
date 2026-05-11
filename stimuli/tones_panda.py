from ethopy.stimuli.panda import Objects, Panda
import numpy as np


class TonesPanda(Panda):
    """ This class handles the presentation of Objects (Panda) and tone stimuli"""

    def __init__(self):
        super().__init__()
        self.cond_tables = ['Tones', 'Panda', 'Panda.Object', 'Panda.Environment', 'Panda.Light', 'Panda.Movie']
        self.required_fields = ['tone_duration', 'tone_frequency', 'obj_id', 'obj_dur']
        self.default_key = {
            'background_color'  : (0, 0, 0),
            'ambient_color'     : (0.1, 0.1, 0.1, 1),
            'light_idx'         : (1, 2),
            'tone_pulse_freq'   : 0,
            'tone_volume'       : 50,
            'light_color'       : (np.array([0.7, 0.7, 0.7, 1]), np.array([0.2, 0.2, 0.2, 1])),
            'light_dir'         : (np.array([0, -20, 0]), np.array([180, -20, 0])),
            'obj_pos_x'         : 0,
            'obj_pos_y'         : 0,
            'obj_mag'           : .5,
            'obj_rot'           : 0,
            'obj_tilt'          : 0,
            'obj_yaw'           : 0,
            'obj_delay'         : 0,
            'obj_occluder'      : 0,
            'perspective'       : 0
        }

    def start(self):
        tone_frequency = self.curr_cond['tone_frequency']
        tone_volume = self.curr_cond['tone_volume']
        tone_pulse_freq = self.curr_cond['tone_pulse_freq']
        if 0 < self.curr_cond['tone_pulse_freq'] < 10:
            raise ValueError('Tone pulse frequency cannot be between zero and 10Hz (not including)')
        self.exp.interface.give_sound(tone_frequency, tone_volume, tone_pulse_freq)
        super().start()

    def stop(self):
        self.log_stop()
        self.in_operation = False
        self.exp.interface.stop_sound()
        super().stop()
        
