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
    y_value = int(math.pow(2, coord['z']) - 1)
    return f"https://internet.play.pl/maps-resources/tiles/{map_type}/{coord['z']}/{coord['x']}/{y_value - coord['y']}.png"

def generate_orange_url(coord, map_type="2g"):
    """
        Map address: https://www.orange.pl/view/mapazasiegu
        :param coord:
        :param map_type: type of map
            internet2G - 2G
            internet3G - 3G
            internet4G - 4G
            internet5G - 5G (350 Mb/s CA)
            internet5gC - 5G C-band
        :return: url as string
    """
    layer_parameter = {
        "internet2g": "cov_gsm_opl",
        "internet3G": "cov_umts_opl",
        "internet4G": "cov_lte_opl",
        "internet5G": "cov_ca_5g",
        "internet5gC": "cov_c_band"
    }
    if map_type not in layer_parameter:
        raise ValueError("Invalid map_type for Orange")
    return f"https://www.orange.pl/rangemaps/wmts?&request=getTile&Layer=orangeCoverage:{layer_parameter[map_type]}&format=image/png8&Tilematrixset=EPSG:900913&Tilematrix=EPSG:900913:{coord['z']}&Tilerow={coord['y']}&TileCol={coord['x']}&style=orangeCoverage:{map_type}"

def generate_plus_url(coord, map_type=""):
    """
        Map address: https://www.plus.pl/mapa-zasiegu
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
        :return: url as string
    """
    return "Not implemented yet"


def generate_tmobile_url(coord, map_type="2G"):
    """
        Map address: https://www.t-mobile.pl/c/mapa-zasiegu
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
            2G - GSM/GPRS/EDGE network
            4G - 4G/LTE network
            5G - 5G network
            5G-more - 5G in 3.7-3.8 GHz band
        :return: url as string
    """
    y_value = int(math.pow(2, coord['z']) - 1)
    return f"https://mapa4.t-mobile.pl/maps_new/{map_type}/{coord['z']}/{coord['x']}/{y_value-coord['y']}.png"

def generate_orange_slovensko_url(coord, map_type=""):
    """
        Map address: https://www.orange.sk/onas/mapa-pokrytia/
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
        :return: url as string
    """
    return "Not implemented yet"

def generate_telkom_slovensko_url(coord, map_type=""):
    """
        Map address: https://www.telekom.sk/wiki/mapa-pokrytia#
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
        :return: url as string
    """
    return "Not implemented yet"

def generate_o2_slovakia_url(coord, map_type="edge"):
    """
        Map address: https://www.o2.sk/podpora/siet-a-pokrytie/mapa-dostupnosti-sluzieb-o2
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
            edge - GPRS/EDGE network, up to 250 kb/s
            hspa - 3G network, up to 14,4 Mb/s
            lte - LTE network, up to 73 Mb/s
            5g - 5G network, up to 200 Mb/s
        :return: url as string
    """
    return f"https://mapy.o2.sk/backend/sk/tile/{map_type}/z{coord['z']}-x{coord['x']}-y{coord['y']}.png"

def generate_4ka_url(coord, map_type=""):
    """
        Map address: https://www.4ka.sk/fix/podpora/mapa-pokrytia/
        :param coord: coordinates (x,y,z)
        :param map_type: type of map
        :return: url as string
    """
    return "Not implemented yet"