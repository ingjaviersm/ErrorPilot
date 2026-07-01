import re


class LogNormalizer:
    """
    Normaliza mensajes de error PHP para agrupar errores similares.
    """

    def normalize(self, message: str) -> str:

        if re.match(r'^Undefined array key ', message):
            return 'Undefined array key'

        if re.match(r'^Undefined variable ', message):
            return 'Undefined variable'

        if re.match(r'^Undefined property: ', message):
            return 'Undefined property'

        if re.match(r'^Attempt to read property ', message):
            return 'Attempt to read property on null'

        if re.match(r'^Call to a member function ', message):
            return 'Call to a member function on null'

        if re.match(r'^ini_set\(\): Session ini settings cannot be changed', message):
            return 'Session ini settings cannot be changed when active'

        return message