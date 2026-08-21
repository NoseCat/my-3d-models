from PIL import Image
import glob

file_list = sorted(glob.glob('*.png')) 

frames = [Image.open(img) for img in file_list]

frames[0].save('output.gif', 
               save_all=True, 
               append_images=frames[1:], 
               duration=42, 
               loop=0)
