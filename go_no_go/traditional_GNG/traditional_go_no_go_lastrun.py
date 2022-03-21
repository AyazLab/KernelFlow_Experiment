﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 21, 2022, at 06:29
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
expName = 'traditional_go_no_go'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\go_no_go\\traditional_GNG\\traditional_go_no_go_lastrun.py',
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
os.chdir("..")
kernel_socket_path = os.path.join(os.getcwd(), "main", "kernel_socket")
os.chdir(cwd)
import sys
sys.path.insert(0, kernel_socket_path)
from kernel_socket import Marker
marker = Marker()

loop_num = -1  # increased by 1 each loop 

GNG_conditions_dir = os.path.join(cwd, "traditional_GNG_conditions")

go_csv_list = []
GNG_csv_list = []

for csv_filename in os.listdir(GNG_conditions_dir):
    if "go" in csv_filename:
        go_csv_list.append(os.path.join("traditional_GNG_conditions", csv_filename))
    elif "GNG" in csv_filename:
        GNG_csv_list.append(os.path.join("traditional_GNG_conditions", csv_filename))
        
practice_dir = os.path.join(cwd, "practice")
for csv_filename in os.listdir(practice_dir):
    if "loop_count" in csv_filename:
        practice_loop_path = os.path.join(practice_dir, csv_filename)
    elif "GNG_stims" in csv_filename:
        practice_csv_path = os.path.join(practice_dir, csv_filename)
        
marker.send_marker("experiment_start")

