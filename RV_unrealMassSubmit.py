''' run this script from the  batch script we use for instapy to launch in an environment
    doesnt acutally even need an environment though since it just uses the batch command


'''
import os


PROJECT_FILE = 'X:\\UNREAL_ARCHIVE\\FARM_TEST\\Farm_2\\Farm_2.uproject'
SEQUENCE_DIR = '/Game/PhotoStudio/Sequences/'
MAP = '/Game/PhotoStudio/Levels/Cinematic/Cinematic.Cinematic'
OUTPUT_DIR = 'x:\\UNREAL_ARCHIVE\\FARM_TEST\\RENDER\\'
FRAME_RANGE = '1-10'
CHUNK_SIZE = '100'

''' can be optimized to split from same path as sequence dir but this is fine for now'''

SEQUENCE_DIR_SYS =  'X:/UNREAL_ARCHIVE/FARM_TEST/Farm_2/Content/PhotoStudio/Sequences'

DEADLINE_PATH = "C:/Progra~1/Thinkbox/Deadline10/bin/deadlinecommand.exe"
SCRIPT_PATH = "X:\\PIPELINE\\PYTHON\\RV_unrealMassSubmit\\"

obj = os.scandir(SEQUENCE_DIR_SYS)

# List all files and directories in the specified path
for entry in obj:
    if entry.is_dir() or entry.is_file():
        x = entry.name.split(".")[0]
        print(x)

        SEQUENCE_NAME = x
        JOB_NAME = SEQUENCE_NAME
        RENDER_PATH =  OUTPUT_DIR + SEQUENCE_NAME + '\\'
        SEQUENCE_PATH = SEQUENCE_DIR + SEQUENCE_NAME + '.' + SEQUENCE_NAME

        JobInfo = {
            'Name': SEQUENCE_NAME,
            'Plugin': 'UnrealEngine',
            'Frames': FRAME_RANGE,
            'ChunkSize': CHUNK_SIZE
            }

        PluginInfo = {
            'OutputDir': RENDER_PATH,
            'MovieName': JOB_NAME,
            'ProjectFile': PROJECT_FILE,
            'Map': MAP,
            'LevelSequence': SEQUENCE_PATH,
            'Version': '4',
            'OutputFormat': 'jpg',
            'OutputQuality': '75',
            'OverrideResolution': 'True',
            'ResX': '1920',
            'ResY': '1080',
            'FrameRate': '30',
            'DisableTextureStreaming': 'True',
            'CinematicMode': 'True',
            'WarmupFrames': '0',
            'CaptureHDR': 'True',
            'HideMessages': 'False',
            'VSyncEnabled': 'True'
            }

        JOB_INFO_PATH = SCRIPT_PATH + "job_info_temp.txt"
        PLUGIN_INFO_PATH = SCRIPT_PATH + "plugin_info_temp.txt"

        with open(JOB_INFO_PATH, 'w') as f:
            for key, value in JobInfo.items():
                f.write('%s=%s\n' % (key, value))

        with open(PLUGIN_INFO_PATH, 'w') as f:
            for key, value in PluginInfo.items():
                f.write('%s=%s\n' % (key, value))


        command = DEADLINE_PATH + ' ' + JOB_INFO_PATH + ' ' + PLUGIN_INFO_PATH
        #print(command)
        os.system(command)
