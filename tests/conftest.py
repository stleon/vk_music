def pytest_report_header(config):
    if config.option.verbose > 0:
        with open('requirements.txt') as f:
            data = f.read().replace('\n', ', ')

        return "project deps: %s" % data
