---
name: lesson-to-audio-workflow
description: Turn lesson plans, teaching notes, course outlines, or raw educational material into video-ready page scripts, natural spoken narration, full TTS text, and audio files. Use when the user asks for 教案转文案, 演示视频文案, 逐页口播稿, TTS narration, 口播音频, CosyVoice audio, or an automated workflow from lesson plan to demo script to narration to audio.
---

# Lesson To Audio Workflow

## Output Contract

Produce a reusable lesson workspace with these files:

```text
lesson.md       # original lesson plan or teaching notes
pages.md        # page-by-page demo script
narration.md    # page-by-page spoken script
full.txt        # clean full text for TTS
audio.wav       # optional generated audio
voice.mp3       # optional generated audio
```

If the user's project already has its own lesson pipeline, prefer the project's commands and file layout. If not, create the files manually using this skill's workflow.

## Quick Workflow

1. Put the source lesson in `lesson.md`.
2. Convert `lesson.md` to `pages.md`.
3. Convert `pages.md` to `narration.md`.
4. Extract only spoken text from `narration.md` into `full.txt`.
5. Generate audio from `full.txt` with the available TTS engine.
6. Listen/check and revise text before regenerating audio.

Use `references/prompts.md` when you need ready prompts or output format details.

## Step 1: Build The Lesson Workspace

If the user gives a target folder, use it. Otherwise create a short slugged folder under the current project, for example:

```text
lessons/chapter-name/
```

You may run the helper:

```bash
python ~/.codex/skills/lesson-to-audio-workflow/scripts/prepare_lesson_workspace.py lessons/chapter-name
```

If the project has commands like `npm run lesson:init -- <slug>`, use the project command instead.

## Step 2: Lesson Plan To Page Script

Write `pages.md` as page-based demo content.

Each page must contain:

```text
## Page N: short title

【画面标题】
...

【旁白】
...

【画面建议】
...

【预计时长】
...
```

Rules:

- Organize the whole lesson as `导入问题 -> 核心概念 -> 示例说明 -> 方法步骤 -> 总结提升`.
- Keep one page to one teaching point.
- Make the language clear, oral, and student-friendly.
- Make `画面建议` concrete enough for HTML/PPT animation later.
- Prefer examples, analogies, and simple contrasts over dense definitions.

## Step 3: Page Script To Spoken Narration

Write `narration.md` as page-by-page spoken script.

Each page should contain only:

```text
## Page N: short title

【口播稿】
...
```

Rules:

- Keep page order from `pages.md`.
- Use natural teacher-like speech.
- Use short sentences for TTS.
- Explain new terms in plain language the first time they appear.
- Add light transitions between pages.
- Do not include visual instructions in spoken text.

## Step 4: Narration To Full TTS Text

Write `full.txt` by extracting only the spoken text from `narration.md`.

Rules:

- Remove page headings, field labels, Markdown decoration, and visual notes.
- Keep paragraphs readable.
- Put a blank line between pages.
- Do not include stage directions or bracket labels.
- Normalize tricky terms for TTS if needed, for example spell out acronyms or add Chinese explanations.

## Step 5: Generate Audio

Use the best available local/project TTS path.

Preferred order:

1. Project-provided command, for example `npm run lesson:audio -- <slug>`.
2. Existing local CosyVoice script, if available.
3. Another TTS tool already configured in the workspace.
4. If no TTS is available, stop after `full.txt` and tell the user exactly what is missing.

When using CosyVoice, preserve both WAV and MP3 if possible:

```text
audio.wav
voice.mp3
```

Quality check audio for:

- Natural pacing.
- Misread English terms, numbers, and names.
- Sentences that are too long for TTS.
- Concepts that sound too dense when spoken.

Revise `narration.md` and regenerate `full.txt` before regenerating audio.

## Project Integration

If working inside `ai-html-video-factory`, prefer:

```bash
npm run lesson:init -- <slug>
npm run lesson:pages -- <slug>
npm run lesson:narration -- <slug>
npm run lesson:full -- <slug>
npm run lesson:audio -- <slug>
```

Expected project files:

```text
lessons/<slug>/lesson.md
lessons/<slug>/pages.md
lessons/<slug>/narration.md
lessons/<slug>/full.txt
lessons/<slug>/audio.wav
lessons/<slug>/voice.mp3
```

## Completion Criteria

The workflow is complete when:

- `pages.md` exists and is page-structured.
- `narration.md` exists and contains natural page-by-page spoken text.
- `full.txt` contains only the spoken content for TTS.
- Audio is generated, or the user is told precisely which TTS dependency is missing.
