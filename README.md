# Happy Passengers 0.8.0

A coach gameplay mod for Euro Truck Simulator 2.  
《欧洲卡车模拟 2》的客车玩法 MOD。

## Current Features
当前功能

### Zero Satisfaction Penalties for Speeding and G-Force
超速与 G 力零扣分

Speeding and both G-force tiers apply no passenger satisfaction penalty.  
超速和两档 G 力均不扣除乘客满意度。

The original trigger thresholds, probabilities and cooldowns are retained.  
触发门槛、概率和冷却时间保持原版。

Collisions, vehicle wear, lateness and traffic offences can still reduce satisfaction.  
碰撞、车辆磨损、晚点和交通违章仍可能降低满意度。

A speeding ticket may still cause a separate traffic-offence penalty.  
超速罚款仍可能触发独立的交通违章扣分。

The original job-failure rules for extreme impacts remain in effect.  
严重冲击导致任务失败的原版规则仍然生效。

### Penalty-Free Driving Rewards Every 10 km
连续无扣分行驶 10 km 奖励

The penalty-free driving reward distance is reduced from 30 km to 10 km.  
连续无扣分行驶的奖励间隔从 30 km 缩短至 10 km。

Each qualifying reward retains the original increase of 6–12 percentage points.  
每次符合条件的奖励仍按原版增加 6–12 个百分点。

Eligibility, distance tracking, resets and satisfaction limits follow the original game logic.  
触发资格、里程累计、重置及满意度上限沿用原版游戏逻辑。

Other satisfaction rewards, including on-time arrival and penalty-free stage completion, retain their original values.  
准时到达、无扣分完成一段行程等其他满意度奖励保持原值。

### Lower Centers of Gravity for Official Coaches
官方客车低重心

All five chassis variants across the three official coaches receive lower centers of gravity.  
三款官方客车的五种底盘均降低重心。

MAN Lion's Coach: the center-of-gravity value changes from 1.25 to 0.95 on both chassis variants.  
MAN Lion's Coach：两种底盘的重心值均从 1.25 调整为 0.95。

Scania Touring: the center-of-gravity value changes from 1.20 to 0.90 on both chassis variants.  
Scania Touring：两种底盘的重心值均从 1.20 调整为 0.90。

Volvo 9700 DD: the center-of-gravity value changes from 1.40 to 1.05.  
Volvo 9700 DD：重心值从 1.40 调整为 1.05。

These adjustments aim to improve cornering stability, but do not guarantee protection from rollovers.  
这些调整旨在改善过弯稳定性，但不能保证车辆不会侧翻。

Chassis weight, suspension, tires, steering, power and passenger capacity retain their original values.  
底盘重量、悬挂、轮胎、转向、动力和载客量保持原值。

Handling still depends on speed, road geometry, game settings and other physics mods.  
实际操控仍受车速、道路形状、游戏设置及其他物理 MOD 影响。

### Original Passenger Sounds
原版乘客声音

Original passenger, vehicle, navigation and environmental sounds are retained.  
保留原版乘客、车辆、导航和环境声音。

Custom praise messages, praise voices and tutorial modifications are not included.  
不包含自定义称赞提示、称赞语音或教程修改。

## Installation and Updates
安装与升级

When first installing or switching from versioned filenames, disable older Happy Passengers packages and enable `happy_passengers.scs` once.  
首次安装或从带版本号的文件名切换时，停用旧版 Happy Passengers 安装包，并手动启用一次 `happy_passengers.scs`。

Copy `dist/happy_passengers.scs` into the `mod` folder in your game user directory, usually `Documents/Euro Truck Simulator 2/mod`.  
将 `dist/happy_passengers.scs` 复制到游戏用户目录下的 `mod` 文件夹，通常为 `文档/Euro Truck Simulator 2/mod`。

