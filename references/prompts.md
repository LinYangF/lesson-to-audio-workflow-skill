# Prompts

Use these prompts when the project does not already provide prompts.

## Lesson Plan To Page Script

```text
请把下面这段教案改写成适合演示视频使用的文案。

要求：
1. 按“画面页”拆分。
2. 每页包含【画面标题】【旁白】【画面建议】【预计时长】。
3. 语言要口语化，适合学生理解。
4. 每页只讲一个重点。
5. 整体结构按照“导入问题 -> 核心概念 -> 示例说明 -> 方法步骤 -> 总结提升”组织。
6. 不要写成论文，不要堆概念，要像老师在课堂上带着学生理解。
7. 画面建议要能指导后续生成 HTML/PPT 风格页面。

以下是教案内容：

{{LESSON_TEXT}}
```

## Page Script To Spoken Narration

```text
请把下面的演示视频文案改写成逐页口播稿。

要求：
1. 保留原来的画面页顺序。
2. 每页只输出【画面标题】和【口播稿】。
3. 口播稿要像老师对学生自然讲解，不要像书面稿。
4. 短句为主，适合 TTS 朗读。
5. 术语第一次出现时，用一句白话解释。
6. 每页之间加入自然过渡，但不要太啰嗦。
7. 不要输出画面建议和预计时长。

以下是演示视频文案：

{{PAGES_TEXT}}
```

## Full Text Extraction

```text
请把下面的逐页口播稿合并成一份可直接送入 TTS 的整段口播文本。

要求：
1. 只保留要朗读的口播内容。
2. 删除页码、标题标签、【口播稿】等标记。
3. 每页之间空一行。
4. 不要加入画面建议、预计时长、解释性备注。
5. 保持自然口语，不要改成书面论文。

以下是逐页口播稿：

{{NARRATION_TEXT}}
```

## Audio Revision Checklist

After listening, revise text if:

- English terms are misread.
- Numbers sound unnatural.
- Sentences are too long.
- A concept is hard to follow by ear.
- Transitions between pages sound abrupt.
