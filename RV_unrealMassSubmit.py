''' run this script from the  batch script we use for instapy to launch in an environment
    doesnt acutally even need an environment though since it just uses the batch command


'''
import os


PROJECT_FILE = 'X:\\2022_02_RV_NFT\\03_production\\01_cg\\07_unreal\\prototype_1\\prototype_1.uproject'
SEQUENCE_DIR = '/Game/Sequences/variants/'
MAP = '/Game/Maps/Main.Main'
OUTPUT_DIR = 'X:\\2022_02_RV_NFT\\04_renders\\TEMP\\'
FRAME_RANGE = '1-55'
CHUNK_SIZE = '100'

''' can be optimized to split from same path as sequence dir but this is fine for now'''

SEQUENCE_DIR_SYS =  'X:\\2022_02_RV_NFT\\03_production\\01_cg\\07_unreal\\prototype_1\\Content\\Sequences\\variants'

DEADLINE_PATH = "C:/Progra~1/Thinkbox/Deadline10/bin/deadlinecommand.exe"
SCRIPT_PATH = "X:\\PIPELINE\\PYTHON\\RV_unrealMassSubmit\\"


''''note: this does find subdirectories but sequence dir would need to be parsed as sub folders as well, saving that for later'''

def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry

#obj = os.scandir(SEQUENCE_DIR_SYS)
obj = scantree(SEQUENCE_DIR_SYS)

# List all files and directories in the specified path
for entry in obj:
    if entry.is_dir() or entry.is_file():
        x = entry.name.split(".")[0]
        print(x)

        SEQUENCE_NAME = x
        JOB_NAME = 'RVUR_' + SEQUENCE_NAME
        RENDER_PATH =  OUTPUT_DIR + SEQUENCE_NAME + '\\'
        SEQUENCE_PATH = SEQUENCE_DIR + SEQUENCE_NAME + '.' + SEQUENCE_NAME

        JobInfo = {
            'Name': JOB_NAME,
            'Plugin': 'UnrealEngine',
            'Frames': FRAME_RANGE,
            'ChunkSize': CHUNK_SIZE
            }

        PluginInfo = {
            'OutputDir': RENDER_PATH,
            'MovieName': SEQUENCE_NAME,
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
            'WarmupFrames': '5',
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
