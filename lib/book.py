#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    @property
    def title(self):
        """The title property"""
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            print("Title must be a string.")
        
    @property
    def page_count(self):
        """The page_count property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
