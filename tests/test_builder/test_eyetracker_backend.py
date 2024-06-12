from psychopy import plugins, experiment


def test_eyetrackerBackendFound():
    """
    Check that the backend for this eyetracker is found by Builder
    """
    # activate plugins
    plugins.activatePlugins()
    # make an experiment
    exp = experiment.Experiment()
    # get the eyetrackers available from its Settings component
    backends = exp.settings.params['eyetracker'].allowedVals
    # make sure this eyetracker is found
    assert 'Tobii Technology' in backends
