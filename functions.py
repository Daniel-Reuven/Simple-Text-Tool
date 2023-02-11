from loguru import logger
import base64


def encode_base64(decoded):
    try:
        encoded_text = base64.b64encode(bytes(decoded, 'utf-8'))
        final_text = encoded_text.decode('utf-8')
        return final_text
    except Exception as e:
        logger.error(f'An Error has occurred: {e}'.format())


def decode_base64(encoded):
    try:
        base64_bytes = encoded.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        final_text = message_bytes.decode()
        return final_text
    except Exception as e:
        logger.error(f'An Error has occurred: {e}'.format())
