#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 05, 2022, at 15:20
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

import os
csv_dir = r"C:\Users\zackg\OneDrive\Ayaz Lab\KernelFlow_PsychoPy\n_back\n_back_conditions"

# create file names and paths for each condition
for filename in os.listdir(csv_dir):
    if "zero" in filename:
        zero_csv = filename
        zero_csv_path = os.path.join(csv_dir, zero_csv)
    elif "one" in filename:
        one_csv = filename
        one_csv_path = os.path.join(csv_dir, one_csv)
    elif "two" in filename:
        two_csv = filename
        two_csv_path = os.path.join(csv_dir, two_csv)

# get stimulus condition for 0-back
split_csv = zero_csv.split("-")
split_match = split_csv[1].split("_")
match = split_match[1]


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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\n_back\\psychopy\\n_back_lastrun.py',
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
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
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

# Initialize components for Routine "code_setup"
code_setupClock = core.Clock()

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

# Initialize components for Routine "zero_back_prompt"
zero_back_promptClock = core.Clock()
zero_back_prompt_text = visual.TextStim(win=win, name='zero_back_prompt_text',
    text="0-back trial. \n\n Press SPACE if the number is: " + str(match),
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_zero_back"
trial_zero_backClock = core.Clock()
zero_back_num_stim = visual.TextStim(win=win, name='zero_back_num_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
zero_back_resp = keyboard.Keyboard()

# Initialize components for Routine "inter_stimuli_interval"
inter_stimuli_intervalClock = core.Clock()
inter_stimuli_interval_text = visual.TextStim(win=win, name='inter_stimuli_interval_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "one_back_prompt"
one_back_promptClock = core.Clock()
one_back_prompt_text = visual.TextStim(win=win, name='one_back_prompt_text',
    text='1-back trial. \n\nPress SPACE if the current number matches the previous number.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_one_back"
trial_one_backClock = core.Clock()
one_back_num_stim = visual.TextStim(win=win, name='one_back_num_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
one_back_resp = keyboard.Keyboard()

# Initialize components for Routine "inter_stimuli_interval"
inter_stimuli_intervalClock = core.Clock()
inter_stimuli_interval_text = visual.TextStim(win=win, name='inter_stimuli_interval_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "two_back_prompt"
two_back_promptClock = core.Clock()
two_back_prompt_text = visual.TextStim(win=win, name='two_back_prompt_text',
    text='2-back trial. \n\nPress SPACE if the current number matches the number two back.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_two_back"
trial_two_backClock = core.Clock()
two_back_num_stim = visual.TextStim(win=win, name='two_back_num_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
two_back_resp = keyboard.Keyboard()

# Initialize components for Routine "inter_stimuli_interval"
inter_stimuli_intervalClock = core.Clock()
inter_stimuli_interval_text = visual.TextStim(win=win, name='inter_stimuli_interval_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "code_setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
code_setupComponents = []
for thisComponent in code_setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
code_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "code_setup"-------
while continueRoutine:
    # get current time
    t = code_setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=code_setupClock)
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
    for thisComponent in code_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "code_setup"-------
for thisComponent in code_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "code_setup" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "zero_back_prompt"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
zero_back_promptComponents = [zero_back_prompt_text]
for thisComponent in zero_back_promptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
zero_back_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "zero_back_prompt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = zero_back_promptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=zero_back_promptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *zero_back_prompt_text* updates
    if zero_back_prompt_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        zero_back_prompt_text.frameNStart = frameN  # exact frame index
        zero_back_prompt_text.tStart = t  # local t and not account for scr refresh
        zero_back_prompt_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(zero_back_prompt_text, 'tStartRefresh')  # time at next scr refresh
        zero_back_prompt_text.setAutoDraw(True)
    if zero_back_prompt_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > zero_back_prompt_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            zero_back_prompt_text.tStop = t  # not accounting for scr refresh
            zero_back_prompt_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(zero_back_prompt_text, 'tStopRefresh')  # time at next scr refresh
            zero_back_prompt_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in zero_back_promptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "zero_back_prompt"-------
for thisComponent in zero_back_promptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('zero_back_prompt_text.started', zero_back_prompt_text.tStartRefresh)
thisExp.addData('zero_back_prompt_text.stopped', zero_back_prompt_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
zero_back_outer_loop = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='zero_back_outer_loop')
thisExp.addLoop(zero_back_outer_loop)  # add the loop to the experiment
thisZero_back_outer_loop = zero_back_outer_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisZero_back_outer_loop.rgb)
if thisZero_back_outer_loop != None:
    for paramName in thisZero_back_outer_loop:
        exec('{} = thisZero_back_outer_loop[paramName]'.format(paramName))

for thisZero_back_outer_loop in zero_back_outer_loop:
    currentLoop = zero_back_outer_loop
    # abbreviate parameter names if possible (e.g. rgb = thisZero_back_outer_loop.rgb)
    if thisZero_back_outer_loop != None:
        for paramName in thisZero_back_outer_loop:
            exec('{} = thisZero_back_outer_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    zero_back_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(zero_csv_path),
        seed=None, name='zero_back_loop')
    thisExp.addLoop(zero_back_loop)  # add the loop to the experiment
    thisZero_back_loop = zero_back_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisZero_back_loop.rgb)
    if thisZero_back_loop != None:
        for paramName in thisZero_back_loop:
            exec('{} = thisZero_back_loop[paramName]'.format(paramName))
    
    for thisZero_back_loop in zero_back_loop:
        currentLoop = zero_back_loop
        # abbreviate parameter names if possible (e.g. rgb = thisZero_back_loop.rgb)
        if thisZero_back_loop != None:
            for paramName in thisZero_back_loop:
                exec('{} = thisZero_back_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_zero_back"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        zero_back_num_stim.setText(num_stim)
        zero_back_resp.keys = []
        zero_back_resp.rt = []
        _zero_back_resp_allKeys = []
        # keep track of which components have finished
        trial_zero_backComponents = [zero_back_num_stim, zero_back_resp]
        for thisComponent in trial_zero_backComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_zero_backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_zero_back"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_zero_backClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_zero_backClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *zero_back_num_stim* updates
            if zero_back_num_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                zero_back_num_stim.frameNStart = frameN  # exact frame index
                zero_back_num_stim.tStart = t  # local t and not account for scr refresh
                zero_back_num_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(zero_back_num_stim, 'tStartRefresh')  # time at next scr refresh
                zero_back_num_stim.setAutoDraw(True)
            if zero_back_num_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > zero_back_num_stim.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    zero_back_num_stim.tStop = t  # not accounting for scr refresh
                    zero_back_num_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(zero_back_num_stim, 'tStopRefresh')  # time at next scr refresh
                    zero_back_num_stim.setAutoDraw(False)
            
            # *zero_back_resp* updates
            waitOnFlip = False
            if zero_back_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                zero_back_resp.frameNStart = frameN  # exact frame index
                zero_back_resp.tStart = t  # local t and not account for scr refresh
                zero_back_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(zero_back_resp, 'tStartRefresh')  # time at next scr refresh
                zero_back_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(zero_back_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(zero_back_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if zero_back_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > zero_back_resp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    zero_back_resp.tStop = t  # not accounting for scr refresh
                    zero_back_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(zero_back_resp, 'tStopRefresh')  # time at next scr refresh
                    zero_back_resp.status = FINISHED
            if zero_back_resp.status == STARTED and not waitOnFlip:
                theseKeys = zero_back_resp.getKeys(keyList=['space'], waitRelease=False)
                _zero_back_resp_allKeys.extend(theseKeys)
                if len(_zero_back_resp_allKeys):
                    zero_back_resp.keys = _zero_back_resp_allKeys[-1].name  # just the last key pressed
                    zero_back_resp.rt = _zero_back_resp_allKeys[-1].rt
                    # was this correct?
                    if (zero_back_resp.keys == str(match)) or (zero_back_resp.keys == match):
                        zero_back_resp.corr = 1
                    else:
                        zero_back_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_zero_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_zero_back"-------
        for thisComponent in trial_zero_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        zero_back_loop.addData('zero_back_num_stim.started', zero_back_num_stim.tStartRefresh)
        zero_back_loop.addData('zero_back_num_stim.stopped', zero_back_num_stim.tStopRefresh)
        # check responses
        if zero_back_resp.keys in ['', [], None]:  # No response was made
            zero_back_resp.keys = None
            # was no response the correct answer?!
            if str(match).lower() == 'none':
               zero_back_resp.corr = 1;  # correct non-response
            else:
               zero_back_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for zero_back_loop (TrialHandler)
        zero_back_loop.addData('zero_back_resp.keys',zero_back_resp.keys)
        zero_back_loop.addData('zero_back_resp.corr', zero_back_resp.corr)
        if zero_back_resp.keys != None:  # we had a response
            zero_back_loop.addData('zero_back_resp.rt', zero_back_resp.rt)
        zero_back_loop.addData('zero_back_resp.started', zero_back_resp.tStartRefresh)
        zero_back_loop.addData('zero_back_resp.stopped', zero_back_resp.tStopRefresh)
        
        # ------Prepare to start Routine "inter_stimuli_interval"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        inter_stimuli_intervalComponents = [inter_stimuli_interval_text]
        for thisComponent in inter_stimuli_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stimuli_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stimuli_interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = inter_stimuli_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stimuli_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_stimuli_interval_text* updates
            if inter_stimuli_interval_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_stimuli_interval_text.frameNStart = frameN  # exact frame index
                inter_stimuli_interval_text.tStart = t  # local t and not account for scr refresh
                inter_stimuli_interval_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_stimuli_interval_text, 'tStartRefresh')  # time at next scr refresh
                inter_stimuli_interval_text.setAutoDraw(True)
            if inter_stimuli_interval_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_stimuli_interval_text.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_stimuli_interval_text.tStop = t  # not accounting for scr refresh
                    inter_stimuli_interval_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_stimuli_interval_text, 'tStopRefresh')  # time at next scr refresh
                    inter_stimuli_interval_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inter_stimuli_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stimuli_interval"-------
        for thisComponent in inter_stimuli_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        zero_back_loop.addData('inter_stimuli_interval_text.started', inter_stimuli_interval_text.tStartRefresh)
        zero_back_loop.addData('inter_stimuli_interval_text.stopped', inter_stimuli_interval_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'zero_back_loop'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'zero_back_outer_loop'


# ------Prepare to start Routine "one_back_prompt"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
one_back_promptComponents = [one_back_prompt_text]
for thisComponent in one_back_promptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
one_back_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "one_back_prompt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = one_back_promptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=one_back_promptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *one_back_prompt_text* updates
    if one_back_prompt_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        one_back_prompt_text.frameNStart = frameN  # exact frame index
        one_back_prompt_text.tStart = t  # local t and not account for scr refresh
        one_back_prompt_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one_back_prompt_text, 'tStartRefresh')  # time at next scr refresh
        one_back_prompt_text.setAutoDraw(True)
    if one_back_prompt_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > one_back_prompt_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            one_back_prompt_text.tStop = t  # not accounting for scr refresh
            one_back_prompt_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(one_back_prompt_text, 'tStopRefresh')  # time at next scr refresh
            one_back_prompt_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in one_back_promptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "one_back_prompt"-------
for thisComponent in one_back_promptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('one_back_prompt_text.started', one_back_prompt_text.tStartRefresh)
thisExp.addData('one_back_prompt_text.stopped', one_back_prompt_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
one_back_outer_loop = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='one_back_outer_loop')
thisExp.addLoop(one_back_outer_loop)  # add the loop to the experiment
thisOne_back_outer_loop = one_back_outer_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisOne_back_outer_loop.rgb)
if thisOne_back_outer_loop != None:
    for paramName in thisOne_back_outer_loop:
        exec('{} = thisOne_back_outer_loop[paramName]'.format(paramName))

for thisOne_back_outer_loop in one_back_outer_loop:
    currentLoop = one_back_outer_loop
    # abbreviate parameter names if possible (e.g. rgb = thisOne_back_outer_loop.rgb)
    if thisOne_back_outer_loop != None:
        for paramName in thisOne_back_outer_loop:
            exec('{} = thisOne_back_outer_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    one_back_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(one_csv_path),
        seed=None, name='one_back_loop')
    thisExp.addLoop(one_back_loop)  # add the loop to the experiment
    thisOne_back_loop = one_back_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOne_back_loop.rgb)
    if thisOne_back_loop != None:
        for paramName in thisOne_back_loop:
            exec('{} = thisOne_back_loop[paramName]'.format(paramName))
    
    for thisOne_back_loop in one_back_loop:
        currentLoop = one_back_loop
        # abbreviate parameter names if possible (e.g. rgb = thisOne_back_loop.rgb)
        if thisOne_back_loop != None:
            for paramName in thisOne_back_loop:
                exec('{} = thisOne_back_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_one_back"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        one_back_num_stim.setText(num_stim)
        one_back_resp.keys = []
        one_back_resp.rt = []
        _one_back_resp_allKeys = []
        # keep track of which components have finished
        trial_one_backComponents = [one_back_num_stim, one_back_resp]
        for thisComponent in trial_one_backComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_one_backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_one_back"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_one_backClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_one_backClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *one_back_num_stim* updates
            if one_back_num_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                one_back_num_stim.frameNStart = frameN  # exact frame index
                one_back_num_stim.tStart = t  # local t and not account for scr refresh
                one_back_num_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one_back_num_stim, 'tStartRefresh')  # time at next scr refresh
                one_back_num_stim.setAutoDraw(True)
            if one_back_num_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > one_back_num_stim.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    one_back_num_stim.tStop = t  # not accounting for scr refresh
                    one_back_num_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(one_back_num_stim, 'tStopRefresh')  # time at next scr refresh
                    one_back_num_stim.setAutoDraw(False)
            
            # *one_back_resp* updates
            waitOnFlip = False
            if one_back_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                one_back_resp.frameNStart = frameN  # exact frame index
                one_back_resp.tStart = t  # local t and not account for scr refresh
                one_back_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one_back_resp, 'tStartRefresh')  # time at next scr refresh
                one_back_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(one_back_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(one_back_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if one_back_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > one_back_resp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    one_back_resp.tStop = t  # not accounting for scr refresh
                    one_back_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(one_back_resp, 'tStopRefresh')  # time at next scr refresh
                    one_back_resp.status = FINISHED
            if one_back_resp.status == STARTED and not waitOnFlip:
                theseKeys = one_back_resp.getKeys(keyList=['space'], waitRelease=False)
                _one_back_resp_allKeys.extend(theseKeys)
                if len(_one_back_resp_allKeys):
                    one_back_resp.keys = _one_back_resp_allKeys[-1].name  # just the last key pressed
                    one_back_resp.rt = _one_back_resp_allKeys[-1].rt
                    # was this correct?
                    if (one_back_resp.keys == str(match)) or (one_back_resp.keys == match):
                        one_back_resp.corr = 1
                    else:
                        one_back_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_one_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_one_back"-------
        for thisComponent in trial_one_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        one_back_loop.addData('one_back_num_stim.started', one_back_num_stim.tStartRefresh)
        one_back_loop.addData('one_back_num_stim.stopped', one_back_num_stim.tStopRefresh)
        # check responses
        if one_back_resp.keys in ['', [], None]:  # No response was made
            one_back_resp.keys = None
            # was no response the correct answer?!
            if str(match).lower() == 'none':
               one_back_resp.corr = 1;  # correct non-response
            else:
               one_back_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for one_back_loop (TrialHandler)
        one_back_loop.addData('one_back_resp.keys',one_back_resp.keys)
        one_back_loop.addData('one_back_resp.corr', one_back_resp.corr)
        if one_back_resp.keys != None:  # we had a response
            one_back_loop.addData('one_back_resp.rt', one_back_resp.rt)
        one_back_loop.addData('one_back_resp.started', one_back_resp.tStartRefresh)
        one_back_loop.addData('one_back_resp.stopped', one_back_resp.tStopRefresh)
        
        # ------Prepare to start Routine "inter_stimuli_interval"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        inter_stimuli_intervalComponents = [inter_stimuli_interval_text]
        for thisComponent in inter_stimuli_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stimuli_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stimuli_interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = inter_stimuli_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stimuli_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_stimuli_interval_text* updates
            if inter_stimuli_interval_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_stimuli_interval_text.frameNStart = frameN  # exact frame index
                inter_stimuli_interval_text.tStart = t  # local t and not account for scr refresh
                inter_stimuli_interval_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_stimuli_interval_text, 'tStartRefresh')  # time at next scr refresh
                inter_stimuli_interval_text.setAutoDraw(True)
            if inter_stimuli_interval_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_stimuli_interval_text.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_stimuli_interval_text.tStop = t  # not accounting for scr refresh
                    inter_stimuli_interval_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_stimuli_interval_text, 'tStopRefresh')  # time at next scr refresh
                    inter_stimuli_interval_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inter_stimuli_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stimuli_interval"-------
        for thisComponent in inter_stimuli_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        one_back_loop.addData('inter_stimuli_interval_text.started', inter_stimuli_interval_text.tStartRefresh)
        one_back_loop.addData('inter_stimuli_interval_text.stopped', inter_stimuli_interval_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'one_back_loop'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'one_back_outer_loop'


# ------Prepare to start Routine "two_back_prompt"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
two_back_promptComponents = [two_back_prompt_text]
for thisComponent in two_back_promptComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
two_back_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "two_back_prompt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = two_back_promptClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=two_back_promptClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *two_back_prompt_text* updates
    if two_back_prompt_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        two_back_prompt_text.frameNStart = frameN  # exact frame index
        two_back_prompt_text.tStart = t  # local t and not account for scr refresh
        two_back_prompt_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two_back_prompt_text, 'tStartRefresh')  # time at next scr refresh
        two_back_prompt_text.setAutoDraw(True)
    if two_back_prompt_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > two_back_prompt_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            two_back_prompt_text.tStop = t  # not accounting for scr refresh
            two_back_prompt_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(two_back_prompt_text, 'tStopRefresh')  # time at next scr refresh
            two_back_prompt_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in two_back_promptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "two_back_prompt"-------
for thisComponent in two_back_promptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('two_back_prompt_text.started', two_back_prompt_text.tStartRefresh)
thisExp.addData('two_back_prompt_text.stopped', two_back_prompt_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
two_back_outer_loop = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='two_back_outer_loop')
thisExp.addLoop(two_back_outer_loop)  # add the loop to the experiment
thisTwo_back_outer_loop = two_back_outer_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTwo_back_outer_loop.rgb)
if thisTwo_back_outer_loop != None:
    for paramName in thisTwo_back_outer_loop:
        exec('{} = thisTwo_back_outer_loop[paramName]'.format(paramName))

for thisTwo_back_outer_loop in two_back_outer_loop:
    currentLoop = two_back_outer_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTwo_back_outer_loop.rgb)
    if thisTwo_back_outer_loop != None:
        for paramName in thisTwo_back_outer_loop:
            exec('{} = thisTwo_back_outer_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    two_back_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(two_csv_path),
        seed=None, name='two_back_loop')
    thisExp.addLoop(two_back_loop)  # add the loop to the experiment
    thisTwo_back_loop = two_back_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTwo_back_loop.rgb)
    if thisTwo_back_loop != None:
        for paramName in thisTwo_back_loop:
            exec('{} = thisTwo_back_loop[paramName]'.format(paramName))
    
    for thisTwo_back_loop in two_back_loop:
        currentLoop = two_back_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTwo_back_loop.rgb)
        if thisTwo_back_loop != None:
            for paramName in thisTwo_back_loop:
                exec('{} = thisTwo_back_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_two_back"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        two_back_num_stim.setText(num_stim)
        two_back_resp.keys = []
        two_back_resp.rt = []
        _two_back_resp_allKeys = []
        # keep track of which components have finished
        trial_two_backComponents = [two_back_num_stim, two_back_resp]
        for thisComponent in trial_two_backComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_two_backClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_two_back"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_two_backClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_two_backClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *two_back_num_stim* updates
            if two_back_num_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_num_stim.frameNStart = frameN  # exact frame index
                two_back_num_stim.tStart = t  # local t and not account for scr refresh
                two_back_num_stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_num_stim, 'tStartRefresh')  # time at next scr refresh
                two_back_num_stim.setAutoDraw(True)
            if two_back_num_stim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_num_stim.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_num_stim.tStop = t  # not accounting for scr refresh
                    two_back_num_stim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(two_back_num_stim, 'tStopRefresh')  # time at next scr refresh
                    two_back_num_stim.setAutoDraw(False)
            
            # *two_back_resp* updates
            waitOnFlip = False
            if two_back_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_back_resp.frameNStart = frameN  # exact frame index
                two_back_resp.tStart = t  # local t and not account for scr refresh
                two_back_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_back_resp, 'tStartRefresh')  # time at next scr refresh
                two_back_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(two_back_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(two_back_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if two_back_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_back_resp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    two_back_resp.tStop = t  # not accounting for scr refresh
                    two_back_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(two_back_resp, 'tStopRefresh')  # time at next scr refresh
                    two_back_resp.status = FINISHED
            if two_back_resp.status == STARTED and not waitOnFlip:
                theseKeys = two_back_resp.getKeys(keyList=['space'], waitRelease=False)
                _two_back_resp_allKeys.extend(theseKeys)
                if len(_two_back_resp_allKeys):
                    two_back_resp.keys = _two_back_resp_allKeys[-1].name  # just the last key pressed
                    two_back_resp.rt = _two_back_resp_allKeys[-1].rt
                    # was this correct?
                    if (two_back_resp.keys == str(match)) or (two_back_resp.keys == match):
                        two_back_resp.corr = 1
                    else:
                        two_back_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_two_backComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_two_back"-------
        for thisComponent in trial_two_backComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        two_back_loop.addData('two_back_num_stim.started', two_back_num_stim.tStartRefresh)
        two_back_loop.addData('two_back_num_stim.stopped', two_back_num_stim.tStopRefresh)
        # check responses
        if two_back_resp.keys in ['', [], None]:  # No response was made
            two_back_resp.keys = None
            # was no response the correct answer?!
            if str(match).lower() == 'none':
               two_back_resp.corr = 1;  # correct non-response
            else:
               two_back_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for two_back_loop (TrialHandler)
        two_back_loop.addData('two_back_resp.keys',two_back_resp.keys)
        two_back_loop.addData('two_back_resp.corr', two_back_resp.corr)
        if two_back_resp.keys != None:  # we had a response
            two_back_loop.addData('two_back_resp.rt', two_back_resp.rt)
        two_back_loop.addData('two_back_resp.started', two_back_resp.tStartRefresh)
        two_back_loop.addData('two_back_resp.stopped', two_back_resp.tStopRefresh)
        
        # ------Prepare to start Routine "inter_stimuli_interval"-------
        continueRoutine = True
        routineTimer.add(2.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        inter_stimuli_intervalComponents = [inter_stimuli_interval_text]
        for thisComponent in inter_stimuli_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        inter_stimuli_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "inter_stimuli_interval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = inter_stimuli_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=inter_stimuli_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_stimuli_interval_text* updates
            if inter_stimuli_interval_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_stimuli_interval_text.frameNStart = frameN  # exact frame index
                inter_stimuli_interval_text.tStart = t  # local t and not account for scr refresh
                inter_stimuli_interval_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_stimuli_interval_text, 'tStartRefresh')  # time at next scr refresh
                inter_stimuli_interval_text.setAutoDraw(True)
            if inter_stimuli_interval_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_stimuli_interval_text.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_stimuli_interval_text.tStop = t  # not accounting for scr refresh
                    inter_stimuli_interval_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_stimuli_interval_text, 'tStopRefresh')  # time at next scr refresh
                    inter_stimuli_interval_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in inter_stimuli_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "inter_stimuli_interval"-------
        for thisComponent in inter_stimuli_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        two_back_loop.addData('inter_stimuli_interval_text.started', inter_stimuli_interval_text.tStartRefresh)
        two_back_loop.addData('inter_stimuli_interval_text.stopped', inter_stimuli_interval_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'two_back_loop'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'two_back_outer_loop'


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
