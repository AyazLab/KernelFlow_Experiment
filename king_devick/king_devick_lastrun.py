#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 28, 2022, at 16:33
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
expName = 'king_devick'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\king_devick\\king_devick_lastrun.py',
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

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='This is the King Devick experiment. \n\nPress SPACE to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "demo_card_instructions"
demo_card_instructionsClock = core.Clock()
demo_instructions_text = visual.TextStim(win=win, name='demo_instructions_text',
    text='This is the Demonstration card. \n\nRead the lines of numbers left to right as quickly as you can without mistakes. If you do make a mistake, please continue reading the numbers. \n\nPress SPACE to begin. Press SPACE again as soon as you finish reading all numbers.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demo_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "demo_card"
demo_cardClock = core.Clock()
demo_image = visual.ImageStim(
    win=win,
    name='demo_image', 
    image='king_devick_stimuli/demo_card.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
demo_resp = keyboard.Keyboard()

# Initialize components for Routine "post_demo_code"
post_demo_codeClock = core.Clock()

# Initialize components for Routine "test1_card_instructions"
test1_card_instructionsClock = core.Clock()
test1_instructions_text = visual.TextStim(win=win, name='test1_instructions_text',
    text='This is the Test 1 card. \n\nRead the lines of numbers left to right as quickly as you can without mistakes. If you do make a mistake, please continue reading the numbers. \n\nPress SPACE to begin. Press SPACE again as soon as you finish reading all numbers.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test1_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "test1_card"
test1_cardClock = core.Clock()
marker.send_marker("stimuli_start")
test1_image = visual.ImageStim(
    win=win,
    name='test1_image', 
    image='king_devick_stimuli/test1_card.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
test1_resp = keyboard.Keyboard()

# Initialize components for Routine "post_stimuli_code"
post_stimuli_codeClock = core.Clock()

# Initialize components for Routine "test2_card_instructions"
test2_card_instructionsClock = core.Clock()
test2_instructions_text = visual.TextStim(win=win, name='test2_instructions_text',
    text='This is the Test 2 card. \n\nRead the lines of numbers left to right as quickly as you can without mistakes. If you do make a mistake, please continue reading the numbers. \n\nPress SPACE to begin. Press SPACE again as soon as you finish reading all numbers.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test2_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "test2_card"
test2_cardClock = core.Clock()
test2_image = visual.ImageStim(
    win=win,
    name='test2_image', 
    image='king_devick_stimuli/test2_card.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
test2_resp = keyboard.Keyboard()

# Initialize components for Routine "post_stimuli_code"
post_stimuli_codeClock = core.Clock()

# Initialize components for Routine "test3_card_instructions"
test3_card_instructionsClock = core.Clock()
test3_instructions_text = visual.TextStim(win=win, name='test3_instructions_text',
    text='This is the Test 3 card. \n\nRead the lines of numbers left to right as quickly as you can without mistakes. If you do make a mistake, please continue reading the numbers. \n\nPress SPACE to begin. Press SPACE again as soon as you finish reading all numbers.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
test3_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "test3_card"
test3_cardClock = core.Clock()
marker.send_marker("stimuli_start")
test3_image = visual.ImageStim(
    win=win,
    name='test3_image', 
    image='king_devick_stimuli/test3_card.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
test3_resp = keyboard.Keyboard()

# Initialize components for Routine "post_stimuli_code"
post_stimuli_codeClock = core.Clock()

# Initialize components for Routine "experiment_end_code"
experiment_end_codeClock = core.Clock()

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

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions_resp.keys = []
instructions_resp.rt = []
_instructions_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instructions_text, instructions_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    
    # *instructions_resp* updates
    if instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_resp.frameNStart = frameN  # exact frame index
        instructions_resp.tStart = t  # local t and not account for scr refresh
        instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_resp, 'tStartRefresh')  # time at next scr refresh
        instructions_resp.status = STARTED
        # keyboard checking is just starting
        instructions_resp.clock.reset()  # now t=0
    if instructions_resp.status == STARTED:
        theseKeys = instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions_resp_allKeys.extend(theseKeys)
        if len(_instructions_resp_allKeys):
            instructions_resp.keys = _instructions_resp_allKeys[-1].name  # just the last key pressed
            instructions_resp.rt = _instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_card_instructions"-------
continueRoutine = True
# update component parameters for each repeat
demo_instructions_resp.keys = []
demo_instructions_resp.rt = []
_demo_instructions_resp_allKeys = []
# keep track of which components have finished
demo_card_instructionsComponents = [demo_instructions_text, demo_instructions_resp]
for thisComponent in demo_card_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_card_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_card_instructions"-------
while continueRoutine:
    # get current time
    t = demo_card_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_card_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo_instructions_text* updates
    if demo_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_instructions_text.frameNStart = frameN  # exact frame index
        demo_instructions_text.tStart = t  # local t and not account for scr refresh
        demo_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_instructions_text, 'tStartRefresh')  # time at next scr refresh
        demo_instructions_text.setAutoDraw(True)
    
    # *demo_instructions_resp* updates
    if demo_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_instructions_resp.frameNStart = frameN  # exact frame index
        demo_instructions_resp.tStart = t  # local t and not account for scr refresh
        demo_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        demo_instructions_resp.status = STARTED
        # keyboard checking is just starting
        demo_instructions_resp.clock.reset()  # now t=0
    if demo_instructions_resp.status == STARTED:
        theseKeys = demo_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _demo_instructions_resp_allKeys.extend(theseKeys)
        if len(_demo_instructions_resp_allKeys):
            demo_instructions_resp.keys = _demo_instructions_resp_allKeys[-1].name  # just the last key pressed
            demo_instructions_resp.rt = _demo_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_card_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_card_instructions"-------
for thisComponent in demo_card_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "demo_card_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo_card"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("practice_start")
demo_resp.keys = []
demo_resp.rt = []
_demo_resp_allKeys = []
# keep track of which components have finished
demo_cardComponents = [demo_image, demo_resp]
for thisComponent in demo_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demo_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demo_card"-------
while continueRoutine:
    # get current time
    t = demo_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demo_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo_image* updates
    if demo_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_image.frameNStart = frameN  # exact frame index
        demo_image.tStart = t  # local t and not account for scr refresh
        demo_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_image, 'tStartRefresh')  # time at next scr refresh
        demo_image.setAutoDraw(True)
    
    # *demo_resp* updates
    waitOnFlip = False
    if demo_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_resp.frameNStart = frameN  # exact frame index
        demo_resp.tStart = t  # local t and not account for scr refresh
        demo_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_resp, 'tStartRefresh')  # time at next scr refresh
        demo_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demo_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demo_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demo_resp.status == STARTED and not waitOnFlip:
        theseKeys = demo_resp.getKeys(keyList=['space'], waitRelease=False)
        _demo_resp_allKeys.extend(theseKeys)
        if len(_demo_resp_allKeys):
            demo_resp.keys = _demo_resp_allKeys[-1].name  # just the last key pressed
            demo_resp.rt = _demo_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo_card"-------
for thisComponent in demo_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('demo_image.started', demo_image.tStartRefresh)
thisExp.addData('demo_image.stopped', demo_image.tStopRefresh)
# check responses
if demo_resp.keys in ['', [], None]:  # No response was made
    demo_resp.keys = None
thisExp.addData('demo_resp.keys',demo_resp.keys)
if demo_resp.keys != None:  # we had a response
    thisExp.addData('demo_resp.rt', demo_resp.rt)
thisExp.addData('demo_resp.started', demo_resp.tStartRefresh)
thisExp.addData('demo_resp.stopped', demo_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "demo_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "post_demo_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("practice_end")
# keep track of which components have finished
post_demo_codeComponents = []
for thisComponent in post_demo_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_demo_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "post_demo_code"-------
while continueRoutine:
    # get current time
    t = post_demo_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_demo_codeClock)
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
    for thisComponent in post_demo_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_demo_code"-------
for thisComponent in post_demo_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "post_demo_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test1_card_instructions"-------
continueRoutine = True
# update component parameters for each repeat
test1_instructions_resp.keys = []
test1_instructions_resp.rt = []
_test1_instructions_resp_allKeys = []
# keep track of which components have finished
test1_card_instructionsComponents = [test1_instructions_text, test1_instructions_resp]
for thisComponent in test1_card_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test1_card_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test1_card_instructions"-------
while continueRoutine:
    # get current time
    t = test1_card_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test1_card_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test1_instructions_text* updates
    if test1_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1_instructions_text.frameNStart = frameN  # exact frame index
        test1_instructions_text.tStart = t  # local t and not account for scr refresh
        test1_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1_instructions_text, 'tStartRefresh')  # time at next scr refresh
        test1_instructions_text.setAutoDraw(True)
    
    # *test1_instructions_resp* updates
    if test1_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1_instructions_resp.frameNStart = frameN  # exact frame index
        test1_instructions_resp.tStart = t  # local t and not account for scr refresh
        test1_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        test1_instructions_resp.status = STARTED
        # keyboard checking is just starting
        test1_instructions_resp.clock.reset()  # now t=0
    if test1_instructions_resp.status == STARTED:
        theseKeys = test1_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _test1_instructions_resp_allKeys.extend(theseKeys)
        if len(_test1_instructions_resp_allKeys):
            test1_instructions_resp.keys = _test1_instructions_resp_allKeys[-1].name  # just the last key pressed
            test1_instructions_resp.rt = _test1_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test1_card_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test1_card_instructions"-------
for thisComponent in test1_card_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test1_card_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test1_card"-------
continueRoutine = True
# update component parameters for each repeat
test1_resp.keys = []
test1_resp.rt = []
_test1_resp_allKeys = []
# keep track of which components have finished
test1_cardComponents = [test1_image, test1_resp]
for thisComponent in test1_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test1_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test1_card"-------
while continueRoutine:
    # get current time
    t = test1_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test1_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test1_image* updates
    if test1_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1_image.frameNStart = frameN  # exact frame index
        test1_image.tStart = t  # local t and not account for scr refresh
        test1_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1_image, 'tStartRefresh')  # time at next scr refresh
        test1_image.setAutoDraw(True)
    
    # *test1_resp* updates
    waitOnFlip = False
    if test1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test1_resp.frameNStart = frameN  # exact frame index
        test1_resp.tStart = t  # local t and not account for scr refresh
        test1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test1_resp, 'tStartRefresh')  # time at next scr refresh
        test1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test1_resp.status == STARTED and not waitOnFlip:
        theseKeys = test1_resp.getKeys(keyList=['space'], waitRelease=False)
        _test1_resp_allKeys.extend(theseKeys)
        if len(_test1_resp_allKeys):
            test1_resp.keys = _test1_resp_allKeys[-1].name  # just the last key pressed
            test1_resp.rt = _test1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test1_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test1_card"-------
for thisComponent in test1_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test1_image.started', test1_image.tStartRefresh)
thisExp.addData('test1_image.stopped', test1_image.tStopRefresh)
# check responses
if test1_resp.keys in ['', [], None]:  # No response was made
    test1_resp.keys = None
thisExp.addData('test1_resp.keys',test1_resp.keys)
if test1_resp.keys != None:  # we had a response
    thisExp.addData('test1_resp.rt', test1_resp.rt)
thisExp.addData('test1_resp.started', test1_resp.tStartRefresh)
thisExp.addData('test1_resp.stopped', test1_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "test1_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "post_stimuli_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("stimuli_end")
# keep track of which components have finished
post_stimuli_codeComponents = []
for thisComponent in post_stimuli_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_stimuli_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "post_stimuli_code"-------
while continueRoutine:
    # get current time
    t = post_stimuli_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_stimuli_codeClock)
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
    for thisComponent in post_stimuli_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_stimuli_code"-------
for thisComponent in post_stimuli_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "post_stimuli_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test2_card_instructions"-------
continueRoutine = True
# update component parameters for each repeat
test2_instructions_resp.keys = []
test2_instructions_resp.rt = []
_test2_instructions_resp_allKeys = []
# keep track of which components have finished
test2_card_instructionsComponents = [test2_instructions_text, test2_instructions_resp]
for thisComponent in test2_card_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test2_card_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test2_card_instructions"-------
while continueRoutine:
    # get current time
    t = test2_card_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test2_card_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test2_instructions_text* updates
    if test2_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test2_instructions_text.frameNStart = frameN  # exact frame index
        test2_instructions_text.tStart = t  # local t and not account for scr refresh
        test2_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2_instructions_text, 'tStartRefresh')  # time at next scr refresh
        test2_instructions_text.setAutoDraw(True)
    
    # *test2_instructions_resp* updates
    if test2_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test2_instructions_resp.frameNStart = frameN  # exact frame index
        test2_instructions_resp.tStart = t  # local t and not account for scr refresh
        test2_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        test2_instructions_resp.status = STARTED
        # keyboard checking is just starting
        test2_instructions_resp.clock.reset()  # now t=0
    if test2_instructions_resp.status == STARTED:
        theseKeys = test2_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _test2_instructions_resp_allKeys.extend(theseKeys)
        if len(_test2_instructions_resp_allKeys):
            test2_instructions_resp.keys = _test2_instructions_resp_allKeys[-1].name  # just the last key pressed
            test2_instructions_resp.rt = _test2_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test2_card_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test2_card_instructions"-------
