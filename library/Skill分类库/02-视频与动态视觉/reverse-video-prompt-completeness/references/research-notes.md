# 参考说明

这些开源项目只作为规则设计参考，本地 skill 运行时不依赖它们。

- [Video-ChatGPT](https://github.com/mbzuai-oryx/Video-ChatGPT)：参考它把视频理解拆成时间维度视觉描述，而不是单帧 caption。
- [Video-LLaVA](https://github.com/PKU-YuanGroup/Video-LLaVA)：参考多模态视频指令理解和视频级推理方式。
- [ShareGPT4Video](https://github.com/ShareGPT4Omni/ShareGPT4Video)：参考 dense video caption 数据对细粒度视频描述的要求。
- [InternVideo](https://github.com/OpenGVLab/InternVideo)：参考视频表征、动作感知和视频理解方向。
- [PySceneDetect](https://github.com/Breakthrough/PySceneDetect)：参考先切镜头再逐镜头校验 prompt 的思路。

## 转化成产品规则

- 反推 prompt 应按镜头或时间段检查，不能只看一整段文字。
- 动作必须基于可见证据；只有看到或用户要求的动作才补。
- 主体动作和相机运动必须分开检查，混在一起容易漏细节。
- 字幕和口播要独立抽取、独立校验。
- 场景切分有助于判断转场和连续性是否完整。
- 先做完整性检查，再压缩到 2000 字以内；不要先压缩再补细节。

