from fcs import fc01
from fcs import fc02
from fcs import fc03
from fcs import fc04
from fcs import fc05
from fcs import fc06
from fcs import fc15
from fcs import fc16
request = {
    1: fc01.parse_request,
    2: fc02.parse_request,
    3: fc03.parse_request,
    4: fc04.parse_request,
    5: fc05.parse_request,
    6: fc06.parse_request,
    15: fc15.parse_request,
    16: fc16.parse_request,
}
response = {
    1: fc01.parse_response,
    2: fc02.parse_response,
    3: fc03.parse_response,
    4: fc04.parse_response,
    5: fc05.parse_response,
    6: fc06.parse_response,
    15: fc15.parse_response,
    16: fc16.parse_response,
}
