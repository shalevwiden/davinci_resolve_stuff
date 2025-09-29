import os

pm=res.GetProjectManager()
proj = pm.GetCurrentProject()


mp = proj.GetMediaPool()

mediafolder = "/Users/shalevwiden/Downloads/youtubestuff/framesrendered/line_animations/apple"
# logic to get the media files
videofiles = [os.path.join(mediafolder, f) for f in os.listdir(mediafolder) if f.lower().endswith(('.mov', '.mp4', '.avi'))]
audiofiles='definelater'
imagefiles='definelater'
# clips will be a list of media clip objects
clips=mp.ImportMedia(videofiles)
print(f"Imported {len(videofiles)} files into Media Pool.")
pm.SaveProject()	





# logic to get the media files
videofiles = [os.path.join(mediafolder, f) for f in os.listdir(mediafolder) if f.lower().endswith(('.mov', '.mp4', '.avi'))]

timeline_name = "Main Timeline"
timeline = proj.GetCurrentTimeline()

if not timeline:
    timeline = mp.CreateEmptyTimeline(timeline_name)

# clips is already a list
mp.AppendToTimeline(clips)	
pm.SaveProject()	
