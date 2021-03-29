import sys
import random
import re
import time
import math
try:
	from PIL import Image
except:
	print("Pillow is not installed. Any texture cannot be loaded")
file= time.time()
file=str(file)
vertices=0
faces=0
scalar=1
vtlist=[]
mtl=None
endstring=str("99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999999944999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999999499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999940499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999405999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999494004999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999949400049999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999494000099999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999944940000499999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999994499500005999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999994940000004999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999404000059999999999999999999999999999999999999999999999999999999999999999999945549999999999999999999999\n"+
	"99999999999999999999999994044000049999999999999999999999999999999999999999999999999999999999999999999405999999999999999999999999\n"+
	"99999999999999999999999945995000599999999999999999999999999999999999999999999999999999999999999999994049999999999999999999999999\n"+
	"99999999999999999999994549940000499999449999999949999999999400054999999999999999999999999999999999940499999999999999999999999999\n"+
	"99999999999999999999995499940005999994049999999499999999440055000999999999999999999999999999999999404999999999999999999999999999\n"+
	"99999999999999999999949999900004999940599999999999999940054999940999999999999999999999999999999999049999999999999999999999999999\n"+
	"99999999999999999999499999400059999400499999999999994000599999995999999999999999999999999999999995099999999999999999999999999999\n"+
	"99999999999999999999999999500049995004995499999944454500999999940999999999994999999999999999999940499999999999999999999999999999\n"+
	"99999999999999999999999999000499400059400999999400549004999999940999999994999999999999999999999405999999999999999999999999999999\n"+
	"99999999999999999999999994000994040094005999995005994059999999904999999404999949999999999999994009999999999999999999999999999999\n"+
	"99999999999999999999999990004400450440004999440004940049999999404999994050009949999999944555440049999999999999999999999999999999\n"+
	"99999999999999999999999940004049404400004999400059940099999999009999940004004994494999999999400049999999999999999999999999999999\n"+
	"99999999999999999999999900000494009000040494000049900499999994059999500049504940049999499994000500449449999999999999999999999999\n"+
	"99999999999999999999999500049995045000094040000599500499999990049990044599004905404994999940004994445499999999999999999999999999\n"+
	"99999999999999999999994000499940440040499000550499005999999950499940099554009904945945000000059999999999999999999999999999999999\n"+
	"99999999999999999999940005999405400440999005905994045999999400999900499900049900440054440000099999999999999999999999999999999999\n"+
	"99999999999999999994540009549004004405995005409990045999994004999404999950054450000499404000499999999999999999999999999999999999\n"+
	"99999999999999999444940049045040049504940590049940045499950049994009999400494944004994544004999999994499999999999999999999999999\n"+
	"99999999999999994999900099940450499009400990049400445994000499995049994004944994049454940054999999444999999999999999999999999999\n"+
	"99999999999999999999400494400504994044004990049505400000004999990099940049999940445044940099999994499999999999999999999999999999\n"+
	"99999999999999999994005949505059990040049940044004400000549999940499400499999900554999900499449499999999999999999999999999999999\n"+
	"99999999999999999995009444000499940400499950445059994449999999900994004999994054499999404994509999999999999999999999999999999999\n"+
	"99999999999999999940049990004999900504999905400099999999999999405940049999950599999999009994049999999999999999999999999999999999\n"+
	"99999999999999999950099940049999404059999404500999999999999999504400499994004999999999059994499999999999999999999999999999999999\n"+
	"99999999999999999400499400499999500099999004004999999999999999505049999940049999999999004454999999999999999999994499999999999999\n"+
	"99999999999999999005994009999999000999994000059999999999999999400499999905499999999999400049999999999999999999400099999999999999\n"+
	"99999999999999994004994499999994004999995000059999999999999999449999999999999999999999944999999999999999999990000599999999999999\n"+
	"99999999999999940049999999999990049999940040049999999999999999999999999999999999999999999999999999999999999950000499999999999999\n"+
	"99999999999999940099999999999940499999940450049999999999999999999999999999999999999999999999999999999999999400000499999999999999\n"+
	"99999999999999900499999999999904999999944404099999999999999999999999999999999999999999999999999999999999994000900999999999999999\n"+
	"99999999999999405999999999999949999999999004599999999999999999999999999999999999999999999999999999999999990004405999999999999999\n"+
	"99999999999994009999999999999999999999994054499999999999999999999999999999999999999999999999999999999999900049504999999999999999\n"+
	"99999999999990049999999999999999999999940090999999999999999999999999999999999999999999999999999999999994000494059999999999999999\n"+
	"99999999999940099999999999999999999999400445999994999999999999999999999999999999999999999999999999999990004994049999999999999999\n"+
	"99999999999900499999999999999999999999504404999944999999999999999999999999999999999999999999999999999900009990499999999999999999\n"+
	"99999999999505999999999999999999999999049559999949994455555444999999999999999999999999999999999999999400049900999999999999999999\n"+
	"99999999994004999999999999999999999994044049999445000000000000054999999999999999999999999999999999994000499504999999999999999999\n"+
	"99999999990049999999999999999999999940540499944000000000000000000054999999999999999999999999999999990005994009999999999999999999\n"+
	"99999999940499999999999999999999999950404944000000000444444550000000049999999999999999999999999999900004940049999999999999999999\n"+
	"99999999405999999999999999999999999900044000000054449999999999444000000549999999999999999999999999500049400499999999999999999999\n"+
	"99999999004999999999999999999999999400400000000999999999999999999450000004999999999949999999999994000494004999999999999999999999\n"+
	"99999994049999999999999999999999999440000005444999999999999999999990000004999999999499999999999940004940049999999999999999999999\n"+
	"99999940499999999999999999999999944000000549999999999999999999999999500005999999999999999999999900009400599999999999999999999999\n"+
	"99999905999999999999999999999994000000004999999999999999999999999999900000499999999999999999999400044004999999999999999999999999\n"+
	"99999459999999999999999999999940000000499999999999999999999999999999940000099999999999999999999000440049999999999999999999999999\n"+
	"99994049999999999999999999999400000049999999999999999999999999999999990000099999999999999999994000004999999999999999999999999999\n"+
	"99994499999999999999999999994000004999999999999999999999999999999999990000049999999999999999990000049999999999999999999945059999\n"+
	"99949999999999999999999999400000049999999999999999999999999999999999994000049999999999999999940000499999999999999999999400049999\n"+
	"99949990999999999999999994000000499999999999999999999999999999999999994000059999999999999999500049999999999999999999994000499999\n"+
	"99999999999999999999999940000004999999999999999999999999999999999999994000009999999999999994000499999999999999999999990004999999\n"+
	"99999999999999999999999500000049999999999999999999999999999999999999994000009999999999999950004999999999999999999999950049999999\n"+
	"99999999999999999999994000000499999999999999999999999999999999999999994000009999999999999000049999999999999999999999405999999999\n"+
	"99999999999999999999940000005999999999999999999999999999999999999999994000009999999999940000599999999999999999999994049999999999\n"+
	"99999999999999999999400000004999999999999999999999999999999999999999999000009999999999400000999999999999999999999990499999999999\n"+
	"99999999999999999999000000099999999999999999999999999999999999999999999000009999999995050009999999999999999999999944999999999999\n"+
	"99999999999999999994000000499999999999999999999999999999999999999999999000009999999400400049999999944999999999999949999999999999\n"+
	"99999999999999999940000005999999999999999999999999999999999999999999994000009999995054000499999945000999999999999999999999999999\n"+
	"99999999999999999950000004999999999999999999999999999999999999999999994000009999400495004999999400000999999999999999999999999999\n"+
	"99999999999999999400000049999999999999999999999999999999999999999999994000009995059940049999940054000999999999999999499999999999\n"+
	"99999999999999999000000599999999999999999999999999999999999999999999994000009900499400099999500499500999999999999945499999999999\n"+
	"99999999999999994000000499999999999999999999999999999999999999999999999000004059994000499940049999400999999999999404999999999999\n"+
	"99999999999999990000004999999999999999999999999999999999999999999999999000000499994004999400499999400999999999940059999999999999\n"+
	"99999999999999940000009999999999999999999999999999999999999999999999999000004999940049994004999999505999999999400099999999999999\n"+
	"99999999999999900000049999999999999999999999999999999999999999999999994000009999400599940599999994005549999940000999999999999999\n"+
	"99999999999999400000599999999999999999999999999999999999999999999999994000009999500999504999999990009940544000004999999999999999\n"+
	"99999999999999400000499999999999999999999999999999999999999999999999994000009994004995049999999940049994000400049999999999999999\n"+
	"99999999999999500000999999999999999999999999999999999999999999999999940000009940049950499999999950094450044000099999999999944499\n"+
	"99999999999999000004999999999999999999999999999999999999999999999999400000009400599004999999999400000054999000494499999944054999\n"+
	"99999999999994000004999999999999999999999999999999999999999999999994540000059400440049999999994004999999994000999444445054999999\n"+
	"99999999999994000009999999999999999999999999999999999999999999999945440000049004400499999999940009999999940004999999999999999999\n"+
	"99999999999995000059999999999999999999999999999999999999999999999459940000044050004999999999400049999999950049999999999999999999\n"+
	"99999999999990000059999999999999999999999999999999999999999999994499900000090000599999999999000499999999400099999999999999999999\n"+
	"99999999999990000059999999999999999999999999999999999999999999944999900000540004999999999990004999999994000499999999999999999999\n"+
	"99999999999990000049999999999999999999999999999999999999999999449999400000400049999999999950049999999995004999999999999999999999\n"+
	"99999999999940000049999999999999999999999999999999999999999999999999500000400499999999999000499999999940049999999999999999999999\n"+
	"99999999999940000049999999999999999999999999999999999999999949999999000005005099999999940004999999999900499999999999999999999999\n"+
	"99999999999940000049999999999999999999999999999999999999999949999999000004009049999999400049999999999005999999999999999999999999\n"+
	"99999999999940000049999999999999999999999999999999999999999999999994000050059409999994000499999999990009999999999999999999999999\n"+
	"99999999999940000049999999999999999999999999999999999999999999999995000050049945999940004999999999950049994999999999999999999999\n"+
	"99999999999940000049999999999999999999999999999999999999999999999940000400099994055000049999999999500499944999999999999999999999\n"+
	"99999999999990000059999999999999999999999999999999999999999999999400005400499999400004999999999994004999999999999999999999999999\n"+
	"99999999999995000009999999999999999999999999999999999999999999994000009500499999944499999999999940049999999999999999999999999999\n"+
	"99999999999995000009999999999999999999999999999999999999999999940000059454999999999999999999999400599999999999999999999999999999\n"+
	"99999999999994000004999999999999999999999999999999999999999999400000099999999999999999999999994000999999999999999999999999999999\n"+
	"99999999999999000005999999999999999999999999999999999999999994000000499999999999999999999999990009999999999999999999999999999999\n"+
	"99999999999999000000999999999999999999999999999999999999999950000004999999999999999999999999950099999999999999999999999999999999\n"+
	"99999999999994400000499999999999999999999999999999999999994000000049999999999999999999999999400999999999999999999999999999999999\n"+
	"99999999999994900000599999999999999999999999999999999999900000005999999999999999999999999994004999999999999999999999999999999999\n"+
	"99999999999999440000049999999999999999999999999999999994000000049999999999999999999999999940049999999999999999999999999999999999\n"+
	"99999999999999444000004999999999999999999999999999999990000000499999999999999999999999999400599999999999999999999999999999999999\n"+
	"99999999999999954000000499999999999999999999999999999950000004999999999999999999999999999005999999999999999999999999999999999999\n"+
	"99999999999999995400000054999999999999999999999999994500000499999999999999999999999999995009999999999999999999999999999999999999\n"+
	"99999999999999994450000000049999999999999999999999940000004999999999999999999999999999940099999999999999999999999999999999999999\n"+
	"99999999999999999990000000004999999999999999999999400000049999999999999999999999999999400999999999999999999999999999999999999999\n"+
	"99999999999999999944000000000599999999999999999940000004999999999999999999999999999994059999999999999999999999999999999999999999\n"+
	"99999999999999999999400000000004999999999999450000004499999999999999999999999999999940599999999999999999999999999999999999999999\n"+
	"99999999999999999999995000000000049999994450000000499999999999999999999999999999999400999999999999999999999999999999999999999999\n"+
	"99999999999999999999999444000000000000000000000549999999999999999999999999999999990059999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999994500000000000000059999999999999999999999999999999999950499999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999445500000554499999999999999999999999999999999999404999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999999999999999999999999999999999999999999999945049999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999999999999999999999999999999999999999999999400499999999999999999999999999999999999999999999999\n"+
	"99999999999999999999999999999999999999999999999999999999999999999999999999994005999999999999999999999999999999999999999999999999\n"+
	"00099909990999999099999999900999990099900009990909099009909999999999999999940049999999999999999999999999999999999999999999999999\n"+
	"09909990909999099099999999099099909909909990990909090990909999999999999999400499999999999999999999999999999999999999999999999999\n"+
	"00099999099999999099999999909999900009909990990909090000909999999999999994059999999999999999999999999999999999999999999999999999\n"+
	"09909999099999999099999999990999909909900009990909090990909999999999999940499999999999999999999999999999999999999999999999999999\n"+
	"00099999099999099099999999099099909909909990990909090990909999999999994504999999999999999999999999999999999999999999999999999999\n"+
	"99999999099999999000009909900999909909909990999090990990900000999999940049999999999999999999999999999999999999999999999999999999\n")
