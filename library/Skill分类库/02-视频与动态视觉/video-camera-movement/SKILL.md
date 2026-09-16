---
name: video-camera-movement
description: >-
  视频运镜分类与镜头语言知识库。用于AI视频生成时选择运镜方式、编写运镜提示词、
  分析视频镜头运动。当用户提到运镜、镜头运动、camera movement、视频拍摄技巧、
  AI视频prompt中的镜头描述时使用。
---

# 视频运镜分类体系 (Camera Movement Taxonomy)

## 核心原则

运镜描述必须包含：**运动方式 + 速度 + 方向 + 起止状态**
例：「镜头从人物脚部缓慢上升至面部特写，随后固定」

---

## 一、基础属性

### 1.1 视频尺寸 (Aspect Ratio)

| 比例 | 用途 | 英文提示词 |
|------|------|-----------|
| 16:9 | 横屏，YouTube/B站 | `16:9 widescreen` |
| 9:16 | 竖屏，抖音/小红书/Reels | `9:16 vertical` |
| 1:1 | 方形，Instagram Feed | `1:1 square` |
| 4:3 | 传统比例，复古风格 | `4:3 aspect ratio` |
| 2.35:1 | 超宽银幕，电影感 | `2.35:1 anamorphic widescreen` |
| 21:9 | 超宽屏，沉浸式 | `21:9 ultrawide` |

### 1.2 镜头速度 (Speed)

| 类型 | 描述 | 英文提示词 |
|------|------|-----------|
| 极慢 | 几乎感觉不到移动，情绪烘托 | `very slow, barely perceptible` |
| 缓慢 | 平稳舒缓，叙事节奏 | `slow, smooth` |
| 中速 | 正常跟拍速度 | `moderate pace` |
| 快速 | 紧张感、动作场景 | `fast-paced` |
| 极快/甩 | 瞬间切换，转场用 | `whip, rapid` |
| 变速 | 从慢到快或反之 | `speed ramp, accelerating/decelerating` |

### 1.3 景别 (Shot Size)

| 景别 | 范围 | 英文提示词 | 常见搭配 |
|------|------|-----------|---------|
| 大远景 | 极远全貌 | `extreme wide shot (EWS)` | 固定/航拍升降 |
| 远景 | 环境+人物全身 | `wide shot (WS)` | 推/拉/移 |
| 全景 | 人物全身 | `full shot (FS)` | 跟/移 |
| 中景 | 膝盖以上 | `medium shot (MS)` | 推/跟/摇 |
| 中近景 | 腰部以上 | `medium close-up (MCU)` | 推/固定 |
| 近景 | 胸部以上 | `close-up (CU)` | 固定/微推 |
| 特写 | 面部/局部 | `extreme close-up (ECU)` | 固定/微移 |

---

## 二、运镜动作分类 (Camera Movements)

### 2.1 固定镜头 (Static Shot)

- **定义**：摄像机完全固定，无任何运动，画面内元素自行变动
- **适用**：对话、口播正面、静态展示、情绪定格
- **提示词**：`static shot`, `locked-off camera`, `fixed camera position`
- **变体**：
  - 纯固定：画面完全不动
  - 微固定：几乎不动，带极轻微呼吸感抖动（增加真实感）

### 2.2 跟随镜头 (Following/Tracking Shot)

- **定义**：镜头跟随特定物体/人物运动
- **关键**：必须说明「跟随什么」+「主体的运动方式」+「镜头与主体的相对位置」
- **提示词**：`tracking shot`, `following shot`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 背跟 | 镜头在主体背后跟随前进 | `camera follows from behind` |
| 正跟 | 镜头在主体正前方后退拍摄 | `camera moves backward facing the subject` |
| 侧跟 | 镜头在主体侧面平行移动 | `side tracking shot` |
| 低角度跟 | 低机位跟随脚步/宠物 | `low-angle tracking shot` |
| 高角度跟 | 俯视角度跟随 | `overhead tracking shot` |
| 环绕跟 | 边跟随边环绕主体 | `orbiting tracking shot` |

### 2.3 推镜头 (Dolly In / Push In)

- **定义**：镜头向主体逐渐靠近，元素在画面内逐渐放大
- **作用**：聚焦注意力、强调情绪、揭示细节
- **提示词**：`dolly in`, `push in`, `camera moves closer`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 缓推 | 缓慢靠近，情绪递进 | `slow dolly in` |
| 快推 | 快速靠近，冲击感 | `fast push in` |
| 微推 | 几乎不可察觉，增加画面张力 | `subtle push in` |
| 推至特写 | 从中景推到面部特写 | `dolly in to close-up` |
| 推至细节 | 推到物体局部细节 | `push in to detail` |
| 阶梯推 | 推-停-推，节奏分段 | `stepped dolly in` |

