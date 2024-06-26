﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on October 25, 2022, at 16:16
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

from datetime import datetime
import time
import os
import sys
import csv

initial_timestamp = time.time()
clock_time_offset = logging.defaultClock.getTime()
task_start_timestamp = initial_timestamp - clock_time_offset  # account for timestamp delay from clock creation

task_start_timestamp_fmt = int(task_start_timestamp * 1e9)
start_time = datetime.fromtimestamp(task_start_timestamp).strftime("%Y-%m-%d-%H-%M-%S-%f")


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
    originPath='C:\\Users\\Sim\\Desktop\\KernelFlow_PsychoPy\\king_devick\\king_devick_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-0.7000, -0.7000, -0.7000], colorSpace='rgb',
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
win.mouseVisible = False

# setup dirs and files -----
tasks_dir = os.path.dirname(_thisDir)
task_dir = os.path.join(tasks_dir, expName)
par_dir = os.path.join(tasks_dir, "participants", f"participant_{expInfo['participant']}")
par_task_dir = os.path.join(par_dir, f"{str(expName)}")
data_dir = os.path.join(par_task_dir, "data")

try:
    os.mkdir(data_dir)
except:
    pass

filename = os.path.join(data_dir, f"{str(expInfo['participant'])}_{str(expInfo['session'])}_{str(expName)}_{start_time}")
thisExp.dataFileName = filename
logFile = logging.LogFile(filename +'.log', level=logging.EXP)

# setup markers -----
cwd = os.getcwd()
kernel_socket_path = os.path.join(os.path.dirname(cwd), "main", "kernel_socket")
sys.path.insert(0, kernel_socket_path)
from kernel_socket import Marker
marker = Marker(par_dir)

# task order -----
for task_filename in os.listdir(task_dir):
    if "TO" in task_filename:
        task_order_csv = os.path.join(task_dir, task_filename)

# read task order file -----
file = open(task_order_csv)
csvreader = csv.reader(file)

rows = []
for row in csvreader:
        rows.append(row[0])
file.close()

card_1 = rows[1]
card_2 = rows[2]
card_3 = rows[3]
order = [card_1, card_2, card_3]

# start experiment marker -----
marker.send_marker(31, task_start_timestamp_fmt)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='This is the King Devick task.\n\nYou will be presented with one practice card and then three task cards.\n\nPress SPACE to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "demo_card_instructions"
demo_card_instructionsClock = core.Clock()
demo_instructions_text = visual.TextStim(win=win, name='demo_instructions_text',
    text='This is the practice card. \n\nRead the numbers row by row from left to right as quickly as you can without making mistakes. If you do make a mistake, please continue reading the numbers. \n\nYour goal is to complete this task as quickly as possible.\n\nPress SPACE to begin. Press SPACE again as soon as you finish reading all numbers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
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
    texRes=128.0, interpolate=True, depth=0.0)
demo_resp = keyboard.Keyboard()

# Initialize components for Routine "loop_code"
loop_codeClock = core.Clock()

# Initialize components for Routine "card_instructions"
card_instructionsClock = core.Clock()
card_instructions_text = visual.TextStim(win=win, name='card_instructions_text',
    text='This is a task card. \n\nRead the numbers row by row from left to right as quickly as you can without making mistakes. If you do make a mistake, please continue reading the numbers. \n\nYour goal is to complete this task as quickly as possible.\n\nPress SPACE to begin. Press SPACE again as soon as you finish reading all numbers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
card_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "card"
cardClock = core.Clock()
card_image = visual.ImageStim(
    win=win,
    name='card_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
card_resp = keyboard.Keyboard()

# Initialize components for Routine "done"
doneClock = core.Clock()
done_text = visual.TextStim(win=win, name='done_text',
    text='The King Devick task is now complete.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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
    if demo_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo_resp.frameNStart = frameN  # exact frame index
        demo_resp.tStart = t  # local t and not account for scr refresh
        demo_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo_resp, 'tStartRefresh')  # time at next scr refresh
        demo_resp.status = STARTED
        # keyboard checking is just starting
        demo_resp.clock.reset()  # now t=0
    if demo_resp.status == STARTED:
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
# the Routine "demo_card" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
king_devick_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('king_devick_TO.csv'),
    seed=None, name='king_devick_loop')
thisExp.addLoop(king_devick_loop)  # add the loop to the experiment
thisKing_devick_loop = king_devick_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisKing_devick_loop.rgb)
if thisKing_devick_loop != None:
    for paramName in thisKing_devick_loop:
        exec('{} = thisKing_devick_loop[paramName]'.format(paramName))

