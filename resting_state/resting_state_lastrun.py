#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on May 17, 2022, at 10:19
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
expName = 'resting_state'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Sim\\Desktop\\KernelFlow_PsychoPy\\resting_state\\resting_state_lastrun.py',
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
for task_filename in os.listdir(par_task_dir):
    if "RS_TO-" in task_filename:
        task_order_csv = os.path.join(par_task_dir, task_filename)

# read task order file -----
file = open(task_order_csv)
csvreader = csv.reader(file)

rows = []
for row in csvreader:
        rows.append(row[0])
file.close()

resting_state_1 = rows[1]
resting_state_2 = rows[2]
resting_state_order = [resting_state_1, resting_state_2]

# start experiment marker -----
marker.send_marker(51, task_start_timestamp_fmt)

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcome_text = visual.TextStim(win=win, name='welcome_text',
    text="This is the 7-minute resting state task\n\nPlease sit still with your " + str(resting_state_order[0]) + ".\n\n" + "Halfway through the task, you will hear a tone. After the tone, please sit still with your " + str(resting_state_order[1]) + " for the remainder of the task. You will hear a second tone when the task is complete.\n\nPress SPACE when you are ready to begin.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
halfway_tone = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='halfway_tone')
halfway_tone.setVolume(1.0)
trial_cross = visual.ShapeStim(
    win=win, name='trial_cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "done"
doneClock = core.Clock()
done_sound = sound.Sound('A', secs=0.5, stereo=True, hamming=True,
    name='done_sound')
done_sound.setVolume(1.0)
done_text = visual.TextStim(win=win, name='done_text',
    text='The resting state task is now complete.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcome_text, welcome_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_text* updates
    if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_text.frameNStart = frameN  # exact frame index
        welcome_text.tStart = t  # local t and not account for scr refresh
        welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
        welcome_text.setAutoDraw(True)
    
    # *welcome_resp* updates
    if welcome_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        welcome_resp.clock.reset()  # now t=0
    if welcome_resp.status == STARTED:
        theseKeys = welcome_resp.getKeys(keyList=['space'], waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(420.000000)
# update component parameters for each repeat
halfway_tone.setSound('A', secs=0.5, hamming=True)
halfway_tone.setVolume(1.0, log=False)
# keep track of which components have finished
trialComponents = [halfway_tone, trial_cross]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop halfway_tone
    if halfway_tone.status == NOT_STARTED and tThisFlip >= 210-frameTolerance:
        # keep track of start time/frame for later
        halfway_tone.frameNStart = frameN  # exact frame index
        halfway_tone.tStart = t  # local t and not account for scr refresh
        halfway_tone.tStartRefresh = tThisFlipGlobal  # on global time
        halfway_tone.play(when=win)  # sync with win flip
    if halfway_tone.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > halfway_tone.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            halfway_tone.tStop = t  # not accounting for scr refresh
            halfway_tone.frameNStop = frameN  # exact frame index
            win.timeOnFlip(halfway_tone, 'tStopRefresh')  # time at next scr refresh
            halfway_tone.stop()
    
    # *trial_cross* updates
    if trial_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trial_cross.frameNStart = frameN  # exact frame index
        trial_cross.tStart = t  # local t and not account for scr refresh
        trial_cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_cross, 'tStartRefresh')  # time at next scr refresh
        trial_cross.setAutoDraw(True)
    if trial_cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > trial_cross.tStartRefresh + 420-frameTolerance:
            # keep track of stop time/frame for later
            trial_cross.tStop = t  # not accounting for scr refresh
            trial_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(trial_cross, 'tStopRefresh')  # time at next scr refresh
            trial_cross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
halfway_tone.stop()  # ensure sound has stopped at end of routine
thisExp.addData('halfway_tone.started', halfway_tone.tStartRefresh)
thisExp.addData('halfway_tone.stopped', halfway_tone.tStopRefresh)
thisExp.addData('trial_cross.started', trial_cross.tStartRefresh)
thisExp.addData('trial_cross.stopped', trial_cross.tStopRefresh)

# ------Prepare to start Routine "done"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
done_sound.setSound('A', secs=0.5, hamming=True)
done_sound.setVolume(1.0, log=False)
# keep track of which components have finished
doneComponents = [done_sound, done_text]
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
    # start/stop done_sound
    if done_sound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_sound.frameNStart = frameN  # exact frame index
        done_sound.tStart = t  # local t and not account for scr refresh
        done_sound.tStartRefresh = tThisFlipGlobal  # on global time
        done_sound.play(when=win)  # sync with win flip
    if done_sound.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done_sound.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            done_sound.tStop = t  # not accounting for scr refresh
            done_sound.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done_sound, 'tStopRefresh')  # time at next scr refresh
            done_sound.stop()
    
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
        if tThisFlipGlobal > done_text.tStartRefresh + 5-frameTolerance:
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
done_sound.stop()  # ensure sound has stopped at end of routine
thisExp.addData('done_sound.started', done_sound.tStartRefresh)
thisExp.addData('done_sound.stopped', done_sound.tStopRefresh)
# end experiment marker -----
task_end_timestamp = time.time() - clock_time_offset
task_end_timestamp_fmt = int(task_end_timestamp * 1e9)
marker.send_marker(52, task_end_timestamp_fmt)

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
