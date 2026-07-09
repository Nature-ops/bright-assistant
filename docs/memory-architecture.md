# Bright Memory Architecture

## Purpose

The memory system is the foundation of the Bright Platform.

Its purpose is to allow Bright to remember, organize, retrieve, and reason over information across conversations, projects, and specialized modules.

Rather than treating every conversation as isolated, Bright continuously builds knowledge about users, projects, goals, and tasks.

---

# Design Principles

Before implementing any memory feature we ask:

- What responsibility does this memory have?
- Who owns it?
- Will this design still make sense in one year?
- Can another Bright module reuse it?
- Is the memory searchable?
- Can it scale?

---

# Types of Memory

Bright stores different kinds of memory.

Conversation is only one of them.

```
Memory

├── Conversation
├── Facts
├── Goals
├── Projects
├── Learning
├── Tasks
├── Preferences
├── Contacts
├── Events
├── Health
└── Knowledge
```

---

# Conversation Memory

Purpose:

Store chronological conversations between the user and Bright.

Example:

User:
"I am studying AWS."

Assistant:
"Great! Let's build a study plan."

Characteristics

- chronological
- temporary context
- recent messages
- summarized when large

---

# Facts

Facts describe things that are expected to remain true.

Examples

- User's name
- Preferred programming language
- Lives in Germany
- Favorite football formation

Facts rarely change.

---

# Goals

Goals describe what the user wants to achieve.

Examples

- Pass AWS Solutions Architect
- Build Bright Assistant
- Coach football
- Start Bright Care

Goals are long-term.

---

# Projects

Projects contain structured work.

Examples

Bright Assistant

Bright Care

Bright Sports

Drone Platform

Each project has

- milestones
- documentation
- repositories
- deadlines
- notes

---

# Learning

Tracks current education.

Examples

AWS

Terraform

Python

Computer Vision

Football Coaching

Learning memories help Bright become a tutor.

---

# Tasks

Tasks are short-term actions.

Examples

Finish Memory API

Commit code

Update CHANGELOG

Tasks can expire.

---

# Preferences

Examples

Dark mode

VS Code

Python

FastAPI

German language

Preferred coding style

---

# Contacts

Examples

Football club

Family

Business partners

Care home staff

Doctors

---

# Events

Examples

Birthdays

Coaching sessions

AWS exam

Football matches

Meetings

---

# Health

Used primarily by Bright Care.

Examples

Medication schedule

Appointments

Daily reports

Vitals

Emergency contacts

---

# Knowledge

Knowledge differs from memory.

Knowledge comes from

PDFs

Books

Documentation

Websites

Research papers

Later this will become the RAG system.

---

# Memory Flow

```
User

↓

Conversation

↓

Memory Classifier

↓

Store

↓

Retrieve

↓

Conversation Builder

↓

LLM

↓

Response
```

---

# Future Vision

Eventually Bright will maintain separate memories for:

Bright Assistant

Bright Care

Bright Sports

Bright Engineering

Bright Cloud

Bright Robotics

Each module will share the same memory engine while storing different categories of information.

---

# Long-Term Goal

The memory system should become one of Bright's core competitive advantages.

Bright should understand not only what was said, but what matters.