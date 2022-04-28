#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 27, 2022, at 20:16
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
expName = 'vSAT'  # from the Builder filename that created this script
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
par_task_dir = os.path.join(tasks_dir, "participants", f"participant_{expInfo['participant']}", f"{str(expName)}")
data_dir = os.path.join(par_task_dir, "data")
print("DATA DIR ", data_dir)

try:
    os.mkdir(data_dir)
except:
    pass

filename = os.path.join(data_dir, f"{str(expInfo['participant'])}_{str(expInfo['session'])}_{str(expName)}_{start_time}")
thisExp.dataFileName = filename
logFile = logging.LogFile(filename + '.log', level=logging.EXP)

# task order -----
for task_filename in os.listdir(par_task_dir):
    if "vSAT_TO-" in task_filename:
        task_order_csv = os.path.join(par_task_dir, task_filename)

# task conditions -----
cond_dir = os.path.join(par_task_dir, f"{str(expName)}_conditions")
conds_list = os.listdir(cond_dir)

# start experiment marker -----
marker.send_marker(91, start_timestamp)

# Initialize components for Routine "initial_instructions"
initial_instructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='This is the Visuospatial Sustained Attention (vSAT) Task. \n\nPress RIGHT as soon as you hear the tone if a stimulus appeared. \nPress LEFT as soon as you hear the tone if a stimulus did not appear.\n\nYou will hear a second, higher pitched tone only after a correct response.\n\nPress SPACE to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "main_loop_code"
main_loop_codeClock = core.Clock()

# Initialize components for Routine "experiment_instructions"
experiment_instructionsClock = core.Clock()
experiment_SAT_text = visual.TextStim(win=win, name='experiment_SAT_text',
    text='This is a SAT trial.\n\nRemember, the stimulus will appear in the center of the screen. \n\nPress SPACE to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
experiment_vSAT_text = visual.TextStim(win=win, name='experiment_vSAT_text',
    text='This is a vSAT trial.\n\nRemember, the stimulus will appear in different locations on the screen. \n\nPress SPACE to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
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

# Initialize components for Routine "signal_response"
signal_responseClock = core.Clock()
stim_resp = keyboard.Keyboard()
response_sound = sound.Sound('A', secs=0.43, stereo=True, hamming=True,
    name='response_sound')
response_sound.setVolume(1.0)

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
main_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(task_order_csv),
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
    for cond in conds_list:
        if cond == task_order:
            this_loop_conditions = os.path.join(cond_dir, cond)
            
    # instructions text display -----
    if "vSAT_stims" in task_order:
        text_display = [1, 0]
    else:  # SAT
        text_display = [0, 1]
    
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
    experiment_SAT_text.setOpacity(text_display[1])
    experiment_vSAT_text.setOpacity(text_display[0])
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
        if experiment_instructions_rep.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            experiment_instructions_rep.frameNStart = frameN  # exact frame index
            experiment_instructions_rep.tStart = t  # local t and not account for scr refresh
            experiment_instructions_rep.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(experiment_instructions_rep, 'tStartRefresh')  # time at next scr refresh
            experiment_instructions_rep.status = STARTED
            # keyboard checking is just starting
            experiment_instructions_rep.clock.reset()  # now t=0
        if experiment_instructions_rep.status == STARTED:
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
        vSAT_square.setOpacity(int(match))
        vSAT_square.setPos([x_pos, y_pos])
        thisExp.addData("stim_begin_datetime", datetime.now().strftime("%Y-%m-%d_%H:%M:%S.%f"))
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
        
        # ------Prepare to start Routine "signal_response"-------
        continueRoutine = True
        routineTimer.add(2.030000)
        # update component parameters for each repeat
        stim_resp.keys = []
        stim_resp.rt = []
        _stim_resp_allKeys = []
        response_sound.setSound('A', secs=0.43, hamming=True)
        response_sound.setVolume(1.0, log=False)
        # keep track of which components have finished
        signal_responseComponents = [stim_resp, response_sound]
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
                if tThisFlipGlobal > stim_resp.tStartRefresh + 2.03-frameTolerance:
                    # keep track of stop time/frame for later
                    stim_resp.tStop = t  # not accounting for scr refresh
                    stim_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stim_resp, 'tStopRefresh')  # time at next scr refresh
                    stim_resp.status = FINISHED
            if stim_resp.status == STARTED and not waitOnFlip:
                theseKeys = stim_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _stim_resp_allKeys.extend(theseKeys)
                if len(_stim_resp_allKeys):
                    stim_resp.keys = _stim_resp_allKeys[-1].name  # just the last key pressed
                    stim_resp.rt = _stim_resp_allKeys[-1].rt
                    # was this correct?
                    if (stim_resp.keys == str(corr_key)) or (stim_resp.keys == corr_key):
                        stim_resp.corr = 1
                    else:
                        stim_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # start/stop response_sound
            if response_sound.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
                # keep track of start time/frame for later
                response_sound.frameNStart = frameN  # exact frame index
                response_sound.tStart = t  # local t and not account for scr refresh
                response_sound.tStartRefresh = tThisFlipGlobal  # on global time
                response_sound.play(when=win)  # sync with win flip
            if response_sound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response_sound.tStartRefresh + 0.43-frameTolerance:
                    # keep track of stop time/frame for later
                    response_sound.tStop = t  # not accounting for scr refresh
                    response_sound.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response_sound, 'tStopRefresh')  # time at next scr refresh
                    response_sound.stop()
            
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
        # check responses
        if stim_resp.keys in ['', [], None]:  # No response was made
            stim_resp.keys = None
            # was no response the correct answer?!
            if str(corr_key).lower() == 'none':
               stim_resp.corr = 1;  # correct non-response
            else:
               stim_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for vSAT_loop (TrialHandler)
        vSAT_loop.addData('stim_resp.keys',stim_resp.keys)
        vSAT_loop.addData('stim_resp.corr', stim_resp.corr)
        if stim_resp.keys != None:  # we had a response
            vSAT_loop.addData('stim_resp.rt', stim_resp.rt)
        vSAT_loop.addData('stim_resp.started', stim_resp.tStartRefresh)
        vSAT_loop.addData('stim_resp.stopped', stim_resp.tStopRefresh)
        response_sound.stop()  # ensure sound has stopped at end of routine
        vSAT_loop.addData('response_sound.started', response_sound.tStartRefresh)
        vSAT_loop.addData('response_sound.stopped', response_sound.tStopRefresh)
        
        # ------Prepare to start Routine "signal_response_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        if match == 1 and stim_resp.keys == "right":   # if stim and right
            correct_resp = 1
        elif match == 0 and stim_resp.keys == "left":  # if no stim and left 
            correct_resp = 1
        else:                                          # if incorrect response
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

# end experiment marker -----
end_time = datetime.now()
end_timestamp = int(datetime.timestamp(end_time) * 1e9)
marker.send_marker(92, end_timestamp)

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
