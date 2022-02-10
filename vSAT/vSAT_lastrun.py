﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 09, 2022, at 19:03
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
expName = 'SAT'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\vSAT\\vSAT_lastrun.py',
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
exp_dir = os.getcwd()
loop_num = -1  # increased by 1 each loop 

SAT_conditions_dir = r"C:\Users\zackg\OneDrive\Ayaz Lab\KernelFlow_PsychoPy\vSAT\SAT_conditions"
vSAT_conditions_dir = r"C:\Users\zackg\OneDrive\Ayaz Lab\KernelFlow_PsychoPy\vSAT\vSAT_conditions"

SAT_csv_list = []
vSAT_csv_list = []

for csv_filename in os.listdir(SAT_conditions_dir):
    SAT_csv_list.append(os.path.join("SAT_conditions", csv_filename))
    
for csv_filename in os.listdir(vSAT_conditions_dir):
    vSAT_csv_list.append(os.path.join("vSAT_conditions", csv_filename))

for filename in os.listdir(exp_dir):
    if "vSAT_task_order-" in filename:
        vSAT_task_order = filename

# Initialize components for Routine "initial_instructions"
initial_instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='This is the Sustained Attention Task. \n\nLEFT CLICK the mouse if the signal is present.\nRIGHT CLICK the mouse if the signal is not present.\n\nPress SPACE to begin the experiment. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "main_loop_code"
main_loop_codeClock = core.Clock()

