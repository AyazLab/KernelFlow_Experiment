#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on July 06, 2022, at 16:10
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
expName = 'video_narrative_sherlock'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\video_narrative\\video_narrative_sherlock_lastrun.py',
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

# start experiment marker -----
marker.send_marker(81, task_start_timestamp_fmt)

# Initialize components for Routine "sherlock_instructions"
sherlock_instructionsClock = core.Clock()
sherlock_instructions_text = visual.TextStim(win=win, name='sherlock_instructions_text',
    text='This is the 5-minute "Sherlock" video clip.\n\nPlease pay attention to the story.\n\nPress SPACE when you are ready to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sherlock_instructions_resp = keyboard.Keyboard()

# Initialize components for Routine "sherlock_video"
sherlock_videoClock = core.Clock()
sherlock_clip = visual.MovieStim3(
    win=win, name='sherlock_clip',
    noAudio = False,
    filename='video_clips/sherlock_clip.mov',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    depth=0.0,
    )
video_start = visual.TextStim(win=win, name='video_start',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sherlock_details"
sherlock_detailsClock = core.Clock()
sherlock_details_text = visual.TextStim(win=win, name='sherlock_details_text',
    text='Please recall details from the "Sherlock" clip. You will have 3 minutes to type your response. \n\nPress SPACE when you are ready to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sherlock_details_resp = keyboard.Keyboard()

# Initialize components for Routine "sherlock_text_response"
sherlock_text_responseClock = core.Clock()
sherlock_participant_response = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(-0.1, 0),     letterHeight=0.04,
     size=(1.5, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='sherlock_participant_response',
     autoLog=True,
)

# Initialize components for Routine "done"
doneClock = core.Clock()
done_text = visual.TextStim(win=win, name='done_text',
    text='The Video Narrative task is now complete.',
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

# ------Prepare to start Routine "sherlock_instructions"-------
continueRoutine = True
# update component parameters for each repeat
sherlock_instructions_resp.keys = []
sherlock_instructions_resp.rt = []
_sherlock_instructions_resp_allKeys = []
# keep track of which components have finished
sherlock_instructionsComponents = [sherlock_instructions_text, sherlock_instructions_resp]
for thisComponent in sherlock_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sherlock_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sherlock_instructions"-------
while continueRoutine:
    # get current time
    t = sherlock_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sherlock_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sherlock_instructions_text* updates
    if sherlock_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock_instructions_text.frameNStart = frameN  # exact frame index
        sherlock_instructions_text.tStart = t  # local t and not account for scr refresh
        sherlock_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock_instructions_text, 'tStartRefresh')  # time at next scr refresh
        sherlock_instructions_text.setAutoDraw(True)
    
    # *sherlock_instructions_resp* updates
    if sherlock_instructions_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock_instructions_resp.frameNStart = frameN  # exact frame index
        sherlock_instructions_resp.tStart = t  # local t and not account for scr refresh
        sherlock_instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock_instructions_resp, 'tStartRefresh')  # time at next scr refresh
        sherlock_instructions_resp.status = STARTED
        # keyboard checking is just starting
        sherlock_instructions_resp.clock.reset()  # now t=0
    if sherlock_instructions_resp.status == STARTED:
        theseKeys = sherlock_instructions_resp.getKeys(keyList=['space'], waitRelease=False)
        _sherlock_instructions_resp_allKeys.extend(theseKeys)
        if len(_sherlock_instructions_resp_allKeys):
            sherlock_instructions_resp.keys = _sherlock_instructions_resp_allKeys[-1].name  # just the last key pressed
            sherlock_instructions_resp.rt = _sherlock_instructions_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sherlock_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sherlock_instructions"-------
for thisComponent in sherlock_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "sherlock_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sherlock_video"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
sherlock_videoComponents = [sherlock_clip, video_start]
for thisComponent in sherlock_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sherlock_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sherlock_video"-------
while continueRoutine:
    # get current time
    t = sherlock_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sherlock_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sherlock_clip* updates
    if sherlock_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock_clip.frameNStart = frameN  # exact frame index
        sherlock_clip.tStart = t  # local t and not account for scr refresh
        sherlock_clip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock_clip, 'tStartRefresh')  # time at next scr refresh
        sherlock_clip.setAutoDraw(True)
    
    # *video_start* updates
    if video_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        video_start.frameNStart = frameN  # exact frame index
        video_start.tStart = t  # local t and not account for scr refresh
        video_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(video_start, 'tStartRefresh')  # time at next scr refresh
        video_start.setAutoDraw(True)
    if video_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > video_start.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            video_start.tStop = t  # not accounting for scr refresh
            video_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(video_start, 'tStopRefresh')  # time at next scr refresh
            video_start.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sherlock_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sherlock_video"-------
for thisComponent in sherlock_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sherlock_clip.stop()
thisExp.addData('video_start.started', video_start.tStartRefresh)
thisExp.addData('video_start.stopped', video_start.tStopRefresh)
# the Routine "sherlock_video" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sherlock_details"-------
continueRoutine = True
# update component parameters for each repeat
sherlock_details_resp.keys = []
sherlock_details_resp.rt = []
_sherlock_details_resp_allKeys = []
# keep track of which components have finished
sherlock_detailsComponents = [sherlock_details_text, sherlock_details_resp]
for thisComponent in sherlock_detailsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sherlock_detailsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sherlock_details"-------
while continueRoutine:
    # get current time
    t = sherlock_detailsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sherlock_detailsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sherlock_details_text* updates
    if sherlock_details_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock_details_text.frameNStart = frameN  # exact frame index
        sherlock_details_text.tStart = t  # local t and not account for scr refresh
        sherlock_details_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock_details_text, 'tStartRefresh')  # time at next scr refresh
        sherlock_details_text.setAutoDraw(True)
    
    # *sherlock_details_resp* updates
    if sherlock_details_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock_details_resp.frameNStart = frameN  # exact frame index
        sherlock_details_resp.tStart = t  # local t and not account for scr refresh
        sherlock_details_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock_details_resp, 'tStartRefresh')  # time at next scr refresh
        sherlock_details_resp.status = STARTED
        # keyboard checking is just starting
        sherlock_details_resp.clock.reset()  # now t=0
    if sherlock_details_resp.status == STARTED:
        theseKeys = sherlock_details_resp.getKeys(keyList=['space'], waitRelease=False)
        _sherlock_details_resp_allKeys.extend(theseKeys)
        if len(_sherlock_details_resp_allKeys):
            sherlock_details_resp.keys = _sherlock_details_resp_allKeys[-1].name  # just the last key pressed
            sherlock_details_resp.rt = _sherlock_details_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sherlock_detailsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sherlock_details"-------
