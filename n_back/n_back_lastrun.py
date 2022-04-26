#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 20, 2022, at 15:58
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
start_time = datetime.now()
start_timestamp = int(datetime.timestamp(start_time) * 1e9)
start_time = start_time.strftime("%Y-%m-%d-%H-%M-%S-%f")

# setup markers -----
import os
cwd = os.getcwd()
kernel_socket_path = os.path.join(os.path.dirname(cwd), "main", "kernel_socket")
import sys
sys.path.insert(0, kernel_socket_path)
from kernel_socket import Marker
marker = Marker()



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'n_back'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\n_back\\n_back_lastrun.py',
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
# setup dirs and files -----
tasks_dir = os.path.dirname(_thisDir)
task_dir = os.path.join(tasks_dir, expName)
par_task_dir = os.path.join(tasks_dir, "participants", f"participant_{expInfo['participant']}", f"{str(expName)}")
data_dir = os.path.join(par_task_dir, "data")

try:
    os.mkdir(data_dir)
except:
    pass

filename = os.path.join(data_dir, f"{str(expInfo['participant'])}_{str(expInfo['session'])}_{str(expName)}_{start_time}")
thisExp.dataFileName = filename
logFile = logging.LogFile(filename +'.log', level=logging.EXP)

# task order -----
for filename in os.listdir(par_task_dir):
    if "NB_TO-" in filename:
        task_order_csv = os.path.join(par_task_dir, filename)
        
# task conditions -----
cond_dir = os.path.join(par_task_dir, f"{str(expName)}_conditions")
conds_list = os.listdir(cond_dir)

# start experiment marker -----
marker.send_marker(51, start_timestamp)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='These are the instructions for the N-back experiment. \n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "main_loop_code"
main_loop_codeClock = core.Clock()

