#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 28, 2022, at 18:01
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

GNG_conditions_dir = os.path.join(cwd, "affective_GNG_conditions")

go_csv_list = []
GNG_csv_list = []

for csv_filename in os.listdir(GNG_conditions_dir):
    if "go" in csv_filename:
        go_csv_list.append(os.path.join("affective_GNG_conditions", csv_filename))
    elif "GNG" in csv_filename:
        GNG_csv_list.append(os.path.join("affective_GNG_conditions", csv_filename))

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
    text='You are going to see either a PUPPY or a SPIDER appear on the screen. Press the RIGHT ARROW as fast as you can when you see a PUPPY. Press the LEFT ARROW as fast as you can when you see a SPIDER. \n\nWhen the image disappears, a plus sign will appear on the screen. Stare at the plus sign until the next image appears. Remember to press the arrow keys as fast as you can without making any mistakes.\n\nPress SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
initial_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "practice_instructions"
practice_instructionsClock = core.Clock()
practice_instructions_text = visual.TextStim(win=win, name='practice_instructions_text',
    text='This is a practice trial.\n\nRemember: \nPress RIGHT ARROW as soon as a PUPPY appears.\nPress LEFT ARROW as soon a SPIDER appears.\n\nPress SPACE to begin the practice trial.',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "practice_start_code"
practice_start_codeClock = core.Clock()

# Initialize components for Routine "practice_interval"
practice_intervalClock = core.Clock()
practice_interval_plus = visual.ShapeStim(
    win=win, name='practice_interval_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "practice_trial"
practice_trialClock = core.Clock()
practice_text = visual.TextStim(win=win, name='practice_text',
    text='Press key now!',
    font='Open Sans',
    pos=(0, 0.35), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_plus = visual.ShapeStim(
    win=win, name='practice_plus', vertices='cross',
    size=(0.25, 0.25),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
practice_image = visual.ImageStim(
    win=win,
    name='practice_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "finish_practice"
finish_practiceClock = core.Clock()
finish_practice_text = visual.TextStim(win=win, name='finish_practice_text',
    text='Press SPACE to complete practice and begin the trial.\n\nPress BACKSPACE for more practice.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
finish_practice_resp = keyboard.Keyboard()

# Initialize components for Routine "finish_practice_code"
finish_practice_codeClock = core.Clock()

# Initialize components for Routine "GNG_loop_code"
GNG_loop_codeClock = core.Clock()

# Initialize components for Routine "go_instructions"
go_instructionsClock = core.Clock()
go_instructions_text = visual.TextStim(win=win, name='go_instructions_text',
    text='This is the GO experiment. \n\nPUPPIES = GO\nOnly press SPACE when a GO stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
go_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "block_start_code"
block_start_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_match_code"
inter_stim_match_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
marker.send_marker("trial_start")
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
go_image = visual.ImageStim(
    win=win,
    name='go_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "post_stim_code"
post_stim_codeClock = core.Clock()

# Initialize components for Routine "block_end_code"
block_end_codeClock = core.Clock()

# Initialize components for Routine "GNG_instructions"
GNG_instructionsClock = core.Clock()
GNG_instructions_text = visual.TextStim(win=win, name='GNG_instructions_text',
    text='This is the GO/NO-GO experiment. \n\nPUPPIES = GO\nSPIDERS = NO-GO\n\nPress SPACE when a GO stimulus appears.\nDo not press anything when a NO-GO stimulus appears.\n\nPress SPACE when you are ready to continue. ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
GNG_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "block_start_code"
block_start_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_match_code"
inter_stim_match_codeClock = core.Clock()

# Initialize components for Routine "inter_stim_interval"
inter_stim_intervalClock = core.Clock()
marker.send_marker("trial_start")
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
GNG_image = visual.ImageStim(
    win=win,
    name='GNG_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.85, 0.85),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "post_stim_code"
post_stim_codeClock = core.Clock()

# Initialize components for Routine "block_end_code"
block_end_codeClock = core.Clock()

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

# ------Prepare to start Routine "practice_instructions"-------
continueRoutine = True
# update component parameters for each repeat
practice_instructions_resp.keys = []
practice_instructions_resp.rt = []
_practice_instructions_resp_allKeys = []
# keep track of which components have finished
practice_instructionsComponents = [practice_instructions_text, practice_instructions_resp]
for thisComponent in practice_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_instructions"-------
while continueRoutine:
    # get current time
    t = practice_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_instructions_text* updates
    if practice_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_instructions_text.frameNStart = frameN  # exact frame index
        practice_instructions_text.tStart = t  # local t and not account for scr refresh
        practice_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_instructions_text, 'tStartRefresh')  # time at next scr refresh
        practice_instructions_text.setAutoDraw(True)
    
    # *practice_instructions_resp* updates
    if practice_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_instructions_resp.frameNStart = frameN  # exact frame index
        practice_instructions_resp.tStart = t  # local t and not account for scr refresh
        practice_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        practice_instructions_resp.status = STARTED
        # keyboard checking is just starting
        practice_instructions_resp.clock.reset()  # now t=0
    if practice_instructions_resp.status == STARTED:
        theseKeys = practice_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _practice_instructions_resp_allKeys.extend(theseKeys)
        if len(_practice_instructions_resp_allKeys):
            practice_instructions_resp.keys = _practice_instructions_resp_allKeys[-1].name  # just the last key pressed
            practice_instructions_resp.rt = _practice_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instructions"-------
for thisComponent in practice_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_start_code"-------
continueRoutine = True
# update component parameters for each repeat
marker.send_marker("practice_start")
# keep track of which components have finished
practice_start_codeComponents = []
for thisComponent in practice_start_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_start_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_start_code"-------
while continueRoutine:
    # get current time
    t = practice_start_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_start_codeClock)
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
    for thisComponent in practice_start_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_start_code"-------
for thisComponent in practice_start_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_start_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(practice_loop_path),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    practice_trial_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(practice_csv_path),
        seed=None, name='practice_trial_loop')
    thisExp.addLoop(practice_trial_loop)  # add the loop to the experiment
    thisPractice_trial_loop = practice_trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_loop.rgb)
    if thisPractice_trial_loop != None:
        for paramName in thisPractice_trial_loop:
            exec('{} = thisPractice_trial_loop[paramName]'.format(paramName))
    
    for thisPractice_trial_loop in practice_trial_loop:
        currentLoop = practice_trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial_loop.rgb)
        if thisPractice_trial_loop != None:
            for paramName in thisPractice_trial_loop:
                exec('{} = thisPractice_trial_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice_interval"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        practice_intervalComponents = [practice_interval_plus]
        for thisComponent in practice_intervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practice_intervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practice_interval"-------
        while continueRoutine:
            # get current time
            t = practice_intervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practice_intervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_interval_plus* updates
            if practice_interval_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_interval_plus.frameNStart = frameN  # exact frame index
                practice_interval_plus.tStart = t  # local t and not account for scr refresh
                practice_interval_plus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_interval_plus, 'tStartRefresh')  # time at next scr refresh
                practice_interval_plus.setAutoDraw(True)
            if practice_interval_plus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_interval_plus.tStartRefresh + 0-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_interval_plus.tStop = t  # not accounting for scr refresh
                    practice_interval_plus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practice_interval_plus, 'tStopRefresh')  # time at next scr refresh
                    practice_interval_plus.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_intervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_interval"-------
        for thisComponent in practice_intervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "practice_interval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "practice_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        practice_image.setImage(GNG_stim)
        # keep track of which components have finished
        practice_trialComponents = [practice_text, practice_plus, practice_image]
        for thisComponent in practice_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "practice_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practice_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=practice_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *practice_text* updates
            if practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_text.frameNStart = frameN  # exact frame index
                practice_text.tStart = t  # local t and not account for scr refresh
                practice_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_text, 'tStartRefresh')  # time at next scr refresh
                practice_text.setAutoDraw(True)
            if practice_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_text.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_text.tStop = t  # not accounting for scr refresh
                    practice_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practice_text, 'tStopRefresh')  # time at next scr refresh
                    practice_text.setAutoDraw(False)
            
            # *practice_plus* updates
            if practice_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_plus.frameNStart = frameN  # exact frame index
                practice_plus.tStart = t  # local t and not account for scr refresh
                practice_plus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_plus, 'tStartRefresh')  # time at next scr refresh
                practice_plus.setAutoDraw(True)
            if practice_plus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_plus.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_plus.tStop = t  # not accounting for scr refresh
                    practice_plus.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practice_plus, 'tStopRefresh')  # time at next scr refresh
                    practice_plus.setAutoDraw(False)
            
            # *practice_image* updates
            if practice_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_image.frameNStart = frameN  # exact frame index
                practice_image.tStart = t  # local t and not account for scr refresh
                practice_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_image, 'tStartRefresh')  # time at next scr refresh
                practice_image.setAutoDraw(True)
            if practice_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > practice_image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    practice_image.tStop = t  # not accounting for scr refresh
                    practice_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(practice_image, 'tStopRefresh')  # time at next scr refresh
                    practice_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_trial"-------
        for thisComponent in practice_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_trial_loop'
    
    
    # ------Prepare to start Routine "finish_practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    finish_practice_resp.keys = []
    finish_practice_resp.rt = []
    _finish_practice_resp_allKeys = []
    # keep track of which components have finished
    finish_practiceComponents = [finish_practice_text, finish_practice_resp]
    for thisComponent in finish_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    finish_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "finish_practice"-------
    while continueRoutine:
        # get current time
        t = finish_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=finish_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *finish_practice_text* updates
        if finish_practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_practice_text.frameNStart = frameN  # exact frame index
            finish_practice_text.tStart = t  # local t and not account for scr refresh
            finish_practice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_practice_text, 'tStartRefresh')  # time at next scr refresh
            finish_practice_text.setAutoDraw(True)
        
        # *finish_practice_resp* updates
        if finish_practice_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            finish_practice_resp.frameNStart = frameN  # exact frame index
            finish_practice_resp.tStart = t  # local t and not account for scr refresh
            finish_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(finish_practice_resp, 'tStartRefresh')  # time at next scr refresh
            finish_practice_resp.status = STARTED
            # keyboard checking is just starting
            finish_practice_resp.clock.reset()  # now t=0
        if finish_practice_resp.status == STARTED:
            theseKeys = finish_practice_resp.getKeys(keyList=['space', 'backspace'], waitRelease=False)
            _finish_practice_resp_allKeys.extend(theseKeys)
            if len(_finish_practice_resp_allKeys):
                finish_practice_resp.keys = _finish_practice_resp_allKeys[-1].name  # just the last key pressed
                finish_practice_resp.rt = _finish_practice_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in finish_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "finish_practice"-------
    for thisComponent in finish_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "finish_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "finish_practice_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    if finish_practice_resp.keys == "space":
        marker.send_marker("practice_end")
        break
    elif finish_practice_resp.keys == "backspace":
        pass
    # keep track of which components have finished
    finish_practice_codeComponents = []
    for thisComponent in finish_practice_codeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    finish_practice_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "finish_practice_code"-------
    while continueRoutine:
        # get current time
        t = finish_practice_codeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=finish_practice_codeClock)
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
        for thisComponent in finish_practice_codeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "finish_practice_code"-------
    for thisComponent in finish_practice_codeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "finish_practice_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_loop'


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
    
    go_stims_csv_path = go_csv_list[loop_num]
    GNG_stims_csv_path = GNG_csv_list[loop_num]
    
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
        if go_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
    marker.send_marker("block_start")
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
        trialList=data.importConditions(go_stims_csv_path),
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
            corr_key = "space"
        elif match == 0:
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
        go_image.setImage(go_stim)
        # keep track of which components have finished
        go_trialComponents = [go_resp, go_plus, go_image]
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
            if go_resp.keys:
                if go_resp.keys == corr_key:
                    marker.send_marker("correct_ans")
                else:
                    marker.send_marker("incorrect_ans")
            
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
        go_block.addData('go_image.started', go_image.tStartRefresh)
        go_block.addData('go_image.stopped', go_image.tStopRefresh)
        
        # ------Prepare to start Routine "post_stim_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        post_stim_codeComponents = []
        for thisComponent in post_stim_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        post_stim_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "post_stim_code"-------
        while continueRoutine:
            # get current time
            t = post_stim_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=post_stim_codeClock)
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
            for thisComponent in post_stim_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post_stim_code"-------
        for thisComponent in post_stim_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "post_stim_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
        if GNG_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
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
    
    # ------Prepare to start Routine "block_start_code"-------
    continueRoutine = True
    # update component parameters for each repeat
    marker.send_marker("block_start")
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
        trialList=data.importConditions(GNG_stims_csv_path),
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
            corr_key = "space"
        elif match == 0:
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
        GNG_image.setImage(GNG_stim)
        # keep track of which components have finished
        GNG_trialComponents = [GNG_resp, GNG_plus, GNG_image]
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
        if GNG_resp.keys[0] == corr_key:
            marker.send_marker("correct_ans")
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
        GNG_block.addData('GNG_image.started', GNG_image.tStartRefresh)
        GNG_block.addData('GNG_image.stopped', GNG_image.tStopRefresh)
        
        # ------Prepare to start Routine "post_stim_code"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        post_stim_codeComponents = []
        for thisComponent in post_stim_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        post_stim_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "post_stim_code"-------
        while continueRoutine:
            # get current time
            t = post_stim_codeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=post_stim_codeClock)
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
            for thisComponent in post_stim_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "post_stim_code"-------
        for thisComponent in post_stim_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "post_stim_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