# Initialize components for Routine "initial_instructions"
initial_instructionsClock = core.Clock()
initial_instructions_text = visual.TextStim(win=win, name='initial_instructions_text',
    text='You are going to see either a GREEN or a RED circle appear on the screen. Press the RIGHT ARROW as fast as you can when you see the GREEN circle. Press the LEFT ARROW as fast as you can when you see the RED circle. \n\nWhen the circle disappears, a plus sign will appear on the screen. Stare at the plus sign until the next circle appears. Remember to press the arrow keys as fast as you can without making any mistakes.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
initial_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "GNG_loop_code"
GNG_loop_codeClock = core.Clock()

# Initialize components for Routine "go_instructions"
go_instructionsClock = core.Clock()
go_instructions_text = visual.TextStim(win=win, name='go_instructions_text',
    text='This is the GO experiment. \n\nGREEN circle = GO\nPress SPACE when a GO stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
go_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "block_start_code"
block_start_codeClock = core.Clock()
marker.send_marker("block_start")

# Initialize components for Routine "inter_stim_match_code"
inter_stim_match_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
inter_stim_plus = visual.ShapeStim(
    win=win, name='inter_stim_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "go_trial"
go_trialClock = core.Clock()
go_resp = keyboard.Keyboard()
go_plus = visual.ShapeStim(
    win=win, name='go_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
go_circle = visual.ShapeStim(
    win=win, name='go_circle',
    size=(0.5, 0.5), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='[0, 0, 0]', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "block_end_code"
block_end_codeClock = core.Clock()

# Initialize components for Routine "GNG_instructions"
GNG_instructionsClock = core.Clock()
GNG_instructions_text = visual.TextStim(win=win, name='GNG_instructions_text',
    text='This is the GO/NO-GO experiment. \n\nGREEN circle = GO\nRED circle = NO-GO\n\nPress SPACE when a GO stimulus appears.\nDo not press anything when a NO-GO stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GNG_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "block_start_code"
block_start_codeClock = core.Clock()
marker.send_marker("block_start")

# Initialize components for Routine "inter_stim_match_code"
inter_stim_match_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
inter_stim_plus = visual.ShapeStim(
    win=win, name='inter_stim_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "GNG_trial"
GNG_trialClock = core.Clock()
GNG_resp = keyboard.Keyboard()
GNG_plus = visual.ShapeStim(
    win=win, name='GNG_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
GNG_circle = visual.ShapeStim(
    win=win, name='GNG_circle',
    size=(0.5, 0.5), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='[0, 0, 0]', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "block_end_code"
block_end_codeClock = core.Clock()

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

# ------Prepare to start Routine "initial_instructions"-------
continueRoutine = True
# update component parameters for each repeat
initial_instructions_resp.keys = []
initial_instructions_resp.rt = []
_initial_instructions_resp_allKeys = []
# keep track of which components have finished
initial_instructionsComponents = [initial_instructions_text, initial_instructions_resp]
for thisComponent in initial_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
initial_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "initial_instructions"-------
while continueRoutine:
    # get current time
    t = initial_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=initial_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initial_instructions_text* updates
    if initial_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        initial_instructions_text.frameNStart = frameN  # exact frame index
        initial_instructions_text.tStart = t  # local t and not account for scr refresh
        initial_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(initial_instructions_text, 'tStartRefresh')  # time at next scr refresh
        initial_instructions_text.setAutoDraw(True)
    
    # *initial_instructions_resp* updates
    if initial_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        initial_instructions_resp.frameNStart = frameN  # exact frame index
        initial_instructions_resp.tStart = t  # local t and not account for scr refresh
        initial_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(initial_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        initial_instructions_resp.status = STARTED
        # keyboard checking is just starting
        initial_instructions_resp.clock.reset()  # now t=0
    if initial_instructions_resp.status == STARTED:
        theseKeys = initial_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _initial_instructions_resp_allKeys.extend(theseKeys)
        if len(_initial_instructions_resp_allKeys):
            initial_instructions_resp.keys = _initial_instructions_resp_allKeys[-1].name  # just the last key pressed
            initial_instructions_resp.rt = _initial_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initial_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "initial_instructions"-------
for thisComponent in initial_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "initial_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
GNG_loop = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='GNG_loop')
thisExp.addLoop(GNG_loop)  # add the loop to the experiment
thisGNG_loop = GNG_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisGNG_loop.rgb)
if thisGNG_loop != None:
    for paramName in thisGNG_loop:
        exec('{} = thisGNG_loop[paramName]'.format(paramName))

for thisGNG_loop in GNG_loop:
    currentLoop = GNG_loop
    # abbreviate parameter names if possible (e.g. rgb = thisGNG_loop.rgb)
    if thisGNG_loop != None:
        for paramName in thisGNG_loop:
            exec('{} = thisGNG_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "GNG_loop_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    # increases the loop number to iterate
    # through the datasets
    
    loop_num += 1
    
    go_stims = go_csv_list[loop_num]
    GNG_stims = GNG_csv_list[loop_num]
    # keep track of which components have finished
    GNG_loop_codeComponents = []
    for thisComponent in GNG_loop_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GNG_loop_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GNG_loop_code"-------
    while continueRoutine:
        # get current time
        t = GNG_loop_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GNG_loop_codeClock)
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
        for thisComponent in GNG_loop_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GNG_loop_code"-------
    for thisComponent in GNG_loop_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "GNG_loop_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "go_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    go_instructions_resp.keys = []
    go_instructions_resp.rt = []
    _go_instructions_resp_allKeys = []
    # keep track of which components have finished
    go_instructionsComponents = [go_instructions_text, go_instructions_resp]
    for thisComponent in go_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    go_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "go_instructions"-------
    while continueRoutine:
        # get current time
        t = go_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=go_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *go_instructions_text* updates
        if go_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            go_instructions_text.frameNStart = frameN  # exact frame index
            go_instructions_text.tStart = t  # local t and not account for scr refresh
            go_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go_instructions_text, 'tStartRefresh')  # time at next scr refresh
            go_instructions_text.setAutoDraw(True)
        
        # *go_instructions_resp* updates
        if go_instructions_resp.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            go_instructions_resp.frameNStart = frameN  # exact frame index
            go_instructions_resp.tStart = t  # local t and not account for scr refresh
            go_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            go_instructions_resp.status = STARTED
            # keyboard checking is just starting
            go_instructions_resp.clock.reset()  # now t=0
        if go_instructions_resp.status == STARTED:
            theseKeys = go_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
            _go_instructions_resp_allKeys.extend(theseKeys)
            if len(_go_instructions_resp_allKeys):
                go_instructions_resp.keys = _go_instructions_resp_allKeys[-1].name  # just the last key pressed
                go_instructions_resp.rt = _go_instructions_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in go_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "go_instructions"-------
    for thisComponent in go_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "go_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "block_start_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    block_start_codeComponents = []
    for thisComponent in block_start_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_start_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_start_code"-------
    while continueRoutine:
        # get current time
        t = block_start_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_start_codeClock)
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
        for thisComponent in block_start_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_start_code"-------
    for thisComponent in block_start_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_start_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    go_block = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(go_stims),
        seed=None, name='go_block')
    thisExp.addLoop(go_block)  # add the loop to the experiment
    thisGo_block = go_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGo_block.rgb)
    if thisGo_block != None:
        for paramName in thisGo_block:
            exec('{} = thisGo_block[paramName]'.format(paramName))
    
    for thisGo_block in go_block:
        currentLoop = go_block
        # abbreviate parameter names if possible (e.g. rgb = thisGo_block.rgb)
        if thisGo_block != None:
            for paramName in thisGo_block:
                exec('{} = thisGo_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "inter_stim_match_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        if match == 1:
            trial_color = [0, 1, 0]  # green
            corr_key = "space"
        elif match == 0:
            trial_color = [1, 0, 0]  # red
            corr_key = None
        # keep track of which components have finished
        inter_stim_match_codeComponents = []
        for thisComponent in inter_stim_match_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stim_match_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stim_match_code"-------
        while continueRoutine:
            # get current time
            t = inter_stim_match_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stim_match_codeClock)
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
            for thisComponent in inter_stim_match_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stim_match_code"-------
        for thisComponent in inter_stim_match_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "inter_stim_match_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "inter_stim_interval"-------
        continueRoutine = True
        # update component parameters for each repeat
        marker.send_marker("trial_start")
        # keep track of which components have finished
        inter_stim_intervalComponents = [inter_stim_plus]
        for thisComponent in inter_stim_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stim_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stim_interval"-------
        while continueRoutine:
            # get current time
            t = inter_stim_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stim_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_stim_plus* updates
            if inter_stim_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_stim_plus.frameNStart = frameN  # exact frame index
                inter_stim_plus.tStart = t  # local t and not account for scr refresh
                inter_stim_plus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_stim_plus, 'tStartRefresh')  # time at next scr refresh
                inter_stim_plus.setAutoDraw(True)
            if inter_stim_plus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_stim_plus.tStartRefresh + inter_stim_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_stim_plus.tStop = t  # not accounting for scr refresh
                    inter_stim_plus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_stim_plus, 'tStopRefresh')  # time at next scr refresh
                    inter_stim_plus.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inter_stim_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stim_interval"-------
        for thisComponent in inter_stim_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        go_block.addData('inter_stim_plus.started', inter_stim_plus.tStartRefresh)
        go_block.addData('inter_stim_plus.stopped', inter_stim_plus.tStopRefresh)
        # the Routine "inter_stim_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "go_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        marker.send_marker("stimuli_start")
        go_resp.keys = []
        go_resp.rt = []
        _go_resp_allKeys = []
        go_circle.setFillColor(trial_color)
        # keep track of which components have finished
        go_trialComponents = [go_resp, go_plus, go_circle]
        for thisComponent in go_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        go_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "go_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = go_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=go_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *go_resp* updates
            waitOnFlip = False
            if go_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                go_resp.frameNStart = frameN  # exact frame index
                go_resp.tStart = t  # local t and not account for scr refresh
                go_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go_resp, 'tStartRefresh')  # time at next scr refresh
                go_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(go_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(go_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if go_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > go_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    go_resp.tStop = t  # not accounting for scr refresh
                    go_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(go_resp, 'tStopRefresh')  # time at next scr refresh
                    go_resp.status = FINISHED
            if go_resp.status == STARTED and not waitOnFlip:
                theseKeys = go_resp.getKeys(keyList=['space'], waitRelease=False)
                _go_resp_allKeys.extend(theseKeys)
                if len(_go_resp_allKeys):
                    go_resp.keys = _go_resp_allKeys[-1].name  # just the last key pressed
                    go_resp.rt = _go_resp_allKeys[-1].rt
                    # was this correct?
                    if (go_resp.keys == str(corr_key)) or (go_resp.keys == corr_key):
                        go_resp.corr = 1
                    else:
                        go_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *go_plus* updates
            if go_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                go_plus.frameNStart = frameN  # exact frame index
                go_plus.tStart = t  # local t and not account for scr refresh
                go_plus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go_plus, 'tStartRefresh')  # time at next scr refresh
                go_plus.setAutoDraw(True)
            if go_plus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > go_plus.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    go_plus.tStop = t  # not accounting for scr refresh
                    go_plus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(go_plus, 'tStopRefresh')  # time at next scr refresh
                    go_plus.setAutoDraw(False)
            
            # *go_circle* updates
            if go_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                go_circle.frameNStart = frameN  # exact frame index
                go_circle.tStart = t  # local t and not account for scr refresh
                go_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go_circle, 'tStartRefresh')  # time at next scr refresh
                go_circle.setAutoDraw(True)
            if go_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > go_circle.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    go_circle.tStop = t  # not accounting for scr refresh
                    go_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(go_circle, 'tStopRefresh')  # time at next scr refresh
                    go_circle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in go_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "go_trial"-------
        for thisComponent in go_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        marker.send_marker("stimuli_end")
        
        if go_resp.keys:
            if go_resp.keys == corr_key:
                marker.send_marker("correct_ans")
            else:
                marker.send_marker("incorrect_ans")
        else:
            marker.send_marker("incorrect_ans")
            
        marker.send_marker("trial_end")
        # check responses
        if go_resp.keys in ['', [], None]:  # No response was made
            go_resp.keys = None
            # was no response the correct answer?!
            if str(corr_key).lower() == 'none':
               go_resp.corr = 1;  # correct non-response
            else:
               go_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for go_block (TrialHandler)
        go_block.addData('go_resp.keys',go_resp.keys)
        go_block.addData('go_resp.corr', go_resp.corr)
        if go_resp.keys != None:  # we had a response
            go_block.addData('go_resp.rt', go_resp.rt)
        go_block.addData('go_resp.started', go_resp.tStartRefresh)
        go_block.addData('go_resp.stopped', go_resp.tStopRefresh)
        go_block.addData('go_circle.started', go_circle.tStartRefresh)
        go_block.addData('go_circle.stopped', go_circle.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'go_block'
    
    
    # ------Prepare to start Routine "block_end_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    marker.send_marker("block_end")
    # keep track of which components have finished
    block_end_codeComponents = []
    for thisComponent in block_end_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_end_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_end_code"-------
    while continueRoutine:
        # get current time
        t = block_end_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_end_codeClock)
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
        for thisComponent in block_end_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_end_code"-------
    for thisComponent in block_end_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_end_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "GNG_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    GNG_instructions_resp.keys = []
    GNG_instructions_resp.rt = []
    _GNG_instructions_resp_allKeys = []
    # keep track of which components have finished
    GNG_instructionsComponents = [GNG_instructions_text, GNG_instructions_resp]
    for thisComponent in GNG_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GNG_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GNG_instructions"-------
    while continueRoutine:
        # get current time
        t = GNG_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GNG_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GNG_instructions_text* updates
        if GNG_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GNG_instructions_text.frameNStart = frameN  # exact frame index
            GNG_instructions_text.tStart = t  # local t and not account for scr refresh
            GNG_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GNG_instructions_text, 'tStartRefresh')  # time at next scr refresh
            GNG_instructions_text.setAutoDraw(True)
        
        # *GNG_instructions_resp* updates
        waitOnFlip = False
        if GNG_instructions_resp.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            GNG_instructions_resp.frameNStart = frameN  # exact frame index
            GNG_instructions_resp.tStart = t  # local t and not account for scr refresh
            GNG_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GNG_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            GNG_instructions_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(GNG_instructions_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(GNG_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if GNG_instructions_resp.status == STARTED and not waitOnFlip:
            theseKeys = GNG_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
            _GNG_instructions_resp_allKeys.extend(theseKeys)
            if len(_GNG_instructions_resp_allKeys):
                GNG_instructions_resp.keys = _GNG_instructions_resp_allKeys[-1].name  # just the last key pressed
                GNG_instructions_resp.rt = _GNG_instructions_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GNG_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GNG_instructions"-------
    for thisComponent in GNG_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if GNG_instructions_resp.keys in ['', [], None]:  # No response was made
        GNG_instructions_resp.keys = None
    GNG_loop.addData('GNG_instructions_resp.keys',GNG_instructions_resp.keys)
    if GNG_instructions_resp.keys != None:  # we had a response
        GNG_loop.addData('GNG_instructions_resp.rt', GNG_instructions_resp.rt)
    GNG_loop.addData('GNG_instructions_resp.started', GNG_instructions_resp.tStartRefresh)
    GNG_loop.addData('GNG_instructions_resp.stopped', GNG_instructions_resp.tStopRefresh)
    # the Routine "GNG_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "block_start_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    block_start_codeComponents = []
    for thisComponent in block_start_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_start_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_start_code"-------
    while continueRoutine:
        # get current time
        t = block_start_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_start_codeClock)
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
        for thisComponent in block_start_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_start_code"-------
    for thisComponent in block_start_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_start_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    GNG_block = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(GNG_stims),
        seed=None, name='GNG_block')
    thisExp.addLoop(GNG_block)  # add the loop to the experiment
    thisGNG_block = GNG_block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGNG_block.rgb)
    if thisGNG_block != None:
        for paramName in thisGNG_block:
            exec('{} = thisGNG_block[paramName]'.format(paramName))
    
    for thisGNG_block in GNG_block:
        currentLoop = GNG_block
        # abbreviate parameter names if possible (e.g. rgb = thisGNG_block.rgb)
        if thisGNG_block != None:
            for paramName in thisGNG_block:
                exec('{} = thisGNG_block[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "inter_stim_match_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        if match == 1:
            trial_color = [0, 1, 0]  # green
            corr_key = "space"
        elif match == 0:
            trial_color = [1, 0, 0]  # red
            corr_key = None
        # keep track of which components have finished
        inter_stim_match_codeComponents = []
        for thisComponent in inter_stim_match_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stim_match_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stim_match_code"-------
        while continueRoutine:
            # get current time
            t = inter_stim_match_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stim_match_codeClock)
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
            for thisComponent in inter_stim_match_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stim_match_code"-------
        for thisComponent in inter_stim_match_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "inter_stim_match_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "inter_stim_interval"-------
        continueRoutine = True
        # update component parameters for each repeat
        marker.send_marker("trial_start")
        # keep track of which components have finished
        inter_stim_intervalComponents = [inter_stim_plus]
        for thisComponent in inter_stim_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stim_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stim_interval"-------
        while continueRoutine:
            # get current time
            t = inter_stim_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stim_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_stim_plus* updates
            if inter_stim_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_stim_plus.frameNStart = frameN  # exact frame index
                inter_stim_plus.tStart = t  # local t and not account for scr refresh
                inter_stim_plus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_stim_plus, 'tStartRefresh')  # time at next scr refresh
                inter_stim_plus.setAutoDraw(True)
            if inter_stim_plus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_stim_plus.tStartRefresh + inter_stim_interval-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_stim_plus.tStop = t  # not accounting for scr refresh
                    inter_stim_plus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_stim_plus, 'tStopRefresh')  # time at next scr refresh
                    inter_stim_plus.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inter_stim_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stim_interval"-------
        for thisComponent in inter_stim_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        GNG_block.addData('inter_stim_plus.started', inter_stim_plus.tStartRefresh)
        GNG_block.addData('inter_stim_plus.stopped', inter_stim_plus.tStopRefresh)
        # the Routine "inter_stim_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "GNG_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        marker.send_marker("stimuli_start")
        GNG_resp.keys = []
        GNG_resp.rt = []
        _GNG_resp_allKeys = []
        GNG_circle.setFillColor(trial_color)
        # keep track of which components have finished
        GNG_trialComponents = [GNG_resp, GNG_plus, GNG_circle]
        for thisComponent in GNG_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        GNG_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "GNG_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = GNG_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=GNG_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *GNG_resp* updates
            waitOnFlip = False
            if GNG_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                GNG_resp.frameNStart = frameN  # exact frame index
                GNG_resp.tStart = t  # local t and not account for scr refresh
                GNG_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GNG_resp, 'tStartRefresh')  # time at next scr refresh
                GNG_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(GNG_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(GNG_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if GNG_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GNG_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    GNG_resp.tStop = t  # not accounting for scr refresh
                    GNG_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GNG_resp, 'tStopRefresh')  # time at next scr refresh
                    GNG_resp.status = FINISHED
            if GNG_resp.status == STARTED and not waitOnFlip:
                theseKeys = GNG_resp.getKeys(keyList=['space'], waitRelease=False)
                _GNG_resp_allKeys.extend(theseKeys)
                if len(_GNG_resp_allKeys):
                    GNG_resp.keys = _GNG_resp_allKeys[-1].name  # just the last key pressed
                    GNG_resp.rt = _GNG_resp_allKeys[-1].rt
                    # was this correct?
                    if (GNG_resp.keys == str(corr_key)) or (GNG_resp.keys == corr_key):
                        GNG_resp.corr = 1
                    else:
                        GNG_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *GNG_plus* updates
            if GNG_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                GNG_plus.frameNStart = frameN  # exact frame index
                GNG_plus.tStart = t  # local t and not account for scr refresh
                GNG_plus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GNG_plus, 'tStartRefresh')  # time at next scr refresh
                GNG_plus.setAutoDraw(True)
            if GNG_plus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GNG_plus.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    GNG_plus.tStop = t  # not accounting for scr refresh
                    GNG_plus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GNG_plus, 'tStopRefresh')  # time at next scr refresh
                    GNG_plus.setAutoDraw(False)
            
            # *GNG_circle* updates
            if GNG_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                GNG_circle.frameNStart = frameN  # exact frame index
                GNG_circle.tStart = t  # local t and not account for scr refresh
                GNG_circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GNG_circle, 'tStartRefresh')  # time at next scr refresh
                GNG_circle.setAutoDraw(True)
            if GNG_circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GNG_circle.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    GNG_circle.tStop = t  # not accounting for scr refresh
                    GNG_circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GNG_circle, 'tStopRefresh')  # time at next scr refresh
                    GNG_circle.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GNG_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "GNG_trial"-------
        for thisComponent in GNG_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        marker.send_marker("stimuli_end")
        
        if go_resp.keys:
            if go_resp.keys == corr_key:
                marker.send_marker("correct_ans")
            else:
                marker.send_marker("incorrect_ans")
        else:
            marker.send_marker("incorrect_ans")
            
        marker.send_marker("trial_end")
        # check responses
        if GNG_resp.keys in ['', [], None]:  # No response was made
            GNG_resp.keys = None
            # was no response the correct answer?!
            if str(corr_key).lower() == 'none':
               GNG_resp.corr = 1;  # correct non-response
            else:
               GNG_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for GNG_block (TrialHandler)
        GNG_block.addData('GNG_resp.keys',GNG_resp.keys)
        GNG_block.addData('GNG_resp.corr', GNG_resp.corr)
        if GNG_resp.keys != None:  # we had a response
            GNG_block.addData('GNG_resp.rt', GNG_resp.rt)
        GNG_block.addData('GNG_resp.started', GNG_resp.tStartRefresh)
        GNG_block.addData('GNG_resp.stopped', GNG_resp.tStopRefresh)
        GNG_block.addData('GNG_circle.started', GNG_circle.tStartRefresh)
        GNG_block.addData('GNG_circle.stopped', GNG_circle.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'GNG_block'
    
    
    # ------Prepare to start Routine "block_end_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    marker.send_marker("block_end")
    # keep track of which components have finished
    block_end_codeComponents = []
    for thisComponent in block_end_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block_end_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "block_end_code"-------
    while continueRoutine:
        # get current time
        t = block_end_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block_end_codeClock)
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
        for thisComponent in block_end_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block_end_code"-------
    for thisComponent in block_end_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_end_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'GNG_loop'


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