# Initialize components for Routine "trial_instructions"
trial_instructionsClock = core.Clock()
exp_zero_back_text = visual.TextStim(win=win, name='exp_zero_back_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
exp_one_back_text = visual.TextStim(win=win, name='exp_one_back_text',
    text='This is a 1-Back trial. \n\nPress RIGHT if the current number matches the previous number. Otherwise, press LEFT.\n\nPress SPACE when you are ready to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
exp_two_back_text = visual.TextStim(win=win, name='exp_two_back_text',
    text='This is a 2-back trial. \n\nPress RIGHT if the current number matches the number two back. Otherwise, press LEFT.\n\nPress SPACE when you are ready to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
trial_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions_pause"
instructions_pauseClock = core.Clock()
pause_cross = visual.ShapeStim(
    win=win, name='pause_cross', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "stim"
stimClock = core.Clock()
stim_text = visual.TextStim(win=win, name='stim_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stim_resp = keyboard.Keyboard()
stim_cross = visual.ShapeStim(
    win=win, name='stim_cross', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

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

# set up handler to look after randomisation of conditions etc
n_back_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(task_order_csv),
    seed=None, name='n_back_loop')
thisExp.addLoop(n_back_loop)  # add the loop to the experiment
thisN_back_loop = n_back_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisN_back_loop.rgb)
if thisN_back_loop != None:
    for paramName in thisN_back_loop:
        exec('{} = thisN_back_loop[paramName]'.format(paramName))

for thisN_back_loop in n_back_loop:
    currentLoop = n_back_loop
    # abbreviate parameter names if possible (e.g. rgb = thisN_back_loop.rgb)
    if thisN_back_loop != None:
        for paramName in thisN_back_loop:
            exec('{} = thisN_back_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "main_loop_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    # path to conds file for this block -----
    for cond in conds_list:
        if cond == task_order:
            this_loop_conditions = os.path.join(cond_dir, cond)
    
    # display match number if ZB -----
    if "ZB" in task_order:
        match_num = task_order.split("-")[1].split("_")[1]
        text_display = [1, 0, 0]
    elif "OB" in task_order:
        match_num = ""
        text_display = [0, 1, 0]
    elif "TB" in task_order:
        match_num = ""
        text_display = [0, 0, 1]
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
    
    # ------Prepare to start Routine "trial_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    exp_zero_back_text.setOpacity(text_display[0])
    exp_zero_back_text.setText("This is a 0-back trial. \n\nPress RIGHT if the number is: " + str(match_num) + ".\nOtherwise, press LEFT. \n\nPress SPACE when you are ready to begin.")
    exp_one_back_text.setOpacity(text_display[1])
    exp_two_back_text.setOpacity(text_display[2])
    trial_instructions_resp.keys = []
    trial_instructions_resp.rt = []
    _trial_instructions_resp_allKeys = []
    # keep track of which components have finished
    trial_instructionsComponents = [exp_zero_back_text, exp_one_back_text, exp_two_back_text, trial_instructions_resp]
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
        
        # *exp_zero_back_text* updates
        if exp_zero_back_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exp_zero_back_text.frameNStart = frameN  # exact frame index
            exp_zero_back_text.tStart = t  # local t and not account for scr refresh
            exp_zero_back_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exp_zero_back_text, 'tStartRefresh')  # time at next scr refresh
            exp_zero_back_text.setAutoDraw(True)
        
        # *exp_one_back_text* updates
        if exp_one_back_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exp_one_back_text.frameNStart = frameN  # exact frame index
            exp_one_back_text.tStart = t  # local t and not account for scr refresh
            exp_one_back_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exp_one_back_text, 'tStartRefresh')  # time at next scr refresh
            exp_one_back_text.setAutoDraw(True)
        
        # *exp_two_back_text* updates
        if exp_two_back_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exp_two_back_text.frameNStart = frameN  # exact frame index
            exp_two_back_text.tStart = t  # local t and not account for scr refresh
            exp_two_back_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exp_two_back_text, 'tStartRefresh')  # time at next scr refresh
            exp_two_back_text.setAutoDraw(True)
        
        # *trial_instructions_resp* updates
        if trial_instructions_resp.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            trial_instructions_resp.frameNStart = frameN  # exact frame index
            trial_instructions_resp.tStart = t  # local t and not account for scr refresh
            trial_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            trial_instructions_resp.status = STARTED
            # keyboard checking is just starting
            trial_instructions_resp.clock.reset()  # now t=0
        if trial_instructions_resp.status == STARTED:
            theseKeys = trial_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
            _trial_instructions_resp_allKeys.extend(theseKeys)
            if len(_trial_instructions_resp_allKeys):
                trial_instructions_resp.keys = _trial_instructions_resp_allKeys[-1].name  # just the last key pressed
                trial_instructions_resp.rt = _trial_instructions_resp_allKeys[-1].rt
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
    # the Routine "trial_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_pause"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instructions_pauseComponents = [pause_cross]
    for thisComponent in instructions_pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions_pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pause_cross* updates
        if pause_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pause_cross.frameNStart = frameN  # exact frame index
            pause_cross.tStart = t  # local t and not account for scr refresh
            pause_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pause_cross, 'tStartRefresh')  # time at next scr refresh
            pause_cross.setAutoDraw(True)
        if pause_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pause_cross.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                pause_cross.tStop = t  # not accounting for scr refresh
                pause_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pause_cross, 'tStopRefresh')  # time at next scr refresh
                pause_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_pause"-------
    for thisComponent in instructions_pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
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
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        stim_text.setText(num_stim)
        stim_resp.keys = []
        stim_resp.rt = []
        _stim_resp_allKeys = []
        thisExp.addData("stim_begin_datetime", datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"))
        # keep track of which components have finished
        stimComponents = [stim_text, stim_resp, stim_cross]
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
            
            # *stim_text* updates
            if stim_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_text.frameNStart = frameN  # exact frame index
                stim_text.tStart = t  # local t and not account for scr refresh
                stim_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_text, 'tStartRefresh')  # time at next scr refresh
                stim_text.setAutoDraw(True)
            if stim_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_text.tStop = t  # not accounting for scr refresh
                    stim_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim_text, 'tStopRefresh')  # time at next scr refresh
                    stim_text.setAutoDraw(False)
            
            # *stim_resp* updates
            waitOnFlip = False
            if stim_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stim_resp.frameNStart = frameN  # exact frame index
                stim_resp.tStart = t  # local t and not account for scr refresh
                stim_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_resp, 'tStartRefresh')  # time at next scr refresh
                stim_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stim_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stim_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stim_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_resp.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_resp.tStop = t  # not accounting for scr refresh
                    stim_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim_resp, 'tStopRefresh')  # time at next scr refresh
                    stim_resp.status = FINISHED
            if stim_resp.status == STARTED and not waitOnFlip:
                theseKeys = stim_resp.getKeys(keyList=['right', 'left'], waitRelease=False)
                _stim_resp_allKeys.extend(theseKeys)
                if len(_stim_resp_allKeys):
                    stim_resp.keys = _stim_resp_allKeys[-1].name  # just the last key pressed
                    stim_resp.rt = _stim_resp_allKeys[-1].rt
                    # was this correct?
                    if (stim_resp.keys == str(corr_key)) or (stim_resp.keys == corr_key):
                        stim_resp.corr = 1
                    else:
                        stim_resp.corr = 0
            
            # *stim_cross* updates
            if stim_cross.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                stim_cross.frameNStart = frameN  # exact frame index
                stim_cross.tStart = t  # local t and not account for scr refresh
                stim_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_cross, 'tStartRefresh')  # time at next scr refresh
                stim_cross.setAutoDraw(True)
            if stim_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stim_cross.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_cross.tStop = t  # not accounting for scr refresh
                    stim_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim_cross, 'tStopRefresh')  # time at next scr refresh
                    stim_cross.setAutoDraw(False)
            
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
        stim_loop.addData('stim_text.started', stim_text.tStartRefresh)
        stim_loop.addData('stim_text.stopped', stim_text.tStopRefresh)
        # check responses
        if stim_resp.keys in ['', [], None]:  # No response was made
            stim_resp.keys = None
            # was no response the correct answer?!
            if str(corr_key).lower() == 'none':
               stim_resp.corr = 1;  # correct non-response
            else:
               stim_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for stim_loop (TrialHandler)
        stim_loop.addData('stim_resp.keys',stim_resp.keys)
        stim_loop.addData('stim_resp.corr', stim_resp.corr)
        if stim_resp.keys != None:  # we had a response
            stim_loop.addData('stim_resp.rt', stim_resp.rt)
        stim_loop.addData('stim_resp.started', stim_resp.tStartRefresh)
        stim_loop.addData('stim_resp.stopped', stim_resp.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'stim_loop'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'n_back_loop'

# end experiment marker -----
end_time = datetime.now()
end_timestamp = int(datetime.timestamp(end_time) * 1e9)
marker.send_marker(52, end_timestamp)

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
