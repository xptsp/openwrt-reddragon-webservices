include $(TOPDIR)/rules.mk

PKG_NAME:=reddragon-webservices
PKG_VERSION:=0.3
PKG_RELEASE:=1
PKG_LICENSE:=GPL-3.0-or-later
PKG_MAINTAINER:=Douglas Orend <doug.orend2@gmail.com>

include $(INCLUDE_DIR)/package.mk

define Package/reddragon-webservices
	SECTION:=utils
	CATEGORY:=Utilities
	TITLE:=RedDragon Web Services
	DEPENDS:=+luci-theme-argon +bash
	PKGARCH:=all
endef

define Package/reddragon-webservices/description
Package that dynamically show only the services proxied by Nginx on OpenWrt.
Shown services must include the "/etc/nginx/reverse_proxy" file in the Nginx
configuration files, and must proxy to a service in the "location" field and
should include the service name after the "location" field in order to be 
listed by this web service.
endef

define Build/Prepare
endef

define Build/Configure
endef

define Build/Compile
endef

define Package/reddragon-webservices/install
	$(INSTALL_DIR) $(1)/www/
	$(INSTALL_DATA) ./files/home.html $(1)/www/home.html

	$(INSTALL_DIR) $(1)/www/cgi-bin
	$(INSTALL_BIN) ./files/home.cgi $(1)/www/cgi-bin/home

	$(INSTALL_DIR) $(1)/etc/init.d
	$(INSTALL_BIN) ./files/webservices.init $(1)/etc/init.d/webservices

	$(INSTALL_DIR) $(1)/www/icons
	$(INSTALL_DATA) ./icons/* $(1)/www/icons/

	$(INSTALL_DIR) $(1)/etc/nginx/
	$(INSTALL_DATA) ./files/reverse_proxy $(1)/etc/nginx/reverse_proxy

	$(INSTALL_DIR) $(1)/etc/nginx/conf.d
	$(INSTALL_DATA) ./files/services.locations $(1)/etc/nginx/conf.d
endef

$(eval $(call BuildPackage,reddragon-webservices))
