# psychopy-eyetracker-tobii

Extension for PsychoPy which adds support for [Tobii](https://www.tobii.com/) 
eyetrackers (via ioHub)

## Supported Devices

Installing this package alongside PsychoPy will enable support for the following 
devices:

* Supported Tobii eye trackers
    
## Installing

Install this package with the following shell command:: 

    pip install psychopy-eyetracker-tobii

You may also use PsychoPy's builtin plugin/package manager to install this 
package.

## Usage

Once the package is installed, PsychoPy will automatically load it when started 
and the `psychopy.iohub.devices.eyetracker.hw.tobii` namespace will contain the
loaded objects.