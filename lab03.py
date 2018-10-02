# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 19:20:03 2018

@author: gvb18161
"""

class Assignment:
    def __init__(self, assignmentType1, assignmentMark1, assignmentType2, assignmentMark2):
        self.assignmentType1 = assignmentType1
        self.assignmentType2 = assignmentType2
        self.assignmentMark1 = assignmentMark1
        self.assignmentMark2 = assignmentMark2 
        
    def setAssignmentType1(self, assignmentType1):
        self.assignmentType1 = assignmentType1
    def setAssignmentType2(self, assignmentType2):
        self.assignmentType2 = assignmentType2
    def setAssignmentMark1(self, assignmentMark1):
        self.assignmentMark1 = assignmentMark1
    def setAssignmentMark2(self, assignmentMark2):
        self.assignmentMark2 = assignmentMark2
    
    def getAssignmentType1(self):
        return self.assignmentType1
    def getAssignmentType2(self):
        return self.assignmentType2
    def getAssignmentMark1(self):
        return self.assignmentMark1
    def getAssignmentMark2(self):
        return self.assignmentMark2
    
    
    
    
class Module:
    def __init__(self, assignment, moduleName1, moduleName2, moduleName3):
        self.assignment = assignment 
        self.moduleName1 = moduleName1
        self.moduleName2 = moduleName2 
        self.moduleName3 = moduleName3 
    
    def setModuleName1(self, moduleName1):
        self.moduleName1 = moduleName1
    def setModuleName2(self, moduleName2):
        self.moduleName2 = moduleName2
    def setModuleName3(self, moduleName3):
        self.moduleName3 = moduleName3
    def setAssignment(self, assignment):
        self.assignment = assignment
        
    def getModuleName1(self): 
        return self.moduleName1 
    def getModuleName2(self): 
        return self.moduleName2
    def getModuleName3(self): 
        return self.moduleName3
    def getAssignment(self):
        return self.assignment
    
class Student:
    def __init__(self, name, stNo, module):
        self.name = name 
        self.stNo = stNo 
        self.module = module 
        
    def setName(self, name): 
        self.name = name 
    def setStudentNo(self, stNo):
        self.stNo = stNo
    def setModule(self, module):
        self.module = module
        
    def getName(self):
        return self.name 
    def getModule(self):
        return self.module
    def getStNo(self):
        return self.stNo
    
def test():
    a = Assignment("lab", 30, "final", 50)
    m = Module (a, "994","995","996")
    st = Student("wjs", "1234", m)
    print (st.name, m.moduleName1, (a.assignmentMark1+ a.assignmentMark2))
    
        
    
    
        
