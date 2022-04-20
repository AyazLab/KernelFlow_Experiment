#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 20, 2022, at 10:40
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
expName = 'go_no_go'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\go_no_go\\go_no_go_lastrun.py',
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
    if "GNG_TO-" in filename:
        task_order_csv = os.path.join(par_task_dir, filename)

# task conditions -----
cond_dir = os.path.join(par_task_dir, f"{str(expName)}_conditions")
conds_list = os.listdir(cond_dir)

# start experiment marker -----
marker.send_marker(21, start_timestamp)

# Initialize components for Routine "initial_instructions"
initial_instructionsClock = core.Clock()
initial_instructions_text = visual.TextStim(win=win, name='initial_instructions_text',
    text='You are going to see either a PUPPY or a SPIDER appear on the screen. Press SPACE as fast as you can when you see a PUPPY. Do not press anything when you see a SPIDER. \n\nWhen the image disappears, a plus sign will appear on the screen. Stare at the plus sign until the next image appears. Remember to press SPACE as fast as you can without making mistakes.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
initial_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "GNG_loop_code"
GNG_loop_codeClock = core.Clock()

# Initialize components for Routine "GNG_instructions"
GNG_instructionsClock = core.Clock()
go_instructions_text = visual.TextStim(win=win, name='go_instructions_text',
    text='This is the GO experiment. \n\nPUPPIES = GO\nOnly press SPACE when a GO stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
no_go_instructions_text = visual.TextStim(win=win, name='no_go_instructions_text',
    text='This is the GO/NO-GO experiment. \n\nPUPPIES = GO\nSPIDERS = NO-GO\n\nPress SPACE when a GO stimulus appears.\nDo not press anything when a NO-GO stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
GNG_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
inter_stim_plus = visual.ShapeStim(
    win=win, name='inter_stim_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "GNG_trial"
GNG_trialClock = core.Clock()
go_resp = keyboard.Keyboard()
go_plus = visual.ShapeStim(
    win=win, name='go_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
go_image = visual.ImageStim(
    win=win,
    name='go_image', 
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
GNG_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(task_order_csv),
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
    for cond in conds_list:
        if cond == task_order:
            this_loop_conditions = os.path.join(cond_dir, cond)
            
    # instructions text display -----
    if "go" in task_order:
        text_display = [1, 0]
    elif "GNG" in task_order:
        text_display = [0, 1]
    
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
    
    # ------Prepare to start Routine "GNG_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    go_instructions_text.setOpacity(text_display[0])
    no_go_instructions_text.setOpacity(text_display[1])
    GNG_instructions_resp.keys = []
    GNG_instructions_resp.rt = []
    _GNG_instructions_resp_allKeys = []
    # keep track of which components have finished
    GNG_instructionsComponents = [go_instructions_text, no_go_instructions_text, GNG_instructions_resp]
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
        
        # *go_instructions_text* updates
        if go_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            go_instructions_text.frameNStart = frameN  # exact frame index
            go_instructions_text.tStart = t  # local t and not account for scr refresh
            go_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go_instructions_text, 'tStartRefresh')  # time at next scr refresh
            go_instructions_text.setAutoDraw(True)
        
        # *no_go_instructions_text* updates
        if no_go_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no_go_instructions_text.frameNStart = frameN  # exact frame index
            no_go_instructions_text.tStart = t  # local t and not account for scr refresh
            no_go_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_go_instructions_text, 'tStartRefresh')  # time at next scr refresh
            no_go_instructions_text.setAutoDraw(True)
        
        # *GNG_instructions_resp* updates
        if GNG_instructions_resp.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            GNG_instructions_resp.frameNStart = frameN  # exact frame index
            GNG_instructions_resp.tStart = t  # local t and not account for scr refresh
            GNG_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GNG_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            GNG_instructions_resp.status = STARTED
            # keyboard checking is just starting
            GNG_instructions_resp.clock.reset()  # now t=0
        if GNG_instructions_resp.status == STARTED:
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
    # the Routine "GNG_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    GNG_block = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(this_loop_conditions),
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
        
        # ------Prepare to start Routine "inter_stim_interval"-------
        continueRoutine = True
        # update component parameters for each repeat
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
        go_resp.keys = []
        go_resp.rt = []
        _go_resp_allKeys = []
        go_image.setImage(go_stim)
        # keep track of which components have finished
        GNG_trialComponents = [go_resp, go_plus, go_image]
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
            
            # *go_image* updates
            if go_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                go_image.frameNStart = frameN  # exact frame index
                go_image.tStart = t  # local t and not account for scr refresh
                go_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go_image, 'tStartRefresh')  # time at next scr refresh
                go_image.setAutoDraw(True)
            if go_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > go_image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    go_image.tStop = t  # not accounting for scr refresh
                    go_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(go_image, 'tStopRefresh')  # time at next scr refresh
                    go_image.setAutoDraw(False)
            
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
        # check responses
        if go_resp.keys in ['', [], None]:  # No response was made
            go_resp.keys = None
            # was no response the correct answer?!
            if str(corr_key).lower() == 'none':
               go_resp.corr = 1;  # correct non-response
            else:
               go_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for GNG_block (TrialHandler)
        GNG_block.addData('go_resp.keys',go_resp.keys)
        GNG_block.addData('go_resp.corr', go_resp.corr)
        if go_resp.keys != None:  # we had a response
            GNG_block.addData('go_resp.rt', go_resp.rt)
        GNG_block.addData('go_resp.started', go_resp.tStartRefresh)
        GNG_block.addData('go_resp.stopped', go_resp.tStopRefresh)
        GNG_block.addData('go_image.started', go_image.tStartRefresh)
        GNG_block.addData('go_image.stopped', go_image.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'GNG_block'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'GNG_loop'

# end experiment marker -----
end_time = datetime.now()
end_timestamp = int(datetime.timestamp(start_time) * 1e9)
marker.send_marker(22, end_timestamp)

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
