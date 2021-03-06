
import astropy.io.fits
import os,glob


datafolder = 'input'
targetfolder = 'output'


def do_something(input_file, output_file, factor=10):
    data = astropy.io.fits.getdata(input_file)
    divided = data / factor
    astropy.io.fits.writeto(output_file, divided)


def so_something_on_folder(input_, output_, factor, pattern):
    filelist=sorted(glob.glob(input_+'/'+pattern))
    print filelist
    for filename in filelist:
        filename=os.path.basename(filename)
        print filename
        filename2,ext=os.path.splitext(filename)
        if filename.lower().endswith('.fits'):
            output_file = os.path.join(output_, filename2+'-divided'+ext)
            input_file = os.path.join(datafolder, filename)
            do_something(input_file, output_file, factor)


if __name__ == '__main__':
    so_something_on_folder(datafolder, targetfolder, factor=1, pattern='*.fits')
