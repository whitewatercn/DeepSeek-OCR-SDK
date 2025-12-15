"""
Example 1: Basic Usage

This example demonstrates the basic usage of DeepSeek OCR SDK.
"""

import os
from pathlib import Path
from multi_ocr_sdk import DeepSeekOCR

# Set your API key (or use DS_OCR_API_KEY environment variable)
API_KEY = os.getenv("DS_OCR_API_KEY", "your_api_key_here")


def main():
    """Basic OCR example."""
    # Initialize client
    client = DeepSeekOCR(api_key=API_KEY)

    # Example 1: Simple document (use FREE_OCR mode - fastest)
    print("Example 1: Processing simple document with FREE_OCR...")
    sample_file = "sample_docs/simple_document.pdf"
    if not Path(sample_file).exists():
        print(f"Note: Sample file not found at {sample_file}")
        print("Please provide your own PDF file to test.\n")
    else:
        try:
            text = client.parse(
                sample_file,
                mode="free_ocr",
            )
            print(f"Extracted text ({len(text)} chars):")
            print(text[:500])  # Print first 500 chars
            print("\n" + "=" * 60 + "\n")
        except Exception as e:
            print(f"Error: {e}\n")

    # Example 2: Document with complex tables (use GROUNDING mode)
    print("Example 2: Processing document with complex tables...")
    table_file = "sample_docs/complex_table.pdf"
    if not Path(table_file).exists():
        print(f"Note: Sample file not found at {table_file}")
        print("Please provide your own PDF file with tables to test.\n")
    else:
        try:
            text = client.parse(
                table_file,
                mode="grounding",
            )
            print(f"Extracted text ({len(text)} chars):")
            print(text[:500])
            print("\n" + "=" * 60 + "\n")
        except Exception as e:
            print(f"Error: {e}\n")

    # Example 3: Custom DPI for better quality
    print("Example 3: Processing with custom DPI...")
    sample_file = "sample_docs/simple_document.pdf"
    if not Path(sample_file).exists():
        print(f"Note: Sample file not found at {sample_file}")
        print("Please provide your own PDF file to test.\n")
    else:
        try:
            text = client.parse(
                sample_file,
                mode="free_ocr",
                dpi=300,  # Higher DPI for better quality (slower, larger)
            )
            print(f"Extracted text ({len(text)} chars):")
            print(text[:500])
            print("\n" + "=" * 60 + "\n")
        except Exception as e:
            print(f"Error: {e}\n")



if __name__ == "__main__":
    # Run synchronous examples
    main()
    
    # Note: Async features have been removed in this version.
    # Users should implement their own async wrappers if needed.
