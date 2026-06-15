# 教案转音频工作流 Skill

这是一个 Codex Skill，用来把原始教案转换成适合演示视频使用的文案、逐页口播稿、完整 TTS 文本和自然口播音频。

## 它能做什么

这个 Skill 会引导 Codex 按照固定流程处理教案：

```text
教案 -> 演示文案 -> 逐页口播稿 -> 完整 TTS 文本 -> 音频
```

它适合课程创作者、老师、知识博主，以及需要把教案快速变成演示视频旁白的人。

## 仓库结构

```text
lesson-to-audio-workflow-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── prompts.md
└── scripts/
    └── prepare_lesson_workspace.py
```

## 生成产物

工作流会在课程目录中创建或维护这些文件：

```text
lesson.md       # 原始教案或教学笔记
pages.md        # 按画面页拆分的演示文案
narration.md    # 按画面页整理的口播稿
full.txt        # 用于 TTS 的完整纯口播文本
audio.wav       # 可选，生成的 WAV 音频
voice.mp3       # 可选，生成的 MP3 音频
```

## 推荐提示词

在 Codex 中可以这样调用：

```text
Use $lesson-to-audio-workflow to turn this lesson plan into page scripts, spoken narration, full TTS text, and audio.
```

如果你想用中文提示，也可以这样说：

```text
使用 $lesson-to-audio-workflow，把这份教案转换成演示文案、逐页口播稿、完整 TTS 文本，并在可用时生成音频。
```

## 辅助脚本

创建一个标准课程工作目录：

```bash
python scripts/prepare_lesson_workspace.py lessons/my-lesson
```

脚本会创建这些初始文件：

```text
lesson.md
pages.md
narration.md
full.txt
```

## 安装方式

把这个仓库克隆到 Codex 的 skills 目录中：

```bash
git clone git@github.com:LinYangF/lesson-to-audio-workflow-skill.git ~/.codex/skills/lesson-to-audio-workflow
```

之后在 Codex 中通过 skill 名称调用：

```text
$lesson-to-audio-workflow
```

## 使用建议

如果你的项目里已经有自己的课程处理命令，这个 Skill 会优先使用项目内的工作流。  
如果本地还没有配置 TTS 或 CosyVoice，它会先生成文本产物，并告诉你缺少什么音频生成依赖。
