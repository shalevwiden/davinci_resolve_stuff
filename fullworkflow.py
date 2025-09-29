import os
import subprocess
import time
from datetime import datetime

class workflow:
    '''
    Make different ones for this for different channels

    Then spend the full day grinding my ass off for each one

    Copy paste this entire thing to generate a video fast.
    The only thing that you need to change is self.variabledict
    '''
    def __init__(self):
        
        # hmmmm
        self.medialocation=""

        now = datetime.now()
        self.time=now.strftime("%d %H:%M")  # e.g. "29 13:47"








        '''
        This is the only thing that needs to be changed actually
        '''
        self.variabledict={
            "projectname":"pianogrind",
            "mediafolder":"/Users/shalevwiden/Downloads/youtubestuff/ChordScape/sep25-26/workingfolder",
            "vertical":True,
             "TargetDir": "/Users/shalevwiden/Downloads/youtubestuff/ChordScape/sep25-26/output",
            "CustomName": f"output{self.time}",


        }
        if not os.path.exists(self.variabledict['TargetDir']):
            os.mkdir(self.variabledict['TargetDir'])

        self.projectname=self.variabledict['projectname']

        def essentials(projectname):
            pm=res.GetProjectManager()

            pm.CreateProject(projectname)
            pm.LoadProject(projectname)	

            proj = pm.GetCurrentProject()
            mp = proj.GetMediaPool()

            return pm,proj,mp,projectname

        self.pm,self.proj,self.mp,self.projectname=essentials(projectname=self.variabledict['projectname'])


        self.mediafolder = self.variabledict['mediafolder']
        # logic to get the media files
        self.videofiles = [os.path.join(self.mediafolder, f) for f in os.listdir(self.mediafolder) if f.lower().endswith(('.mov', '.mp4', '.avi'))]
        audiofiles='definelater'
        imagefiles='definelater'


        self.save_settings = {
          "TargetDir": self.variabledict['TargetDir'],
            "CustomName": self.variabledict['CustomName']


        }

    def setup(self):
        '''
    
        add more functions in the future
        
        '''
        print(f'setting up ')
        def set_settings():
            # default stuff
            settings = self.proj.GetSetting()
            # settings is a dict object

            # this should work
            # for good apple quality
            self.proj.SetCurrentRenderFormatAndCodec("mov", "ProRes422HQ")

            # this works phew
            vertical=self.variabledict['vertical']
            if vertical:
                # as a string
                self.proj.SetSetting("timelineResolutionWidth",  "1080")   
                self.proj.SetSetting("timelineResolutionHeight", "1920")
                

            self.pm.SaveProject()

        set_settings()  


    def addtotimeline(self):
        clips=self.mp.ImportMedia(self.videofiles)
        print(f"Imported {len(self.videofiles)} files into Media Pool.")
        self.pm.SaveProject()	


        timeline_name = "Main Timeline"
        timeline = self.proj.GetCurrentTimeline()

        if not timeline:
            timeline = self.mp.CreateEmptyTimeline(timeline_name)

        # clips is already a list
        time.sleep(1)
        self.mp.AppendToTimeline(clips)	
        self.pm.SaveProject()	
        res.OpenPage('edit')
        
    def edit_clips(self):
        '''
        This function should handle alot of the actual editing logic.

        Like adding text, music, transitions, filters, all that cool stuff ngl bro.
        
        '''
        pass
        
        def change_clip_speed():
            pass
            
    def renderandsave(self):
        time.sleep(1)
                # in this file we will render and save the final product
        timeline = self.proj.GetCurrentTimeline()
        # current = timeline.GetRenderSettings()

        # can change output location and add a name to the file.

        self.proj.SetRenderSettings(self.save_settings)	
        # 2. Create a render job (returns a job ID you can track)
        job_id = self.proj.AddRenderJob()

        self.proj.StartRendering()

        # proj.SetCurrentTimeline(timeline) maybe this

        def helpful():
            presets=self.proj.GetRenderPresetList()	

def main():
    workflow_obj=workflow()
    workflow_obj.setup()
    # workflow_obj.addtotimeline()
    # workflow_obj.renderandsave()

def just_render():
    workflow_obj=workflow()
    workflow_obj.renderandsave()

# just_render()


main()