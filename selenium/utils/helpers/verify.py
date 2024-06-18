import logging


class Verify:
    @staticmethod
    def equals(actual, expected, message_on_fail):
        try:
            assert actual == expected, message_on_fail
        except AssertionError as err:
            Verify.equals_error_handling(err, actual, expected, message_on_fail)

    @staticmethod
    def not_equals(actual, expected, message_on_fail):
        try:
            assert actual != expected, message_on_fail
        except AssertionError as err:
            Verify.equals_error_handling(err, actual, expected, message_on_fail)

    @staticmethod
    def true(condition, message_on_fail):
        try:
            assert condition, message_on_fail
        except AssertionError as err:
            Verify.condition_error_handling(err, message_on_fail)

    @staticmethod
    def false(condition, message_on_fail):
        try:
            assert not condition, message_on_fail
        except AssertionError as err:
            Verify.condition_error_handling(err, message_on_fail)

    @staticmethod
    def equals_error_handling(err, actual, expected, message_on_fail):
        err_type = err.__class__.__name__
        logging.error("%s: %s", err_type, message_on_fail)
        logging.debug("\n\tactual: %s, expected: %s", actual, expected)
        raise err

    @staticmethod
    def condition_error_handling(err, message_on_fail):
        err_type = err.__class__.__name__
        logging.error("%s: %s", err_type, message_on_fail)
        raise err
