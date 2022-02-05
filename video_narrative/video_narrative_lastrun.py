#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 05, 2022, at 16:19
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
expName = 'video_narrative'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\zackg\\OneDrive\\Ayaz Lab\\KernelFlow_PsychoPy\\video_narrative\\video_narrative_lastrun.py',
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

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
instructions1_text = visual.TextStim(win=win, name='instructions1_text',
    text='This is the "Catch Me If You Can" video clip.\n\nPlease pay attention to the story.\n\nPress SPACE when you are ready to watch the clip.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions1_resp = keyboard.Keyboard()

# Initialize components for Routine "catchme_video"
catchme_videoClock = core.Clock()
catchme_clip = visual.MovieStim3(
    win=win, name='catchme_clip',
    noAudio = False,
    filename='video_clips/video_1.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "details1"
details1Clock = core.Clock()
details1_text = visual.TextStim(win=win, name='details1_text',
    text='Please recall details from the "Catch Me If You Can" clip.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
details1_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instructions2_text = visual.TextStim(win=win, name='instructions2_text',
    text='This is the "Sherlock" video clip.\n\nPlease pay attention to the story.\n\nPress SPACE when you are ready to watch the clip.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions2_resp = keyboard.Keyboard()

# Initialize components for Routine "sherlock_video"
sherlock_videoClock = core.Clock()
sherlock_clip = visual.MovieStim3(
    win=win, name='sherlock_clip',
    noAudio = False,
    filename='video_clips/video_2.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "details2"
details2Clock = core.Clock()
details2_text = visual.TextStim(win=win, name='details2_text',
    text='Please recall details from the "Sherlock" clip.\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
details2_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
instructions1_resp.keys = []
instructions1_resp.rt = []
_instructions1_resp_allKeys = []
# keep track of which components have finished
instructions1Components = [instructions1_text, instructions1_resp]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions1_text* updates
    if instructions1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions1_text.frameNStart = frameN  # exact frame index
        instructions1_text.tStart = t  # local t and not account for scr refresh
        instructions1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1_text, 'tStartRefresh')  # time at next scr refresh
        instructions1_text.setAutoDraw(True)
    
    # *instructions1_resp* updates
    waitOnFlip = False
    if instructions1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions1_resp.frameNStart = frameN  # exact frame index
        instructions1_resp.tStart = t  # local t and not account for scr refresh
        instructions1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions1_resp, 'tStartRefresh')  # time at next scr refresh
        instructions1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions1_resp.status == STARTED and not waitOnFlip:
        theseKeys = instructions1_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions1_resp_allKeys.extend(theseKeys)
        if len(_instructions1_resp_allKeys):
            instructions1_resp.keys = _instructions1_resp_allKeys[-1].name  # just the last key pressed
            instructions1_resp.rt = _instructions1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions1_text.started', instructions1_text.tStartRefresh)
thisExp.addData('instructions1_text.stopped', instructions1_text.tStopRefresh)
# check responses
if instructions1_resp.keys in ['', [], None]:  # No response was made
    instructions1_resp.keys = None
thisExp.addData('instructions1_resp.keys',instructions1_resp.keys)
if instructions1_resp.keys != None:  # we had a response
    thisExp.addData('instructions1_resp.rt', instructions1_resp.rt)
thisExp.addData('instructions1_resp.started', instructions1_resp.tStartRefresh)
thisExp.addData('instructions1_resp.stopped', instructions1_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "catchme_video"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
catchme_videoComponents = [catchme_clip]
for thisComponent in catchme_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
catchme_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "catchme_video"-------
while continueRoutine:
    # get current time
    t = catchme_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=catchme_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *catchme_clip* updates
    if catchme_clip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        catchme_clip.frameNStart = frameN  # exact frame index
        catchme_clip.tStart = t  # local t and not account for scr refresh
        catchme_clip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(catchme_clip, 'tStartRefresh')  # time at next scr refresh
        catchme_clip.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in catchme_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "catchme_video"-------
for thisComponent in catchme_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
catchme_clip.stop()
# the Routine "catchme_video" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "details1"-------
continueRoutine = True
# update component parameters for each repeat
details1_resp.keys = []
details1_resp.rt = []
_details1_resp_allKeys = []
# keep track of which components have finished
details1Components = [details1_text, details1_resp]
for thisComponent in details1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
details1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "details1"-------
while continueRoutine:
    # get current time
    t = details1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=details1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *details1_text* updates
    if details1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        details1_text.frameNStart = frameN  # exact frame index
        details1_text.tStart = t  # local t and not account for scr refresh
        details1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(details1_text, 'tStartRefresh')  # time at next scr refresh
        details1_text.setAutoDraw(True)
    
    # *details1_resp* updates
    waitOnFlip = False
    if details1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        details1_resp.frameNStart = frameN  # exact frame index
        details1_resp.tStart = t  # local t and not account for scr refresh
        details1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(details1_resp, 'tStartRefresh')  # time at next scr refresh
        details1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(details1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(details1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if details1_resp.status == STARTED and not waitOnFlip:
        theseKeys = details1_resp.getKeys(keyList=['space'], waitRelease=False)
        _details1_resp_allKeys.extend(theseKeys)
        if len(_details1_resp_allKeys):
            details1_resp.keys = _details1_resp_allKeys[-1].name  # just the last key pressed
            details1_resp.rt = _details1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in details1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "details1"-------
for thisComponent in details1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('details1_text.started', details1_text.tStartRefresh)
thisExp.addData('details1_text.stopped', details1_text.tStopRefresh)
# check responses
if details1_resp.keys in ['', [], None]:  # No response was made
    details1_resp.keys = None
thisExp.addData('details1_resp.keys',details1_resp.keys)
if details1_resp.keys != None:  # we had a response
    thisExp.addData('details1_resp.rt', details1_resp.rt)
thisExp.addData('details1_resp.started', details1_resp.tStartRefresh)
thisExp.addData('details1_resp.stopped', details1_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "details1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
instructions2_resp.keys = []
instructions2_resp.rt = []
_instructions2_resp_allKeys = []
# keep track of which components have finished
instructions2Components = [instructions2_text, instructions2_resp]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions2_text* updates
    if instructions2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2_text.frameNStart = frameN  # exact frame index
        instructions2_text.tStart = t  # local t and not account for scr refresh
        instructions2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2_text, 'tStartRefresh')  # time at next scr refresh
        instructions2_text.setAutoDraw(True)
    
    # *instructions2_resp* updates
    waitOnFlip = False
    if instructions2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions2_resp.frameNStart = frameN  # exact frame index
        instructions2_resp.tStart = t  # local t and not account for scr refresh
        instructions2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions2_resp, 'tStartRefresh')  # time at next scr refresh
        instructions2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions2_resp.status == STARTED and not waitOnFlip:
        theseKeys = instructions2_resp.getKeys(keyList=['space'], waitRelease=False)
        _instructions2_resp_allKeys.extend(theseKeys)
        if len(_instructions2_resp_allKeys):
            instructions2_resp.keys = _instructions2_resp_allKeys[-1].name  # just the last key pressed
            instructions2_resp.rt = _instructions2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions2_text.started', instructions2_text.tStartRefresh)
thisExp.addData('instructions2_text.stopped', instructions2_text.tStopRefresh)
# check responses
if instructions2_resp.keys in ['', [], None]:  # No response was made
    instructions2_resp.keys = None
thisExp.addData('instructions2_resp.keys',instructions2_resp.keys)
if instructions2_resp.keys != None:  # we had a response
    thisExp.addData('instructions2_resp.rt', instructions2_resp.rt)
thisExp.addData('instructions2_resp.started', instructions2_resp.tStartRefresh)
thisExp.addData('instructions2_resp.stopped', instructions2_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sherlock_video"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
sherlock_videoComponents = [sherlock_clip]
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
# the Routine "sherlock_video" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "details2"-------
continueRoutine = True
# update component parameters for each repeat
details2_resp.keys = []
details2_resp.rt = []
_details2_resp_allKeys = []
# keep track of which components have finished
details2Components = [details2_text, details2_resp]
for thisComponent in details2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
details2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "details2"-------
while continueRoutine:
    # get current time
    t = details2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=details2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *details2_text* updates
    if details2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        details2_text.frameNStart = frameN  # exact frame index
        details2_text.tStart = t  # local t and not account for scr refresh
        details2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(details2_text, 'tStartRefresh')  # time at next scr refresh
        details2_text.setAutoDraw(True)
    
    # *details2_resp* updates
    waitOnFlip = False
    if details2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        details2_resp.frameNStart = frameN  # exact frame index
        details2_resp.tStart = t  # local t and not account for scr refresh
        details2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(details2_resp, 'tStartRefresh')  # time at next scr refresh
        details2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(details2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(details2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if details2_resp.status == STARTED and not waitOnFlip:
        theseKeys = details2_resp.getKeys(keyList=['space'], waitRelease=False)
        _details2_resp_allKeys.extend(theseKeys)
        if len(_details2_resp_allKeys):
            details2_resp.keys = _details2_resp_allKeys[-1].name  # just the last key pressed
            details2_resp.rt = _details2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in details2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "details2"-------
for thisComponent in details2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('details2_text.started', details2_text.tStartRefresh)
thisExp.addData('details2_text.stopped', details2_text.tStopRefresh)
# check responses
if details2_resp.keys in ['', [], None]:  # No response was made
    details2_resp.keys = None
thisExp.addData('details2_resp.keys',details2_resp.keys)
if details2_resp.keys != None:  # we had a response
    thisExp.addData('details2_resp.rt', details2_resp.rt)
thisExp.addData('details2_resp.started', details2_resp.tStartRefresh)
thisExp.addData('details2_resp.stopped', details2_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "details2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
