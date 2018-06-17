import os
import sys
import time
import retro.data
import matplotlib.pyplot as plt

from tqdm import tqdm

from matplotlib import animation
from IPython.display import display

import tempfile
from zipfile import ZipFile

import requests
import urllib


def save_frames_as_gif(frames, filename=None):
    """
    Save a list of frames as a gif
    """ 
    patch = plt.imshow(frames[0])
    plt.axis('off')
    def animate(i):
        patch.set_data(frames[i])
    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    if filename:
        anim.save(filename, dpi=72, writer='imagemagick')
        
###########################################################
# Utilities from https://github.com/frenchie4111/dumbrain #
###########################################################

# Global
_download_pbar = None

def install_games_from_rom_dir(romdir):
    """
    Add the ROMs to the Retro Game list
    """
    roms = [os.path.join(romdir, rom) for rom in os.listdir(romdir)]
    retro.data.merge(*roms, quiet=False)

def mkdirp( folder ):
    if not os.path.exists( folder ):
        print( 'Directory', folder, 'didn\'t exist, making' )
        os.makedirs( folder )

def download( url, dest_file, show_progress=True, loading_bar=tqdm ):
    """
    Downloads file to given file. Path to file should exist. Uses _download_pbar
    global
    """

    def reporthook( count, part_size, total_size ):
        global _download_pbar
        if _download_pbar is None:
            _download_pbar = loading_bar(total = total_size)
        _download_pbar.update(part_size)

    urllib.request.urlretrieve(url, dest_file, reporthook=reporthook)
    global _download_pbar
    _download_pbar.close()
    _download_pbar = None

def unzip(zip_filename, dest_folder, loading_bar=tqdm ):
    """
    Unzipping archive
    """
    zip_file = ZipFile( zip_filename )

    all_files = zip_file.infolist()
    uncompressed_size = sum((file.file_size for file in zip_file.infolist()))

    files = zip_file
    # Uncompressing
    with loading_bar(total=uncompressed_size ) as pbar:
        for file in all_files:
            zip_file.extract( file, dest_folder)
            pbar.update(file.file_size )

def download_and_unzip_rom_archive_from_url(download_url, save_folder, loading_bar=tqdm):
    
    # Create folder
    mkdirp(save_folder)

    temp_zip_filename = 'temp.zip'

    with tempfile.TemporaryDirectory() as temp_dir:
        full_temp_zip_filename = os.path.join(temp_dir, temp_zip_filename)
        download(download_url, full_temp_zip_filename, loading_bar=loading_bar)
        unzip(full_temp_zip_filename, save_folder, loading_bar=loading_bar)
