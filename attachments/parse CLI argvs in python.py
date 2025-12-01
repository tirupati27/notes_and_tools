# Parsing CLI arguments

import sys
argv_list = sys.argv[1:]
# Default actions
choice = ""
show_help = False
show_formats = True
url = ""
for arg in argv_list:
    # Handle all the possible flags which is expected from the user
    if arg in ("-v","--video"):
        choice="video"
    elif arg in ("-a","--audio"):
        choice="audio"
    elif arg in ("-vc","--video-clip"):
        choice="video-clip"
    elif arg in ("-ac","--audio-clip"):
        choice="audio-clip"
    elif arg == "--help":
        show_help = True
    elif arg == "--":
        show_formats = False
    elif arg.startswith("-"):
        print(f"Invalid flag: {arg}")
        print("Exiting the script")
        sys.exit()
    else:
        url = arg

# Now check here if the required arguments are passed
    