### 2.4 拉镜头 (Dolly Out / Pull Out)

- **定义**：摄像机逐渐远离主体，视角从局部扩展到全貌
- **作用**：揭示环境、交代场景关系、结束感
- **提示词**：`dolly out`, `pull out`, `camera moves away`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 缓拉 | 缓慢远离，渐渐展示全貌 | `slow dolly out` |
| 快拉 | 快速远离，震撼揭示 | `fast pull out` |
| 拉远后固定 | 拉到一定距离后镜头固定 | `dolly out then hold` |
| 拉至远景 | 从特写一直拉到大远景 | `pull out to wide shot` |
| 无限拉远 | 持续远离至极远（航拍感） | `infinite pull out, aerial reveal` |

### 2.5 移镜头 / 横移 (Lateral Tracking)

- **定义**：摄像机整体左右平移，视角明显横向运动
- **提示词**：`lateral tracking`, `truck shot`, `crab shot`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 向左平移 | 匀速向左水平移动 | `truck left`, `tracking left` |
| 向右平移 | 匀速向右水平移动 | `truck right`, `tracking right` |
| 斜向移动 | 对角线方向移动 | `diagonal tracking` |
| 不规则移动 | 非匀速、非直线的横向移动 | `irregular lateral movement` |
| 弧线移动 | 沿弧线横向移动 | `arc tracking shot` |
| 穿越移动 | 穿过障碍物/人群横移 | `tracking through obstacles` |

### 2.6 旋转镜头 / 环绕 (Orbit / Rotation)

- **定义**：摄像机围绕静止主体旋转移动，主体呈现旋转效果
- **提示词**：`orbit shot`, `revolving shot`, `circular tracking`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 顺时针环绕 | 从主体左侧到右侧 | `clockwise orbit` |
| 逆时针环绕 | 从主体右侧到左侧 | `counterclockwise orbit` |
| 半环绕(180°) | 绕主体半圈 | `180-degree orbit` |
| 全环绕(360°) | 绕主体一整圈 | `360-degree orbit` |
| 螺旋上升环绕 | 边环绕边升高 | `spiral ascending orbit` |
| 螺旋下降环绕 | 边环绕边降低 | `spiral descending orbit` |

### 2.7 升降镜头 (Crane / Boom / Pedestal)

- **定义**：镜头在垂直方向上做升降运动，景别产生高度差变化
- **提示词**：`crane shot`, `boom shot`, `pedestal`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 升镜头 | 从低位上升到高位 | `crane up`, `pedestal up`, `rising shot` |
| 降镜头 | 从高位下降到低位 | `crane down`, `pedestal down`, `descending shot` |
| 升后俯瞰 | 升到最高后俯视 | `crane up to bird's eye` |
| 降至平视 | 从高处降到平视 | `descend to eye level` |
| 升降结合推拉 | 升降同时推或拉 | `crane up while dolly in` |
| 揭示升降 | 升起后揭示背后场景 | `reveal crane shot` |

### 2.8 摇镜头 (Pan / Tilt)

- **定义**：摄像机位置固定，通过旋转镜头方向带出画面其他视角
- **提示词**：`pan` (水平), `tilt` (垂直)

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 水平左摇 | 镜头从右向左水平旋转 | `pan left` |
| 水平右摇 | 镜头从左向右水平旋转 | `pan right` |
| 垂直上摇 | 镜头从下向上旋转 | `tilt up` |
| 垂直下摇 | 镜头从上向下旋转 | `tilt down` |
| 斜向摇 | 对角线方向旋转 | `diagonal pan-tilt` |
| 360°旋转摇 | 水平方向旋转一整圈 | `360-degree pan` |
| 揭示摇 | 摇到最终位置揭示关键元素 | `reveal pan` |

### 2.9 甩镜头 (Whip Pan / Swish Pan)

- **定义**：镜头急速摇转至另一方向，画面产生运动模糊
- **作用**：转场、时间跳跃、制造紧张感
- **提示词**：`whip pan`, `swish pan`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 水平甩 | 快速水平甩向一侧 | `horizontal whip pan` |
| 垂直甩 | 快速垂直甩向上/下 | `vertical whip tilt` |
| 甩接甩 | 两个甩镜头衔接转场 | `whip pan transition` |
| 对角甩 | 斜向急速甩 | `diagonal whip` |

### 2.10 晃动镜头 (Handheld / Shake)

- **定义**：摄像机在空间上随机小幅度晃动，增加纪实感/临场感
- **提示词**：`handheld`, `shaky camera`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 轻微晃动 | 有呼吸感的微抖 | `subtle handheld` |
| 明显晃动 | 纪录片/战争场景 | `shaky handheld` |
| 跟随晃动 | 跟随主体同时晃动 | `handheld tracking` |
| 奔跑晃动 | 模拟跑动拍摄 | `running handheld` |

