# processing a GET-request with params

class GetRequests:

    @staticmethod
    def pars_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        # obtain equest params
        query_string = environ['QUERY_STRING']
        # turn params into dict
        request_params = GetRequest.pars_input_data(query_string)
        return request_params


