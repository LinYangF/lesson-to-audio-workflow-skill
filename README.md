# Lesson to Audio Workflow Skill

[中文说明](README.zh-CN.md)

A Codex skill for turning lesson plans into video-ready teaching scripts, spoken narration, full TTS text, and natural audio.

## What It Does

This skill guides Codex through a repeatable lesson production workflow:

```text
Lesson plan -> Page script -> Spoken narration -> Full TTS text -> Audio
```

It is designed for course creators, teachers, and educational video workflows where a raw lesson plan needs to become clear, student-friendly voiceover material.

## Repository Structure

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

## Outputs

The workflow creates or maintains these files in a lesson workspace:

```text
lesson.md       # original lesson plan or teaching notes
pages.md        # page-by-page demo script
narration.md    # page-by-page spoken script
full.txt        # clean full text for TTS
audio.wav       # optional generated audio
voice.mp3       # optional generated audio
```

## Example Prompt

```text
Use $lesson-to-audio-workflow to turn this lesson plan into page scripts, spoken narration, full TTS text, and audio.
```

## Helper Script

Create a standard lesson workspace:

```bash
python scripts/prepare_lesson_workspace.py lessons/my-lesson
```

This creates starter files for:

```text
lesson.md
pages.md
narration.md
full.txt
```

## Installation

Copy or clone this folder into your Codex skills directory, for example:

```bash
git clone git@github.com:LinYangF/lesson-to-audio-workflow-skill.git ~/.codex/skills/lesson-to-audio-workflow
```

Then invoke it by name in Codex:

```text
$lesson-to-audio-workflow
```

## Notes

The skill can use project-specific lesson pipelines when available. If no local TTS engine is configured, it still produces the text artifacts and reports what audio dependency is missing.