### 2.11 变焦镜头 (Zoom)

- **定义**：通过改变镜头焦距实现放大/缩小，摄像机位置不变
- **提示词**：`zoom in`, `zoom out`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 缓慢变焦推 | 缓慢拉近焦距 | `slow zoom in` |
| 快速变焦推 | 瞬间拉近 | `snap zoom in` |
| 变焦拉 | 焦距从长变短 | `zoom out` |
| 希区柯克变焦 | 推镜头+反向变焦（眩晕感） | `dolly zoom`, `vertigo effect` |

### 2.12 滚转镜头 (Roll / Dutch Angle Movement)

- **定义**：镜头沿光轴旋转，画面产生倾斜旋转效果
- **提示词**：`camera roll`, `dutch angle rotation`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 顺时针滚转 | 画面顺时针旋转 | `clockwise roll` |
| 逆时针滚转 | 画面逆时针旋转 | `counterclockwise roll` |
| 微滚转 | 轻微倾斜增加不安感 | `subtle dutch angle` |

### 2.13 航拍运镜 (Aerial / Drone)

- **定义**：高空视角的运镜
- **提示词**：`aerial shot`, `drone shot`

| 子类型 | 描述 | 提示词 |
|--------|------|--------|
| 俯冲 | 从高空快速下降至主体 | `drone dive`, `descending aerial` |
| 拉升 | 从低位快速上升至鸟瞰 | `drone ascend`, `aerial pull up` |
| 航拍环绕 | 高空绕主体飞行 | `aerial orbit` |
| 航拍跟随 | 高空跟随主体移动 | `aerial tracking` |
| 航拍平移 | 高空水平飞行 | `aerial lateral` |
| 穿越机视角 | FPV无人机穿越 | `FPV drone shot` |

---

## 三、转场 (Transitions)

| 转场类型 | 描述 | 适用场景 | 提示词 |
|---------|------|---------|--------|
| 自然过渡 | 平滑衔接，内容关联 | 连续叙事 | `smooth transition` |
| 淡入 | 从黑/白屏渐现 | 开场、新章节 | `fade in` |
| 淡出 | 画面渐隐至黑/白 | 结尾、时间流逝 | `fade out`, `fade to black` |
| 交叉叠化 | 前后画面交叉溶解 | 时间转换、回忆 | `cross dissolve` |
| 前景遮挡 | 前景物体遮住镜头后切换 | 无缝转场 | `foreground wipe transition` |
| 甩转场 | 利用甩镜头动态模糊衔接 | 快节奏剪辑 | `whip pan transition` |
| 匹配剪辑 | 前后画面形状/动作匹配 | 创意转场 | `match cut` |
| 跳切 | 同景别直接跳跃 | 口播、时间压缩 | `jump cut` |
| 遮罩转场 | 形状遮罩擦除 | 创意/MG风格 | `mask wipe transition` |

---

## 四、口播场景运镜方案 (Talking Head Scenarios)

### 13种常见口播场景及推荐运镜

| # | 场景 | 推荐运镜 | 景别 |
|---|------|---------|------|
| 1 | 正面直拍 | 固定镜头 / 微推 | 中近景~近景 |
| 2 | 半身侧面 | 固定 + 轻微弧线移动 | 中景 |
| 3 | 走路口播 | 正跟/侧跟 + 稳定器 | 中景~中近景 |
| 4 | 坐姿口播 | 固定 / 缓推 | 中景~近景 |
| 5 | 车内口播 | 固定(吸盘) / 轻微晃动 | 近景 |
| 6 | 户外站立 | 固定 / 缓慢环绕 | 中景 |
| 7 | 探店口播 | 跟随 + 手持晃动 + 推拉 | 中景~全景 |
| 8 | 屏幕录制+画中画 | 固定(人物) + 屏幕录制 | 近景(人物窗口) |
| 9 | 产品展示 | 固定(人) + 推至产品特写 | 中景→特写 |
| 10 | Vlog式 | 手持自拍 + 晃动 + 切换 | 近景~中近景 |
| 11 | 采访式 | 固定/缓推 + 正反打 | 中景~近景 |
| 12 | 双人对话 | 固定 + 摇镜头切换 | 中景 |
| 13 | 情景演绎 | 跟随 + 推拉 + 升降组合 | 多景别切换 |

---

## 五、AI视频提示词结构 (Prompt Template)

```
[镜头运动], [景别], [主体描述] [动作], [环境/场景], [光线/时间], [速度/风格]
```

**示例**：
```
Slow dolly in, medium close-up, a woman speaking to camera in a modern 
office, soft natural window light, subtle handheld feel, cinematic 4K
```

## 详细参考

- 运镜组合与复合运动详见 [combinations.md](combinations.md)
- 各场景完整prompt示例见 [prompt-examples.md](prompt-examples.md)
