# # import the main window object (mw) from aqt
# from aqt import mw
# # import the "show info" tool from utils.py
# from aqt.utils import showInfo, qconnect
# # import all of the Qt GUI library
# from aqt.qt import *

# # We're going to add a menu item below. First we want to create a function to
# # be called when the menu item is activated.

# def testFunction() -> None:
#     # get the number of cards in the current collection, which is stored in
#     # the main window
#     cardCount = mw.col.cardCount()
#     # show a message box
#     showInfo("Card count: %d" % cardCount)

# # create a new menu item, "test"
# action = QAction("test", mw)
# # set it to call testFunction when it's clicked
# qconnect(action.triggered, testFunction)
# # and add it to the tools menu
# mw.form.menuTools.addAction(action)

# import the main window object (mw) from aqt
import aqt
import aqt.editor
import aqt.gui_hooks
# import anki.hooks
# from PyQt6.QtWidgets import QApplication
from typing import List, Tuple
from anki.models import NotetypeDict, NotetypeId
# import sys
from aqt import mw
from aqt.notetypechooser import NotetypeChooser

def editor_switch_note_card_type(editor: aqt.editor.Editor, note_type: str):
    # doesn't do anything
    editor.note.note_type = mw.col.models.by_name(note_type)
    # does something
    editor.note['Front'] += 'hello world'
    # not sure if this does anything
    mw.col.update_note(editor.note)
    
    # print(editor.note.note_type()[id])

    # print(f"editor_switch_focus_field, field_name: {field_name}")
    # what the fk is this? just gets the note type of something?
    # print(editor.note)
    # note_type_name = editor.note.model()['name']
    # print(note_type)
    # print(editor.note)

    # check if we're acting on the right not
    # if note_type_name == note_type:
    #     # basically loop over all the fields to check if we've met something
    #     field_index = 0
    #     for field in editor.note.model()['flds']:
    #         if field['name'] == field_name:
    #             break
    #         field_index += 1
    #     print(f"focusing on field index {field_index}")
    #     # don't know what setfocus does
    #     editor.web.setFocus()
    #     # calls focus a specific field
    #     editor.web.eval("focusField(%d);" % int(field_index))

def editor_init_shortcuts(shortcuts: List[Tuple], editor: aqt.editor.Editor):
    # get the config for a specific field
    config = aqt.mw.addonManager.getConfig(__name__)

    # grab the specific json object from the dictionary
    focus_field_shortcuts = config['change_note_card_type_shortcuts']
    # for every user-defined shortcut
    for shortcut in focus_field_shortcuts:
        # get the keybinding
        shortcut_combination: str = shortcut['shortcut']
        # get the notetype for which it applies to 
        note_type: str = shortcut['note_type']
        # print(f"set up shortcut {shortcut_combination} for field {field_name}")
        shortcut_entry = (shortcut_combination, lambda note_type=note_type: editor_switch_note_card_type(editor, note_type), True)
        shortcuts.append(shortcut_entry)
    print("everything is loaded")

def note_type_changed_notification(note_type_dic: NotetypeDict): 
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')
    print('--------------------[note type actually changed]')

# add shortcuts to quickly focus on a particular field the function that we're
# hooking into automatically gives a shortcut and editor global object which we
# can write to
aqt.gui_hooks.editor_did_init_shortcuts.append(editor_init_shortcuts)
aqt.gui_hooks.current_note_type_did_change.append(note_type_changed_notification)