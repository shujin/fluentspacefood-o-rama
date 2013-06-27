# Create your views here.
import requests
import random

from django.template import Context, loader
from django.http import HttpResponse

def index(request):
  # ll=3.102222,101.5994444
  uri = "https://api.foursquare.com/v2/venues/explore?sw=3.10027,101.59768&ne=3.10698,101.60011&section=food&limit=50&venuePhotos=1&query=food&limit=30&client_id=AHRI2C3I0GXB1MNWI5OSWPBDWH222VNJERYH0PZCNK0PMJOF&client_secret=YLODU3QTTL5FX5TMVC4FQASAKM5LCGUDAKUZVKKAP1H0TH5G&v=20130605"
  # 
  req = requests.get(uri)
  all_places = req.json()["response"]["groups"][0]["items"]
  selected_place = random.choice(all_places)
  print selected_place
  t = loader.get_template('places/index.html')
  c = Context({
    'selected_place': selected_place,
  })
  return HttpResponse(t.render(c))