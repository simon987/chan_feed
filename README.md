### chan_feed

Daemon that fetches posts from compatible *chan
image boards and publishes serialised JSON to redis
 for real-time ingest.
 
Compatible image boards: 4chan, lainchan, uboachan,
22chan, wizchan, 1chan, 2ch.hk, endchan, 38chan, alokal,
horochan, doushio, desuchan, tgchan, lolnada, 7chan, chanon,
chan.org.li, hispachan, 8kun, nowere, iichan, 2chan and more.

Can optionally push monitoring data to InfluxDB. Below is an
example of Grafana being used to display it.

![monitoring.png](monitoring.png)