Enable Happy Passengers in the current profile's Mod Manager, confirm the changes and reload the save.  
在当前存档的 MOD 管理器中启用 Happy Passengers，确认修改后重新载入存档。

Copying the file alone does not activate the mod on first installation.  
首次安装时，仅复制文件不会自动启用 MOD。

For later compatible updates, exit the game and overwrite the same `happy_passengers.scs` file without renaming it.  
后续更新兼容版本时，先退出游戏，再覆盖同名的 `happy_passengers.scs` 文件，不要重命名。

Keep only the fixed-name package in the game's mod folder to avoid loading multiple Happy Passengers versions.  
游戏的 MOD 文件夹中仅保留固定名称的安装包，避免同时载入多个 Happy Passengers 版本。

Give this mod higher priority than other mods changing the same coach economy or chassis definitions.  
将本 MOD 的优先级设为高于其他修改相同客车经济或底盘配置的 MOD。

## Requirements and Compatibility
运行要求与兼容性

The Coaches DLC is required.  
需要 Coaches DLC。

This release targets ETS2 1.62.x and is based on the original definitions from version 1.62.3.2.  
本版面向 ETS2 1.62.x，基于 1.62.3.2 的原版配置制作。

The package overrides one shared coach economy file and five official coach chassis files.  
安装包覆盖一份共享客车经济配置和五份官方客车底盘配置。

Other mods overriding these files may conflict, and the higher-priority version takes effect.  
其他覆盖这些文件的 MOD 可能产生冲突，并以优先级较高的版本为准。

Truck chassis, global physics definitions and user stability settings are not modified.  
不修改货车底盘、全局物理配置或用户稳定性设置。

The project does not automatically install the mod, change game files or edit saves.  
项目不会自动安装 MOD、修改游戏原文件或编辑存档。

## Validation Status
验证状态

Static configuration comparisons and package integrity checks have passed.  
静态配置对比与安装包完整性检查已通过。

The user has reported that the zero-penalty configuration works in game.  
用户已反馈零扣分配置在游戏中生效。

The 10 km reward interval and the handling improvement from the lower centers of gravity have not yet been verified in game.  
10 km 奖励间隔及低重心带来的操控改善幅度尚未游戏内验证。

Steam Workshop Uploader validation and publication have not been completed.  
尚未完成 Steam Workshop Uploader 验证或工坊发布。

## Building and Outputs
打包与产物

With Python 3 installed, run `python tools/build.py` from the project directory.  
安装 Python 3 后，在项目目录运行 `python tools/build.py`。

The local package is generated at `dist/happy_passengers.scs`.  
本地安装包生成于 `dist/happy_passengers.scs`。

The Workshop content directory is generated at `dist/workshop_0.8.0/`.  
工坊内容目录生成于 `dist/workshop_0.8.0/`。

The preview image is available at `mod/mod_icon.jpg`.  
预览图位于 `mod/mod_icon.jpg`。

The builder reads the package version from `mod/manifest.sii` for tag validation and Workshop directory names, while keeping the local package filename fixed.  
打包脚本从 `mod/manifest.sii` 读取版本号，用于标签校验和工坊目录命名，本地安装包文件名保持固定。

Keep only the current release outputs in `dist/` and remove obsolete builds.  
`dist/` 中仅保留当前版本产物，旧版产物予以删除。

## Automatic GitHub Releases
GitHub 自动发布

