from pathlib import Path
import cv2, numpy as np
if __name__=='__main__':
    out=Path('artifacts');out.mkdir(exist_ok=True)
    image=np.zeros((256,256,3),dtype=np.uint8)
    cv2.rectangle(image,(40,40),(210,210),(80,140,220),-1)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    for name,data in [('input',image),('gray',gray),('equalized',cv2.equalizeHist(gray)),('edges',cv2.Canny(gray,50,150))]:
        if not cv2.imwrite(str(out/f'{name}.png'),data): raise RuntimeError('Image save failed')
    print('Wrote four synthetic-image examples to artifacts/')
