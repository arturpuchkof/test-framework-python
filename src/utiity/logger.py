import json
import logging

import requests


class Logger:
    def __init__(self, name: str = 'api'):
        self._logger = logging.getLogger(name=name)


    def log_response(self, response: requests.Response, *args, **kwargs):
        request = response.request
        lines = [f'REQUEST: {request.method} {request.url}', f'{request.headers}']
        if request.body:
            lines.append('REQUEST BODY:')
            lines.append(self.format_body(request.body))
        lines.append('=' * 130)
        lines.append(f'RESPONSE: {response.status_code} {response.reason}')
        lines.append('RESPONSE BODY:')
        lines.append(self.format_body(response.text))
        lines.append('=' * 130)
        self._logger.info("\n".join(lines))


    @staticmethod
    def format_body(body) -> str:
        return json.dumps(json.loads(body), indent=2, ensure_ascii=False)
