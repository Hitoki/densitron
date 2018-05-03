from django.contrib.gis.geoip2 import GeoIP2

from geoip2.errors import AddressNotFoundError

from products.models import CountryFlag


class SetCountryMiddleware(object):
    def process_request(self, request):
        g = GeoIP2()
        abbrs = [i['abbreviation'] for i in
                 CountryFlag.objects.all().values('abbreviation')]
        _row = 'ROW'
        if get_client_ip(request) != '127.0.0.1':
            try:
                country = g.country(get_client_ip(request))\
                    .get('country_code')
                if country in abbrs:
                    request.country = country
                else:
                    request.country = _row
            except AddressNotFoundError:
                request.country = _row
        else:
            request.country = _row
        if 'country' in request.session and request.session['country']:
            request.country = request.session['country']
        return None


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip