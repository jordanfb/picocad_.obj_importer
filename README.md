# picocad .obj importer
requires Python3

In terminal:
`python importobj.py {obj file} {scale(optional)}`

I advise using some tool to shrink the number of polygons before importing it to picocad, or else picocad may be unresponsive, or unbearably slow.

I used meshlab's "quadratic edge collapse decimation" to do this for meshes that were supposedly "low-poly"

Not by picocad's standards ;)

If you want textures to be imported as well, have python pillow installed.
I ran the toaster example through the .obj exporter, and back through this .obj importer:


## Before:  
![alt text](https://github.com/Zinc-OS/picocad_.obj_importer/blob/main/files/picocad_4.gif)  
## After:  
![alt text](https://github.com/Zinc-OS/picocad_.obj_importer/blob/main/files/picocad_7.gif)  
