# reddragon-webservices
 
This package that dynamically show only the services proxied by Nginx on OpenWrt.  Nginx is a requirement for this package, however, it is not listed in the dependencies as a requirement, primarily because I could not build the "nginx-ssl" package on my development machine.  It also requires the "luci-theme-argon" package.

In the Nginx configuration files, services must use a similar structure in order to be listed on the web page of services: 

    config server 'owrt_domain'
	       option include 'reverse_proxy'
	       option server_name 'openwrt.your.domain.here'
	       option location '/ { proxy_pass https://127.0.0.1; } # OpenWRT'

In the "location" option, there NEEDS to be a hash-tag ("#") followed by a short name of the service being proxied to.

# Desktop Screenshot

NOTE: This screenshot was taken on my computer (image size is 1920x872).

<img src="https://github.com/xptsp/openwrt-reddragon-webservices/blob/main/desktop.jpg?raw=true" width="320" height="148" />

# Mobile Screenshot

NOTE: This screenshot was taken on my phone in portrait mode (image size is 1080x1529).

<img src="https://github.com/xptsp/openwrt-reddragon-webservices/blob/main/mobile.jpg?raw=true" width="180" height="334" />
