#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: NoteMenu.py
@time: 19-5-1 下午8:32 
Description: 
"""

import sys
from src.reading.object2.c2.NoteBooks import NoteBooks

class NoteMenu:
    def __init__(self):
        self.notebooks = NoteBooks()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu 
        
        1. Show all notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option : \n")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebooks.notes

        for note in notes:
            print("{0}: {1}\n{2}".format(note.id,note.tags,note.memo))

    def search_notes(self):
        filter = input("Search for : ")
        notes = self.notebooks.search(filter)
        self.show_notes()

    def add_notes(self):
        memo = input("Enter a memo:\n")
        self.notebooks.new_notes(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id : ")
        memo = input("Enter a memo : ")
        tags = input("Enter tags : ")

        if memo:
            self.notebooks.modify_memo(id,memo)

        if tags:
            self.notebooks.modify_tags(id,tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit()

if __name__ == '__main__':
    NoteMenu().run()
    pass