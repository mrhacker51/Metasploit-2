#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search, I


def cloudflare(headers, content):
    detect = False
    for header in headers.items():
        detect |= header[0].lower() == "cf-ray"
        detect |= search(r'__cfduid=|cloudflare-nginx|cloudflare[-]', header[1], I) is not None
        if detect: break
    detect |= search(r"CloudFlare Ray ID:|var CloudFlare=", content) is not None
    if detect:
        return "CloudFlare Web Application Firewall (CloudFlare)"
