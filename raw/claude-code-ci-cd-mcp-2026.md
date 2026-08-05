# Claude Code CI/CD + MCP Integration (2026)

## Part 1: Docker + GitHub Actions Pipeline

### Dockerfile (.github/docker/qa-agent.Dockerfile)
```dockerfile
FROM mcr.microsoft.com/playwright:v1.50.0-jammy

RUN apt-get update && apt-get install -y \
    xvfb \
    xterm \
    xdotool \
    fluxbox \
    scrot \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY package*.json ./
RUN npm ci
RUN npx playwright install chromium

ENV DISPLAY=:99
ENV SCREEN_WIDTH=1280
ENV SCREEN_HEIGHT=800
ENV SCREEN_DEPTH=24

COPY .github/docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
```

### Entrypoint (.github/docker/entrypoint.sh)
```bash
#!/bin/bash
set -e
echo "Starting virtual display (Xvfb) on DISPLAY ${DISPLAY}..."
Xvfb ${DISPLAY} -screen 0 ${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH} &
sleep 2
echo "Starting window manager (Fluxbox)..."
fluxbox &
sleep 2
exec "$@"
```

### GitHub Actions (.github/workflows/ai-qa-pipeline.yml)
```yaml
name: Autonomous Agentic Testing (Claude Code)
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
jobs:
  agentic-qa:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      - name: Build QA Agent Image
        uses: docker/build-push-action@v5
        with:
          context: .
          file: .github/docker/qa-agent.Dockerfile
          tags: qa-agent:latest
          outputs: type=docker,dest=/tmp/qa-agent.tar
      - name: Load Docker Image
        run: docker load -i /tmp/qa-agent.tar
      - name: Run Claude Code Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
        run: |
          docker run --rm \
            -e ANTHROPIC_API_KEY \
            -e SLACK_BOT_TOKEN \
            -e JIRA_API_TOKEN \
            -v ${{ github.workspace }}:/app \
            qa-agent:latest \
            npx claude use skill qa-hybrid-computer-use \
              "Запусти тесты. При падении используй Computer Use для отладки, 
               сделай скриншот и отправь баг-репорт через MCP."
```

## Part 2: MCP Integration (Slack + Jira)

### MCP Config (.claude/mcp-config.json)
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "env:SLACK_BOT_TOKEN"
      }
    },
    "jira": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-jira"],
      "env": {
        "JIRA_URL": "https://atlassian.net",
        "JIRA_EMAIL": "qa-bot@company.com",
        "JIRA_API_TOKEN": "env:JIRA_API_TOKEN"
      }
    }
  }
}
```

### Workflow 4: Escalation via MCP (дополнение к SKILL.md)
```
### Workflow 4: Escalation via MCP (Slack & Jira Alerting)
При definitively failed тесте после self-healing:
1. **Capture Evidence:** screenshot → `./playwright-report/failure-snapshots/last_error.png`
2. **Context Gathering:** 50 строк terminal error log + network payloads
3. **Format Bug Report:** RCA + координаты/selector + environment (Run ID, Commit SHA)
4. **Jira:** `jira.create_issue` — Project: QA, Type: Bug,
   Summary: "[AI Auto-Bug] E2E Failure on Layout Component"
5. **Slack:** `slack.post_message` — #qa-alerts,
   "🚨 Critical Test Failure Detected by Claude Agent!"
   + Jira ticket ID + failure reason + CI artifact link

### Guardrails
- ❌ No duplicate tickets — check `jira.search_issues` first
- ❌ Redact sensitive keys/passwords before posting
```

## Step 3: Closed-Loop Assignee — Commit Author → Jira → Slack

### GitHub Actions — Extract Author Metadata
```yaml
      - name: Extract Commit Author Metadata
        id: git-meta
        run: |
          echo "COMMIT_AUTHOR_EMAIL=$(git log -1 --format='%ae')" >> $GITHUB_ENV
          echo "COMMIT_AUTHOR_NAME=$(git log -1 --format='%an')" >> $GITHUB_ENV
      - name: Run Claude Code Agent
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
          JIRA_API_TOKEN: ${{ secrets.JIRA_API_TOKEN }}
          GIT_COMMIT_AUTHOR_EMAIL: ${{ env.COMMIT_AUTHOR_EMAIL }}
          GIT_COMMIT_AUTHOR_NAME: ${{ env.COMMIT_AUTHOR_NAME }}
        run: |
          docker run --rm \
            -e ANTHROPIC_API_KEY \
            -e SLACK_BOT_TOKEN \
            -e JIRA_API_TOKEN \
            -e GIT_COMMIT_AUTHOR_EMAIL \
            -e GIT_COMMIT_AUTHOR_NAME \
            -v ${{ github.workspace }}:/app \
            qa-agent:latest \
            npx claude use skill qa-hybrid-computer-use \
              "Запусти тесты. При падении создай тикет в Jira на автора
               ($GIT_COMMIT_AUTHOR_EMAIL) и тегни его в Slack."
```

### Workflow 4: Smart Escalation & Closed-Loop Assignee (SKILL.md update)
```
### Workflow 4: Smart Escalation & Closed-Loop Assignee Alerting
If a test definitively fails after self-healing:

1. **Capture Evidence:** screenshot → `./playwright-report/failure-snapshots/last_error.png`
2. **Read Author Context:** `$GIT_COMMIT_AUTHOR_EMAIL`, `$GIT_COMMIT_AUTHOR_NAME`
3. **Resolve Jira Assignee:**
   - `jira.user_search(GIT_COMMIT_AUTHOR_EMAIL)` → extract `accountId`
   - Fallback: QA Team Lead accountId если not found
4. **Create & Assign Jira Ticket:**
   - `jira.create_issue` — Project: QA, Type: Bug
   - Summary: "[AI Auto-Bug] E2E Failure by $GIT_COMMIT_AUTHOR_NAME"
   - Assignee: resolved accountId
   - Description: RCA + terminal log + commit link
   - Attach screenshot
5. **Resolve Slack User ID:**
   - `slack.users_lookupByEmail(GIT_COMMIT_AUTHOR_EMAIL)` → User ID
   - Fallback: @GIT_COMMIT_AUTHOR_NAME
6. **Dispatch Slack Notification:**
   - `slack.post_message` → #qa-alerts
   - "<@SLACK_USER_ID>, твой коммит сломал билд.
      Тикет QA-XXX создан на тебя."
```

## Full Pipeline Flow
1. Разработчик пушит коммит → PR
2. GitHub Actions извлекает email автора
3. Docker контейнер с Xvfb :99 дисплеем
4. Claude Code запускает тесты
5. При сбое → Computer Use (screenshot, визуальная локализация)
6. Jira: поиск пользователя по email → создание тикета → assign на автора
7. Slack: поиск по email → @упоминание с ID тикета
8. Цикл замкнут без ручного участия