The repository is [Qwerto107/Happy-Passengers](https://github.com/Qwerto107/Happy-Passengers).  
仓库地址为 [Qwerto107/Happy-Passengers](https://github.com/Qwerto107/Happy-Passengers)。

Commit and push the sources, build script and `.github/workflows/release.yml` to the repository before the first release.  
首次发布前，将源文件、打包脚本及 `.github/workflows/release.yml` 提交并推送到仓库。

With GitHub Actions enabled, pushing a tag such as `v0.8.0` automatically builds and publishes a GitHub Release.  
启用 GitHub Actions 后，推送如 `v0.8.0` 的标签会自动打包并发布 GitHub Release。

For the current version, run `git tag v0.8.0` on the intended commit and then `git push origin v0.8.0`.  
当前版本可在准备发布的提交上执行 `git tag v0.8.0`，再执行 `git push origin v0.8.0`。

The tag must equal `v` followed by `package_version` in `mod/manifest.sii`, or the build stops before publication.  
标签必须等于 `v` 加上 `mod/manifest.sii` 中的 `package_version`，否则打包会在发布前停止。

Editing the version or pushing ordinary commits alone does not trigger a release.  
仅修改版本号或推送普通提交不会触发发布。

Each release includes the fixed-name `happy_passengers.scs` and a versioned Workshop ZIP such as `workshop_0.8.0.zip`.  
每次发布包含固定名称的 `happy_passengers.scs`，以及带版本号的工坊 ZIP，例如 `workshop_0.8.0.zip`。

The mod version remains in the manifest and Release tag, so updating it does not change the installed package filename.  
MOD 版本号仍保留在清单和 Release 标签中，更新版本不会改变安装包文件名。

The Workshop ZIP contains `versions.sii` and `v1_62/` at its root; extract it before selecting the directory in the Workshop Uploader.  
工坊 ZIP 根目录包含 `versions.sii` 和 `v1_62/`，请先解压再在工坊上传工具中选择该目录。

Release notes use the bilingual text from `mod/mod_description.txt`.  
Release 说明使用 `mod/mod_description.txt` 中的中英对照文本。

The workflow uses the built-in `GITHUB_TOKEN` and requires no personal access token or Steam credentials.  
工作流使用内置的 `GITHUB_TOKEN`，无需个人访问令牌或 Steam 账号凭据。

Existing releases are not overwritten; inspect failures in the repository's Actions tab before retrying.  
已有 Release 不会被覆盖，重试前请先在仓库的 Actions 页面检查失败原因。

GitHub publication does not upload to Steam Workshop or install and activate the mod in the game.  
GitHub 发布不会上传至 Steam 创意工坊，也不会在游戏中安装或启用 MOD。

## Project Layout
项目目录

`mod/` contains the mod sources, description, manifest and icon.  
`mod/` 存放 MOD 源文件、说明、清单和图标。

`tools/` contains the build script.  
`tools/` 存放打包脚本。

`.github/workflows/` contains the tag-triggered GitHub Release workflow.  
`.github/workflows/` 存放由标签触发的 GitHub Release 工作流。

`dist/` contains generated packages and Workshop content and is excluded from version control.  
`dist/` 存放生成的安装包和工坊内容，不纳入版本管理。

`.work/reference/` contains the six original game definitions used for local comparisons and is excluded from version control.  
`.work/reference/` 存放用于本地对照的六份原版游戏配置，不纳入版本管理。

`.work/tools/` contains locally downloaded resource tools and is excluded from version control.  
`.work/tools/` 存放本机下载的资源工具，不纳入版本管理。

Original game references and extracted assets must stay inside the ignored `.work/` directory and must not be committed.  
原版游戏对照文件及解包资源必须留在已忽略的 `.work/` 目录内，不得提交。

## References
参考资料

See the official [Mod Manager documentation](https://modding.scssoft.com/wiki/Documentation/Engine/Mod_manager) for package metadata and activation requirements.  
安装包元数据和启用要求请参阅官方 [MOD 管理器文档](https://modding.scssoft.com/wiki/Documentation/Engine/Mod_manager)。

See the official [chassis documentation](https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_chassis_data) for the center-of-gravity parameter.  
重心参数请参阅官方 [底盘配置文档](https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_chassis_data)。

See the official [Workshop package structure](https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Workshop_mod_structure) for upload directory requirements.  
上传目录要求请参阅官方 [工坊安装包结构文档](https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Workshop_mod_structure)。
