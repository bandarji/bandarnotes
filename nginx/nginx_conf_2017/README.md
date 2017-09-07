# NGINX Conference 2017

# Vendors

* CloudFlare
* Intel
* Red Hat
* DataDog
* Mashape

# Openning Keynote, NGINX CEO, Gus Robertson

* Istio
* Data intelligence
  * Too much data
  * Not enough intelligence
* Current self-driving cars produce 10GB data every mile driven
* NGINX Application Platform

# NGINX Product Announcements

* Panel
  * NGINX Head of Product, Owen Gerrit
  * NGINX Chief Architect, Chris Stetson
  * NGINX Engineer, Rachael Paasov
* NGINX Unit
  * Application server for cloud-native services
  * Multi-(language,stack,naming)
  * PHP, Go, Python with multi-version support
  * REST / JSON
* NGINX Controller
  * Webapp Mission Control: benevolent, God's eye view of NGINX processing
  * Workflow automation and policy management
  * Multi-tenant and RBAC
  * Compliance and auditing
  * Monitoring / analytics
  * Front multiple cloud installations
  * Underdeveloped, but private betas coming, initial release in 2018q1
  * GraphQL / GraphiQL
  * Import existing configuration

# Long Arc of Open Collaborative Innovation

* Red Hat Senior Director of Product, Rich Sharples, [@richsharples](https://twitter.com/richsharples)
  * Involved in over 1M OSS projects, not just 'a Linux company'
  * Notable OSS Aquisitions
    * CentOS 2014
    * Ansible 2015
    * 3Scale 2016
  * What OSS gets wrong or does not do well
    * User experience
    * QA and integration
    * Predictable life cycle
    * Upstream change acceptance

# Application and API Security

* Stepan Ilyin, Wallarm Co-founder
* Free: mod_security WAF
  * Blocks top 10 OWASP
  * Simple
  * Signature-based
  * Lots of false positives
  * Tip: use public rules for monitoring, private for blocking
  * Ivan Ristic's book "Modsecurity Handbook"
* Free: naxsi
  * Does not use signatures, but character patterns
  * nxutil to manage rulesets
  * Dumps to ELK
* Commercial: Wallarm
  * Machine learning adaptive security platform
* Commercial: Signal Sciences
* Repsheet
  * Behavior monitoring (calls, GeoIP, etc)
  * Interacts with Redis
* NGINX Mirroring
  * duplicate request to other backend, for processing
  * ```mirror``` directive
* Bots and DDoS
  * [test_cookie module](https://github.com/kyprizel/testcookie-nginx-module)
* Neural networks and machine learning
  * Bad and good requests look alike in logs
  * Github [SaveTheRbtz](https://github.com/SaveTheRbtz)
  * PyBrain
* Code 444
  * Close connection, provide no response
* Use ipset
  * ipset -N ban iphash
  * ipset -A xxx (from logs)
* GeoIP
  * ngx_http_geoip_module
  * not accurate
* Limit buffers, timeouts, etc
  * Every resource has a limit

# Intel QuickAssist Technology / Payload Compression

* Gordon McFadden, Intel Architect
* QAT
  * Intel C627 chipset
  * 100+ gbps bulk crypto
  * 100kops RSA 2k decrypt
* NGINX changes
  * deflate calls eat up CPU
  * ```ngx_http_gzip_filter_module.c``` deflate calls move to hardware
  * ```ngx_http_gzip_filter_add_data``` crc32 expensive software calculation
* QATzip library changes
  * If the hardware exists, the library talks to the driver and uses it
  * Otherwise, uses software
* Results
  * Pages: cnn 137231 bytes, timesofindia 372028 bytes, shanghaidaily 64137
  * Concatenate 573396 bytes
  * ```ab -n 32000 -c 24 http://192.168.1.1/file & x3```
  * 2x Intel Xeon Gold 6150 2.7 GHz, C627 Chip B1, DDR4 2133 MHz 192 GB
  * 72 cores
  * 10GE - no comp: 45s, SW comp: 17s, QATzip: 13s
  * 10GE - no comp: 1 percent CPU, sw: 80, QATzip: 12
  * 40GE - similar, just with shorter page load times

# Optimizing Webservers for High Throughput and Low Latency

* Alexey Ivanov / [@SaveTheRbtz](https://twitter.com/SaveTheRbtz), SRE, Dropbox
* [Blogpost](https://blogs.dropbox.com/tech/2017/09/optimizing-web-servers-for-high-throughput-and-low-latency/)

# Better Metrics Through Scripting

* Matthew Williams, Evangelist, DataDog [@technovangelist](https://twitter.com/technovangelist)
* [Slides](http://dtdg.co/nginx17deck)
* Pull metrics from localhost/nginx_status/, for example
* Lua / OpenResty http://dtdg.co/nginx17-lua
  * Mature software with an active community
* nginScript
  * Like JavaScript
  * Created by NGINX
* [Reloader](http://dtdg.co/nginx17-reload)
* [Aggregated Stats](http://luameter.com)
* [RestyStat](http://dtdg.co/nginx17-restystat)
* [ngx_lua_datadog](http://dtdg.co/nginx17-luadatadog)
* [nginx-dogstatsd](http://dtdg.co/nginx17-dogstatsd)
* [Other](http://dtdg.co/nginx17-awesome)

# NGINX and IoT / MQTT

* [Liam Crilly / @liamcrilly](https://twitter.com/liamcrilly), Director of Product Management, NGINX, Inc.
* [MQTT](http://mqtt.org)

# NGINX+ and Highly Available WebSockets in an Auto-Scaling AWS Environment

* Patrick Synor, Technical Manager, Linux Operations, SolvIT Inc.
* AWS did not support WebSocket until ALB in 2016
* NGINX supported WebSocket since 2013

# Thursday

# NGINX Unit

Run multiple application languages and language versions off a server
configurable by JSON/REST. No more configuration files.

* [NGINX Unit product page](https://www.nginx.com/products/nginx-unit/)
* [NGINX Unit site](http://unit.nginx.org/)

# The Business of Open Source

* Elsie Phillips / [@elsiephilly](https://twitter.com/elsiephilly), CoreOS
* Myths
  * OSS is free (as in beer)
  * "Linux is only free if your time has no value." -- jwz
  * The community will do your work for you
  * Companies contribute for altruistic reasons
* Complementaries
  * If you like cereal, you buy a lot of cerial on sale, but milk no matter what
  * Sun could give away Java, because it meant more hardware sales
* Monetizing OSS
  * Consulting
  * Training
  * Indemnity
  * Create a marketplace
    * Unity for gaming
    * Creators need to retain content ownership, thoug
  * Open Core, but don't limit features (NGINX vs NGINX+)

# Building an Exothermic Community

* Kara Sowles / [@feynudibranch](https://twitter.com/feynudibranch), Puppet
* User bases are endothermic. Company makes widget. User base consumes it.
* User base can become an exothermic community
  * Produce code
  * Generate conversation online
  * Give talks
  * Norms / codes of conduct / tone / methodology / practices / problem solving
* People may not see all the inputs
  * Bug reports
  * Teachers, leaders,
* Activation energy
  * Minimum energy required to start a reaction
  * Investment worth it?
* Needed for happiness and to stay engaged
  * Meaningful vision of the future
  * Sense of purpose
  * Great relationships

# NGINX [Ampify](https://amplify.nginx.com/)

* Metrics out of the box
* 12+ months in beta
* Two thousand accounts
* 1B metrics collected

# NGINX Unit Deep Dive Demo

```
cd /srv/unit/
./configure --help
./configure php
./configure python
./configure python --config=python3.5-config
./configure go
make all
ls -l build/unitd build/*.unit.so
./build/unitd --help
./build/unitd --control 127.0.0.1:8443
ps aufx | tail
curl 127.0.0.1:8443
# add just phpinfo() to an index.php, create config file
curl -X PUT -d@demo/start.json 127.0.0.1:8443
curl -X PUT -d@demo/python.json '127.0.0.1:8443/applications/python_sample'
# make this py app run on same listening port
curl -X PUT -d'"python_sample" '127.0.0.1:8443/listeners/*:8300/application'
curl http://127.0.0.1:8{3..5}0{0,1}/
curl -X DELETE '127.0.0.1:8443/listeners/*:8300'
curl -X DELETE '127.0.0.1:8443/applications/phpinfo'
```

*Sample Application*
```
import sys
def application(environ, start_response):
    body = sys.version.encode('utf-8')
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [body]
```

alessfg

# Running NGINX on GCP

* Mike Graboski, Sales Engineer, Google
* Stackdriver metrics
  * Connections: active, reading, writing, waiting
  * Request counts
* Networking
  * Proxies: L4, L7, SSL
  * Route requests to closest NGINX VM
  * Single global address for all regions
* [NGINX+ on GCP](https://goo.gl/mUkRuA)

# Monitoring with Amplify

# PKI / TLS

# Monitoring Microservices Minus the Migraine

# Fun with Health Checks Using NGINX+ and Docker

# Building a Powerful, Efficient and Highly Available Caching Layer with NGINX

