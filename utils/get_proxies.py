import urllib

def get_system_proxysettings():
    proxies = urllib.getproxies()
    print "Complete proxy list: %s" % proxies
    #urllib.getproxies() returns system proxies as following dictionary
    #{'http': 'http://proxy_ip:proxy_port', 'socks': 'socks://proxy_ip:proxy_port'}
    proxy_list = []
    #proxies will be tried in following order
    # on linux platform, 'all' is returned for 'socks' proxy
    proxy_order = ['socks', 'all', 'http']
    for ptype in proxy_order:
        if ptype in proxies:
            pvalue = proxies.get(ptype)
            proxy_host, proxy_port, proxy_type = parse_proxystr(ptype, pvalue)
            if proxy_type <> None:
                proxy_list.append((proxy_host, int(proxy_port), proxy_type),)
    return proxy_list

if __name__ == "__main__":
    print "System proxy list: %s" % get_system_proxysettings()
