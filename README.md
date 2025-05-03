# reddragon-webservices
 
This package dynamically shows any services that are proxied by Nginx on OpenWrt, as well as any other services 
that adminstrators chose to include.

In ```/etc/config/nginx```, proxied services must be listed like such: 

    config server 'openwrt'
	       option include 'reverse_proxy'
	       option server_name 'openwrt.your.domain.here'
	       option location '/ { proxy_pass https://127.0.0.1; } # OpenWRT'

Icon name follows the ```config server``` line (ie: ```openwrt```) and may be a SVG (preferred) or PNG file in 
the ```/www/icons``` directory.  In the ```location``` option, there NEEDS to be a hash-tag (```#```) followed by 
a short name of the service being proxied to.

For services that are not proxied, these services must be listed like such:

    config redirect 'gitea'
    	option comment 'Gitea'
    	option location 'http://nas.lan:3000'

Display order is unsorted and ungrouped, with proxied services being listed first, then included services.
