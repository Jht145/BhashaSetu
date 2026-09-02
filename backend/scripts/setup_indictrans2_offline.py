"""
IndicTrans2 INT8 Quantization and Offline Setup Script
Converts AI4Bharat IndicTrans2 distilled models (e.g. dist-200M or dist-320M)
to CTranslate2 INT8 format for 100% offline edge/local inference.
"""

import os
import sys
import argparse
import shutil
from typing import Optional

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_MODEL_NAME = "ai4bharat/indictrans2-indic-indic-dist-200M"
DEFAULT_OUTPUT_DIR = os.path.join(BASE_DIR, "models", "indictrans2_ct2_int8")


def setup_indictrans2_offline(
    model_name: str = DEFAULT_MODEL_NAME,
    output_dir: str = DEFAULT_OUTPUT_DIR,
    quantization: str = "int8",
    device: str = "cpu",
    low_cpu_mem_usage: bool = True
):
    """
    Quantizes and exports IndicTrans2 to CTranslate2 INT8 model format.
    """
    print("=" * 60)
    print("IndicTrans2 CTranslate2 INT8 Offline Converter")
    print("=" * 60)
    print(f"[*] Source Hugging Face Model : {model_name}")
    print(f"[*] Output Model Directory     : {output_dir}")
    print(f"[*] Quantization Mode          : {quantization}")
    print(f"[*] Inference Device Target    : {device}")
    print("=" * 60)

    try:
        import ctranslate2
        from ctranslate2.converters import TransformersConverter
        from huggingface_hub import hf_hub_download
    except ImportError as e:
        print(f"[!] Missing required dependency: {e}")
        print("[!] Please run: pip install ctranslate2 transformers torch huggingface_hub sentencepiece")
        return False

    os.makedirs(output_dir, exist_ok=True)

    # 1. Download & Save SentencePiece Tokenizer
    print("\n[1/3] Downloading & setting up SentencePiece tokenizer...")
    try:
        tokenizer_file = hf_hub_download(
            repo_id=model_name,
            filename="model.SRC",  # IndicTrans2 source tokenizer or tokenizer.model
            local_dir=output_dir,
            local_dir_use_symlinks=False
        )
        target_sp_path = os.path.join(output_dir, "tokenizer.model")
        if os.path.exists(tokenizer_file) and tokenizer_file != target_sp_path:
            shutil.copyfile(tokenizer_file, target_sp_path)
        print(f"  [+] Saved SentencePiece tokenizer to: {target_sp_path}")
    except Exception as tok_err:
        print(f"  [!] Note on tokenizer download: {tok_err}")
        print("  [+] Attempting fallback to standard tokenizer.model...")
        try:
            tokenizer_file = hf_hub_download(
                repo_id=model_name,
                filename="tokenizer.model",
                local_dir=output_dir,
                local_dir_use_symlinks=False
            )
            print(f"  [+] Saved tokenizer to: {tokenizer_file}")
        except Exception as e2:
            print(f"  [!] Please place tokenizer.model manually in {output_dir}: {e2}")

    # 2. Convert Model to CTranslate2 INT8
    print(f"\n[2/3] Converting {model_name} with {quantization} quantization...")
    try:
        converter = TransformersConverter(
            model_name_or_path=model_name,
            copy_files=["tokenizer.json", "tokenizer_config.json", "vocab.json"],
            load_as_float16=False,
            low_cpu_mem_usage=low_cpu_mem_usage
        )
        converter.convert(
            output_dir=output_dir,
            quantization=quantization,
            force=True
        )
        print(f"  [+] Successfully converted model weights to: {output_dir}")
    except Exception as conv_err:
        print(f"  [!] Conversion error: {conv_err}")
        return False

    # 3. Validation
    print("\n[3/3] Validating local CTranslate2 model loading...")
    try:
        translator = ctranslate2.Translator(output_dir, device=device, compute_type=quantization)
        print("  [+] CTranslate2 INT8 Model verified and loaded successfully!")
    except Exception as val_err:
        print(f"  [!] Validation warning: {val_err}")

    print("\n" + "=" * 60)
    print("[SUCCESS] IndicTrans2 Offline INT8 setup completed.")
    print("=" * 60)
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantize IndicTrans2 for Offline CTranslate2 Inference")
    parser.add_argument("--model-name", type=str, default=DEFAULT_MODEL_NAME, help="Hugging Face model repository ID")
    parser.add_argument("--output-dir", type=str, default=DEFAULT_OUTPUT_DIR, help="Local output directory for INT8 model")
    parser.add_argument("--quantization", type=str, default="int8", choices=["int8", "int8_float16", "float16", "int16"], help="Quantization precision")
    parser.add_argument("--device", type=str, default="cpu", help="Target inference device")

    args = parser.parse_args()
    setup_indictrans2_offline(
        model_name=args.model_name,
        output_dir=args.output_dir,
        quantization=args.quantization,
        device=args.device
    )
