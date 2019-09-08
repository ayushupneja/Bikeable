#!/usr/bin/env python
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
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests, json


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
CORS(app)

HERE_APP_ID = "r6ekBx0XS2Vo20WiW8gN"
HERE_APP_CODE = "w3sv0mJ_a5dthoHMZ6FgKQ"
HERE_ENDPOINT = "https://route.api.here.com/routing/7.2/calculateroute.json"
GEOCODING_ENDPOINT = "https://maps.googleapis.com/maps/api/geocode/json?address="
GEOCODING_KEY = "AIzaSyAXU-NQ4vA2RHiz2x3L7tO6Ay3fbgT0-90"

@app.route('/')
def index():
    response = render_template('bikeable.html')
    return response

@app.route('/bikeTheft.html')
def theft():
    return render_template('bikeTheft.html')

@app.route('/heatmaps.html')
def about():
    response = render_template('heatmaps.html')
    return response

@app.route('/routing/')
def routing():
    origin = request.args.get('origin')
    dest = request.args.get('dest')
    if all([origin, dest]):
        origin_resp = requests.post(GEOCODING_ENDPOINT + origin.replace(' ', '+') + "&key=" + GEOCODING_KEY)
        dest_resp = requests.post(GEOCODING_ENDPOINT + dest.replace(' ', '+') + dest + "&key=" + GEOCODING_KEY)

        origin_json = json.loads(origin_resp.content.decode('utf-8'))
        dest_json = json.loads(dest_resp.content.decode('utf-8'))
        wp_o = str(origin_json['results'][0]['geometry']['location']['lat']) + "," + str(origin_json['results'][0]['geometry']['location']['lng'])
        wp_d = str(dest_json['results'][0]['geometry']['location']['lat']) + "," + str(dest_json['results'][0]['geometry']['location']['lng'])

        with open('static/data/avoid.json') as json_file:
            data = json.load(json_file)

        avoid_str = "&avoidareas="

        for i in range(len(data)):
            avoid_str += str(data[i][0]) + ',' + str(data[i][1]) + ';' + str(data[i][2]) + ',' + str(data[i][3])
            if i < len(data) - 1:
                avoid_str += '!'


        resp = requests.post(
            HERE_ENDPOINT +
            "?app_id="   + HERE_APP_ID +
            "&app_code=" + HERE_APP_CODE +
            "&waypoint0=" + wp_o +
            "&waypoint1=" + wp_d +
            "&mode=fastest;bicycle;traffic:disabled&alternatives=3" +
            avoid_str
            )

        print(
            HERE_ENDPOINT +
            "?app_id="   + HERE_APP_ID +
            "&app_code=" + HERE_APP_CODE +
            "&waypoint0=" + wp_o +
            "&waypoint1=" + wp_d +
            "&mode=fastest;bicycle;traffic:disabled&alternatives=3" +
            avoid_str
        )

        resp_json = json.loads(resp.content.decode('utf-8'))
        resp_waypoints = resp_json['response']['route'][0]['waypoint']
        resp_legs = resp_json['response']['route'][0]['leg'][0]['maneuver']

        route = []
        directions = []

        # Distance is in meters and time is in seconds
        stats = {
            'distance': resp_json['response']['route'][0]['summary']['distance'],
            'time': resp_json['response']['route'][0]['summary']['travelTime']
                }

        # Get the origin, intermediate waypoints, and destination
        route.append([resp_waypoints[0]['mappedPosition']['latitude'], resp_waypoints[0]['mappedPosition']['longitude']])
        directions.append("Start at " + origin)
        for leg in resp_legs:
            route.append([leg['position']['latitude'], leg['position']['longitude']])
            directions.append(leg['instruction'])
        route.append([resp_waypoints[1]['mappedPosition']['latitude'], resp_waypoints[1]['mappedPosition']['longitude']])
        directions.append("Arrive at " + dest)

        j_output = {'route': route, 'directions': directions, 'stats': stats}
        response = jsonify(j_output)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        response = "<h3>GET request missing either origin or destination or has improper coordinate formatting<h3>"
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
