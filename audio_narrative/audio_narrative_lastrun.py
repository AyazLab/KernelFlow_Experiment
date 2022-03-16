#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 02, 2022, at 13:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'video_narrative'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\audio_narrative\\audio_narrative_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "initial_exp_code"
initial_exp_codeClock = core.Clock()
import os
# path to kernel socket module
cwd = os.getcwd()
os.chdir("..")
kernel_socket_path = os.path.join(os.getcwd(), "main", "kernel_socket")
os.chdir(cwd)
import sys
sys.path.insert(0, kernel_socket_path)
from kernel_socket import Marker
marker = Marker()

marker.send_marker("experiment_start")

# Initialize components for Routine "pieman_instructions"
pieman_instructionsClock = core.Clock()
instructions1_text = visual.TextStim(win=win, name='instructions1_text',
    text='This is the "Pie-man" audio clip.\n\nPlease pay attention to the story.\n\nPress SPACE when you are ready to listen the clip.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions1_resp = keyboard.Keyboard()

# Initialize components for Routine "pieman_recall_details"
pieman_recall_detailsClock = core.Clock()
pieman_details_text = visual.TextStim(win=win, name='pieman_details_text',
    text='Please recall details from the "Pie-man" clip.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
pieman_details_resp = keyboard.Keyboard()

# Initialize components for Routine "unrehearsed_instructions"
unrehearsed_instructionsClock = core.Clock()
instructions2_text = visual.TextStim(win=win, name='instructions2_text',
    text='This is the "Unreheared real-life story" audio clip.\n\nPlease pay attention to the story.\n\nPress SPACE when you are ready to listen to the clip.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions2_resp = keyboard.Keyboard()

# Initialize components for Routine "unrehearsed_audio"
unrehearsed_audioClock = core.Clock()
unrehearsed_clip = sound.Sound('audio_clips/audio_1.m4a', secs=-1, stereo=True, hamming=True,
    name='unrehearsed_clip')
unrehearsed_clip.setVolume(1.0)
unrehearsed_cross = visual.ShapeStim(
    win=win, name='unrehearsed_cross', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "unrehearsed_recall_details"
unrehearsed_recall_detailsClock = core.Clock()
unrehearsed_details_text = visual.TextStim(win=win, name='unrehearsed_details_text',
    text='Please recall details from the "Unrehearsed real-life story" clip.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
unrehearsed_details_resp = keyboard.Keyboard()

# Initialize components for Routine "end_experiment_code"
end_experiment_codeClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "initial_exp_code"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
initial_exp_codeComponents = []
for thisComponent in initial_exp_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initial_exp_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initial_exp_code"-------
while continueRoutine:
    # get current time
    t = initial_exp_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initial_exp_codeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initial_exp_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initial_exp_code"-------
for thisComponent in initial_exp_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initial_exp_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pieman_instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions1_resp.keys = []
instructions1_resp.rt = []
_instructions1_resp_allKeys = []
# keep track of which components have finished
pieman_instructionsComponents = [instructions1_text, instructions1_resp]
for thisComponent in pieman_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pieman_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pieman_instructions"-------
while continueRoutine:
    # get current time
    t = pieman_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pieman_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions1_text* updates
    if instructions1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions1_text.frameNStart = frameN  # exact frame index
        instructions1_text.tStart = t  # local t and not account for scr refresh
        instructions1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1_text, 'tStartRefresh')  # time at next scr refresh
        instructions1_text.setAutoDraw(True)
    
    # *instructions1_resp* updates
    waitOnFlip = False
    if instructions1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions1_resp.frameNStart = frameN  # exact frame index
        instructions1_resp.tStart = t  # local t and not account for scr refresh
        instructions1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1_resp, 'tStartRefresh')  # time at next scr refresh
        instructions1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions1_resp.status == STARTED and not waitOnFlip:
        theseKeys = instructions1_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions1_resp_allKeys.extend(theseKeys)
        if len(_instructions1_resp_allKeys):
            instructions1_resp.keys = _instructions1_resp_allKeys[-1].name  # just the last key pressed
            instructions1_resp.rt = _instructions1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pieman_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pieman_instructions"-------
for thisComponent in pieman_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions1_text.started', instructions1_text.tStartRefresh)
thisExp.addData('instructions1_text.stopped', instructions1_text.tStopRefresh)
# check responses
if instructions1_resp.keys in ['', [], None]:  # No response was made
    instructions1_resp.keys = None
thisExp.addData('instructions1_resp.keys',instructions1_resp.keys)
if instructions1_resp.keys != None:  # we had a response
    thisExp.addData('instructions1_resp.rt', instructions1_resp.rt)
thisExp.addData('instructions1_resp.started', instructions1_resp.tStartRefresh)
thisExp.addData('instructions1_resp.stopped', instructions1_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "pieman_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pieman_recall_details"-------
continueRoutine = True
# update component parameters for each repeat
pieman_details_resp.keys = []
pieman_details_resp.rt = []
_pieman_details_resp_allKeys = []
# keep track of which components have finished
pieman_recall_detailsComponents = [pieman_details_text, pieman_details_resp]
for thisComponent in pieman_recall_detailsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pieman_recall_detailsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pieman_recall_details"-------
while continueRoutine:
    # get current time
    t = pieman_recall_detailsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pieman_recall_detailsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pieman_details_text* updates
    if pieman_details_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pieman_details_text.frameNStart = frameN  # exact frame index
        pieman_details_text.tStart = t  # local t and not account for scr refresh
        pieman_details_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pieman_details_text, 'tStartRefresh')  # time at next scr refresh
        pieman_details_text.setAutoDraw(True)
    
    # *pieman_details_resp* updates
    waitOnFlip = False
    if pieman_details_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pieman_details_resp.frameNStart = frameN  # exact frame index
        pieman_details_resp.tStart = t  # local t and not account for scr refresh
        pieman_details_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pieman_details_resp, 'tStartRefresh')  # time at next scr refresh
        pieman_details_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(pieman_details_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(pieman_details_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if pieman_details_resp.status == STARTED and not waitOnFlip:
        theseKeys = pieman_details_resp.getKeys(keyList=['space'], waitRelease=False)
        _pieman_details_resp_allKeys.extend(theseKeys)
        if len(_pieman_details_resp_allKeys):
            pieman_details_resp.keys = _pieman_details_resp_allKeys[-1].name  # just the last key pressed
            pieman_details_resp.rt = _pieman_details_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pieman_recall_detailsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pieman_recall_details"-------
for thisComponent in pieman_recall_detailsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pieman_details_text.started', pieman_details_text.tStartRefresh)
thisExp.addData('pieman_details_text.stopped', pieman_details_text.tStopRefresh)
# check responses
if pieman_details_resp.keys in ['', [], None]:  # No response was made
    pieman_details_resp.keys = None
thisExp.addData('pieman_details_resp.keys',pieman_details_resp.keys)
if pieman_details_resp.keys != None:  # we had a response
    thisExp.addData('pieman_details_resp.rt', pieman_details_resp.rt)
thisExp.addData('pieman_details_resp.started', pieman_details_resp.tStartRefresh)
thisExp.addData('pieman_details_resp.stopped', pieman_details_resp.tStopRefresh)
thisExp.nextEntry()
marker.send_marker("trial_end")
# the Routine "pieman_recall_details" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "unrehearsed_instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions2_resp.keys = []
instructions2_resp.rt = []
_instructions2_resp_allKeys = []
# keep track of which components have finished
unrehearsed_instructionsComponents = [instructions2_text, instructions2_resp]
for thisComponent in unrehearsed_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
unrehearsed_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "unrehearsed_instructions"-------
while continueRoutine:
    # get current time
    t = unrehearsed_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=unrehearsed_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions2_text* updates
    if instructions2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2_text.frameNStart = frameN  # exact frame index
        instructions2_text.tStart = t  # local t and not account for scr refresh
        instructions2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2_text, 'tStartRefresh')  # time at next scr refresh
        instructions2_text.setAutoDraw(True)
    
    # *instructions2_resp* updates
    waitOnFlip = False
    if instructions2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2_resp.frameNStart = frameN  # exact frame index
        instructions2_resp.tStart = t  # local t and not account for scr refresh
        instructions2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2_resp, 'tStartRefresh')  # time at next scr refresh
        instructions2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions2_resp.status == STARTED and not waitOnFlip:
        theseKeys = instructions2_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions2_resp_allKeys.extend(theseKeys)
        if len(_instructions2_resp_allKeys):
            instructions2_resp.keys = _instructions2_resp_allKeys[-1].name  # just the last key pressed
            instructions2_resp.rt = _instructions2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in unrehearsed_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "unrehearsed_instructions"-------
for thisComponent in unrehearsed_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions2_text.started', instructions2_text.tStartRefresh)
thisExp.addData('instructions2_text.stopped', instructions2_text.tStopRefresh)
# check responses
if instructions2_resp.keys in ['', [], None]:  # No response was made
    instructions2_resp.keys = None
thisExp.addData('instructions2_resp.keys',instructions2_resp.keys)
if instructions2_resp.keys != None:  # we had a response
    thisExp.addData('instructions2_resp.rt', instructions2_resp.rt)
thisExp.addData('instructions2_resp.started', instructions2_resp.tStartRefresh)
thisExp.addData('instructions2_resp.stopped', instructions2_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "unrehearsed_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "unrehearsed_audio"-------
continueRoutine = True
# update component parameters for each repeat
unrehearsed_clip.setSound('audio_clips/audio_1.m4a', hamming=True)
unrehearsed_clip.setVolume(1.0, log=False)
# keep track of which components have finished
unrehearsed_audioComponents = [unrehearsed_clip, unrehearsed_cross]
for thisComponent in unrehearsed_audioComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
unrehearsed_audioClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "unrehearsed_audio"-------
while continueRoutine:
    # get current time
    t = unrehearsed_audioClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=unrehearsed_audioClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop unrehearsed_clip
    if unrehearsed_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unrehearsed_clip.frameNStart = frameN  # exact frame index
        unrehearsed_clip.tStart = t  # local t and not account for scr refresh
        unrehearsed_clip.tStartRefresh = tThisFlipGlobal  # on global time
        unrehearsed_clip.play(when=win)  # sync with win flip
    
    # *unrehearsed_cross* updates
    if unrehearsed_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unrehearsed_cross.frameNStart = frameN  # exact frame index
        unrehearsed_cross.tStart = t  # local t and not account for scr refresh
        unrehearsed_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unrehearsed_cross, 'tStartRefresh')  # time at next scr refresh
        unrehearsed_cross.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in unrehearsed_audioComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "unrehearsed_audio"-------
for thisComponent in unrehearsed_audioComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
unrehearsed_clip.stop()  # ensure sound has stopped at end of routine
thisExp.addData('unrehearsed_clip.started', unrehearsed_clip.tStartRefresh)
thisExp.addData('unrehearsed_clip.stopped', unrehearsed_clip.tStopRefresh)
thisExp.addData('unrehearsed_cross.started', unrehearsed_cross.tStartRefresh)
thisExp.addData('unrehearsed_cross.stopped', unrehearsed_cross.tStopRefresh)
# the Routine "unrehearsed_audio" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "unrehearsed_recall_details"-------
continueRoutine = True
# update component parameters for each repeat
unrehearsed_details_resp.keys = []
unrehearsed_details_resp.rt = []
_unrehearsed_details_resp_allKeys = []
# keep track of which components have finished
unrehearsed_recall_detailsComponents = [unrehearsed_details_text, unrehearsed_details_resp]
for thisComponent in unrehearsed_recall_detailsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
unrehearsed_recall_detailsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "unrehearsed_recall_details"-------
while continueRoutine:
    # get current time
    t = unrehearsed_recall_detailsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=unrehearsed_recall_detailsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *unrehearsed_details_text* updates
    if unrehearsed_details_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unrehearsed_details_text.frameNStart = frameN  # exact frame index
        unrehearsed_details_text.tStart = t  # local t and not account for scr refresh
        unrehearsed_details_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unrehearsed_details_text, 'tStartRefresh')  # time at next scr refresh
        unrehearsed_details_text.setAutoDraw(True)
    
    # *unrehearsed_details_resp* updates
    waitOnFlip = False
    if unrehearsed_details_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        unrehearsed_details_resp.frameNStart = frameN  # exact frame index
        unrehearsed_details_resp.tStart = t  # local t and not account for scr refresh
        unrehearsed_details_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(unrehearsed_details_resp, 'tStartRefresh')  # time at next scr refresh
        unrehearsed_details_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(unrehearsed_details_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(unrehearsed_details_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if unrehearsed_details_resp.status == STARTED and not waitOnFlip:
        theseKeys = unrehearsed_details_resp.getKeys(keyList=['space'], waitRelease=False)
        _unrehearsed_details_resp_allKeys.extend(theseKeys)
        if len(_unrehearsed_details_resp_allKeys):
            unrehearsed_details_resp.keys = _unrehearsed_details_resp_allKeys[-1].name  # just the last key pressed
            unrehearsed_details_resp.rt = _unrehearsed_details_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in unrehearsed_recall_detailsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "unrehearsed_recall_details"-------
for thisComponent in unrehearsed_recall_detailsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('unrehearsed_details_text.started', unrehearsed_details_text.tStartRefresh)
thisExp.addData('unrehearsed_details_text.stopped', unrehearsed_details_text.tStopRefresh)
# check responses
if unrehearsed_details_resp.keys in ['', [], None]:  # No response was made
    unrehearsed_details_resp.keys = None
thisExp.addData('unrehearsed_details_resp.keys',unrehearsed_details_resp.keys)
if unrehearsed_details_resp.keys != None:  # we had a response
    thisExp.addData('unrehearsed_details_resp.rt', unrehearsed_details_resp.rt)
thisExp.addData('unrehearsed_details_resp.started', unrehearsed_details_resp.tStartRefresh)
thisExp.addData('unrehearsed_details_resp.stopped', unrehearsed_details_resp.tStopRefresh)
thisExp.nextEntry()
marker.send_marker("trial_end")
# the Routine "unrehearsed_recall_details" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end_experiment_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("experiment_end")
# keep track of which components have finished
end_experiment_codeComponents = []
for thisComponent in end_experiment_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_experiment_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_experiment_code"-------
while continueRoutine:
    # get current time
    t = end_experiment_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_experiment_codeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_experiment_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_experiment_code"-------
for thisComponent in end_experiment_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end_experiment_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
