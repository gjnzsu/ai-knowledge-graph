# Skill Usage Tracking System

**Goal**: Monitor which skills you actually use over time to understand patterns and optimize your skill ecosystem.

---

## 🎯 Tracking Approaches

### Option 1: Automatic Tracking via Hooks (Recommended)
**How it works**: Claude Code hooks automatically log when skills are invoked

**Pros**:
- ✅ Automatic - no manual work
- ✅ Accurate - captures every use
- ✅ Timestamped - know when you used it
- ✅ Context-aware - knows what task you were doing

**Cons**:
- Requires Claude Code hook configuration
- Only tracks skills invoked via `/skill` command

---

### Option 2: Manual Logging
**How it works**: You manually log when you use a skill

**Pros**:
- ✅ Simple to set up
- ✅ Works for any skill usage
- ✅ Can add notes about effectiveness

**Cons**:
- ❌ Requires discipline
- ❌ Easy to forget
- ❌ Time-consuming

---

### Option 3: Session Analysis (Hybrid)
**How it works**: Analyze Claude Code session logs to extract skill usage

**Pros**:
- ✅ Retroactive - can analyze past sessions
- ✅ Automatic once set up
- ✅ Rich context from conversations

**Cons**:
- Requires parsing session logs
- May miss some skill uses

---

## 🚀 Recommended Implementation: Automatic Tracking

### Step 1: Create Usage Log File

```bash
# Create tracking directory
mkdir -p ~/.claude/skill-usage

# Create log file
touch ~/.claude/skill-usage/usage.jsonl
```

### Step 2: Add Hook to Track Skill Usage

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "SkillInvoke": {
      "command": "bash",
      "args": ["-c", "echo \"{\\\"timestamp\\\":\\\"$(date -Iseconds)\\\",\\\"skill\\\":\\\"$SKILL_NAME\\\",\\\"session\\\":\\\"$SESSION_ID\\\"}\" >> ~/.claude/skill-usage/usage.jsonl"]
    }
  }
}
```

### Step 3: Create Analysis Script

Save as `analyze_skill_usage.py`:

```python
import json
from collections import defaultdict, Counter
from datetime import datetime, timedelta
import sys

