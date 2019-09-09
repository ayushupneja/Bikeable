Live at: [bikeable.tech](bikeable.tech)

Devpost: [https://devpost.com/software/bikeable](https://devpost.com/software/bikeable)

## Developers

Created by [Ayush Upneja](upneja.me), [Parker Van Roy](https://www.linkedin.com/in/parkervr/), [Catherine Lee](https://github.com/catherinelee274), and [Will Pine](https://github.com/wpine215)



## Inspiration

Parker was riding his bike down Commonwealth Avenue on his way to work this summer when a car pulled out of nowhere and hit his front tire. Lucky, he wasn't hurt, he saw his life flash before his eyes in that moment and it really left an impression on him. (His bike made it out okay as well, other than a bit of tire misalignment!)

As bikes become more and more ubiquitous as a mode of transportation in big cities with the growth of rental services and bike lanes, bike safety is more prevalent than ever.


## What it does

We designed _ Bikeable _ - a Boston directions app for bicyclists that uses machine learning to generate directions for users based on prior bike accidents in police reports. You simply enter your origin and destination, and Bikeable creates a path for you to follow that balances efficiency with safety. While it's comforting to know that you're on a safe path, we also incorporated heat maps, so you can see where the hotspots of bicycle theft and accidents occur, so you can be more well-informed in the future! 


## How we built it

Bikeable is built in Google Cloud Platform's App Engine (GAE) and utilizes the best features three mapping apis: Google Maps, Here.com, and Leaflet to deliver directions in one seamless experience. Being build in GAE, Flask served as a solid bridge between a Python backend with machine learning algorithms and a HTML/JS frontend. Domain.com allowed us to get a cool domain name for our site and GCP allowed us to connect many small features quickly as well as host our database.

## Challenges we ran into

We ran into several challenges.

Right off the bat we were incredibly productive, and got a snappy UI up and running immediately through the accessible Google Maps API. We were off to an incredible start, but soon realized that the only effective way to best account for safety while maintaining maximum efficiency in travel time would be by highlighting clusters to steer waypoints away from. We realized that the Google Maps API would not be ideal for the ML in the back-end, simply because our avoidance algorithm did not work well with how the API is set up. We then decided on the HERE Maps API because of its unique ability to avoid areas in the algorithm. Once the front end for HERE Maps was developed, we soon attempted to deploy to Flask, only to find that JQuery somehow hindered our ability to view the physical map on our website. After hours of working through App Engine and Flask, we found a third map API/JS library called Leaflet that had much of the visual features we wanted. We ended up combining the best components of all three APIs to develop Bikeable over the past two days.

The second large challenge we ran into was the Cross-Origin Resource Sharing (CORS) errors that seemed to never end. In the final stretch of the hackathon we were getting ready to link our front and back end with json files, but we kept getting blocked by the CORS errors. After several hours of troubleshooting we realized our mistake of crossing through localhost and public domain, and kept deploying to test rather than running locally through flask.


## Accomplishments that we're proud of

We are incredibly proud of two things in particular.

Primarily, all of us worked on technologies and languages we had never touched before. This was an insanely productive hackathon, in that we honestly got to experience things that we never would have the confidence to even consider if we were not in such an environment. We're proud that we all stepped out of our comfort zone and developed something worthy of a pin on github.

We also were pretty impressed with what we were able to accomplish in the 36 hours. We set up multiple front ends, developed a full ML model complete with incredible data visualizations, and hosted on multiple different services. We also did not all know each other and the team chemistry that we had off the bat was astounding given that fact!


## What we learned

We learned BigQuery, NumPy, Scikit-learn, Google App Engine, Firebase, and Flask.


## What's next for Bikeable

Stay tuned! Or invest in us that works too :)

**Features that are to be implemented shortly and fairly easily given the current framework:**

- User reported incidents - like Waze for safe biking!
- Bike parking recommendations based on theft reports
- Large altitude increase avoidance to balance comfort with safety and efficiency.
