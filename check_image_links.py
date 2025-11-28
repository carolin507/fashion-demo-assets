# check_image_links.py
# 用法：在專案根目錄執行 `python check_image_links.py`，它會列出所有 .py 檔案中所引用的 raw.githubusercontent.com 的圖片連結，並列出目前 repo 下 assets/ 的實際檔案，幫你比對是否對上。

import os
import re

# 你 repo 中實際放圖片的資料夾
ASSETS_DIRS = ["assets/product", "assets/streetstyle", "assets"]

raw_pattern = re.compile(
    r"https://raw.githubusercontent.com/[^/]+/[^/]+/main/([^\"')\s]+)"
)

def scan_py_files(root_dir="."):
    links = []
    for dirpath, _, filenames in os.walk(root_dir):
        for fn in filenames:
            if fn.endswith(".py"):
                path = os.path.join(dirpath, fn)
                with open(path, encoding="utf-8") as f:
                    for idx, line in enumerate(f, start=1):
                        for m in raw_pattern.findall(line):
                            links.append({
                                "file": path,
                                "lineno": idx,
                                "raw_path": m
                            })
    return links

def all_asset_files():
    files = []
    for d in ASSETS_DIRS:
        for dirpath, _, filenames in os.walk(d):
            for fn in filenames:
                rel = os.path.relpath(os.path.join(dirpath, fn), start=".")
                files.append(rel.replace("\\", "/"))
    return set(files)

if __name__ == "__main__":
    links = scan_py_files()
    assets = all_asset_files()

    print("# ==== repo asset files ====")
    for a in sorted(assets):
        print(a)
    print("\n# ==== referenced raw github links ====")
    for link in links:
        print(f'{link["file"]}:{link["lineno"]} → {link["raw_path"]}')

    print("\n# ==== missing assets (referenced but not found in assets/) ====")
    for link in links:
        if link["raw_path"] not in assets:
            print(f'MISSING → {link["file"]}:{link["lineno"]} → {link["raw_path"]}')