for thisKing_devick_loop in king_devick_loop:
    currentLoop = king_devick_loop
    # abbreviate parameter names if possible (e.g. rgb = thisKing_devick_loop.rgb)
    if thisKing_devick_loop != None:
        for paramName in thisKing_devick_loop:
            exec('{} = thisKing_devick_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loop_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    card_image_path = os.path.join(task_dir, "king_devick_stimuli", task_order)
    # keep track of which components have finished
    loop_codeComponents = []
    for thisComponent in loop_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loop_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loop_code"-------
    while continueRoutine:
        # get current time
        t = loop_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loop_codeClock)
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
        for thisComponent in loop_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop_code"-------
    for thisComponent in loop_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "loop_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "card_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    card_instructions_resp.keys = []
    card_instructions_resp.rt = []
    _card_instructions_resp_allKeys = []
    # keep track of which components have finished
    card_instructionsComponents = [card_instructions_text, card_instructions_resp]
    for thisComponent in card_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    card_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "card_instructions"-------
    while continueRoutine:
        # get current time
        t = card_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=card_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *card_instructions_text* updates
        if card_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_instructions_text.frameNStart = frameN  # exact frame index
            card_instructions_text.tStart = t  # local t and not account for scr refresh
            card_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_instructions_text, 'tStartRefresh')  # time at next scr refresh
            card_instructions_text.setAutoDraw(True)
        
        # *card_instructions_resp* updates
        if card_instructions_resp.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            card_instructions_resp.frameNStart = frameN  # exact frame index
            card_instructions_resp.tStart = t  # local t and not account for scr refresh
            card_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            card_instructions_resp.status = STARTED
            # keyboard checking is just starting
            card_instructions_resp.clock.reset()  # now t=0
        if card_instructions_resp.status == STARTED:
            theseKeys = card_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
            _card_instructions_resp_allKeys.extend(theseKeys)
            if len(_card_instructions_resp_allKeys):
                card_instructions_resp.keys = _card_instructions_resp_allKeys[-1].name  # just the last key pressed
                card_instructions_resp.rt = _card_instructions_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in card_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "card_instructions"-------
    for thisComponent in card_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "card_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "card"-------
    continueRoutine = True
    # update component parameters for each repeat
    card_image.setImage(card_image_path)
    card_resp.keys = []
    card_resp.rt = []
    _card_resp_allKeys = []
    # keep track of which components have finished
    cardComponents = [card_image, card_resp]
    for thisComponent in cardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    cardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "card"-------
    while continueRoutine:
        # get current time
        t = cardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=cardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *card_image* updates
        if card_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_image.frameNStart = frameN  # exact frame index
            card_image.tStart = t  # local t and not account for scr refresh
            card_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_image, 'tStartRefresh')  # time at next scr refresh
            card_image.setAutoDraw(True)
        
        # *card_resp* updates
        waitOnFlip = False
        if card_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card_resp.frameNStart = frameN  # exact frame index
            card_resp.tStart = t  # local t and not account for scr refresh
            card_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card_resp, 'tStartRefresh')  # time at next scr refresh
            card_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(card_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(card_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if card_resp.status == STARTED and not waitOnFlip:
            theseKeys = card_resp.getKeys(keyList=['space'], waitRelease=False)
            _card_resp_allKeys.extend(theseKeys)
            if len(_card_resp_allKeys):
                card_resp.keys = _card_resp_allKeys[-1].name  # just the last key pressed
                card_resp.rt = _card_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "card"-------
    for thisComponent in cardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    king_devick_loop.addData('card_image.started', card_image.tStartRefresh)
    king_devick_loop.addData('card_image.stopped', card_image.tStopRefresh)
    # check responses
    if card_resp.keys in ['', [], None]:  # No response was made
        card_resp.keys = None
    king_devick_loop.addData('card_resp.keys',card_resp.keys)
    if card_resp.keys != None:  # we had a response
        king_devick_loop.addData('card_resp.rt', card_resp.rt)
    king_devick_loop.addData('card_resp.started', card_resp.tStartRefresh)
    king_devick_loop.addData('card_resp.stopped', card_resp.tStopRefresh)
    # the Routine "card" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'king_devick_loop'


# ------Prepare to start Routine "done"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
doneComponents = [done_text]
for thisComponent in doneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
doneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "done"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = doneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=doneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done_text* updates
    if done_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_text.frameNStart = frameN  # exact frame index
        done_text.tStart = t  # local t and not account for scr refresh
        done_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_text, 'tStartRefresh')  # time at next scr refresh
        done_text.setAutoDraw(True)
    if done_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done_text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            done_text.tStop = t  # not accounting for scr refresh
            done_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done_text, 'tStopRefresh')  # time at next scr refresh
            done_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "done"-------
for thisComponent in doneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# end experiment marker -----
task_end_timestamp = time.time() - clock_time_offset
task_end_timestamp_fmt = int(task_end_timestamp * 1e9)
marker.send_marker(32, task_end_timestamp_fmt)

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
