# -*- coding: utf-8 -*-
# Copyright 2016 Mirco Kraenz <contact@kraenz.eu>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

# Tested on Anki Version 2.0.33, Qt 4.8.4, PyQt 4.10

# import the main window object (mw) from ankiqt
from aqt import mw
from aqt.editor import Editor # the editor when you click "Add" in Anki
from anki.hooks import addHook

SHORTCUT = "Alt+D"
    
def clear_editor(editor):
    u'''Remove text from fields in editor. '''
    note = editor.note
    # enumerate all fieldNames of the current note
    for c, field_name in enumerate(mw.col.models.fieldNames(note.model())):
        note[field_name] = ''
    note.flush()  # never forget to flush
    mw.reset()  # refresh gui
    
def setup_buttons(editor):
    u"""Add the buttons to the editor."""
    editor._addButton("clear_fields1", lambda edito=editor: clear_editor(edito), _(SHORTCUT),
                       text=u"C", tip="Clear field entries (" + SHORTCUT +")")

# register callback function that gets executed after setupEditorButtons has run. 
# See Editor.setupEditorButtons for details
addHook("setupEditorButtons", setup_buttons)
