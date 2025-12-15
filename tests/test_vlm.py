"""
Tests for the VLM client module.

Basic tests to ensure VLMClient can be imported and initialized correctly.
"""

import pytest

from multi_ocr_sdk import VLMClient, vlm_client


def test_vlm_import_and_structure():
    # Ensure vlm module is importable and symbols exist
    assert hasattr(vlm_client, "VLMClient")

    # Construct a VLM client instance with dummy values (no network calls)
    client = VLMClient(api_key="test", base_url="http://localhost:8000/v1")
    assert hasattr(client, "chat")
    assert hasattr(client.chat, "completions")
    assert hasattr(client.chat.completions, "create")


