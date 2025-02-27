from krave.experiment.task import Task
from krave.experiment.hardware_test import PiTest
from krave import utils


if __name__ == '__main__':
    # PiTest("RZ001", "exp1").test_visual_with_lick(600, 300)
    # PiTest("RZ001", "exp1").test_visual_cue(600, 300)
    # PiTest("RZ001", "exp1").test_water(iterations=50, open_time=0.04, cool_time=0.2)
    # PiTest("RZ002", "exp1").lick_validation(n_licks=10, time_limit=30)
    # PiTest("RZ001", "exp1").test_trigger()
    # Task("RZ001", "exp1", 'shaping2', record=True, forward_file=True).run()
    Task("RZ001", "exp1", 'shaping1', record=True, forward_file=False).run()
    Task("RZ001", "exp1", 'shaping2', record=True, forward_file=False).end()
