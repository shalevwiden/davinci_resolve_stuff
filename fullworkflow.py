import os
import subprocess

class workflow:
    '''
    Make different ones for this for different channels

    Then spend the full day grinding my ass off for each one
    '''
    def __init__(self):
        
        # hmmmm
        self.medialocation=""

        self.variabledict={
            "projectname":"earthvideo",
            "mediafolder":"/Users/shalevwiden/Downloads/youtubestuff/framesrendered/line_animations/apple",
             "TargetDir": "/Users/shalevwiden/Downloads/youtubestuff/framesrendered",
            "CustomName": "appledone1",


        }

        self.projectname=self.variabledict['projectname']

        def essentials(projectname):
            pm=res.GetProjectManager()

            pm.CreateProject(projectname)
            pm.LoadProject(projectname)	

            proj = pm.GetCurrentProject()
            mp = proj.GetMediaPool()

            return pm,proj,mp,projectname

        self.pm,self.proj,self.mp,self.projectname=essentials()


        self.mediafolder = self.variabledict['mediafolder']
        # logic to get the media files
        self.videofiles = [os.path.join(self.mediafolder, f) for f in os.listdir(self.mediafolder) if f.lower().endswith(('.mov', '.mp4', '.avi'))]
        audiofiles='definelater'
        imagefiles='definelater'


        self.save_settings = {
          "TargetDir": self.variabledict['TargetDir'],
            "CustomName": self.variabledict['CustomName']


        }

    def setup():
        pass
    def addtotimeline(self):
        clips=mp.ImportMedia(self.videofiles)
        print(f"Imported {len(self.videofiles)} files into Media Pool.")
        pm.SaveProject()	


        timeline_name = "Main Timeline"
        timeline = proj.GetCurrentTimeline()

        if not timeline:
            timeline = mp.CreateEmptyTimeline(timeline_name)

        # clips is already a list
        mp.AppendToTimeline(clips)	
        pm.SaveProject()	
        
    def edit_clips(self):
        '''
        This function should handle alot of the actual editing logic.

        Like adding text, music, transitions, filters, all that cool stuff ngl bro.
        
        '''
        pass
        
        def change_clip_speed():
            pass
            
    def renderandsave(self):
                # in this file we will render and save the final product
        timeline = proj.GetCurrentTimeline()
        # current = timeline.GetRenderSettings()

        # can change output location and add a name to the file.

        proj.SetRenderSettings(self.save_settings)	
        # 2. Create a render job (returns a job ID you can track)
        job_id = proj.AddRenderJob()

        proj.StartRendering()

        # proj.SetCurrentTimeline(timeline) maybe this

        def helpful():
            presets=proj.GetRenderPresetList()	
