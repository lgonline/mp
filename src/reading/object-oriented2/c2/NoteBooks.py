#!/usr/bin/env python  
# -*- coding: utf-8 -*-

"""
@author: mlcc
@file: NoteBooks.py
@time: 19-5-1 下午6:27 
Description: 
"""



class NoteBooks:
    def __init__(self):
        self.notes = []

    def new_notes(self, memo, tags=''):
        self.notes.append(Note(memo,tags))

    def modify_memo(self,noteid ,memo):
        for note in self.notes:
            if note.id == noteid:
                note.memo = memo
                break

    def modify_tags(self,noteid,tags):
        for note in self.notes:
            if noteid == noteid:
                note.tags = tags

    def search(self,filter):
        return [note for note in self.notes if note.mathc(filter)]

# if __name__ == '__main__':
#     n1 = NoteBooks()
#     n1.new_notes("hello world!!!")
#     n1.new_notes("liugang52")
#
#     print(n1.notes)
#     pass