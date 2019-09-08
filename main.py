# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, render_template, request
import requests, json


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

HERE_APP_ID = "r6ekBx0XS2Vo20WiW8gN"
HERE_APP_CODE = "w3sv0mJ_a5dthoHMZ6FgKQ"
HERE_ENDPOINT = "https://route.api.here.com/routing/7.2/calculateroute.json"
GEOCODING_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json?address="
GEOCODING_KEY = "AIzaSyAjYIJDSpRo90YUDZNtLnSCTmuMHfLMAlo"

@app.route('/') 
def index():
    return render_template('bikeable.html')
    #print("<h1>Hello, world!</h1>")
'''
@app.route('/routing/')
def routing():
    origin = request.args.get('origin')
    dest = request.args.get('dest')
    if all([origin, dest]):
        origin_resp = requests.get(GEOCODING_ENDPOINT + origin + "&key=" + GEOCODING_KEY)
        dest_resp = requests.get(GEOCODING_ENDPOINT + dest + "&key=" + GEOCODING_KEY)
        origin_json = json.loads(origin_resp)
        dest_json = json.loads(dest_resp)
        wp_o = origin_json['results'][0]['geometry']['location']['lat'] + "," + origin_json['results'][0]['geometry']['location']['lng']
        wp_d = dest_json['results'][0]['geometry']['location']['lat'] + "," + dest_json['results'][0]['geometry']['location']['lng']
        resp = requests.get(
            HERE_ENDPOINT + 
            "?app_id="   + HERE_APP_ID +
            "&app_code=" + HERE_APP_CODE +
            "&waypoint0=" + wp_o +
            "&waypoint1=" + wp_d +
            "&mode=fastest;bicycle;traffic:disabled&alternatives=3"
            )
        resp_json = json.loads(resp)
        resp_waypoints = resp_json['response']['route'][0]['waypoint']

        route = []
        for wp in resp_waypoints:
            route.append([wp['mappedPosition']['latitude'], wp['mappedPosition']['longitude']])
        route_json = json.dumps(route)
        print(route_json)
            

    else:
        print("<h3>GET request missing either origin or destination or has improper coordinate formatting<h3>")
'''


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
