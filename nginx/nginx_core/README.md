# Agenda, Part I

* Overview
  * 2002, Igor Sysov, Rambler
  * 2004, first OSS release
  * 2011, company founded
  * Master: evaluates config, modules, logs
  * Workers: handles requests
  * Shared memory: counters, variables
* Static Content
* Proxying Connections
* Logging
* Security
* Variables

# Agenda, Part II

* Routing connections
* Load balancing
* Caching
* Compression
* Dynamic configuration
* Installation

## Basic Commands

```
nginx -s reload #reload config, SIGHUP
nginx -s quit   #drain connections, graceful shutdown
nginx -s stop   #terminate
nginx -t        #syntax check
nginx -T        #display current config
```

## ```server1.conf```

```
map $uri $is_redirect {
    default   0;
    /test1    1;
    /test2    2;
    /test3    3;
}

server {
    listen 443 ssl;
    root /home/student1/public_html;

    error_log /var/log/nginx/server1.error.log info;
    access_log /var/log/nginx/server1.access.log combined;
    auth_basic "protected";
    auth_basic_user_file /etc/nginx/htpasswd;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;
    ssl_protocols TLSv1.2;
    ssl_ciphers "AES256+EECDH:AES256+EDH:!aNULL";
    ssl_prefer_server_ciphers on;
    ssl_ecdh_curve secp384r1;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_session_tickets off;
    add_header Strict-Transport-Security "max-age=63072000; includeSubdomains";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    rewrite ^/media/pics/(.+\.(gif|jpe?g|png))$ /images/$1;

    location /application1 {
        auth_basic off;
        proxy_pass http://localhost:90/sampleApp/;
    }

    location ~ ^/pictures/(.+\.(gif|jpe?g|png))$ {
        alias /data/images/$1;
    }

    location /application2 {
        alias /data/test;
    }

    location ~* /test(\d+)$ {
        return 200 "variable = $is_redirect \n";
    }

    location /images {
        root /data;
    }

    location /shop {
        rewrite ^/shop/greatproducts/(\d+)$ /shop/products/product$1.html break;
        rewrite ^/shop/.+/(\d+)$ /shop/services/service$1.html break;
        return 403;
    }

}

server {
    listen 80;
    return 301 https://$host$request_uri;
}
```

## ```server2.conf```

```
server {
    listen 90;
    root /data/server2;
    error_log /var/log/nginx/server2.error.log info;
    access_log /var/log/nginx/server2.access.log combined;
}
```

## ```backends.conf```

```
server {
    listen 8081;
    root /data/backend1;
    status_zone us;
}

server {
    listen 8082;
    root /data/backend2;
    status_zone us;
}

server {
    listen 8083;
    root /data/backend3;
    status_zone uk;
}
```

## ```myServers.conf```

```
upstream myServers {
    zone backend 64k;
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
    server 127.0.0.1:8083;
}

match health_conditions {
    status 200-399;
    header Content-Type = text/html;
    body !~ maintenance;
}

log_format uplog "$request $status $request_uri $upstream_addr";

server {
    listen 8080;
    root /home/student1/public_html;
    access_log /var/log/nginx/up.access.log uplog;
    error_log /var/log/nginx/upstream.error.log info;

    location / {
        proxy_pass http://myServers;
        health_check match=health_conditions fails=2 uri=/health/test.html;
    }
}

server {
    listen 9090;
    root /usr/share/nginx/html;

    location /upstream_conf {
        upstream_conf;
    }

    location = /status {
        status;
    }

}
```

## Tests

```
$ ( for i in {1..1000} ; do curl -sk -u sje:xyz http://localhost:8080/ ; done ) | sort | uniq -c
    333 this is backend1
    333 this is backend 2
    334 this is backend3
```

```
curl -s -o /dev/null -w "%{http_code}" http://<external ip>/\?${1..100}
```
