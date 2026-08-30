from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
from comtypes import CLSCTX_ALL
devices=AudioUtilities.GetSpeakers()
interface=devices._dev.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
volume=interface.QueryInterface(IAudioEndpointVolume)
def volume_up():
    current_volume=volume.GetMasterVolumeLevelScalar()
    new_volume=min(current_volume+0.10,1.0)
    volume.SetMasterVolumeLevelScalar(new_volume,None)
    print("Volume:",int(new_volume*100),"%")
#volume_up()
def volume_down():
    current_volume=volume.GetMasterVolumeLevelScalar()
    new_volume=max(current_volume-0.10,0.0)
    volume.SetMasterVolumeLevelScalar(new_volume,None)
    print("Volume:",int(new_volume*100),"%")
#volume_down()
def mute():
    volume.SetMute(1,None)
    print("Volume Muted")
def unmute():
    volume.SetMute(0,None)
    print("Volume Unmute")
#mute()
#unmute()