for thisComponent in sherlock_detailsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "sherlock_details" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sherlock_text_response"-------
continueRoutine = True
routineTimer.add(180.000000)
# update component parameters for each repeat
sherlock_participant_response.reset()
# keep track of which components have finished
sherlock_text_responseComponents = [sherlock_participant_response]
for thisComponent in sherlock_text_responseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sherlock_text_responseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sherlock_text_response"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = sherlock_text_responseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sherlock_text_responseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sherlock_participant_response* updates
    if sherlock_participant_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sherlock_participant_response.frameNStart = frameN  # exact frame index
        sherlock_participant_response.tStart = t  # local t and not account for scr refresh
        sherlock_participant_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sherlock_participant_response, 'tStartRefresh')  # time at next scr refresh
        sherlock_participant_response.setAutoDraw(True)
    if sherlock_participant_response.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sherlock_participant_response.tStartRefresh + 180-frameTolerance:
            # keep track of stop time/frame for later
            sherlock_participant_response.tStop = t  # not accounting for scr refresh
            sherlock_participant_response.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sherlock_participant_response, 'tStopRefresh')  # time at next scr refresh
            sherlock_participant_response.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sherlock_text_responseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sherlock_text_response"-------
for thisComponent in sherlock_text_responseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sherlock_participant_response.text',sherlock_participant_response.text)
thisExp.addData('sherlock_participant_response.started', sherlock_participant_response.tStartRefresh)
thisExp.addData('sherlock_participant_response.stopped', sherlock_participant_response.tStopRefresh)

# ------Prepare to start Routine "done"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
doneComponents = [done_text]
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
        if tThisFlipGlobal > done_text.tStartRefresh + 3-frameTolerance:
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
# end experiment marker -----
task_end_timestamp = time.time() - clock_time_offset
task_end_timestamp_fmt = int(task_end_timestamp * 1e9)
marker.send_marker(82, task_end_timestamp_fmt)

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
