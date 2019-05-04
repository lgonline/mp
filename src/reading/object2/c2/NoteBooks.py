#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: NoteBooks.py
@time: 19-5-1 下午6:27 
Description: 
"""

from src.reading.object2.c2.Notes import Note

class NoteBooks:
    def __init__(self):
        self.notes = []

    def new_notes(self, memo, tags=''):
        self.notes.append(Note(memo,tags))

    def __find_note(self,noteid):
        for note in self.notes:
            if str(noteid) == str(noteid):
                return note
        return None

    def modify_memo(self,noteid ,memo):

        # for note in self.notes:
        #     if note.id == noteid:
        #         note.memo = memo
        #         break
        note = self.__find_note(noteid)
        if note:
            note.memo = memo
            return True
        return False
        # self.__find_note(noteid).memo = memo

    def modify_tags(self,noteid,tags):
        for note in self.notes:
            if noteid == noteid:
                note.tags = tags

    def search(self,filter):
        return [note for note in self.notes if note.mathc(filter)]

if __name__ == '__main__':
    n1 = NoteBooks()
    n1.new_notes("hello world!!!")
    n1.new_notes("liugang52")

    print("---------------------1--------------------")
    print("n1.notes[0].memo is ",n1.notes[0].memo)
    print("n1.notes[1].memo is ", n1.notes[1].memo)
    n1.modify_memo(0,"liugang9")
    print("---------------------2--------------------")
    print("n1.notes[0].memo is ", n1.notes[0].memo)
    print("n1.notes[1].memo is ",n1.notes[1].memo)
    pass