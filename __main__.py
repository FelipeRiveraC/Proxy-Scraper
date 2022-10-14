from scraper import Scraper

# Add your sources here
sources = [
    'https://free-proxy-list.net/',
    'https://www.us-proxy.org/',
    'https://www.socks-proxy.net/',
    'https://www.sslproxies.org/'    

]


if __name__ == '__main__':
    print(" # --->  Welcome to WEB Proxy Scraper  <--- # ")
    print(" # --->     Author: FelipeRivera       <--- # ")
    print(" # --->     Version: 1.0.0             <--- # ")
    print("")
    print(" # --->          Sources:              <--- # ")
    for source in sources:
        print("#        + " + source + "       #")
    input("Press Enter to continue...")

    # Create Scraper object
    scraper = Scraper(sources)
    scraper.scrape_multiple_sources()
    lenght = len(scraper.proxies)
    print(f" # --->  {lenght} Proxies found!  <--- # ")
    input("Press Enter to to save to file... (proxies.txt)")
    print(" # --->  Saving to proxies.txt  <--- # ")
    with open('proxies.txt', 'w') as f:
        for proxy in scraper.proxies:
            f.write(proxy + '\n')
    print(" # --->  Done!  <--- # ")
    input("Press Enter to print proxies... ")
    for proxie in scraper.proxies:
        print(proxie)