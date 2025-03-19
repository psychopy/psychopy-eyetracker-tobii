from psychopy.localization import _translate
from psychopy.experiment import Param
from psychopy.experiment.components.settings.eyetracking import EyetrackerBackend


class TobiiEyetrackerBackend(EyetrackerBackend):
    """Experiment settings for Tobii eyetrackers.
    """
    label = 'Tobii Technology (iohub)'
    key = 'eyetracker.hw.tobii.EyeTracker'

    needsFullscreen = False
    needsCalibration = False

    @classmethod
    def getParams(cls):
        # define order
        order = [
            # runtime settings
            "tbSamplingRate",
            "tbTrackEyes"
        ]

        # network settings
        params = {}
        # runtime settings
        params['tbSamplingRate'] = Param(
            "60", 
            valType='str', 
            inputType="single",
            hint=_translate("Sampling rate in Hz."),
            label=_translate("Sampling rate"), 
            categ="Eyetracking"
        )
        params['tbTrackEyes'] = Param(
            'BINOCULAR', 
            valType='str', 
            inputType="choice",
            allowedVals=['BINOCULAR'],
            hint=_translate("Which eye(s) to track."),
            label=_translate("Track eyes"), 
            categ="Eyetracking"
        )

        return params, order

    @classmethod
    def writeDeviceCode(cls, inits, buff):
        code = (
            "ioConfig[%(eyetracker)s] = {\n"
            "    'name': 'tracker',\n"
            "    'runtime_settings': {\n"
            "        'sampling_rate': %(tbSamplingRate)s,\n"
            "        'track_eyes': %(tbTrackEyes)s,\n"
            "    },\n"
            "}\n"
        )
        buff.writeIndentedLines(code % inits)