for thisComponent in test2_card_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test2_card_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test2_card"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("stimuli_start")
test2_resp.keys = []
test2_resp.rt = []
_test2_resp_allKeys = []
# keep track of which components have finished
test2_cardComponents = [test2_image, test2_resp]
for thisComponent in test2_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test2_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test2_card"-------
while continueRoutine:
    # get current time
    t = test2_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test2_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test2_image* updates
    if test2_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test2_image.frameNStart = frameN  # exact frame index
        test2_image.tStart = t  # local t and not account for scr refresh
        test2_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2_image, 'tStartRefresh')  # time at next scr refresh
        test2_image.setAutoDraw(True)
    
    # *test2_resp* updates
    waitOnFlip = False
    if test2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test2_resp.frameNStart = frameN  # exact frame index
        test2_resp.tStart = t  # local t and not account for scr refresh
        test2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test2_resp, 'tStartRefresh')  # time at next scr refresh
        test2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test2_resp.status == STARTED and not waitOnFlip:
        theseKeys = test2_resp.getKeys(keyList=['space'], waitRelease=False)
        _test2_resp_allKeys.extend(theseKeys)
        if len(_test2_resp_allKeys):
            test2_resp.keys = _test2_resp_allKeys[-1].name  # just the last key pressed
            test2_resp.rt = _test2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test2_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test2_card"-------
