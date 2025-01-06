#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file dest_select.py
 @brief RTC for specifying destination using GUI
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


import tkinter as tk
from tkinter import StringVar


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
dest_select_spec = ["implementation_id", "dest_select", 
         "type_name",         "dest_select", 
         "description",       "RTC for specifying destination using GUI", 
         "version",           "1.0.0", 
         "vendor",            "rsdlab", 
         "category",          "User Interface", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         "conf.default.place1", "Home",
         "conf.default.place2", "Reception desk",
         "conf.default.place3", "Room1",
         "conf.default.place4", "Room2",

         "conf.__widget__.place1", "text",
         "conf.__widget__.place2", "text",
         "conf.__widget__.place3", "text",
         "conf.__widget__.place4", "text",

         "conf.__type__.place1", "string",
         "conf.__type__.place2", "string",
         "conf.__type__.place3", "string",
         "conf.__type__.place4", "string",

         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class dest_select
# @brief RTC for specifying destination using GUI
# 
# 
# </rtc-template>
class dest_select(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_gui_in = OpenRTM_aist.instantiateDataType(RTC.TimedShortSeq)
        """
        """
        self._gui_inIn = OpenRTM_aist.InPort("gui_in", self._d_gui_in)
        self._d_gui_out = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        """
        """
        self._gui_outOut = OpenRTM_aist.OutPort("gui_out", self._d_gui_out)
        self._d_place = OpenRTM_aist.instantiateDataType(RTC.TimedWString)
        """
        """
        self._placeOut = OpenRTM_aist.OutPort("place", self._d_place)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """
        
         - Name:  place1
         - DefaultValue: Home
        """
        self._place1 = ['Home']
        """
        
         - Name:  place2
         - DefaultValue: Reception desk
        """
        self._place2 = ['Reception desk']
        """
        
         - Name:  place3
         - DefaultValue: Room1
        """
        self._place3 = ['Room1']
        """
        
         - Name:  place4
         - DefaultValue: Room2
        """
        self._place4 = ['Room2']
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("place1", self._place1, "Home")
        self.bindParameter("place2", self._place2, "Reception desk")
        self.bindParameter("place3", self._place3, "Room1")
        self.bindParameter("place4", self._place4, "Room2")
		
        # Set InPort buffers
        self.addInPort("gui_in",self._gui_inIn)
		
        # Set OutPort buffers
        self.addOutPort("gui_out",self._gui_outOut)
        self.addOutPort("place",self._placeOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
		
        return RTC.RTC_OK

    def onActivated(self, ec_id):
    
        return RTC.RTC_OK
	

    def onDeactivated(self, ec_id):
    
        return RTC.RTC_OK
	

    def onExecute(self, ec_id):

        def button_click1():
            self._d_gui_out.data = 1
            self._d_place.data = self._place1[0]
            
            print(self._d_place.data)
            self._gui_outOut.write()
            self._placeOut.write()

        def button_click2():
            self._d_gui_out.data = 2
            self._d_place.data = self._place2[0]
            print(self._d_place.data)
            self._gui_outOut.write()      
            self._placeOut.write()
            
        def button_click3():
            self._d_gui_out.data = 3
            self._d_place.data = self._place3[0]
            print(self._d_place.data)
            self._gui_outOut.write()      
            self._placeOut.write()
            
        def button_click4():
            self._d_gui_out.data = 4
            self._d_place.data = self._place4[0]
            print(self._d_place.data)
            self._gui_outOut.write()
            self._placeOut.write()
                    
        def close_app():
            root.destroy()  
            
        root=tk.Tk()

        root.title("Guidance")

        root.geometry("500x400")

            
        button1 = tk.Button(
            text=self._place1,
            font=10,
            width=40,
            height=3,
            command = button_click1
        )
        button1.place(x=60, y=20) #ボタンを配置する位置の設定

        button2 = tk.Button(
            text=self._place2,
            font=10,
            width=40,
            height=3,
            command=button_click2,
        )
        button2.place(x=60, y=110) #ボタンを配置する位置の設定

        button3 = tk.Button(
            text=self._place3,
            font=10,
            width=40,
            height=3,
            command=button_click3,
        )
        button3.place(x=60, y=200) #ボタンを配置する位置の設定

        button4 = tk.Button(
            text=self._place4,
            font=10,
            width=40,
            height=3,
            command=button_click4,
        )
        button4.place(x=60, y=290) #ボタンを配置する位置の設定

        root.mainloop()      

        return RTC.RTC_OK
	
 


def dest_selectInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=dest_select_spec)
    manager.registerFactory(profile,
                            dest_select,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    dest_selectInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("dest_select" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

