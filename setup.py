import os


def essentials():
    pm=res.GetProjectManager()

    projectname='applevid'
    pm.CreateProject(projectname)
    pm.LoadProject(projectname)	

    proj = pm.GetCurrentProject()
    mp = proj.GetMediaPool()

    return pm,proj,mp

pm,proj,mp=essentials()


# big ass dictionary lol
def set_settings():
    # default stuff
    settings = proj.GetSetting()
    # settings is a dict object

    # this should work
    # for good apple quality
    proj.SetCurrentRenderFormatAndCodec("mov", "ProRes422HQ")

    # this works phew
    vertical=False
    if vertical:
        # as a string
        proj.SetSetting("timelineResolutionWidth",  "1080")   
        proj.SetSetting("timelineResolutionHeight", "1920")
        

    pm.SaveProject()

set_settings()

def see_settings():
    settings = proj.GetSetting()
    for k, v in settings.items():
        print(k, v)

# theres also a project media location one
location='projectMediaLocation'

# set the name
	

mp = proj.GetMediaPool()

mediafolder = "/Users/shalevwiden/Downloads/youtubestuff/framesrendered/line_animations/apple"
# logic to get the media files
videofiles = [os.path.join(mediafolder, f) for f in os.listdir(mediafolder) if f.lower().endswith(('.mov', '.mp4', '.avi'))]
audiofiles='definelater'
imagefiles='definelater'
mp.ImportMedia(videofiles)
print(f"Imported {len(videofiles)} files into Media Pool.")
pm.SaveProject()	
res.OpenPage('edit')


