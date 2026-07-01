# Project_Pre-Requisite — Install the depended tools and libraries

This will get the machine ready for the projects.

## You Should Already Have

- **Docker** — [install](https://docs.docker.com/get-docker/)
- **kubectl** — [install](https://kubernetes.io/docs/tasks/tools/)
- **Kind** — [install](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)

## Step 1: Python 3.10+

```bash
python3 --version
```

Need 3.10+. If not:
- **macOS:** `brew install python@3.12`
- **Ubuntu:** `sudo apt install python3.12 python3.12-venv`
- **Other:** [python.org/downloads](https://www.python.org/downloads/)

## Step 2: Install Ollama

Ollama runs LLMs locally — no API key, no cost.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull the model we'll use:

```bash
ollama pull gemma4
```

Test it:

```bash
ollama run gemma4 "Say hello in one sentence"
```

## Step 3: Clone the Repo

```bash
git clone https://github.com/Sampatel24/Agentic-AI-Projects.git
cd Agentic-AI-Projects
```

## Step 4: Create a Virtual Environment

A virtual environment keeps this project's dependencies separate from your system Python. Everyone should use one to have the same setup.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` in your terminal prompt. If you open a new terminal, run `source .venv/bin/activate` again.

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Step 5: Verify

```bash
python3 Project_Pre-Requisite/verify_setup.py
```

If everything shows `[PASS]` — you're ready to Build the Agentic AI Projects.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Ollama not running | `ollama serve` (or open Ollama app on macOS) |
| Docker not running | Start Docker Desktop, or `sudo systemctl start docker` |
| Docker permission denied | `sudo usermod -aG docker $USER` then re-login |
| Kind not found | `brew install kind` (macOS) or [install docs](https://kind.sigs.k8s.io/docs/user/quick-start/#installation) |
| Python too old | Install newer version, use `python3.12` instead of `python3` |

---

Next: **[Project 1-Docker Error Explainer](../Project_1-Docker_Error_Explainer/)**
