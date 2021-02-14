import torch


model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
# or any of these variants
# model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet34', pretrained=True)
# model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet50', pretrained=True)
# model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet101', pretrained=True)
# model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet152', pretrained=True)
model.eval()

# Download an example image from the pytorch website
import urllib
from PIL import Image
from torchvision import transforms
#if len(img.shape) > 2 and img.shape[2] == 4:
#    #convert the image from RGBA2RGB
#    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
url, filename = ("https://user-images.githubusercontent.com/15249120/107858311-9b08cd00-6e01-11eb-9891-6caaac901de7.png", "./img/hp.png")
#url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")
try: urllib.URLopener().retrieve(url, filename)
except: urllib.request.urlretrieve(url, filename)
input_image = Image.open(filename)
input_image.mode
input_image.convert('RGB')