# -*- coding: utf-8 -*-
# Copyright 2016 Mirco Kraenz <contact@kraenz.eu>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

# Tested on Anki Version 2.0.33, Qt 4.8.4, PyQt 4.10

from aqt import mw
from aqt.editor import Editor # the editor when you click "Add" in Anki
from anki.hooks import addHook
from . import pyperclip
from paste_to_my_field_by_miro.settings import FIELD_NAMES, SHORTCUT

def paste_to_my_field(editor):
    u'''Paste clipboard text to field specified by constant FIELD_NAMES '''
    note = editor.note
    # enumerate all fieldNames of the current note
    for _, field_name in enumerate(mw.col.models.fieldNames(note.model())):
        if field_name in FIELD_NAMES:
            note[field_name] = pyperclip.paste()
    mw.reset()

def setup_button_paste_to_my_field(editor):
    u"""Add the buttons to the editor."""
    editor._addButton("paste_to_my_field_by_miro", 
                      lambda edito=editor: paste_to_my_field(edito), _(SHORTCUT),
                       text=u"P", tip="Paste to my_field (" + SHORTCUT +")")

addHook("setupEditorButtons", setup_button_paste_to_my_field)
