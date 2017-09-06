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

# Application and API Security / Stepan Ilyin, Wallarm Co-founder

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
  * test_cookie module (github: kyprizel)
* Neural networks and machine learning
  * Bad and good requests look alike in logs
  * SaveTheRbtz on github
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
