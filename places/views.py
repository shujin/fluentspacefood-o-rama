# Create your views here.
import requests
import random

from django.template import Context, loader
from django.http import HttpResponse

def index(request):
  uri = "https://api.foursquare.com/v2/venues/search?ll=3.102222,101.5994444&query=food&radius=500&client_id=AHRI2C3I0GXB1MNWI5OSWPBDWH222VNJERYH0PZCNK0PMJOF&client_secret=YLODU3QTTL5FX5TMVC4FQASAKM5LCGUDAKUZVKKAP1H0TH5G&v=20130605"
  req = requests.get(uri)
  all_places = req.json()["response"]["venues"]
  selected_place = random.choice(all_places)
  t = loader.get_template('places/index.html')
  c = Context({
    'selected_place': selected_place,
  })
  return HttpResponse(t.render(c))