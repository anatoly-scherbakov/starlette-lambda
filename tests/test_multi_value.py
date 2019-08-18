from starlette.applications import Starlette

from starlette_lambda.aws import LambdaFunction


def test_multi_value():
    scope = LambdaFunction(asgi=Starlette()).get_connection_scope(event={
        'httpMethod': 'GET',
        'path': '/foo',
        'headers': {},
        'requestContext': {},
        'queryStringParameters': {'make': 'TOYOTA', 'zip_code': '65301'},
        'multiValueQueryStringParameters': {
            'make': ['TOYOTA'],
            'zip_code': ['02368', '65301']
        }
    }, context={})

    assert scope['query_string'] == 'make=TOYOTA&zip_code=02368&zip_code=65301'

