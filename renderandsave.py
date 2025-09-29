# in this file we will render and save the final product
timeline = proj.GetCurrentTimeline()
# current = timeline.GetRenderSettings()

custom_settings = {
    "TargetDir": "/Users/shalevwiden/Downloads/youtubestuff/framesrendered",
    "CustomName": "output_test"
}
# can change output location and add a name to the file.

proj.SetRenderSettings(custom_settings)	
# 2. Create a render job (returns a job ID you can track)
job_id = proj.AddRenderJob()

proj.StartRendering()

# proj.SetCurrentTimeline(timeline) maybe this

def helpful():
    presets=proj.GetRenderPresetList()	