for thisComponent in test2_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test2_image.started', test2_image.tStartRefresh)
thisExp.addData('test2_image.stopped', test2_image.tStopRefresh)
# check responses
if test2_resp.keys in ['', [], None]:  # No response was made
    test2_resp.keys = None
thisExp.addData('test2_resp.keys',test2_resp.keys)
if test2_resp.keys != None:  # we had a response
    thisExp.addData('test2_resp.rt', test2_resp.rt)
thisExp.addData('test2_resp.started', test2_resp.tStartRefresh)
thisExp.addData('test2_resp.stopped', test2_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "test2_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "post_stimuli_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("stimuli_end")
# keep track of which components have finished
post_stimuli_codeComponents = []
for thisComponent in post_stimuli_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_stimuli_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "post_stimuli_code"-------
while continueRoutine:
    # get current time
    t = post_stimuli_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_stimuli_codeClock)
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
    for thisComponent in post_stimuli_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_stimuli_code"-------
for thisComponent in post_stimuli_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "post_stimuli_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test3_card_instructions"-------
continueRoutine = True
# update component parameters for each repeat
test3_instructions_resp.keys = []
test3_instructions_resp.rt = []
_test3_instructions_resp_allKeys = []
# keep track of which components have finished
test3_card_instructionsComponents = [test3_instructions_text, test3_instructions_resp]
for thisComponent in test3_card_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test3_card_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test3_card_instructions"-------
while continueRoutine:
    # get current time
    t = test3_card_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test3_card_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test3_instructions_text* updates
    if test3_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test3_instructions_text.frameNStart = frameN  # exact frame index
        test3_instructions_text.tStart = t  # local t and not account for scr refresh
        test3_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3_instructions_text, 'tStartRefresh')  # time at next scr refresh
        test3_instructions_text.setAutoDraw(True)
    
    # *test3_instructions_resp* updates
    if test3_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test3_instructions_resp.frameNStart = frameN  # exact frame index
        test3_instructions_resp.tStart = t  # local t and not account for scr refresh
        test3_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        test3_instructions_resp.status = STARTED
        # keyboard checking is just starting
        test3_instructions_resp.clock.reset()  # now t=0
    if test3_instructions_resp.status == STARTED:
        theseKeys = test3_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _test3_instructions_resp_allKeys.extend(theseKeys)
        if len(_test3_instructions_resp_allKeys):
            test3_instructions_resp.keys = _test3_instructions_resp_allKeys[-1].name  # just the last key pressed
            test3_instructions_resp.rt = _test3_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test3_card_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test3_card_instructions"-------
