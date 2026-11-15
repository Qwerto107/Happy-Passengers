"""打包本地 MOD 和创意工坊上传目录，仅使用 Python 标准库。"""

import argparse
from pathlib import Path
import re
import shutil
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "mod"
DIST = ROOT / "dist"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", help="发布标签，必须与清单版本一致，例如 v0.8.0")
    args = parser.parse_args()
    manifest = (SOURCE / "manifest.sii").read_text(encoding="utf-8")
    # 从清单读取版本，用于发布校验与工坊目录命名。
    version_match = re.search(
        r'^\s*package_version:\s*"(\d+\.\d+\.\d+)"\s*$',
        manifest,
        re.MULTILINE,
    )
    if version_match is None:
        raise ValueError("manifest.sii 中的版本号须为数字组成的三段式版本")
    version = version_match.group(1)
    # 发布前验证标签，避免把错误版本的安装包上传到 Release。
    if args.tag is not None and args.tag != f"v{version}":
        raise ValueError(f"发布标签须为 v{version}，实际为 {args.tag}")

    if not (SOURCE / "def" / "bus_economy_data.sii").is_file():
        raise FileNotFoundError("客车满意度配置缺失")
    for relative in (
        "def/vehicle/bus/man.lions_24/chassis/121_4x2.sii",
        "def/vehicle/bus/man.lions_24/chassis/139_6x24.sii",
        "def/vehicle/bus/scania.touring_23/chassis/129_4x2.sii",
        "def/vehicle/bus/scania.touring_23/chassis/137_6x24.sii",
        "def/vehicle/bus/volvo.9700_23/chassis/143_6x24.sii",
    ):
        if not (SOURCE / relative).is_file():
            raise FileNotFoundError(f"必要配置缺失：{relative}")

    files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    DIST.mkdir(exist_ok=True)
    # 固定安装包文件名，让覆盖更新沿用同一 MOD 名称。
    archive = DIST / "happy_passengers.scs"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as package:
        for path in files:
            package.write(path, path.relative_to(SOURCE).as_posix())

    workshop = DIST / f"workshop_{version}"
    content = workshop / "v1_62"
    # 工坊包的名称与版本范围由上传工具和 versions.sii 管理。
    for path in files:
        destination = content / path.relative_to(SOURCE)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if path.name == "manifest.sii":
            lines = path.read_text(encoding="utf-8").splitlines()
            destination.write_text(
                "\n".join(
                    line for line in lines
                    if not line.strip().startswith(("display_name:", "compatible_versions[]:"))
                ) + "\n",
                encoding="utf-8",
            )
        else:
            shutil.copyfile(path, destination)

    (workshop / "versions.sii").write_text(
        'SiiNunit\n{\npackage_version_info : .v162\n{\n'
        '    package_name: "v1_62"\n'
        '    compatible_versions[]: "1.62.*"\n}\n}\n',
        encoding="utf-8",
    )
    print(f"本地安装包：{archive}")
    print(f"工坊上传目录：{workshop}")


if __name__ == "__main__":
    main()
