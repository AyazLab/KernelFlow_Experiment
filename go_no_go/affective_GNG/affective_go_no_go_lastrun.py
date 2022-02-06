#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 06, 2022, at 14:48
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\go_no_go\\affective_GNG\\affective_go_no_go_lastrun.py',
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
exp_dir = os.getcwd()
loop_num = -1  # increased by 1 each loop 

GNG_conditions_dir = r"C:\Users\zackg\OneDrive\Ayaz Lab\KernelFlow_PsychoPy\go_no_go\affective_GNG\affective_GNG_conditions"
os.chdir(GNG_conditions_dir)
csv_list = os.listdir(os.getcwd())

go_csv_list = []
GNG_csv_list = []

for csv_filename in csv_list:
    if "go" in csv_filename:
        go_csv_list.append(os.path.join("affective_GNG_conditions", csv_filename))
    elif "GNG" in csv_filename:
        GNG_csv_list.append(os.path.join("affective_GNG_conditions", csv_filename))
        
os.chdir(exp_dir)

# Initialize components for Routine "GNG_loop_code"
GNG_loop_codeClock = core.Clock()

# Initialize components for Routine "go_instructions"
go_instructionsClock = core.Clock()
go_instructions_text = visual.TextStim(win=win, name='go_instructions_text',
    text='This is the Go experiment. \n\nPuppies = Go\n\nPress SPACE when a Go stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
go_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "inter_stim_time_code"
inter_stim_time_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
inter_stim_text = visual.TextStim(win=win, name='inter_stim_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "go_stimulus"
go_stimulusClock = core.Clock()
go_image = visual.ImageStim(
    win=win,
    name='go_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
go_resp = keyboard.Keyboard()

# Initialize components for Routine "response_interval"
response_intervalClock = core.Clock()
response_interval_text = visual.TextStim(win=win, name='response_interval_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GNG_instructions"
GNG_instructionsClock = core.Clock()
GNG_instructions_text = visual.TextStim(win=win, name='GNG_instructions_text',
    text='This is the Go/No-Go experiment. \n\nPuppies = Go\nSpiders = No-Go\n\nPress SPACE when a Go stimulus appears.\nDo not press anything when a No-Go stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GNG_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "inter_stim_time_code"
inter_stim_time_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
inter_stim_text = visual.TextStim(win=win, name='inter_stim_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "GNG_stimulus"
GNG_stimulusClock = core.Clock()
GNG_image = visual.ImageStim(
    win=win,
    name='GNG_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "response_interval"
response_intervalClock = core.Clock()
response_interval_text = visual.TextStim(win=win, name='response_interval_text',
    text=None,
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
    # This code will randomize the Go and 
    # No-Go condition datasets each loop
    
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
        waitOnFlip = False
        if go_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            go_instructions_resp.frameNStart = frameN  # exact frame index
            go_instructions_resp.tStart = t  # local t and not account for scr refresh
            go_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go_instructions_resp, 'tStartRefresh')  # time at next scr refresh
            go_instructions_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(go_instructions_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(go_instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if go_instructions_resp.status == STARTED and not waitOnFlip:
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
    GNG_loop.addData('go_instructions_text.started', go_instructions_text.tStartRefresh)
    GNG_loop.addData('go_instructions_text.stopped', go_instructions_text.tStopRefresh)
    # check responses
    if go_instructions_resp.keys in ['', [], None]:  # No response was made
        go_instructions_resp.keys = None
    GNG_loop.addData('go_instructions_resp.keys',go_instructions_resp.keys)
    if go_instructions_resp.keys != None:  # we had a response
        GNG_loop.addData('go_instructions_resp.rt', go_instructions_resp.rt)
    GNG_loop.addData('go_instructions_resp.started', go_instructions_resp.tStartRefresh)
    GNG_loop.addData('go_instructions_resp.stopped', go_instructions_resp.tStopRefresh)
    # the Routine "go_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    go_block = data.TrialHandler(nReps=1.0, method='random', 
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
        
        # ------Prepare to start Routine "inter_stim_time_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        import random
        stim_time = random.randint(4, 7)
        # keep track of which components have finished
        inter_stim_time_codeComponents = []
        for thisComponent in inter_stim_time_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stim_time_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stim_time_code"-------
        while continueRoutine:
            # get current time
            t = inter_stim_time_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stim_time_codeClock)
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
            for thisComponent in inter_stim_time_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stim_time_code"-------
        for thisComponent in inter_stim_time_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "inter_stim_time_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "inter_stim_interval"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        inter_stim_intervalComponents = [inter_stim_text]
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
                if tThisFlipGlobal > inter_stim_text.tStartRefresh + stim_time-frameTolerance:
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
        go_block.addData('inter_stim_text.started', inter_stim_text.tStartRefresh)
        go_block.addData('inter_stim_text.stopped', inter_stim_text.tStopRefresh)
        # the Routine "inter_stim_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "go_stimulus"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        go_image.setImage(go_stim)
        go_resp.keys = []
        go_resp.rt = []
        _go_resp_allKeys = []
        # keep track of which components have finished
        go_stimulusComponents = [go_image, go_resp]
        for thisComponent in go_stimulusComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        go_stimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "go_stimulus"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = go_stimulusClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=go_stimulusClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
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
                if tThisFlipGlobal > go_resp.tStartRefresh + 0.5-frameTolerance:
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
                    if (go_resp.keys == str(match)) or (go_resp.keys == match):
                        go_resp.corr = 1
                    else:
                        go_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in go_stimulusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "go_stimulus"-------
        for thisComponent in go_stimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        go_block.addData('go_image.started', go_image.tStartRefresh)
        go_block.addData('go_image.stopped', go_image.tStopRefresh)
        # check responses
        if go_resp.keys in ['', [], None]:  # No response was made
            go_resp.keys = None
            # was no response the correct answer?!
            if str(match).lower() == 'none':
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
        
        # ------Prepare to start Routine "response_interval"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        response_intervalComponents = [response_interval_text]
        for thisComponent in response_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response_interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = response_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_interval_text* updates
            if response_interval_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_interval_text.frameNStart = frameN  # exact frame index
                response_interval_text.tStart = t  # local t and not account for scr refresh
                response_interval_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_interval_text, 'tStartRefresh')  # time at next scr refresh
                response_interval_text.setAutoDraw(True)
            if response_interval_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response_interval_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    response_interval_text.tStop = t  # not accounting for scr refresh
                    response_interval_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response_interval_text, 'tStopRefresh')  # time at next scr refresh
                    response_interval_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response_interval"-------
        for thisComponent in response_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        go_block.addData('response_interval_text.started', response_interval_text.tStartRefresh)
        go_block.addData('response_interval_text.stopped', response_interval_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'go_block'
    
    
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
        if GNG_instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    GNG_loop.addData('GNG_instructions_text.started', GNG_instructions_text.tStartRefresh)
    GNG_loop.addData('GNG_instructions_text.stopped', GNG_instructions_text.tStopRefresh)
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
    
    # set up handler to look after randomisation of conditions etc
    GNG_block = data.TrialHandler(nReps=1.0, method='random', 
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
        
        # ------Prepare to start Routine "inter_stim_time_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        import random
        stim_time = random.randint(4, 7)
        # keep track of which components have finished
        inter_stim_time_codeComponents = []
        for thisComponent in inter_stim_time_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stim_time_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stim_time_code"-------
        while continueRoutine:
            # get current time
            t = inter_stim_time_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stim_time_codeClock)
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
            for thisComponent in inter_stim_time_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stim_time_code"-------
        for thisComponent in inter_stim_time_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "inter_stim_time_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "inter_stim_interval"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        inter_stim_intervalComponents = [inter_stim_text]
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
                if tThisFlipGlobal > inter_stim_text.tStartRefresh + stim_time-frameTolerance:
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
        GNG_block.addData('inter_stim_text.started', inter_stim_text.tStartRefresh)
        GNG_block.addData('inter_stim_text.stopped', inter_stim_text.tStopRefresh)
        # the Routine "inter_stim_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "GNG_stimulus"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        GNG_image.setImage(GNG_stim)
        # keep track of which components have finished
        GNG_stimulusComponents = [GNG_image]
        for thisComponent in GNG_stimulusComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        GNG_stimulusClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "GNG_stimulus"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = GNG_stimulusClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=GNG_stimulusClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *GNG_image* updates
            if GNG_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                GNG_image.frameNStart = frameN  # exact frame index
                GNG_image.tStart = t  # local t and not account for scr refresh
                GNG_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GNG_image, 'tStartRefresh')  # time at next scr refresh
                GNG_image.setAutoDraw(True)
            if GNG_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GNG_image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    GNG_image.tStop = t  # not accounting for scr refresh
                    GNG_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(GNG_image, 'tStopRefresh')  # time at next scr refresh
                    GNG_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GNG_stimulusComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "GNG_stimulus"-------
        for thisComponent in GNG_stimulusComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        GNG_block.addData('GNG_image.started', GNG_image.tStartRefresh)
        GNG_block.addData('GNG_image.stopped', GNG_image.tStopRefresh)
        
        # ------Prepare to start Routine "response_interval"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        response_intervalComponents = [response_interval_text]
        for thisComponent in response_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        response_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "response_interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = response_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=response_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response_interval_text* updates
            if response_interval_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response_interval_text.frameNStart = frameN  # exact frame index
                response_interval_text.tStart = t  # local t and not account for scr refresh
                response_interval_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response_interval_text, 'tStartRefresh')  # time at next scr refresh
                response_interval_text.setAutoDraw(True)
            if response_interval_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response_interval_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    response_interval_text.tStop = t  # not accounting for scr refresh
                    response_interval_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response_interval_text, 'tStopRefresh')  # time at next scr refresh
                    response_interval_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in response_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "response_interval"-------
        for thisComponent in response_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        GNG_block.addData('response_interval_text.started', response_interval_text.tStartRefresh)
        GNG_block.addData('response_interval_text.stopped', response_interval_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'GNG_block'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'GNG_loop'


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