for thisComponent in test3_card_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "test3_card_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test3_card"-------
continueRoutine = True
# update component parameters for each repeat
test3_resp.keys = []
test3_resp.rt = []
_test3_resp_allKeys = []
# keep track of which components have finished
test3_cardComponents = [test3_image, test3_resp]
for thisComponent in test3_cardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test3_cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test3_card"-------
while continueRoutine:
    # get current time
    t = test3_cardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test3_cardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *test3_image* updates
    if test3_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test3_image.frameNStart = frameN  # exact frame index
        test3_image.tStart = t  # local t and not account for scr refresh
        test3_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3_image, 'tStartRefresh')  # time at next scr refresh
        test3_image.setAutoDraw(True)
    
    # *test3_resp* updates
    waitOnFlip = False
    if test3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test3_resp.frameNStart = frameN  # exact frame index
        test3_resp.tStart = t  # local t and not account for scr refresh
        test3_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test3_resp, 'tStartRefresh')  # time at next scr refresh
        test3_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(test3_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(test3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if test3_resp.status == STARTED and not waitOnFlip:
        theseKeys = test3_resp.getKeys(keyList=['space'], waitRelease=False)
        _test3_resp_allKeys.extend(theseKeys)
        if len(_test3_resp_allKeys):
            test3_resp.keys = _test3_resp_allKeys[-1].name  # just the last key pressed
            test3_resp.rt = _test3_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test3_cardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test3_card"-------
for thisComponent in test3_cardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test3_image.started', test3_image.tStartRefresh)
thisExp.addData('test3_image.stopped', test3_image.tStopRefresh)
# check responses
if test3_resp.keys in ['', [], None]:  # No response was made
    test3_resp.keys = None
thisExp.addData('test3_resp.keys',test3_resp.keys)
if test3_resp.keys != None:  # we had a response
    thisExp.addData('test3_resp.rt', test3_resp.rt)
thisExp.addData('test3_resp.started', test3_resp.tStartRefresh)
thisExp.addData('test3_resp.stopped', test3_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "test3_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "post_stimuli_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("stimuli_end")
# keep track of which components have finished
post_stimuli_codeComponents = []
for thisComponent in post_stimuli_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_stimuli_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "post_stimuli_code"-------
while continueRoutine:
    # get current time
    t = post_stimuli_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_stimuli_codeClock)
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
    for thisComponent in post_stimuli_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_stimuli_code"-------
for thisComponent in post_stimuli_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "post_stimuli_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "experiment_end_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("experiment_end")
# keep track of which components have finished
experiment_end_codeComponents = []
for thisComponent in experiment_end_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
experiment_end_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "experiment_end_code"-------
while continueRoutine:
    # get current time
    t = experiment_end_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=experiment_end_codeClock)
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
    for thisComponent in experiment_end_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "experiment_end_code"-------
for thisComponent in experiment_end_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "experiment_end_code" was not non-slip safe, so reset the non-slip timer
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