uvScalar=1
try:
        scalar=float(sys.argv[2])
        print("scaling:"+ str(scalar))
except:
        print("scaling:"+ str(scalar))
with open("object"+file+".txt","w") as f:
	f.write("picocad;obj"+file+";0;1;0\n{\n{"+"\n"+"name='obj', pos={0,0,0}, rot={0,0,0},"+"\n"+"v={\n")
with open(sys.argv[1]) as n:
	with open("object"+file+".txt","a") as f:	
		obj=n.read().split("\n")
		f
		for line in obj:
			x=str(line)
			if x.startswith("mtllib"):
				mtl=x.split(" ")[1]
		if True:#try:
			if mtl:
				with open(mtl,"r") as mtl:
					x=mtl.read().split("\n")
					for line in x:
						if line.strip().startswith("map_kd "):
							png=re.sub("map_kd ","",line.strip())
						if line.strip().startswith("map_Kd "):
							png=re.sub("map_Kd ","",line.strip())
					with Image.open(png) as IMAGE:
						xratio=IMAGE.size[0]/IMAGE.size[1]
						yratio=IMAGE.size[1]/IMAGE.size[0]
						if xratio>1:
							nim=Image.new("RGB",(128,128))
							temp=IMAGE.resize((128,round(yratio*128)))#xratio=128/(128*yration) | xratio=1/yratio
							nim.paste(temp,(0,0))
						elif yratio>1:
							nim=Image.new("RGB",(128,128))
							temp=IMAGE.resize((round(xratio*128),128))
							nim.paste(temp,(0,0))
						else:
							nim=IMAGE.resize((128,128))	
						uvScalarX=nim.size[0]/IMAGE.size[0]
						uvScalarY=nim.size[1]/IMAGE.size[1]
						cList = [
							[(0, 0, 0),"0"],
							[(29, 43, 83),"1"],
							[(126, 37, 83),"2"],
							[(0, 135, 81),"3"],
							[(171, 82, 54),"4"],
							[(95, 87, 79),"5"],
							[(194, 195, 199),"6"],
							[(255, 241, 232),"7"],
							[(255, 0, 77),"8"],
							[(255, 163, 0),"9"],
							[(255, 236, 39),"a"],
							[(0, 228, 54),"b"],
							[(41, 173, 255),"c"],
							[(131, 118, 156),"d"],
							[(255, 119, 168),"e"],
							[(255, 204, 170),"f"]
						]
						px=nim.load()
						xList=[]
						nList=[]
						for y in range(128):
							for x in range(128):
								pixel=px[x,y]
								pList=[]
								for item in cList:
									pItem0=item[0][0]-pixel[0]
									if pItem0<0:
										pItem0=-pItem0
									pItem1=item[0][1]-pixel[1]
									if pItem1<0:
										pItem1=-pItem1
									pItem2=item[0][2]-pixel[2]
									if pItem2<0:
										pItem2=-pItem2
									pList.append([(pItem0,pItem1,pItem2),item[1]])
								for num in range(1,len(pList)):
									pos=num
									cval=pList[num]
									while pos>0 and pList[pos-1][0][0]+pList[pos-1][0][1]+pList[pos-1][0][2]>cval[0][0]+cval[0][1]+cval[0][2]:
										pList[pos]=pList[pos-1]
										pos=pos-1
									pList[pos]=cval	
								if y==64:
									print("\n\n",pList)
								nPixel=pList[0][1]
								xList.append(nPixel)
							nList.append("".join(xList))
							xList=[]
						endstring="\n".join(nList)+"\n"
		#except:
			#print("something went wrong when trying to load the texture file. Either It, or the .mtl file does not exist, or pillow is not installed")
		for line in obj:
			x=str(line)
			if x.startswith("v "):
				vertices+=1
			if x.startswith("f "):
				faces+=1
			if x.startswith("vt "):
				vtlist.append([round(float(x.split(" ")[1])*16*4*uvScalarX)/4,(round(float(x.split(" ")[2])*16*4*uvScalarY)/4-8)*-1+8])
				
		currentVertex=0
		for line in obj:
			x=str(line)
			if x.startswith("v "):
				currentVertex+=1
				vertex=re.sub("v ","", x).strip()
				points=vertex.split(" ")
				for x in range(len(points)):
					points[x]=str(round(float(points[x])*4*scalar)/4)
				vertex=",".join(points)
				if currentVertex==vertices:
					f.write("{"+vertex+"}\n")
				else:
					f.write("{"+vertex+"},\n")
			
				
		f.write("},\n")
		f.write("f={\n")
		currentFace=0
		for line in obj:
			x=str(line)
			if x.startswith("f "):
				currentFace+=1
				face=re.sub("f ","", x).strip()
				faceVertices=face.split(" ");
				Tvertex=[]
				for x in range(len(faceVertices)):
					if len(vtlist)>0:
						Tvertex.append(faceVertices[x].split("/")[1])
					faceVertices[x]=faceVertices[x].split("/")[0]
				face=",".join(faceVertices)
				#-1,-0.25,  17,-0.25,  16.25,15,  -0.75,15
				#
				#
				if currentFace==faces:
					f.write("{"+face+",c=11, dbl=1,")					
					f.write("uv={")
					for faceVertex in range(len(faceVertices)):
						if len(vtlist)>0:
							uvVertexPair=str(vtlist[int(Tvertex[faceVertex])-1][0])+","+str(vtlist[int(Tvertex[faceVertex])-1][1])
						else:
							uvVertexPair=str(int(math.sin(faceVertex/len(faceVertices)*2*math.pi+math.pi/4)*8*16/11.5)/4+8)+","+str(int(math.cos(faceVertex/len(faceVertices)*2*math.pi+math.pi/4)*16*16/11.5)/4+8)
						if faceVertex==len(faceVertices)-1:
							f.write(uvVertexPair)
						else:
							f.write(uvVertexPair+",")
					f.write("} }\n")
				else:
					f.write("{"+face+",c=11, dbl=1,")					
					f.write("uv={")
					
					for faceVertex in range(len(faceVertices)):
						if len(vtlist)>0:
							uvVertexPair=str(vtlist[int(Tvertex[faceVertex])-1][0])+","+str(vtlist[int(Tvertex[faceVertex])-1][1])
						else:
							uvVertexPair=str(int(math.sin(faceVertex/len(faceVertices)*2*math.pi+math.pi/4)*8*16/11.5)/4+8)+","+str(int(math.cos(faceVertex/len(faceVertices)*2*math.pi+math.pi/4)*16*16/11.5)/4+8)
						if faceVertex==len(faceVertices)-1:
							f.write(uvVertexPair)
						else:
							f.write(uvVertexPair+",")
					f.write("} },\n")
		
				
				
				
				
		f.write("} \n")
		f.write("}\n"+
	"}%\n"+endstring
	)
print(str(vertices)+" vertices exported")
print(str(faces)+" faces exported")
	

	