# Initialize components for Routine "experiment_instructions"
experiment_instructionsClock = core.Clock()
experiment_SAT_text = visual.TextStim(win=win, name='experiment_SAT_text',
    text='This is a SAT trial.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
experiment_vSAT_text = visual.TextStim(win=win, name='experiment_vSAT_text',
    text='This is a vSAT trial.\n\nPress SPACE to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
experiment_instructions_rep = keyboard.Keyboard()

# Initialize components for Routine "inter_stimulus_time"
inter_stimulus_timeClock = core.Clock()
inter_stim_text = visual.TextStim(win=win, name='inter_stim_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "signal_event"
signal_eventClock = core.Clock()
vSAT_square = visual.Rect(
    win=win, name='vSAT_square',
    width=(0.25, 0.25)[0], height=(0.25, 0.25)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)

# Initialize components for Routine "delay"
delayClock = core.Clock()
delay_text = visual.TextStim(win=win, name='delay_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "response_cue"
response_cueClock = core.Clock()
response_cue_sound = sound.Sound('A', secs=0.43, stereo=True, hamming=True,
    name='response_cue_sound')
response_cue_sound.setVolume(1.0)

# Initialize components for Routine "signal_response"
signal_responseClock = core.Clock()
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()
stimuli_background = visual.Rect(
    win=win, name='stimuli_background',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='0.0000, 0.0000, 0.0000', fillColor='0.0000, 0.0000, 0.0000',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "signal_response_code"
signal_response_codeClock = core.Clock()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_sound = sound.Sound('B', secs=0.5, stereo=True, hamming=True,
    name='feedback_sound')
feedback_sound.setVolume(1.0)

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
instructions_resp.keys = []
instructions_resp.rt = []
_instructions_resp_allKeys = []
# keep track of which components have finished
initial_instructionsComponents = [instructions_text, instructions_resp]
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
    
    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    
    # *instructions_resp* updates
    waitOnFlip = False
    if instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_resp.frameNStart = frameN  # exact frame index
        instructions_resp.tStart = t  # local t and not account for scr refresh
        instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_resp, 'tStartRefresh')  # time at next scr refresh
        instructions_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_resp.status == STARTED and not waitOnFlip:
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
thisExp.addData('instructions_text.started', instructions_text.tStartRefresh)
thisExp.addData('instructions_text.stopped', instructions_text.tStopRefresh)
# check responses
if instructions_resp.keys in ['', [], None]:  # No response was made
    instructions_resp.keys = None
thisExp.addData('instructions_resp.keys',instructions_resp.keys)
if instructions_resp.keys != None:  # we had a response
    thisExp.addData('instructions_resp.rt', instructions_resp.rt)
thisExp.addData('instructions_resp.started', instructions_resp.tStartRefresh)
thisExp.addData('instructions_resp.stopped', instructions_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "initial_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(vSAT_task_order),
    seed=None, name='main_loop')
thisExp.addLoop(main_loop)  # add the loop to the experiment
thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
if thisMain_loop != None:
    for paramName in thisMain_loop:
        exec('{} = thisMain_loop[paramName]'.format(paramName))

for thisMain_loop in main_loop:
    currentLoop = main_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            exec('{} = thisMain_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "main_loop_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    if task_order == "SAT1":
        this_loop_conditions = SAT_csv_list[0]
        SAT_text_display = 1
        vSAT_text_display = 0
    elif task_order == "SAT2":
        this_loop_conditions = SAT_csv_list[1]
        SAT_text_display = 1
        vSAT_text_display = 0
    elif task_order == "vSAT1":
        this_loop_conditions = vSAT_csv_list[0]
        SAT_text_display = 0
        vSAT_text_display = 1
    elif task_order == "vSAT2":
        this_loop_conditions = vSAT_csv_list[1]
        SAT_text_display = 0
        vSAT_text_display = 1
    # keep track of which components have finished
    main_loop_codeComponents = []
    for thisComponent in main_loop_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    main_loop_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main_loop_code"-------
    while continueRoutine:
        # get current time
        t = main_loop_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=main_loop_codeClock)
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
        for thisComponent in main_loop_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main_loop_code"-------
    for thisComponent in main_loop_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "main_loop_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "experiment_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    experiment_SAT_text.setOpacity(SAT_text_display)
    experiment_vSAT_text.setOpacity(vSAT_text_display)
    experiment_instructions_rep.keys = []
    experiment_instructions_rep.rt = []
    _experiment_instructions_rep_allKeys = []
    # keep track of which components have finished
    experiment_instructionsComponents = [experiment_SAT_text, experiment_vSAT_text, experiment_instructions_rep]
    for thisComponent in experiment_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experiment_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "experiment_instructions"-------
    while continueRoutine:
        # get current time
        t = experiment_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experiment_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *experiment_SAT_text* updates
        if experiment_SAT_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_SAT_text.frameNStart = frameN  # exact frame index
            experiment_SAT_text.tStart = t  # local t and not account for scr refresh
            experiment_SAT_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_SAT_text, 'tStartRefresh')  # time at next scr refresh
            experiment_SAT_text.setAutoDraw(True)
        
        # *experiment_vSAT_text* updates
        if experiment_vSAT_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_vSAT_text.frameNStart = frameN  # exact frame index
            experiment_vSAT_text.tStart = t  # local t and not account for scr refresh
            experiment_vSAT_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_vSAT_text, 'tStartRefresh')  # time at next scr refresh
            experiment_vSAT_text.setAutoDraw(True)
        
        # *experiment_instructions_rep* updates
        waitOnFlip = False
        if experiment_instructions_rep.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_instructions_rep.frameNStart = frameN  # exact frame index
            experiment_instructions_rep.tStart = t  # local t and not account for scr refresh
            experiment_instructions_rep.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_instructions_rep, 'tStartRefresh')  # time at next scr refresh
            experiment_instructions_rep.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(experiment_instructions_rep.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(experiment_instructions_rep.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if experiment_instructions_rep.status == STARTED and not waitOnFlip:
            theseKeys = experiment_instructions_rep.getKeys(keyList=['space'], waitRelease=False)
            _experiment_instructions_rep_allKeys.extend(theseKeys)
            if len(_experiment_instructions_rep_allKeys):
                experiment_instructions_rep.keys = _experiment_instructions_rep_allKeys[-1].name  # just the last key pressed
                experiment_instructions_rep.rt = _experiment_instructions_rep_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experiment_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experiment_instructions"-------
    for thisComponent in experiment_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main_loop.addData('experiment_SAT_text.started', experiment_SAT_text.tStartRefresh)
    main_loop.addData('experiment_SAT_text.stopped', experiment_SAT_text.tStopRefresh)
    main_loop.addData('experiment_vSAT_text.started', experiment_vSAT_text.tStartRefresh)
    main_loop.addData('experiment_vSAT_text.stopped', experiment_vSAT_text.tStopRefresh)
    # check responses
    if experiment_instructions_rep.keys in ['', [], None]:  # No response was made
        experiment_instructions_rep.keys = None
    main_loop.addData('experiment_instructions_rep.keys',experiment_instructions_rep.keys)
    if experiment_instructions_rep.keys != None:  # we had a response
        main_loop.addData('experiment_instructions_rep.rt', experiment_instructions_rep.rt)
    main_loop.addData('experiment_instructions_rep.started', experiment_instructions_rep.tStartRefresh)
    main_loop.addData('experiment_instructions_rep.stopped', experiment_instructions_rep.tStopRefresh)
    # the Routine "experiment_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    vSAT_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(this_loop_conditions),
        seed=None, name='vSAT_loop')
    thisExp.addLoop(vSAT_loop)  # add the loop to the experiment
    thisVSAT_loop = vSAT_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisVSAT_loop.rgb)
    if thisVSAT_loop != None:
        for paramName in thisVSAT_loop:
            exec('{} = thisVSAT_loop[paramName]'.format(paramName))
    
    for thisVSAT_loop in vSAT_loop:
        currentLoop = vSAT_loop
        # abbreviate parameter names if possible (e.g. rgb = thisVSAT_loop.rgb)
        if thisVSAT_loop != None:
            for paramName in thisVSAT_loop:
                exec('{} = thisVSAT_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "inter_stimulus_time"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        inter_stimulus_timeComponents = [inter_stim_text]
        for thisComponent in inter_stimulus_timeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stimulus_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stimulus_time"-------
        while continueRoutine:
            # get current time
            t = inter_stimulus_timeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stimulus_timeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_stim_text* updates
            if inter_stim_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_stim_text.frameNStart = frameN  # exact frame index
                inter_stim_text.tStart = t  # local t and not account for scr refresh
                inter_stim_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_stim_text, 'tStartRefresh')  # time at next scr refresh
                inter_stim_text.setAutoDraw(True)
            if inter_stim_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_stim_text.tStartRefresh + inter_stim_time-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_stim_text.tStop = t  # not accounting for scr refresh
                    inter_stim_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_stim_text, 'tStopRefresh')  # time at next scr refresh
                    inter_stim_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inter_stimulus_timeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stimulus_time"-------
        for thisComponent in inter_stimulus_timeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        vSAT_loop.addData('inter_stim_text.started', inter_stim_text.tStartRefresh)
        vSAT_loop.addData('inter_stim_text.stopped', inter_stim_text.tStopRefresh)
        # the Routine "inter_stimulus_time" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "signal_event"-------
        continueRoutine = True
        # update component parameters for each repeat
        vSAT_square.setOpacity(int(stim_event))
        vSAT_square.setPos([x_pos, y_pos])
        # keep track of which components have finished
        signal_eventComponents = [vSAT_square]
        for thisComponent in signal_eventComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        signal_eventClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "signal_event"-------
        while continueRoutine:
            # get current time
            t = signal_eventClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=signal_eventClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *vSAT_square* updates
            if vSAT_square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vSAT_square.frameNStart = frameN  # exact frame index
                vSAT_square.tStart = t  # local t and not account for scr refresh
                vSAT_square.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vSAT_square, 'tStartRefresh')  # time at next scr refresh
                vSAT_square.setAutoDraw(True)
            if vSAT_square.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > vSAT_square.tStartRefresh + stim_time-frameTolerance:
                    # keep track of stop time/frame for later
                    vSAT_square.tStop = t  # not accounting for scr refresh
                    vSAT_square.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(vSAT_square, 'tStopRefresh')  # time at next scr refresh
                    vSAT_square.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in signal_eventComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "signal_event"-------
        for thisComponent in signal_eventComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        vSAT_loop.addData('vSAT_square.started', vSAT_square.tStartRefresh)
        vSAT_loop.addData('vSAT_square.stopped', vSAT_square.tStopRefresh)
        # the Routine "signal_event" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "delay"-------
        continueRoutine = True
        routineTimer.add(0.100000)
        # update component parameters for each repeat
        # keep track of which components have finished
        delayComponents = [delay_text]
        for thisComponent in delayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        delayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "delay"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = delayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=delayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay_text* updates
            if delay_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                delay_text.frameNStart = frameN  # exact frame index
                delay_text.tStart = t  # local t and not account for scr refresh
                delay_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(delay_text, 'tStartRefresh')  # time at next scr refresh
                delay_text.setAutoDraw(True)
            if delay_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > delay_text.tStartRefresh + 0.1-frameTolerance:
                    # keep track of stop time/frame for later
                    delay_text.tStop = t  # not accounting for scr refresh
                    delay_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(delay_text, 'tStopRefresh')  # time at next scr refresh
                    delay_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "delay"-------
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        vSAT_loop.addData('delay_text.started', delay_text.tStartRefresh)
        vSAT_loop.addData('delay_text.stopped', delay_text.tStopRefresh)
        
        # ------Prepare to start Routine "response_cue"-------
        continueRoutine = True
        routineTimer.add(0.430000)
        # update component parameters for each repeat
        response_cue_sound.setSound('A', secs=0.43, hamming=True)
        response_cue_sound.setVolume(1.0, log=False)
        # keep track of which components have finished
        response_cueComponents = [response_cue_sound]
        for thisComponent in response_cueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_cueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response_cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = response_cueClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_cueClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop response_cue_sound
            if response_cue_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_cue_sound.frameNStart = frameN  # exact frame index
                response_cue_sound.tStart = t  # local t and not account for scr refresh
                response_cue_sound.tStartRefresh = tThisFlipGlobal  # on global time
                response_cue_sound.play(when=win)  # sync with win flip
            if response_cue_sound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response_cue_sound.tStartRefresh + 0.43-frameTolerance:
                    # keep track of stop time/frame for later
                    response_cue_sound.tStop = t  # not accounting for scr refresh
                    response_cue_sound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response_cue_sound, 'tStopRefresh')  # time at next scr refresh
                    response_cue_sound.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response_cue"-------
        for thisComponent in response_cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        response_cue_sound.stop()  # ensure sound has stopped at end of routine
        vSAT_loop.addData('response_cue_sound.started', response_cue_sound.tStartRefresh)
        vSAT_loop.addData('response_cue_sound.stopped', response_cue_sound.tStopRefresh)
        
        # ------Prepare to start Routine "signal_response"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_resp
        mouse_resp.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        signal_responseComponents = [mouse_resp, stimuli_background]
        for thisComponent in signal_responseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        signal_responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "signal_response"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = signal_responseClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=signal_responseClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_resp* updates
            if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_resp.frameNStart = frameN  # exact frame index
                mouse_resp.tStart = t  # local t and not account for scr refresh
                mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
                mouse_resp.status = STARTED
                mouse_resp.mouseClock.reset()
                prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
            if mouse_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mouse_resp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse_resp.tStop = t  # not accounting for scr refresh
                    mouse_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(mouse_resp, 'tStopRefresh')  # time at next scr refresh
                    mouse_resp.status = FINISHED
            if mouse_resp.status == STARTED:  # only update if started and not finished!
                buttons = mouse_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(stimuli_background)
                            clickableList = stimuli_background
                        except:
                            clickableList = [stimuli_background]
                        for obj in clickableList:
                            if obj.contains(mouse_resp):
                                gotValidClick = True
                                mouse_resp.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *stimuli_background* updates
            if stimuli_background.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimuli_background.frameNStart = frameN  # exact frame index
                stimuli_background.tStart = t  # local t and not account for scr refresh
                stimuli_background.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimuli_background, 'tStartRefresh')  # time at next scr refresh
                stimuli_background.setAutoDraw(True)
            if stimuli_background.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stimuli_background.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    stimuli_background.tStop = t  # not accounting for scr refresh
                    stimuli_background.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stimuli_background, 'tStopRefresh')  # time at next scr refresh
                    stimuli_background.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in signal_responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "signal_response"-------
        for thisComponent in signal_responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for vSAT_loop (TrialHandler)
        x, y = mouse_resp.getPos()
        buttons = mouse_resp.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter(stimuli_background)
                clickableList = stimuli_background
            except:
                clickableList = [stimuli_background]
            for obj in clickableList:
                if obj.contains(mouse_resp):
                    gotValidClick = True
                    mouse_resp.clicked_name.append(obj.name)
        vSAT_loop.addData('mouse_resp.x', x)
        vSAT_loop.addData('mouse_resp.y', y)
        vSAT_loop.addData('mouse_resp.leftButton', buttons[0])
        vSAT_loop.addData('mouse_resp.midButton', buttons[1])
        vSAT_loop.addData('mouse_resp.rightButton', buttons[2])
        if len(mouse_resp.clicked_name):
            vSAT_loop.addData('mouse_resp.clicked_name', mouse_resp.clicked_name[0])
        vSAT_loop.addData('mouse_resp.started', mouse_resp.tStart)
        vSAT_loop.addData('mouse_resp.stopped', mouse_resp.tStop)
        vSAT_loop.addData('stimuli_background.started', stimuli_background.tStartRefresh)
        vSAT_loop.addData('stimuli_background.stopped', stimuli_background.tStopRefresh)
        
        # ------Prepare to start Routine "signal_response_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        mouse_press = mouse_resp.getPressed()
        if mouse_press[0] == 1:  # left click
            left_click = 1
            right_click = 0
        elif mouse_press[2] == 1:  # right click
            left_click = 0
            right_click = 1
        else:
            left_click = 0
            right_click = 0
            
        if stim_event == 1 and left_click == 1:     # if stim and right click
            correct_resp = 1
        elif stim_event == 0 and right_click == 1:  # if no stim and left click
            correct_resp = 1
        else:  # if incorrect response
            correct_resp = 0
        
        # keep track of which components have finished
        signal_response_codeComponents = []
        for thisComponent in signal_response_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        signal_response_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "signal_response_code"-------
        while continueRoutine:
            # get current time
            t = signal_response_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=signal_response_codeClock)
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
            for thisComponent in signal_response_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "signal_response_code"-------
        for thisComponent in signal_response_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "signal_response_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        feedback_sound.setSound('B', secs=0.5, hamming=True)
        feedback_sound.setVolume(correct_resp, log=False)
        # keep track of which components have finished
        feedbackComponents = [feedback_sound]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop feedback_sound
            if feedback_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_sound.frameNStart = frameN  # exact frame index
                feedback_sound.tStart = t  # local t and not account for scr refresh
                feedback_sound.tStartRefresh = tThisFlipGlobal  # on global time
                feedback_sound.play(when=win)  # sync with win flip
            if feedback_sound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_sound.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_sound.tStop = t  # not accounting for scr refresh
                    feedback_sound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_sound, 'tStopRefresh')  # time at next scr refresh
                    feedback_sound.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedback_sound.stop()  # ensure sound has stopped at end of routine
        vSAT_loop.addData('feedback_sound.started', feedback_sound.tStartRefresh)
        vSAT_loop.addData('feedback_sound.stopped', feedback_sound.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'vSAT_loop'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'main_loop'


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