# Copyright 2025 AMPEL360 Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
CBOR Encoder
OFEC-23-95-67-12 - Aircraft Publisher

This module handles CBOR encoding for OFEC messages.
"""

from typing import Dict, Any
import struct
import io


class CBOREncoder:
    """
    Encodes OFEC messages to CBOR format.
    
    CBOR (Concise Binary Object Representation) provides
    efficient binary encoding for telemetry data.
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
        """Initialize the CBOR encoder."""
        self._buffer = io.BytesIO()
    
    def encode(self, data: Dict) -> bytes:
        """
        Encode data to CBOR format.
        
        Args:
            data: Dictionary to encode
            
        Returns:
            CBOR-encoded bytes
        """
        self._buffer = io.BytesIO()
        self._encode_value(data)
        return self._buffer.getvalue()
    
    def _encode_value(self, value: Any) -> None:
        """Encode a single value."""
        if value is None:
            self._encode_simple(22)  # null
        elif isinstance(value, bool):
            self._encode_simple(21 if value else 20)
        elif isinstance(value, int):
            self._encode_int(value)
        elif isinstance(value, float):
            self._encode_float(value)
        elif isinstance(value, str):
            self._encode_string(value)
        elif isinstance(value, bytes):
            self._encode_bytes(value)
        elif isinstance(value, list):
            self._encode_array(value)
        elif isinstance(value, dict):
            self._encode_map(value)
        else:
            # Fallback to string representation
            self._encode_string(str(value))
    
    def _encode_head(self, major_type: int, value: int) -> None:
        """Encode CBOR head (major type + additional info)."""
        if value < 24:
            self._buffer.write(bytes([major_type << 5 | value]))
        elif value < 256:
            self._buffer.write(bytes([major_type << 5 | 24, value]))
        elif value < 65536:
            self._buffer.write(bytes([major_type << 5 | 25]))
            self._buffer.write(struct.pack(">H", value))
        elif value < 4294967296:
            self._buffer.write(bytes([major_type << 5 | 26]))
            self._buffer.write(struct.pack(">I", value))
        else:
            self._buffer.write(bytes([major_type << 5 | 27]))
            self._buffer.write(struct.pack(">Q", value))
    
    def _encode_int(self, value: int) -> None:
        """Encode integer."""
        if value >= 0:
            self._encode_head(self.UNSIGNED_INT, value)
        else:
            self._encode_head(self.NEGATIVE_INT, -1 - value)
    
    def _encode_float(self, value: float) -> None:
        """Encode floating point number."""
        # Use double precision (64-bit)
        self._buffer.write(bytes([self.SIMPLE << 5 | 27]))
        self._buffer.write(struct.pack(">d", value))
    
    def _encode_string(self, value: str) -> None:
        """Encode text string."""
        encoded = value.encode("utf-8")
        self._encode_head(self.TEXT_STRING, len(encoded))
        self._buffer.write(encoded)
    
    def _encode_bytes(self, value: bytes) -> None:
        """Encode byte string."""
        self._encode_head(self.BYTE_STRING, len(value))
        self._buffer.write(value)
    
    def _encode_array(self, value: list) -> None:
        """Encode array."""
        self._encode_head(self.ARRAY, len(value))
        for item in value:
            self._encode_value(item)
    
    def _encode_map(self, value: dict) -> None:
        """Encode map (dictionary)."""
        self._encode_head(self.MAP, len(value))
        for k, v in value.items():
            self._encode_value(k)
            self._encode_value(v)
    
    def _encode_simple(self, value: int) -> None:
        """Encode simple value."""
        if value < 24:
            self._buffer.write(bytes([self.SIMPLE << 5 | value]))
        else:
            self._buffer.write(bytes([self.SIMPLE << 5 | 24, value]))


def encode_message(message_dict: Dict) -> bytes:
    """
    Convenience function to encode a message.
    
    Args:
        message_dict: Message dictionary
        
    Returns:
        CBOR-encoded bytes
    """
    encoder = CBOREncoder()
    return encoder.encode(message_dict)


def estimate_size(message_dict: Dict) -> int:
    """
    Estimate encoded message size.
    
    Args:
        message_dict: Message dictionary
        
    Returns:
        Estimated size in bytes
    """
    # Simple estimation based on structure
    return len(encode_message(message_dict))