def analyze_usage(log_file='~/.claude/skill-usage/usage.jsonl'):
    """Analyze skill usage from log file"""
    
    # Read logs
    usage_data = []
    try:
        with open(log_file.replace('~', os.path.expanduser('~')), 'r') as f:
            for line in f:
                if line.strip():
                    usage_data.append(json.loads(line))
    except FileNotFoundError:
        print("No usage data found. Start using skills to track!")
        return
    
    if not usage_data:
        print("No usage data yet.")
        return
    
    # Parse timestamps
    for entry in usage_data:
        entry['datetime'] = datetime.fromisoformat(entry['timestamp'])
    
    # Sort by time
    usage_data.sort(key=lambda x: x['datetime'])
    
    # Analysis
    print("=" * 80)
    print("SKILL USAGE ANALYSIS")
    print("=" * 80)
    
    # Total usage
    print(f"\nTotal skill invocations: {len(usage_data)}")
    print(f"First use: {usage_data[0]['datetime'].strftime('%Y-%m-%d %H:%M')}")
    print(f"Last use: {usage_data[-1]['datetime'].strftime('%Y-%m-%d %H:%M')}")
    
    # Most used skills
    skill_counts = Counter(entry['skill'] for entry in usage_data)
    print("\n" + "=" * 80)
    print("TOP 20 MOST USED SKILLS")
    print("=" * 80)
    for skill, count in skill_counts.most_common(20):
        percentage = (count / len(usage_data)) * 100
        print(f"{skill:<40} {count:>4} uses ({percentage:>5.1f}%)")
    
    # Usage by time period
    now = datetime.now()
    last_7_days = [e for e in usage_data if e['datetime'] > now - timedelta(days=7)]
    last_30_days = [e for e in usage_data if e['datetime'] > now - timedelta(days=30)]
    
    print("\n" + "=" * 80)
    print("USAGE BY TIME PERIOD")
    print("=" * 80)
    print(f"Last 7 days:  {len(last_7_days)} uses")
    print(f"Last 30 days: {len(last_30_days)} uses")
    
    if last_7_days:
        recent_skills = Counter(e['skill'] for e in last_7_days)
        print("\nTop 5 skills (last 7 days):")
        for skill, count in recent_skills.most_common(5):
            print(f"  {skill:<40} {count} uses")
    
    # Usage patterns
    print("\n" + "=" * 80)
    print("USAGE PATTERNS")
    print("=" * 80)
    
    # By day of week
    day_counts = defaultdict(int)
    for entry in usage_data:
        day = entry['datetime'].strftime('%A')
        day_counts[day] += 1
    
    print("\nBy day of week:")
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days_order:
        count = day_counts.get(day, 0)
        bar = '█' * (count // 2)
        print(f"  {day:<10} {count:>3} {bar}")
    
    # By hour
    hour_counts = defaultdict(int)
    for entry in usage_data:
        hour = entry['datetime'].hour
        hour_counts[hour] += 1
    
    print("\nBy hour of day:")
    for hour in range(24):
        count = hour_counts.get(hour, 0)
        bar = '█' * (count // 2)
        print(f"  {hour:02d}:00 {count:>3} {bar}")
    
    # Unused skills
    print("\n" + "=" * 80)
    print("SKILL COVERAGE")
    print("=" * 80)
    
    # Load all skills
    try:
        with open('skills-knowledge-graph.json', 'r') as f:
            all_skills_data = json.load(f)
            all_skill_ids = {s['id'] for s in all_skills_data['skills']}
            used_skill_ids = {e['skill'] for e in usage_data}
            unused_skills = all_skill_ids - used_skill_ids
            
            print(f"Total skills: {len(all_skill_ids)}")
            print(f"Used skills: {len(used_skill_ids)} ({len(used_skill_ids)/len(all_skill_ids)*100:.1f}%)")
            print(f"Unused skills: {len(unused_skills)} ({len(unused_skills)/len(all_skill_ids)*100:.1f}%)")
            
            if unused_skills and len(unused_skills) <= 20:
                print("\nUnused skills:")
                for skill_id in sorted(unused_skills):
                    skill = next((s for s in all_skills_data['skills'] if s['id'] == skill_id), None)
                    if skill:
                        print(f"  - {skill['name']}")
    except FileNotFoundError:
        print("Could not load skills data for coverage analysis")
    
    # Recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    # Skills used only once
    single_use = [skill for skill, count in skill_counts.items() if count == 1]
    if single_use:
        print(f"\n{len(single_use)} skills used only once (consider if they're needed):")
        for skill in single_use[:10]:
            print(f"  - {skill}")
    
    # Core skills not used recently
    core_skills = ['brainstorming', 'writing-plans', 'executing-plans', 
                   'verification-before-completion', 'code-reviewer']
    unused_core = [s for s in core_skills if s not in [e['skill'] for e in last_7_days]]
    if unused_core:
        print(f"\nCore skills not used in last 7 days:")
        for skill in unused_core:
            print(f"  - {skill}")

if __name__ == '__main__':
    import os
    analyze_usage()
```

### Step 4: Run Analysis

```bash
# Analyze your usage
python analyze_skill_usage.py

# Or with custom log file
python analyze_skill_usage.py ~/.claude/skill-usage/usage.jsonl
```

---

## 📊 What You'll Get

### 1. **Usage Statistics**
- Total invocations
- Date range
- Most used skills (top 20)
- Usage percentages

### 2. **Time-Based Analysis**
- Last 7 days usage
- Last 30 days usage
- Trending skills

### 3. **Usage Patterns**
- By day of week (when do you code most?)
- By hour of day (morning vs evening?)
- Peak usage times

### 4. **Coverage Analysis**
- How many skills you've actually used
- Which skills are unused
- Skills used only once (candidates for removal)

### 5. **Recommendations**
- Skills to consider removing
- Core skills you're not using
- Usage trends

---

## 📈 Example Output

```
================================================================================
SKILL USAGE ANALYSIS
================================================================================

Total skill invocations: 156
First use: 2026-04-01 09:23
Last use: 2026-04-19 17:45

================================================================================
TOP 20 MOST USED SKILLS
================================================================================
brainstorming                             23 uses ( 14.7%)
executing-plans                           18 uses ( 11.5%)
code-reviewer                             15 uses (  9.6%)
verification-before-completion            12 uses (  7.7%)
writing-plans                             10 uses (  6.4%)
...

================================================================================
USAGE BY TIME PERIOD
================================================================================
Last 7 days:  45 uses
Last 30 days: 156 uses

Top 5 skills (last 7 days):
  brainstorming                             8 uses
  code-reviewer                             6 uses
  executing-plans                           5 uses

================================================================================
USAGE PATTERNS
================================================================================

By day of week:
  Monday      28 ██████████████
  Tuesday     32 ████████████████
  Wednesday   25 ████████████
  Thursday    30 ███████████████
  Friday      22 ███████████
  Saturday     8 ████
  Sunday      11 █████

By hour of day:
  09:00  12 ██████
  10:00  18 █████████
  11:00  15 ███████
  14:00  22 ███████████
  15:00  19 █████████
  ...

================================================================================
SKILL COVERAGE
================================================================================
Total skills: 279
Used skills: 45 (16.1%)
Unused skills: 234 (83.9%)

================================================================================
RECOMMENDATIONS
================================================================================

12 skills used only once (consider if they're needed):
  - skill-stocktake
  - instinct-manager
  - pm-career-advisor
  ...

Core skills not used in last 7 days:
  - systematic-debugging
```

---

## 🎯 Advanced: Dashboard Visualization

Create `skill_usage_dashboard.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Skill Usage Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Skill Usage Dashboard</h1>
    
    <div style="width: 800px;">
        <canvas id="topSkillsChart"></canvas>
        <canvas id="timelineChart"></canvas>
        <canvas id="heatmapChart"></canvas>
    </div>
    
    <script>
        // Load usage data and create charts
        // (Implementation details...)
    </script>
</body>
</html>
```

---

## 🔄 Integration with Knowledge Graph

Update the visualization to show usage data:

```javascript
// In skills-graph-standalone-improved.html
// Color nodes by usage frequency
nodeElements.append('circle')
    .attr('r', d => {
        const usageCount = usageData[d.id] || 0;
        return 8 + Math.sqrt(usageCount);  // Bigger = more used
    })
    .attr('fill', d => {
        const usageCount = usageData[d.id] || 0;
        if (usageCount === 0) return '#666';  // Gray = unused
        if (usageCount < 5) return '#4a90e2';  // Blue = occasional
        if (usageCount < 20) return '#f39c12';  // Orange = frequent
        return '#e74c3c';  // Red = very frequent
    });
```

---

## 💡 Quick Start

### Simplest Approach (Manual)

Create `skill-usage-log.md`:

```markdown
# Skill Usage Log

## 2026-04-19
- brainstorming (new feature ideation)
- writing-plans (API refactor plan)
- executing-plans (implemented auth)
- code-reviewer (reviewed PR)

## 2026-04-18
- systematic-debugging (fixed login bug)
- verification-before-completion (pre-deploy check)
```

Then analyze manually or with a simple script.

---

## 🎯 Which Approach Should You Use?

| Approach | Best For | Effort | Accuracy |
|----------|----------|--------|----------|
| **Automatic (Hooks)** | Daily use | Low | High |
| **Manual Log** | Occasional use | Medium | Medium |
| **Session Analysis** | Retroactive | High | High |

**My Recommendation**: Start with **Automatic Tracking via Hooks** - set it up once and forget about it!

---

Would you like me to:
1. **Set up the automatic tracking** with hooks?
2. **Create the analysis script** ready to run?
3. **Build a dashboard** to visualize usage?
4. **All of the above**?

Let me know and I'll implement it for you!
