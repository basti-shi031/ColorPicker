from PIL import ImageGrab

img = ImageGrab.grab((500,0,1000,500))
img.save("crop_image.jpg",'jpeg')
