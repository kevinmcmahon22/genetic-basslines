# 
# Evolutionary Music in python
# 
# CSE 848 semester project
# 
# Kevin McMahon
# 
# 
# 
# Using mingus, Lilypond, FluidSynth, midi2audio
# 

from mingus.containers import Track, Bar, Note
from mingus.containers.instrument import MidiInstrument, Piano
from mingus.midi import fluidsynth as fs

import mingus.midi.midi_file_out as mfo
import mingus.extra.lilypond as lilypond
import mingus.extra.tablature as tab

import os

# Determine what output to produce
midi_file = False
playback = True
wav = False
sheet_music = False
tablature = False

bpm = 200

soundfont = 'FluidR3_GM.sf2'



def evaluate_baseline(baseline):
    pass



def play_baseline(baseline):
    '''
    
    Parameters
    ----------
    baseline : list
               notes of baseline

    Returns none
    -------
    None.

    '''
    
    # Create instrument
    i = MidiInstrument("Jazz Bass")
    i.instrument_nr = 34
    
    t = Track(i)
    b = Bar()
    for note in baseline:
        # may change duration to second part of tuple for triplets/eighths
        b.place_notes(Note().from_int(note), 4)
        
        # Create new bar if previous bar full
        if b.is_full():
            t.add_bar(b)
            b = Bar()
    
    # play baseline
    fs.init(soundfont)
    fs.play_Track(t, 1, bpm)
    
def main():
    
    # Create instrument
    i = MidiInstrument("Jazz Bass")
    i.instrument_nr = 34

    # Create track
    t = Track(i)
    
    # For each measure/chord in a progression
    # Create a bar, add notes to bar
    for i in range(2):
        b = Bar()
    
    
        # range('C-0', 'B-8')
        # Use note_int_range(note) to see if random note can be added to melody
        # Check notes when reduced to list notation after GP operations
        b.place_notes("A-3", 4)
        b.place_notes("Bb-3", 4)
        b.place_notes("F#-3", 4)
        b.place_notes('G-3', 4)
        t.add_bar(b)
    
    
    # 
    # OUTPUT
    # 
    
    filename = 'new'
    midi_filename = filename + '.mid'
    
    # Write to midi file
    if midi_file:
        mfo.write_Track(midi_filename, t, bpm=bpm, repeat=0, verbose=True)
    
    # Play midi file
    if playback:
        fs.init(soundfont)
        fs.play_Track(t, 1, bpm)
    
    # Make wav file from .mid
    if wav:
        os.system(f'fluidsynth -F {filename}.wav {soundfont} {midi_filename}')
    
    # Generate sheet music
    if sheet_music:
        bassline_pond = lilypond.from_Track(t)
        lilypond.to_png(bassline_pond, filename)
    
    # Write to ASCII tab if notes in guitar range
    if tablature:
        print(tab.from_Track(t))