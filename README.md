# Purgo Space (Hack Cambridge 2020 project)

Our team of four wanted to tackle the issue of climate change. We decided to tackle a solution that would improve day to day actions, selecting the domain of trash collection.

We developped an iOS mobile app that displays the location of all trash and bins around you. This allows you as a user to look for trash on the street next to you and bin it in the free bins (just like Pokemon Go: collect trash next to you!). Your cleaning actions are rewarded with points that can later be traded for vouchers (popcorn at the cinema, an icecream, etc...)

But how do we gather the data?

We built a simple IoT network of ultrasonic sensors that can send data about how full a bin is, as well as cameras (simulating CCTVs an cameras on public transports) which, using our ML model, can recognize trash on the streets. Both sensors send their tokens with GPS data. The devices communicate push the data to an MQTT layer, where the subscribed server and database combine the data and the GPS location from each token to create a history of the trash in a region and provide the relevant data for the mobile app.

Other goals that we could not fully complete were to use the current data to provide optimal trash collection route for the collection vehicles, as well as compute the trends using the data history.
