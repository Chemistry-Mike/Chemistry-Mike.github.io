"""Decode the pristine, axis-aligned version-5/M poster PNGs; no error correction.
ImageMagick is used only to read grayscale pixels, not to change the source files.
"""
from pathlib import Path
import subprocess,struct,json

def decode(path):
    w,h=struct.unpack('>II',path.read_bytes()[16:24])
    pixels=subprocess.check_output(['convert',str(path),'-depth','8','gray:-'])
    points=[(i%w,i//w) for i,v in enumerate(pixels) if v<128]
    x0=min(x for x,y in points); y0=min(y for x,y in points)
    x1=max(x for x,y in points); y1=max(y for x,y in points)
    y=y0+3; x=next(x for x in range(w) if pixels[y*w+x]<128); end=x
    while pixels[y*w+end]<128:end+=1
    n=round((x1-x0+1)/((end-x)/7)); assert n==37, n
    step=(x1-x0+1)/n
    a=[[pixels[int(y0+(y+.5)*step)*w+int(x0+(x+.5)*step)]<128 for x in range(n)] for y in range(n)]
    reserved=[[False]*n for _ in range(n)]
    def rect(x,y,width,height):
        for yy in range(y,y+height):
            for xx in range(x,x+width):reserved[yy][xx]=True
    rect(0,0,9,9);rect(n-8,0,8,9);rect(0,n-8,9,8)
    rect(28,28,5,5)
    for i in range(n): reserved[6][i]=reserved[i][6]=True
    masks=[lambda x,y:(x+y)%2==0,lambda x,y:y%2==0,lambda x,y:x%3==0,lambda x,y:(x+y)%3==0,lambda x,y:(y//2+x//3)%2==0,lambda x,y:(x*y)%2+(x*y)%3==0,lambda x,y:((x*y)%2+(x*y)%3)%2==0,lambda x,y:((x+y)%2+(x*y)%3)%2==0]
    for mask in masks:
        bits=[]; right=n-1; up=True
        while right>0:
            if right==6:right=5
            for y in (range(n-1,-1,-1) if up else range(n)):
                for x in [right,right-1]:
                    if not reserved[y][x]:bits.append(int(a[y][x]) ^ int(mask(x,y)))
            up=not up;right-=2
        codewords=[int(''.join(map(str,bits[i:i+8])),2) for i in range(0,134*8,8)]
        # Version 5, error-correction M: two interleaved blocks, 43 data bytes each.
        data=codewords[:86:2]+codewords[1:86:2]
        stream=''.join(f'{b:08b}' for b in data)
        if stream[:4]!='0100':continue
        length=int(stream[4:12],2)
        try: result=bytes(int(stream[i:i+8],2) for i in range(12,12+length*8,8)).decode('utf-8')
        except (ValueError,UnicodeError):continue
        if result.startswith('https://'):return result
    raise ValueError('No valid byte-mode URL decoded')

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', nargs='?', default='images/research/p53-gsm/qr')
    root=Path(parser.parse_args().directory)
    for name,url in json.loads((root/'destinations.json').read_text()).items():
        actual=decode(root/(name+'.png')); assert actual==url,(actual,url)
        print(name+': '+actual)
