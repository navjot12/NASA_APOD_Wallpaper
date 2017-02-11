#NASA APOD Wallpaper
######For Ubuntu systems

This script will set your wallpaper to NASA's Astronomy Picture of the Day available at https://apod.nasa.gov/apod/.
If a non-image item is the current APOD, the script will choose any image from the archives.

To use:
1. Clone this repository.
2. In nasa_apod_wallpaper.py, edit "user" variable in **line 9** to your own username.
3. Run nasa_apod_wallpaper.py!

Note: The script sleeps for 15 seconds to allow complete download of the APOD.

To have this script run daily, run the following commands in terminal:

```crontab -e```

This will open a file to be edited in terminal. Enter the following statement in it

```* */12 * * * /path/to/python nasa_apod_wallpaper.py```

where 'path/to/' represents the path to nasa_apod_wallpaper.py script.

Press ```ctrl+x``` to exit file editing mode and press ```Y``` to save changes.

This will run the script in your system in every 12 hours!

PS: Happy birthday to my friend [Arpit Gogia](https://github.com/arpitgogia) who was the inspiration behind this!

##BONUS

A similar script to NASA-APOD, wallpaperscraft.py gets wallpapers from https://wallpaperscraft.com
Modify categories list in **line 12** of script to alter categories to get wallpaper from
Check out categories at _https://wallpaperscraft.com_
