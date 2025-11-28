"""
Message Decoder
OFEC-60-60-20-10 - Ground Receiver

This module decodes CBOR-encoded OFEC messages.
"""

from typing import Dict, Any, Optional
import struct
import io
import logging

logger = logging.getLogger(__name__)


class CBORDecoder:
    """
    Decodes CBOR-encoded OFEC messages.
    """
    
    # CBOR major types
    UNSIGNED_INT = 0
    NEGATIVE_INT = 1
    BYTE_STRING = 2
    TEXT_STRING = 3
    ARRAY = 4
    MAP = 5
    TAG = 6
    SIMPLE = 7
    
    def __init__(self):
        """Initialize the decoder."""
        self._buffer = io.BytesIO()
    
    def decode(self, data: bytes) -> Dict:
        """
        Decode CBOR data to dictionary.
        
        Args:
            data: CBOR-encoded bytes
            
        Returns:
            Decoded dictionary
        """
        self._buffer = io.BytesIO(data)
        return self._decode_value()
    
    def _decode_value(self) -> Any:
        """Decode a single CBOR value."""
        initial_byte = self._read_bytes(1)[0]
        major_type = initial_byte >> 5
        additional_info = initial_byte & 0x1F
        
        if major_type == self.UNSIGNED_INT:
            return self._decode_unsigned(additional_info)
        elif major_type == self.NEGATIVE_INT:
            return -1 - self._decode_unsigned(additional_info)
        elif major_type == self.BYTE_STRING:
            length = self._decode_unsigned(additional_info)
            return self._read_bytes(length)
        elif major_type == self.TEXT_STRING:
            length = self._decode_unsigned(additional_info)
            return self._read_bytes(length).decode("utf-8")
        elif major_type == self.ARRAY:
            length = self._decode_unsigned(additional_info)
            return [self._decode_value() for _ in range(length)]
        elif major_type == self.MAP:
            length = self._decode_unsigned(additional_info)
            result = {}
            for _ in range(length):
                key = self._decode_value()
                value = self._decode_value()
                result[key] = value
            return result
        elif major_type == self.SIMPLE:
            return self._decode_simple(additional_info)
        else:
            raise ValueError(f"Unknown CBOR major type: {major_type}")
    
    def _decode_unsigned(self, additional_info: int) -> int:
        """Decode unsigned integer."""
        if additional_info < 24:
            return additional_info
        elif additional_info == 24:
            return self._read_bytes(1)[0]
        elif additional_info == 25:
            return struct.unpack(">H", self._read_bytes(2))[0]
        elif additional_info == 26:
            return struct.unpack(">I", self._read_bytes(4))[0]
        elif additional_info == 27:
            return struct.unpack(">Q", self._read_bytes(8))[0]
        else:
            raise ValueError(f"Invalid additional info: {additional_info}")
    
    def _decode_simple(self, additional_info: int) -> Any:
        """Decode simple value."""
        if additional_info == 20:
            return False
        elif additional_info == 21:
            return True
        elif additional_info == 22:
            return None
        elif additional_info == 27:
            # Double precision float
            return struct.unpack(">d", self._read_bytes(8))[0]
        else:
            return None
    
    def _read_bytes(self, count: int) -> bytes:
        """Read bytes from buffer."""
        data = self._buffer.read(count)
        if len(data) < count:
            raise ValueError("Unexpected end of CBOR data")
        return data


def decode_message(data: bytes) -> Dict:
    """
    Convenience function to decode a message.
    
    Args:
        data: CBOR-encoded message
        
    Returns:
        Decoded dictionary
    """
    decoder = CBORDecoder()
    return decoder.decode(data)


class MessageDecoder:
    """
    High-level message decoder for OFEC messages.
    """
    
    def __init__(self):
        """Initialize the message decoder."""
        self._cbor_decoder = CBORDecoder()
        self._message_count = 0
    
    def decode_envelope_state(self, data: bytes) -> Optional[Dict]:
        """
        Decode an envelope state message.
        
        Args:
            data: CBOR-encoded message
            
        Returns:
            Decoded message dictionary or None on error
        """
        try:
            message = self._cbor_decoder.decode(data)
            self._message_count += 1
            return message
        except ValueError as e:
            logger.error("CBOR decode error - invalid format: %s", e)
            return None
        except struct.error as e:
            logger.error("CBOR decode error - malformed data: %s", e)
            return None
    
    @property
    def message_count(self) -> int:
        """Get total messages decoded."""
        return self._message_count
