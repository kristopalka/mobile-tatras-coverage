import math


def generate_google_maps_url(coord, map_type="m", subdomain="mt1"):
    """
        Map tiles overview: https://gist.github.com/xantiagoma/39145a3042eca53a57ac3290a1a34973?permalink_comment_id=3415377
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
            h = roads only
            m = standard roadmap
            p = terrain
            r = somehow altered roadmap
            s = satellite only
            t = terrain only
            y = hybrid
        :param subdomain: mt0, mt1, mt2, mt3
        :return: url as string
    """
    return f"https://{subdomain}.google.com/vt/lyrs={map_type}&x={coord['x']}&y={coord['y']}&z={coord['z']}"


def generate_play_url(coord, map_type="cell_all"):
    """
        Map address: https://www.play.pl/pomoc/zasieg/mapa-zasiegu
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
            cell_all - default, calls, SMS, MMS, internet
            5g_cband - 5G and 4G LTE
            airfiber - NET BOX
        :return: url as string
    """
    return f"https://internet.play.pl/maps-resources/tiles/{map_type}/{coord['z']}/{coord['x']}/{1023 - coord['y']}.png"


def generate_tmobile_url(coord):
    y_value = int(math.pow(2, coord['z']) - 1)
    return f"https://mapa9.t-mobile.pl/maps_new/2G/{coord['z']}/{coord['x']}/{y_value-coord['y']}.png"
