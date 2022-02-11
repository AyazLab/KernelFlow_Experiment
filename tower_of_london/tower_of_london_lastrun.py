#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 11, 2022, at 12:01
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
expName = 'affective_go_no_go'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\tower_of_london\\tower_of_london_lastrun.py',
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
cwd = os.getcwd()
loop_num = -1  # increased by 1 each loop 

TOL_conditions_dir = os.path.join(cwd, "TOL_conditions")

ZM_csv_list = []
MM_csv_list = []

for csv_filename in os.listdir(TOL_conditions_dir):
    if "ZM" in csv_filename:
        ZM_csv_list.append(os.path.join("TOL_conditions", csv_filename))
    elif "MM" in csv_filename:
        MM_csv_list.append(os.path.join("TOL_conditions", csv_filename))
        
for filename in os.listdir(cwd):
    if "TOL_task_order-" in filename:
        TOL_task_order = filename

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='These are the instructions for the Tower of London experiment. \n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "TOL_loop_code"
TOL_loop_codeClock = core.Clock()

# Initialize components for Routine "trial_instructions"
trial_instructionsClock = core.Clock()
zero_move_text = visual.TextStim(win=win, name='zero_move_text',
    text='If the Tower of London image can be solved in zero moves, press SPACE.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
multi_move_text = visual.TextStim(win=win, name='multi_move_text',
    text='If the Tower of London image can be solved in exactly two moves, press SPACE.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
exp_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "stim"
stimClock = core.Clock()
TOL_trial_text = visual.TextStim(win=win, name='TOL_trial_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
TOL_trial_resp = keyboard.Keyboard()
TOL_trial_image = visual.ImageStim(
    win=win,
    name='TOL_trial_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

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
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TOL_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(TOL_task_order),
    seed=None, name='TOL_loop')
thisExp.addLoop(TOL_loop)  # add the loop to the experiment
thisTOL_loop = TOL_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTOL_loop.rgb)
if thisTOL_loop != None:
    for paramName in thisTOL_loop:
        exec('{} = thisTOL_loop[paramName]'.format(paramName))

for thisTOL_loop in TOL_loop:
    currentLoop = TOL_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTOL_loop.rgb)
    if thisTOL_loop != None:
        for paramName in thisTOL_loop:
            exec('{} = thisTOL_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TOL_loop_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    if task_order == "ZM1":
        this_loop_conditions = ZM_csv_list[0]
        text_display = [1, 0]
        num_moves = "zero"
    elif task_order == "ZM2":
        this_loop_conditions = ZM_csv_list[1]
        text_display = [1, 0]
        num_moves = "zero"
    elif task_order == "ZM3":
        this_loop_conditions = ZM_csv_list[2]
        text_display = [1, 0]
        num_moves = "zero"
    elif task_order == "MM":
        this_loop_conditions = MM_csv_list[0]
        text_display = [0, 1]
        num_moves = "two"
    elif task_order == "MM2":
        this_loop_conditions = MM_csv_list[1]
        text_display = [0, 1]
        num_moves = "two"
    elif task_order == "MM3":
        this_loop_conditions = MM_csv_list[2]
        num_moves = "two"
        text_display = [0, 1]
    # keep track of which components have finished
    TOL_loop_codeComponents = []
    for thisComponent in TOL_loop_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TOL_loop_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TOL_loop_code"-------
    while continueRoutine:
        # get current time
        t = TOL_loop_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TOL_loop_codeClock)
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
        for thisComponent in TOL_loop_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TOL_loop_code"-------
    for thisComponent in TOL_loop_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "TOL_loop_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    zero_move_text.setOpacity(text_display[0])
    multi_move_text.setOpacity(text_display[1])
    exp_instructions_resp.keys = []
    exp_instructions_resp.rt = []
    _exp_instructions_resp_allKeys = []
    # keep track of which components have finished
    trial_instructionsComponents = [zero_move_text, multi_move_text, exp_instructions_resp]
    for thisComponent in trial_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_instructions"-------
    while continueRoutine:
        # get current time
        t = trial_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *zero_move_text* updates
        if zero_move_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            zero_move_text.frameNStart = frameN  # exact frame index
            zero_move_text.tStart = t  # local t and not account for scr refresh
            zero_move_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(zero_move_text, 'tStartRefresh')  # time at next scr refresh
            zero_move_text.setAutoDraw(True)
        
        # *multi_move_text* updates
        if multi_move_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            multi_move_text.frameNStart = frameN  # exact frame index
            multi_move_text.tStart = t  # local t and not account for scr refresh
            multi_move_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(multi_move_text, 'tStartRefresh')  # time at next scr refresh
            multi_move_text.setAutoDraw(True)
        
        # *exp_instructions_resp* updates
        waitOnFlip = False
        if exp_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exp_instructions_resp.frameNStart = frameN  # exact frame index
            exp_instructions_resp.tStart = t  # local t and not account for scr refresh
            exp_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exp_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            exp_instructions_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(exp_instructions_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(exp_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if exp_instructions_resp.status == STARTED and not waitOnFlip:
            theseKeys = exp_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
            _exp_instructions_resp_allKeys.extend(theseKeys)
            if len(_exp_instructions_resp_allKeys):
                exp_instructions_resp.keys = _exp_instructions_resp_allKeys[-1].name  # just the last key pressed
                exp_instructions_resp.rt = _exp_instructions_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_instructions"-------
    for thisComponent in trial_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TOL_loop.addData('zero_move_text.started', zero_move_text.tStartRefresh)
    TOL_loop.addData('zero_move_text.stopped', zero_move_text.tStopRefresh)
    TOL_loop.addData('multi_move_text.started', multi_move_text.tStartRefresh)
    TOL_loop.addData('multi_move_text.stopped', multi_move_text.tStopRefresh)
    # check responses
    if exp_instructions_resp.keys in ['', [], None]:  # No response was made
        exp_instructions_resp.keys = None
    TOL_loop.addData('exp_instructions_resp.keys',exp_instructions_resp.keys)
    if exp_instructions_resp.keys != None:  # we had a response
        TOL_loop.addData('exp_instructions_resp.rt', exp_instructions_resp.rt)
    TOL_loop.addData('exp_instructions_resp.started', exp_instructions_resp.tStartRefresh)
    TOL_loop.addData('exp_instructions_resp.stopped', exp_instructions_resp.tStopRefresh)
    # the Routine "trial_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    stim_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(this_loop_conditions),
        seed=None, name='stim_loop')
    thisExp.addLoop(stim_loop)  # add the loop to the experiment
    thisStim_loop = stim_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisStim_loop.rgb)
    if thisStim_loop != None:
        for paramName in thisStim_loop:
            exec('{} = thisStim_loop[paramName]'.format(paramName))
    
    for thisStim_loop in stim_loop:
        currentLoop = stim_loop
        # abbreviate parameter names if possible (e.g. rgb = thisStim_loop.rgb)
        if thisStim_loop != None:
            for paramName in thisStim_loop:
                exec('{} = thisStim_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "stim"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        TOL_trial_text.setText("Can you solve this in exactly {num_moves} moves? \n\nPress Y for YES \nPress N for NO")
        TOL_trial_resp.keys = []
        TOL_trial_resp.rt = []
        _TOL_trial_resp_allKeys = []
        TOL_trial_image.setImage(image_stim)
        # keep track of which components have finished
        stimComponents = [TOL_trial_text, TOL_trial_resp, TOL_trial_image]
        for thisComponent in stimComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stimClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stim"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = stimClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stimClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TOL_trial_text* updates
            if TOL_trial_text.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                TOL_trial_text.frameNStart = frameN  # exact frame index
                TOL_trial_text.tStart = t  # local t and not account for scr refresh
                TOL_trial_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TOL_trial_text, 'tStartRefresh')  # time at next scr refresh
                TOL_trial_text.setAutoDraw(True)
            if TOL_trial_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TOL_trial_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    TOL_trial_text.tStop = t  # not accounting for scr refresh
                    TOL_trial_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TOL_trial_text, 'tStopRefresh')  # time at next scr refresh
                    TOL_trial_text.setAutoDraw(False)
            
            # *TOL_trial_resp* updates
            waitOnFlip = False
            if TOL_trial_resp.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
                # keep track of start time/frame for later
                TOL_trial_resp.frameNStart = frameN  # exact frame index
                TOL_trial_resp.tStart = t  # local t and not account for scr refresh
                TOL_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TOL_trial_resp, 'tStartRefresh')  # time at next scr refresh
                TOL_trial_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TOL_trial_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TOL_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TOL_trial_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TOL_trial_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    TOL_trial_resp.tStop = t  # not accounting for scr refresh
                    TOL_trial_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TOL_trial_resp, 'tStopRefresh')  # time at next scr refresh
                    TOL_trial_resp.status = FINISHED
            if TOL_trial_resp.status == STARTED and not waitOnFlip:
                theseKeys = TOL_trial_resp.getKeys(keyList=['space'], waitRelease=False)
                _TOL_trial_resp_allKeys.extend(theseKeys)
                if len(_TOL_trial_resp_allKeys):
                    TOL_trial_resp.keys = _TOL_trial_resp_allKeys[-1].name  # just the last key pressed
                    TOL_trial_resp.rt = _TOL_trial_resp_allKeys[-1].rt
                    # was this correct?
                    if (TOL_trial_resp.keys == str(match)) or (TOL_trial_resp.keys == match):
                        TOL_trial_resp.corr = 1
                    else:
                        TOL_trial_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *TOL_trial_image* updates
            if TOL_trial_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TOL_trial_image.frameNStart = frameN  # exact frame index
                TOL_trial_image.tStart = t  # local t and not account for scr refresh
                TOL_trial_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TOL_trial_image, 'tStartRefresh')  # time at next scr refresh
                TOL_trial_image.setAutoDraw(True)
            if TOL_trial_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TOL_trial_image.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    TOL_trial_image.tStop = t  # not accounting for scr refresh
                    TOL_trial_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TOL_trial_image, 'tStopRefresh')  # time at next scr refresh
                    TOL_trial_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stim"-------
        for thisComponent in stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        stim_loop.addData('TOL_trial_text.started', TOL_trial_text.tStartRefresh)
        stim_loop.addData('TOL_trial_text.stopped', TOL_trial_text.tStopRefresh)
        # check responses
        if TOL_trial_resp.keys in ['', [], None]:  # No response was made
            TOL_trial_resp.keys = None
            # was no response the correct answer?!
            if str(match).lower() == 'none':
               TOL_trial_resp.corr = 1;  # correct non-response
            else:
               TOL_trial_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for stim_loop (TrialHandler)
        stim_loop.addData('TOL_trial_resp.keys',TOL_trial_resp.keys)
        stim_loop.addData('TOL_trial_resp.corr', TOL_trial_resp.corr)
        if TOL_trial_resp.keys != None:  # we had a response
            stim_loop.addData('TOL_trial_resp.rt', TOL_trial_resp.rt)
        stim_loop.addData('TOL_trial_resp.started', TOL_trial_resp.tStartRefresh)
        stim_loop.addData('TOL_trial_resp.stopped', TOL_trial_resp.tStopRefresh)
        stim_loop.addData('TOL_trial_image.started', TOL_trial_image.tStartRefresh)
        stim_loop.addData('TOL_trial_image.stopped', TOL_trial_image.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'stim_loop'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'TOL_loop'


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
